#!/usr/bin/env python
# coding=utf-8

# -------------------------------------------------------------------------------
# Name:        LTSpice_RawWrite.py
# Purpose:     Create RAW Files
#
# Author:      Nuno Brum (nuno.brum@gmail.com)
#
# Created:     16-10-2021
# Licence:     refer to the LICENSE file
# -------------------------------------------------------------------------------

"""
This module generates RAW Files from user data.
It can be used to combine RAW files generated by different Simulation Runs
"""
from typing import Union
from time import strftime
from PyLTSpice.LTSpice_RawRead import DataSet, LTSpiceRawRead
from struct import pack

from numpy import array, float32


def interpolate(values, axis, i, t):
    if i + 1 < len(axis):
        slope = (values[i+1] - values[i]) / (axis[i+1] - axis[i])
        return values[i] + slope * (t - axis[i])
    else:
        # Interpolate based on the last two points
        slope = (values[-1] - values[-2]) / (axis[-1] - axis[-2])
        return values[i] + slope * (t - axis[-1])


class Trace(DataSet):
    """Helper class representing a trace. This class is based on DataSet, therefore, it doesn't support STEPPED data.
    :param name: name of the trace being created
    :type name: str
    :param whattype: time, frequency, voltage or current
    :type whattype: str
    :param data: data for the data write
    :type data: list or numpy.array
    :param numerical_type: real or complex
    :type numerical_type: str
    """

    def __init__(self, name, data, whattype='voltage', numerical_type=''):
        if name == 'time':
            whattype = 'time'
            numerical_type = 'double'
        elif name == 'frequency':
            whattype = 'frequency'
            numerical_type = 'complex'
        elif numerical_type == '':
            if isinstance(data[0], float32) or isinstance(data[0], float):
                numerical_type = 'real'
            elif isinstance(data[0], complex):
                numerical_type = 'complex'
            else:
                raise NotImplementedError

        DataSet.__init__(self, name, whattype, len(data), numerical_type=numerical_type)
        if isinstance(data, (list, tuple)):
            self.data = array(data, dtype=self.data.dtype)
        else:
            self.data[:] = data[:]  # This way the dtype is kept


class LTSpiceRawWrite(object):
    """
    This class represents the RAW data file being generated. Contrary to the the LTSpiceRawRead this class doesn't
    support stepped data.

    """

    def __init__(self, plot_name='Transient Analysis', fastacces=True, numtype='real', encoding='utf_16_le'):
        self._traces = list()
        self.flag_numtype = numtype
        self.flag_stepped = False
        self.flag_fastaccess = fastacces
        self.plot_name = plot_name
        self.offset = 0.0
        self.encoding = encoding

    def _str_flags(self):
        flags = [self.flag_numtype]
        if self.flag_stepped:
            flags.append('stepped')
        if self.flag_fastaccess:
            flags.append('fastaccess')
        return ' '.join(flags)

    def add_trace(self, trace: Trace):
        """
        Adds a trace to the RAW file. The trace needs to have the same size as trace 0 ('time', 'frequency', etc..)
        The first trace added defines the X-Axis and therefore the type of RAW file being generated. If no plot name
        was defined, it will automatically assign a name.
        :param trace: Needs to be of the
        :type trace:
        :return: Nothing
        :rtype: None
        """
        assert isinstance(trace, Trace), "The trace needs to be of the type ""Trace"""
        if self.plot_name is None or len(self._traces) == 0:
            if trace.whattype == 'time':
                self.plot_name = self.plot_name or 'Transient Analysis'
                self.flag_numtype = 'real'
            elif trace.whattype == 'frequency':
                self.plot_name = self.plot_name or 'AC Analysis'
                self.flag_numtype = 'complex'
            elif trace.whattype in ('voltage', 'current'):
                self.plot_name = self.plot_name or 'DC transfer characteristic'
                self.flag_numtype = 'real'
            elif trace.whattype == 'param':
                self.plot_name = self.plot_name or 'Operating Point'
                self.flag_numtype = 'real'
            else:
                raise ValueError("First Trace needs to be either 'time', 'frequency', 'param', 'voltage' or '...'")
        else:
            if len(self._traces[0]) != len(trace):
                raise IndexError("The trace needs to be the same size as trace 0")
        self._traces.append(trace)

    def save(self, filename: str):
        """
        Saves the RAW file into a file. The file format is always binary. Text based RAW output format is not supported
        in this version.

        :param filename: filename to where the RAW file is going to be written. Make sure that the extension of the file
        is .RAW.

        :type filename: str or pathlib.Path
        :return: Nothing
        :rtype: None
        """
        f = open(filename, 'wb')
        f.write("Title: * PyLTSpice LTSpice_RawWrite\n".encode(self.encoding))
        f.write("Date: {}\n".format(strftime("%a %b %d %H:%M:%S %Y")).encode(self.encoding))
        f.write("Plotname: {}\n".format(self.plot_name).encode(self.encoding))
        f.write("Flags: {}\n".format(self._str_flags()).encode(self.encoding))
        f.write("No. Variables: {}\n".format(len(self._traces)).encode(self.encoding))
        f.write("No. Points: {:12}\n".format(len(self._traces[0])).encode(self.encoding))
        f.write("Offset:   {:.16e}\n".format(self.offset).encode(self.encoding))
        f.write("Command: Linear Technology Corporation LTspice XVII\n".encode(self.encoding))
        f.write("Backannotation: \n".encode(self.encoding))
        f.write("Variables:\n".encode(self.encoding))
        for i, trace in enumerate(self._traces):
            f.write("\t{0}\t{1}\t{2}\n".format(i, trace.name, trace.whattype).encode(self.encoding))
        total_bytes = 0
        f.write("Binary:\n".encode(self.encoding))
        if self.flag_fastaccess and self.flag_numtype != 'complex':  # Don't know why, but complex RAW files aren't
            # converted to FastAccess
            for trace in self._traces:
                f.write(trace.data.tobytes())
        else:
            fmts = {trace: tobytes_for_trace(trace) for trace in self._traces}
            for i in range(len(self._traces[0])):
                for trace in self._traces:
                    total_bytes += f.write(fmts[trace](trace.data[i]))
        f.close()

    @staticmethod
    def _rename_netlabel(name, **kwargs) -> str:
        """Renames a trace name making sure that the V() or I() containers are left intact."""
        # Make the rename as requested
        if 'rename_format' in kwargs:
            if name.endswith(')') and name.startswith('V(') or name.startswith('I('):
                new_name = name[:2] + kwargs['rename_format'].format(name[2:-1], **kwargs) + name[-1]
            else:
                new_name = kwargs['rename_format'].format(name, **kwargs)
            return new_name
        else:
            return name

    def _name_exists(self, name: str) -> bool:
        # first check whether it is a duplicate
        for trace in self._traces:
            if trace.name == name:
                return True
        return False

    def add_traces_from_raw(self, other: LTSpiceRawRead, trace_filter: Union[list, tuple, str], **kwargs):
        """
        *(Not fully implemented)*

        Merge two LTSpiceRawWrite classes together resulting in a new instance
        :param other: an instance of the LTSpiceRawRead class where the traces are going to be copied from.
        :type other: LTSpiceRawRead
        :param trace_filter: A list of signals that should be imported into the new file
        :type trace_filter: list, Tuple, or just a string for one trace
        :keyword force_axis_alignment: If two raw files don't have the same axis, an attempt is made to sync the two
        :keyword admissible_error: maximum error allowed in the sync between the two axis
        :keyword rename_format: when adding traces with the same name, it is possible to define a rename format.
            For example, if there are two traces named N001 in order to avoid duplicate names the
            rename format can be defined as "{}_{kwarg_name} where kwarg_name is passed as a keyword
            argument of this function. If just one trace is being added, this can be used to simply give the new name.

        :keyword step: by default only step 0 is added from the second raw. It is possible to add other steps, by
            using this keyword parameter. This is useful when we want to "flatten" the multiple step runs into the same
            view.
        :keyword: minimum_timestep: This parameter forces the two axis to sync using a minimum time step. That is, all
            time increments that are less than this parameter will be suppressed.
        :returns: Nothing
        """
        force_axis_alignment = kwargs.get('force_axis_alignment', False)
        admissible_error = kwargs.get('admissible_error', 1e-11)
        from_step = kwargs.get('step', 0)
        minimum_timestep = kwargs.get('minimum_timestep', 0.0)
        if isinstance(trace_filter, str):
            trace_filter = [trace_filter]

        for flag in other.get_raw_property('Flags').split(' '):
            if flag in ('real', 'complex'):
                other_flag_num_type = flag
                break
        else:
            other_flag_num_type = 'real'

        if len(self._traces):  # there are already traces
            if self.flag_numtype != other_flag_num_type:
                raise ValueError("The two instances should have the same type:\n"
                                 f"Source is {other_flag_num_type} and Destination is {self.flag_numtype}")
            if self._traces[0].whattype != other.get_trace(0).whattype:
                raise ValueError("The two instances should have the same axis type:\n"
                                 f"Source is {other.get_trace(0).whattype} and Destination is {self._traces[0].whattype}")
        else:  # No traces are present
            # if no X axis is present, copy from the first one
            self.flag_numtype = other_flag_num_type
            oaxis = other.get_trace(0)
            new_axis = Trace(oaxis.name, other.get_axis(from_step), oaxis.whattype)
            self._traces.append(new_axis)
            force_axis_alignment = False

        if force_axis_alignment or minimum_timestep > 0.0:
            my_axis = self._traces[0].get_wave()
            other_axis = other.get_axis(from_step)
            new_axis = []
            if minimum_timestep > 0.0:
                raise NotImplementedError
            else:
                i = 0  # incomming data counter
                e = 0  # existing data counter
                existing_data = {}
                existing_types = {}
                incoming_data = {}
                incoming_types = {}
                new_traces = {}
                updated_traces = {}

                for trace_name in trace_filter:
                    new_name = self._rename_netlabel(trace_name, **kwargs)
                    new_traces[new_name] = []
                    otrace = other.get_trace(trace_name)
                    incoming_data[new_name] = otrace.get_wave(from_step)
                    incoming_types[new_name] = otrace.whattype
                for trace in self._traces[1:]:  # not considering axis
                    updated_traces[trace.name] = []
                    existing_data[trace.name] = trace.get_wave()
                    existing_types[trace.name] = trace.whattype

                axis_name = self._traces[0].name  # Saving the trace name for recreating all the traces

                while e < len(my_axis)-1 and i < len(other_axis)-1:
                    error = other_axis[i] - my_axis[e]
                    if abs(error) < admissible_error:
                        new_axis.append(my_axis[e])
                        for trace in incoming_data:
                            new_traces[trace].append(incoming_data[trace][i])
                        for trace in existing_data:
                            updated_traces[trace].append(existing_data[trace][e])
                            i += 1
                            e += 1
                    elif error < 0:
                        # Other axis is smaller
                        new_axis.append(other_axis[i])
                        for trace in incoming_data:
                            new_traces[trace].append(incoming_data[trace][i])
                        for trace in existing_data:
                            value = interpolate(existing_data[trace], my_axis, e - 1, other_axis[i])
                            updated_traces[trace].append(value)
                        i += 1
                    else:
                        new_axis.append(my_axis[e])
                        for trace in incoming_data:
                            value = interpolate(incoming_data[trace], other_axis, i - 1, my_axis[e])
                            new_traces[trace].append(value)
                        for trace in existing_data:
                            updated_traces[trace].append(existing_data[trace][e])
                        e += 1

                axis_whattype = self._traces[0].whattype
                self._traces.clear()  # Cleaning class list of traces
                # Creating the New Axis
                self._traces.append(Trace(axis_name, new_axis, axis_whattype))
                # Now recreating all tre traces
                for trace in incoming_data:
                    self._traces.append(Trace(trace, new_traces[trace], incoming_types[trace]))
                for trace in existing_data:
                    self._traces.append(Trace(trace, updated_traces[trace], existing_types[trace]))

        else:
            assert len(self._traces[0]) == len(other.get_axis(from_step)), \
                "The two instances should have the same size. To avoid this use force_axis_alignment=True option"
            for trace_name in trace_filter:
                trace = other.get_trace(trace_name)
                new_name = self._rename_netlabel(trace_name, **kwargs)
                data = trace.get_wave(from_step)
                self._traces.append(Trace(new_name, data, trace.whattype, numerical_type=trace.numerical_type))

    def get_trace(self, trace_ref):
        """
        Retrieves the trace with the requested name (trace_ref).

        :param trace_ref: Name of the trace
        :type trace_ref: str
        :return: An object containing the requested trace
        :rtype: DataSet subclass
        """
        if isinstance(trace_ref, str):
            for trace in self._traces:
                if trace_ref == trace.name:
                    # assert isinstance(trace, DataSet)
                    return trace
            raise IndexError(f"{self} doesn't contain trace \"{trace_ref}\"\n"
                             f"Valid traces are {[trc.name for trc in self._traces]}")
        else:
            return self._traces[trace_ref]

    def __getitem__(self, item):
        """Helper function to access traces by using the [ ] operator."""
        return self.get_trace(item)


def tobytes_for_trace(trace: Trace):
    def tobytes(value):
        return value.tobytes()
    return tobytes


if __name__ == '__main__':
    import numpy as np
    from LTSpice_RawRead import LTSpiceRawRead

    def test_readme_snippet():
        LW = LTSpiceRawWrite(fastacces=False)
        tx = Trace('time', np.arange(0.0, 3e-3, 997E-11))
        vy = Trace('N001', np.sin(2 * np.pi * tx.data * 10000))
        vz = Trace('N002', np.cos(2 * np.pi * tx.data * 9970))
        LW.add_trace(tx)
        LW.add_trace(vy)
        LW.add_trace(vz)
        LW.save("teste_snippet1.raw")

    def test_trc2raw():  # Convert Teledyne-Lecroy trace files to raw files
        f = open(r"Current_Lock_Front_Right_8V.trc")
        raw_type = ''  # Initialization of parameters that need to be overridden by the file header
        wave_size = 0
        for line in f:
            tokens = line.rstrip('\r\n').split(',')
            if len(tokens) == 4:
                if tokens[0] == 'Segments' and tokens[2] == 'SegmentSize':
                    wave_size = int(tokens[1]) * int(tokens[3])
            if len(tokens) == 2:
                if tokens[0] == 'Time' and tokens[1] == 'Ampl':
                    raw_type = 'transient'
                    break
        if raw_type == 'transient' and wave_size > 0:
            data = np.genfromtxt(f, dtype='float,float', delimiter=',', max_rows=wave_size)
            LW = LTSpiceRawWrite()
            LW.add_trace(Trace('time', [x[0] for x in data]))
            LW.add_trace(Trace('Ampl', [x[1] for x in data]))
            LW.save("teste_trc.raw")
        f.close()


    def test_axis_sync():  # Test axis sync
        LW = LTSpiceRawWrite()
        tx = Trace('time', np.arange(0.0, 3e-3, 997E-11))
        vy = Trace('N001', np.sin(2 * np.pi * tx.data * 10000))
        vz = Trace('N002', np.cos(2 * np.pi * tx.data * 9970))
        LW.add_trace(tx)
        LW.add_trace(vy)
        LW.add_trace(vz)
        LW.save("teste_w.raw")
        LR = LTSpiceRawRead("..\\test_files\\testfile.raw")
        LW.add_traces_from_raw(LR, ('V(out)',), force_axis_alignment=True)
        LW.save("merge.raw")
        test = """
        equal = True
        for ii in range(len(tx)):
            if t[ii] != tx[ii]:
                print(t[ii], tx[ii])
                equal = False
        print(equal)

        v = LR.get_trace('N001')
        max_error = 1.5e-12
        for ii in range(len(vy)):
            err = abs(v[ii] - vy[ii])
            if err > max_error:
                max_error = err
                print(v[ii], vy[ii], v[ii] - vy[ii])
        print(max_error)
        """

    def test_write_ac():
        LW = LTSpiceRawWrite()
        LR = LTSpiceRawRead("..\\tests\\PI_Filter.raw")
        LR1 = LTSpiceRawRead("..\\tests\\PI_Filter_resampled.raw")
        LW.add_traces_from_raw(LR, ('V(N002)',))
        LW.add_traces_from_raw(LR1, 'V(N002)', rename_format='N002_resampled', force_axis_alignment=True)
        LW.flag_fastaccess = False
        LW.save("..\\tests\\PI_filter_rewritten.raw")
        LW.flag_fastaccess = True
        LW.save("..\\tests\\PI_filter_rewritten_fast.raw")

    def test_write_tran():
        LR = LTSpiceRawRead("..\\tests\\TRAN - STEP.raw")
        LW = LTSpiceRawWrite()
        LW.add_traces_from_raw(LR, ('V(out)', 'I(C1)'))
        LW.flag_fastaccess = False
        LW.save("..\\tests\\TRAN - STEP0_normal.raw")
        LW.flag_fastaccess = True
        LW.save("..\\tests\\TRAN - STEP0_fast.raw")

    def test_combine_tran():
        LW = LTSpiceRawWrite()
        for tag, raw in (
            ("AD820_15", "../tests/Batch_Test_AD820_15.raw"),
            # ("AD820_10", "../tests/Batch_Test_AD820_10.raw"),
            ("AD712_15", "../tests/Batch_Test_AD712_15.raw"),
            # ("AD712_10", "../tests/Batch_Test_AD712_10.raw"),
            # ("AD820_5", "../tests/Batch_Test_AD820_5.raw"),
            # ("AD712_5.", "../tests/Batch_Test_AD712_5.raw"),
        ):
            LR = LTSpiceRawRead(raw)
            LW.add_traces_from_raw(LR, ("V(out)", "I(R1)"), rename_format="{}_{tag}", tag=tag, force_axis_alignment=True)
        LW.flag_fastaccess = False
        LW.save("../tests/Batch_Test_Combine.raw")


    # test_readme_snippet()
    # test_axis_sync()
    # test_write_ac()
    # test_write_tran()
    test_combine_tran()
