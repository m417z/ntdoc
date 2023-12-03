Queries various information about the specified process. This function is partially [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationprocess).

# Parameters
 - `ProcessHandle` - a handle to the process or the `NtCurrentProcess` pseudo-handle. For most information classes, the handle must grant either `PROCESS_QUERY_INFORMATION` or `PROCESS_QUERY_LIMITED_INFORMATION` access.
 - `ProcessInformationClass` - the type of information to retrieve.
 - `ProcessInformation` - a pointer to a user-allocated buffer that receives the requested information.
 - `ProcessInformationLength` - the size of the provided buffer in bytes.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written when the function succeeds or the number of bytes requires when the buffer is too small.

# Information classes
For the list of supported info classes and required process access, see `PROCESSINFOCLASS`.

# Notable return values
 - `STATUS_BUFFER_TOO_SMALL` and `STATUS_INFO_LENGTH_MISMATCH` indicate that the requested information does not fit into the provided buffer.

# Related Win32 API
 - [`GetExitCodeProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodeprocess)
 - [`GetProcessId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessid)
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)
 - [`GetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy)
 - [`IsWow64Process`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-iswow64process)
 - [`IsProcessCritical`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-isprocesscritical)
 - [`ProcessIdToSessionId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-processidtosessionid)
 - [`QueryProcessCycleTime`](https://learn.microsoft.com/en-us/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryprocesscycletime)
 - [`QueryProcessAffinityUpdateMode`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queryprocessaffinityupdatemode)
 - [`GetProcessWorkingSetSizeEx`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-getprocessworkingsetsizeex)
 - [`GetProcessTimes`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes)
 - [`GetErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-geterrormode)
 - [`GetProcessHandleCount`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesshandlecount)
 - [`GetProcessPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesspriorityboost)
 - [`GetProcessVersion`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessversion)
 - [`GetProcessGroupAffinity`](https://learn.microsoft.com/en-us/windows/win32/api/processtopologyapi/nf-processtopologyapi-getprocessgroupaffinity)
 - [`GetPriorityClass`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getpriorityclass)

# See also
 - `NtSetInformationProcess`
 - `NtOpenProcess`
 - `NtOpenProcessToken`
