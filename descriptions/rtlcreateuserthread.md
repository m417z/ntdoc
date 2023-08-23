Creates a new thread in the specified process.

# Parameters
 - `ProcessHandle` - a handle to the process where the thread should be created. This can either be the `NtCurrentProcess` pseudo-handle or a handle with `PROCESS_CREATE_THREAD` access.
 - `ThreadSecurityDescriptor` - a security descriptor to protect the new thread with.
 - `CreateSuspended` - whether the new thread should be created in a suspended state or allowed to run immediately. When specifying `TRUE`, you can use `NtResumeThread` to resume the thread later.
 - `ZeroBits` - the number of high-order address bits that must be zero in the base address of the thread's stack. Note that when the value is larger than 32, it becomes a bit mask.
 - `MaximumStackSize` - the maximum size of the stack, in bytes. The system rounds this value up to the nearest page. If this parameter is zero, the new thread uses the default size for the executable.
 - `CommittedStackSize` - the initial size of the stack, in bytes. The system rounds this value up to the nearest page. If this parameter is zero, the new thread uses the default size for the executable.
 - `StartAddress` - the function to execute on the new thread.
 - `Parameter` - a user-provided argument to pass to the thread start routine.
 - `ThreadHandle` - an optional pointer to a variable that receives a handle to the new thread.
 - `ClientId` - an optional pointer to a variable that receives the client ID of the new thread.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

# Implementation details
This function is a wrapper over `NtCreateThreadEx`.

# Related Win32 API
 - [`CreateRemoteThreadEx`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex)

# See also
 - `NtCreateThreadEx`
 - `NtCreateThread`
 - `NtResumeThread`
 - `NtOpenThread`
 - `NtOpenProcess`
 - `RtlCreateUserProcess`
