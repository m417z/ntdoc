Retrieves the context (set of registers) of the specified thread.

# Parameters
 - `ThreadHandle` - a handle to a thread granting `THREAD_GET_CONTEXT` access.
 - `ThreadContext` - a pointer to a `CONTEXT` structure that receives the state of registers. **Note:** make sure to initialize the `ContextFlags` field of the structure with the bit mask defining which portion of the context to query.

# Related Win32 API
 - [`GetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadcontext)

# See also
 - `RtlCopyContext`
 - `RtlGetExtendedContextLength`
 - `NtSetContextThread`
 - `NtOpenThread`
 - `NtQueryInformationThread`
 - `NtSetInformationThread`
