Gracefully terminates the current thread.

# Parameters
 - `ExitStatus` - the value to set as the exist status of the thread.

# Implementation details
The function calls `NtQueryInformationThread` with the the `THREADINFOCLASS` value of `ThreadAmILastThread` (12) and either detaches DLLs and exists the current thread or calls `RtlExitUserProcess`.

# Related Win32 API
 - [`ExitThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread)

# See also
 - `RtlExitUserProcess`
 - `NtTerminateThread`
 - `NtTerminateProcess`
