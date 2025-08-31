Gracefully terminates the current process.

# Parameters
 - `ExitStatus` - the value to set as the exit status for the process.

# Implementation details
This function detaches from DLLs, shuts down various ntdll facilities, and uses `NtTerminateProcess` to perform two-phase termination.

# Related Win32 API
 - [`ExitProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess)

# See also
 - `NtTerminateProcess`
 - `NtTerminateThread`
 - `RtlExitUserThread`
