Waits for the object to enter a signaled state. This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwwaitforsingleobject).

# Parameters
 - `Handle` - a handle granting `SYNCHRONIZE` access.
 - `Alertable` - determines whether the wait should be altertable. This allows external triggers (such as [APCs](https://learn.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls) or calls to `NtAlertThread`) to interrupt wait prematurely.
 - `Timeout` - an optional pointer to a variable that stores the wait internal. A negative value indicates relative timeout for the specified number of 100-nanosecond intervals. To wait a specific number of milliseconds, multiply them by `-10,000`. Positive values indicate an absolute time. `NULL` indicates an infinite timeout.

# Notable return values
 - `STATUS_WAIT_0` - the thread woke due to the object being signaled.
 - `STATUS_ABANDONED_WAIT_0` - the thread woke due to the passed mutex becoming abandoned.
 - `STATUS_TIMEOUT` - the thread woke due to the timeout.
 - `STATUS_USER_APC` - the wait was interrupted by an APC.
 - `STATUS_ALERTED` - the wait was interrupted by a call to `NtAlertThread`.

# Remarks
Despite the name, `NtAlertThreadByThreadId` is unrelated to alertable waits and cannot interrupt them.

# Related Win32 API
 - [`WaitForSingleObjectEx`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex)

# See also
 - `NtWaitForMultipleObjects`
 - `NtDelayExecution`
 - `NtAlertThread`
 - `NtQueueApcThread`
