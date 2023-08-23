Suspends a thread.

# Parameters
 - `ThreadHandle` - a handle to a thread granting `THREAD_SUSPEND_RESUME` access.
 - `PreviousSuspendCount` - an optional pointer to a variable that receives the previous value of the suspension counter of the thread.

# Related Win32 API
 - [`SuspendThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-suspendthread)

# See also
 - `NtOpenThread`
 - `NtResumeThread`
 - `NtSuspendProcess`
 - `NtResumeProcess`
 - `NtDelayExecution`
