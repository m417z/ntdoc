This flags indicates that the thread should be created in a suspended state instead of being allowed to execute immediately.

# Applicable to
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`

# Related flags
 - `THREAD_CREATE_FLAGS_NONE`
 - `THREAD_CREATE_FLAGS_SKIP_THREAD_ATTACH`
 - `THREAD_CREATE_FLAGS_HIDE_FROM_DEBUGGER`
 - `THREAD_CREATE_FLAGS_LOADER_WORKER`
 - `THREAD_CREATE_FLAGS_SKIP_LOADER_INIT`
 - `THREAD_CREATE_FLAGS_BYPASS_PROCESS_FREEZE`

# See also
 - `NtResumeThread`
 - `NtSuspendThread`
