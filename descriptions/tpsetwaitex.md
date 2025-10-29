Sets the wait object, replacing the previous wait object, if any. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.

# Related Win32 API
[`SetThreadpoolWaitEx`](https://learn.microsoft.com/en-us/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwaitex) maps directly to this function.

# See also
- `TpAllocWait`
- `TpSetWait`
- `TpWaitForWait`
- `TpReleaseWait`
