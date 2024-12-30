Queries various information about the specified thread. This function is partially documented in [Windows Driver Kit](https://learn.microsoft.com/en-us/previous-versions/windows/hardware/kernel/mt629133%28v=vs.85%29) and [Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationthread).

# Parameters
 - `ThreadHandle` - a handle to the thread or the `NtCurrentThread` pseudo-handle. For most information classes, the handle must grant either `THREAD_QUERY_INFORMATION` or `THREAD_QUERY_LIMITED_INFORMATION` access.
 - `ThreadInformationClass` - the type of information to retrieve.
 - `ThreadInformation` - a pointer to user-allocated buffer that receives the requested information.
 - `ThreadInformationLength` - the size of the provided buffer in bytes.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written when the function succeeds or the number of bytes requires when the buffer is too small.

# Information classes
For the list of supported info classes and required thread access, see `THREADINFOCLASS`.

# Notable return values
 - `STATUS_BUFFER_TOO_SMALL` and `STATUS_INFO_LENGTH_MISMATCH` indicate that the requested information does not fit into the provided buffer.

# Related Win32 API
 - [`GetThreadInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadinformation)
 - [`GetThreadId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadid)
 - [`GetProcessIdOfThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessidofthread)
 - [`GetExitCodeThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodethread)
 - [`GetThreadDescription`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreaddescription)
 - [`GetThreadIOPendingFlag`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadiopendingflag)
 - [`GetThreadPriority`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadpriority)
 - [`GetThreadTimes`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadtimes)
 - [`Wow64GetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-wow64getthreadcontext)

# See also
 - `NtOpenThread`
 - `NtSetInformationThread`
 - `NtQueryInformationProcess`
 - `NtSetInformationProcess`
