Creates a new thread in the specified process.

# Parameters
 - `ThreadHandle` - a pointer to a variable that receives a handle to the new thread.
 - `DesiredAccess` - the thread access mask to provide on the returned handle. This value is usually `THREAD_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes for the new object/handle, such as the security descriptor and handle inheritance.
 - `ProcessHandle` - a handle to the process where the thread should be created. This can either be the `NtCurrentProcess` pseudo-handle or a handle with `PROCESS_CREATE_THREAD` access.
 - `StartRoutine` - the function to execute on the new thread.
 - `Argument` - a user-provided argument to pass to the thread start routine.
 - `CreateFlags` - a bit mask that control the properties of the new thread or its creation. See below.
 - `ZeroBits` - the number of high-order address bits that must be zero in the base address of the thread's stack. Note that when the value is larger than 32, it becomes a bit mask.
 - `StackSize` - the initial size of the stack, in bytes. The system rounds this value up to the nearest page. If this parameter is zero, the new thread uses the default size for the executable.
 - `MaximumStackSize` - the maximum size of the stack, in bytes. The system rounds this value up to the nearest page. If this parameter is zero, the new thread uses the default size for the executable.
 - `AttributeList` - an optional pointer to a buffer that defines a list of `PS_ATTRIBUTE` structures that control various aspects of thread creation and allow retrieving information about the new thread.

# Creation flags
 - `THREAD_CREATE_FLAGS_CREATE_SUSPENDED` - create the thread in a suspended state instead of allowing it to execute immediately.
 - `THREAD_CREATE_FLAGS_SKIP_THREAD_ATTACH` - the thread should skip calling loaded modules with `DLL_THREAD_ATTACH` reason.
 - `THREAD_CREATE_FLAGS_HIDE_FROM_DEBUGGER` - suppress generation of debug events on the thread.
 - `THREAD_CREATE_FLAGS_LOADER_WORKER` - set the corresponding flag in `TEB`.
 - `THREAD_CREATE_FLAGS_SKIP_LOADER_INIT` - set the corresponding flag in `TEB`.
 - `THREAD_CREATE_FLAGS_BYPASS_PROCESS_FREEZE` - the thread should not be suspended when the system suspends or freezes the process.

Check the corresponding pages for more details.

# Supported attributes
 - `PS_ATTRIBUTE_CLIENT_ID` - allows retrieving the `CLIENT_ID` of the new thread.
 - `PS_ATTRIBUTE_TEB_ADDRESS` - allows retrieving the `TEB` address of the new thread.
 - `PS_ATTRIBUTE_IDEAL_PROCESSOR` - allows specifying the ideal processor for new thread.
 - `PS_ATTRIBUTE_UMS_THREAD` - controls user-mode thread scheduling.
 - `PS_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES` - controls extended thread context features.

Check the corresponding pages for more details.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

For the legacy equivalent of this function, see `NtCreateThread`.

# Related Win32 API
 - [`CreateRemoteThreadEx`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex)

# See also
 - `NtCreateThread`
 - `RtlCreateUserThread`
 - `NtResumeThread`
 - `NtOpenThread`
 - `NtOpenProcess`
 - `NtCreateUserProcess`
