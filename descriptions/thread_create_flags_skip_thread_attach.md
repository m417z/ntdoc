This flags indicates that the new thread should not call any [DllMain](https://learn.microsoft.com/en-us/windows/win32/dlls/dllmain) callbacks with `DLL_THREAD_ATTACH` reason on loaded modules. Keep in mind that this flags might introduce compatibility issues because threads started with it have some of their state not initialized. See [this blog post](https://m417z.com/A-guest-in-another-process-a-story-of-a-remote-thread-crash/) for more details.

# Applicable to
 - `NtCreateThreadEx`

# Implementation details
Using this flag sets the `SkipThreadAttach` flag in the `TEB` of the new thread.

# Related flags
 - `THREAD_CREATE_FLAGS_NONE`
 - `THREAD_CREATE_FLAGS_CREATE_SUSPENDED`
 - `THREAD_CREATE_FLAGS_HIDE_FROM_DEBUGGER`
 - `THREAD_CREATE_FLAGS_LOADER_WORKER`
 - `THREAD_CREATE_FLAGS_SKIP_LOADER_INIT`
 - `THREAD_CREATE_FLAGS_BYPASS_PROCESS_FREEZE`

# See also
 - `RtlIsCurrentThreadAttachExempt`
 - `LDRP_DONT_CALL_FOR_THREADS`
