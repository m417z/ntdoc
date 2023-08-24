This macro is a native equivalent of the [`GetCurrentProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) function. It returns a pseudo-handle that grants `PROCESS_ALL_ACCESS` to the current process. You do not need to call `NtClose` on the returned handle.

# See also
 - `NtCurrentThread`
 - `RtlIsCurrentProcess`
