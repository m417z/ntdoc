Alerts and resumes the specified thread that previously entered an alertable wait and then was suspended. Once the suspension counter drops to zero, the thread wakes and returns `STATUS_ALERTED`.

# Parameters
 - `ThreadHandle` - a handle to a thread granting `THREAD_SUSPEND_RESUME` access.
 - `PreviousSuspendCount` - an optional pointer to a variable that receives the previous value of the suspension counter of the thread.

# Remarks
Despite the name similarity, this function is unrelated to `NtAlertThreadByThreadId`.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtAlertThread`
 - `NtResumeThread`
 - `NtDelayExecution`
 - `NtWaitForSingleObject`
 - `NtWaitForMultipleObjects`
