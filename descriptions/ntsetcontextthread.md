Changes the context of the specified thread.

# Parameters
 - `ThreadHandle` - a handle to a thread granting `THREAD_SET_CONTEXT` access.
 - `ThreadContext` - a pointer to a `CONTEXT` structure that contains the context to be set in the specified thread. **Note:** the value of the `ContextFlags` field specifies which portions of a thread's context to set.

# Related Win32 API
 - [`SetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadcontext)

# See also
 - `NtGetContextThread`
 - `RtlCopyContext`
 - `RtlGetExtendedContextLength`
 - `NtOpenThread`
 - `NtQueryInformationThread`
 - `NtSetInformationThread`
