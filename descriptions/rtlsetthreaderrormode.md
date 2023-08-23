Changes the error mode for the current thread. The value controls how the system should handle serious errors.

# Parameters
 - `NewMode` - a bit mask with flags defining the new behavior.
 - `OldMode` - a pointer to a variable that receives the previous error mode.

# Supported flags
 - `SEM_FAILCRITICALERRORS` - the system does not display the dialog on critical errors and lets the thread handle them.
 - `SEM_NOGPFAULTERRORBOX` - The system does not display the Windows Error Reporting dialog.
 - `SEM_NOALIGNMENTFAULTEXCEPT` - automatically fix alignment faults.
 - `SEM_NOOPENFILEERRORBOX` - OpenFile does not display a message box when it fails to find a file.

# Implementation details
This function sets the `HardErrorMode` field in `TEB`.

# Related Win32 API
 - [`SetThreadErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-setthreaderrormode)

# See also
 - `RtlGetThreadErrorMode`
