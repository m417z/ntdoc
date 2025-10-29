Sets the wait object, replacing the previous wait object, if any. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.

# Related Win32 API
[`SetThreadpoolWait`](https://learn.microsoft.com/en-us/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwait) maps directly to this function.

# See also
- `TpAllocWait`
- `TpSetWaitEx`
- `TpWaitForWait`
- `TpReleaseWait`
