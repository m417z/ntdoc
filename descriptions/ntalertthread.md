Alerts and wakes the specified thread that previously entered an alertable wait, causing it to return `STATUS_ALERTED`.

# Parameters
 - `ThreadHandle` - a handle to a thread granting `THREAD_ALERT` access.

# Remarks
Despite the name similarity, this function is unrelated to `NtAlertThreadByThreadId`.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtDelayExecution`
 - `NtWaitForSingleObject`
 - `NtWaitForMultipleObjects`
