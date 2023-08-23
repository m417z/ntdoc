Wakes another thread that previously called `NtWaitForAlertByThreadId`.

# Parameters
 - `ThreadId` - the ID of the thread to wake. The thread must belong to the same process as the caller.

# Remarks
Despite the name, `NtAlertThread` and alertable waits via `NtDelayExecution` are unrelated to this functionality.

# Related Win32 API
 - [`WakeByAddressSingle`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-wakebyaddresssingle)
 - [`WakeByAddressAll`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-wakebyaddressall)

# Required OS version
This function was introduced in Windows 8.

# See also
 - `NtWaitForAlertByThreadId`
