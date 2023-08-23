Returns the error mode for the current thread. The value controls how the system should handle serious errors.

# Implementation details
This function reads the `HardErrorMode` field from `TEB`.

# Related Win32 API
 - [`GetThreadErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getthreaderrormode)

# See also
 - `RtlSetThreadErrorMode`
