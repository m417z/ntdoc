Forcefully terminates a thread.

# Parameters
 - `ThreadHandle` - an optional handle to a thread granting `THREAD_TERMINATE` access or the `NtCurrentThread` pseudo-handle. If this value is `NULL`, the calling thread is terminated.
 - `ExitStatus` - the value to set as the exit status of the thread.

# Notable return values
 - `STATUS_CANT_TERMINATE_SELF` - indicates that a thread attempted to terminate itself by default (called `NtTerminateThread` with `NULL`) and it was the last thread in the current process.

# Remarks
To exit the current thread gracefully, use `RtlExitUserThread`.

The thread object becomes signalled after termination.

# Related Win32 API
 - [`TerminateThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminatethread)

# See also
 - `RtlExitUserThread`
 - `NtOpenThread`
 - `NtSuspendThread`
 - `NtTerminateProcess`
