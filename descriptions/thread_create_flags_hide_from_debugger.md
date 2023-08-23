This flags indicates that the system should not notify debuggers attached to the target process about thread creation. This option also suppresses other debug events on the target thread for the entirety of its lifetime.

# Applicable to
 - `NtCreateThreadEx`

# Related flags
 - `THREAD_CREATE_FLAGS_NONE`
 - `THREAD_CREATE_FLAGS_CREATE_SUSPENDED`
 - `THREAD_CREATE_FLAGS_SKIP_THREAD_ATTACH`
 - `THREAD_CREATE_FLAGS_LOADER_WORKER`
 - `THREAD_CREATE_FLAGS_SKIP_LOADER_INIT`
 - `THREAD_CREATE_FLAGS_BYPASS_PROCESS_FREEZE`

# See also
 - `NtSetInformationThread` with `ThreadHideFromDebugger`
 - `NtWaitForDebugEvent`
