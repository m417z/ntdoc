Initiates a sleep on the current thread.

# Parameters
 - `Alertable` - determines whether the sleep should be altertable. This allows external triggers (such as [APCs](https://learn.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls) or calls to `NtAlertThread`) to interrupt sleep prematurely.
 - `DelayInterval` - a pointer to a variable that stores the wait internal. A negative value indicates relative timeout for the specified number of 100-nanosecond intervals. To sleep for a specific number of milliseconds, multiply them by `-10,000`. Positive values indicate an absolute time.

# Notable return values
 - `STATUS_SUCCESS` - the thread woke due to the timeout.
 - `STATUS_USER_APC` - the sleep was interrupted by an APC.
 - `STATUS_ALERTED` - the sleep was interrupted by a call to `NtAlertThread`.

# Remarks
Despite the name, `NtAlertThreadByThreadId` is unrelated to alertable sleeps and cannot interrupt them.

# Related Win32 API
 - [`SleepEx`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-sleepex)

# See also
 - `NtWaitForSingleObject`
 - `NtWaitForMultipleObjects`
 - `NtAlertThread`
 - `NtQueueApcThread`
