This macro is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/zwcurrentprocess). It is a native equivalent of the [`GetCurrentProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) function and returns a pseudo-handle that grants `PROCESS_ALL_ACCESS` to the current process. You do not need to call `NtClose` on the returned handle.

# Applicable to
This pseudo-handle can be used with all functions that accept process handles.

# See also
 - `NtCurrentThread`
 - `RtlIsCurrentProcess`
