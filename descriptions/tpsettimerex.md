Sets the timer object, replacing the previous timer, if any. A worker thread calls the timer object's callback after the specified timeout expires.

# Related Win32 API
[`SetThreadpoolTimerEx`](https://learn.microsoft.com/en-us/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimerex) maps directly to this function.

# See also
- `TpAllocTimer`
- `TpSetTimer`
- `TpWaitForTimer`
- `TpReleaseTimer`
