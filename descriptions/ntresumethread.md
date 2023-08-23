Resumes a previously suspended thread.

# Parameters
 - `ThreadHandle` - a handle to a thread granting either `THREAD_SUSPEND_RESUME` or `THREAD_RESUME` access.
 - `PreviousSuspendCount` - an optional pointer to a variable that receives the previous value of the suspension counter of the thread.

# Related Win32 API
 - [`ResumeThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-resumethread)

# See also
 - `NtOpenThread`
 - `NtSuspendThread`
 - `NtSuspendProcess`
 - `NtResumeProcess`
