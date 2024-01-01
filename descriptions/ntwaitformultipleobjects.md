Waits for one or more objects to enter a signaled state.

# Parameters
 - `Count` - the number of handles passed in the `Handles` parameter, up to `MAXIMUM_WAIT_OBJECTS` (64).
 - `Handles` - a pointer to an array of handles. Each handle must grant `SYNCHRONIZE` access.
 - `WaitType` - the type of wait to perform, either `WaitAll` or `WaitAny`.
 - `Alertable` - determines whether the wait should be altertable. This allows external triggers (such as [APCs](https://learn.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls) or calls to `NtAlertThread`) to interrupt wait prematurely.
 - `Timeout` - an optional pointer to a variable that stores the wait internal. A negative value indicates relative timeout for the specified number of 100-nanosecond intervals. To wait a specific number of milliseconds, multiply them by `-10,000`. Positive values indicate an absolute time. `NULL` indicates an infinite timeout.

# Notable return values
 - `STATUS_WAIT_0`..`STATUS_WAIT_63` - the thread woke due to the n'th object being signaled.
 - `STATUS_ABANDONED_WAIT_0`..`STATUS_ABANDONED_WAIT_63` - the thread woke due to the n'th passed mutex becoming abandoned.
 - `STATUS_TIMEOUT` - the thread woke due to the timeout.
 - `STATUS_USER_APC` - the wait was interrupted by an APC.
 - `STATUS_ALERTED` - the wait was interrupted by a call to `NtAlertThread`.

# Remarks
Despite the name, `NtAlertThreadByThreadId` is unrelated to alertable waits and cannot interrupt them.

# Related Win32 API
 - [`WaitForMultipleObjectsEx`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjectsex)

# See also
 - `NtWaitForSingleObject`
 - `NtDelayExecution`
 - `NtAlertThread`
 - `NtQueueApcThread`
