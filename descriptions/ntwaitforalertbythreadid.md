Waits on the specified address to be alerted-by-ID by another thread.

# Parameters
 - `Address` - the user-provided value that serves as a key.
 - `Timeout` - an optional pointer to a timeout for the wait. A negative value indicates relative timeout for the specified number of 100-nanosecond intervals. To wait for a specific number of milliseconds, multiply them by `-10,000`. Positive values indicate an absolute time.

# Notable return values
 - `STATUS_ALERTED` - the thread woke due to a call to `NtAlertThreadByThreadId`.
 - `STATUS_TIMEOUT` - the thread woke due to the timeout.

# Remarks
Despite the name, the wait this function enters is not alertable and, thus, cannot be interrupted by APCs or `NtAlertThread`. Alertable waits via `NtDelayExecution` are unrelated to this functionality.

# Related Win32 API
 - [`WaitOnAddress`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitonaddress)

# Required OS version
This function was introduced in Windows 8.

# See also
 - `NtAlertThreadByThreadId`
