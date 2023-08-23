Creates a new thread in the specified process. This is a legacy function that requires manually allocating stack and preparing thread context.

# Parameters
 - `ThreadHandle` - a pointer to a variable that receives a handle to the new thread.
 - `DesiredAccess` - the thread access mask to provide on the returned handle. This value is usually `THREAD_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes for the new object/handle, such as the security descriptor and handle inheritance.
 - `ProcessHandle` - a handle to the process where the thread should be created. This can either be the `NtCurrentProcess` pseudo-handle or a handle with `PROCESS_CREATE_THREAD` access.
 - `ClientId` - a pointer to a variable that receives the client ID of the new thread.
 - `ThreadContext` - the initial context (a set of registers) for the thread.
 - `InitialTeb` - the structure describing the thread stack.
 - `CreateSuspended` - whether the new thread should be created in a suspended state or allowed to run immediately. When specifying `TRUE`, you can use `NtResumeThread` to resume the thread later.

# Remarks
For the modern equivalent, see `NtCreateThreadEx`.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

# Related Win32 API
This functionality is not exposed in Win32 API. The closest alternative that uses the modern syscall is [`CreateRemoteThreadEx`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex).

# See also
 - `NtCreateThreadEx`
 - `RtlCreateUserThread`
 - `NtResumeThread`
 - `NtOpenThread`
 - `NtOpenProcess`
 - `NtCreateProcess`
