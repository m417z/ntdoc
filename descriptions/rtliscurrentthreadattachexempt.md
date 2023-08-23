Determines whether the current thread is supposed to skip calling [DllMain](https://learn.microsoft.com/en-us/windows/win32/dlls/dllmain) with `DLL_THREAD_ATTACH` reason on loaded modules.

# Implementation details
The function checks for `SkipThreadAttach` and `RanProcessInit` flags in `TEB`.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `THREAD_CREATE_FLAGS_SKIP_THREAD_ATTACH`
 - `LDRP_DONT_CALL_FOR_THREADS`
