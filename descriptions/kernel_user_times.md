This structure describes the timing information for threads.

# Applicable to
 - `NtQueryInformationThread` with `ThreadTimes` (1)
 - `NtQueryInformationProcess` with `ProcessTimes` (4)

# Members

## CreateTime
The number of 100-nanosecond intervals since the 1st of January 1600 to the creation of the thread/process.

## ExitTime
The number of 100-nanosecond intervals since 1st of January 1600 to the termination of the thread/process.

## KernelTime
The number of 100-nanosecond intervals spent by the thread(s) executing in kernel mode.

## UserTime
The number of 100-nanosecond intervals spent by the thread(s) executing in user mode.
