Sets various information about the specified process.

# Parameters
 - `ProcessHandle` - a handle to the process or the `NtCurrentProcess` pseudo-handle. For most information classes, the handle must grant either `PROCESS_SET_INFORMATION` or `PROCESS_SET_LIMITED_INFORMATION` access.
 - `ProcessInformationClass` - the type of information to set.
 - `ProcessInformation` - a pointer to the buffer with the data specific to the request.
 - `ProcessInformationLength` - the size of the provided buffer in bytes.

# Information classes
For the list of supported info classes and required process access, see `PROCESSINFOCLASS`.

# Related Win32 API
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)
 - [`SetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy)
 - [`SetProcessWorkingSetSizeEx`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex)
 - [`SetErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode)
 - [`SetPriorityClass`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setpriorityclass)
 - [`SetProcessAffinityMask`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setprocessaffinitymask)
 - [`SetProcessAffinityUpdateMode`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessaffinityupdatemode)
 - [`SetProcessPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocesspriorityboost)
 - [`SetProcessDefaultCpuSetMasks`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdefaultcpusetmasks)
 - [`SetProcessDefaultCpuSets`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdefaultcpusets)
 - [`SetProcessDynamicEHContinuationTargets`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdynamicehcontinuationtargets)
 - [`SetProcessDynamicEnforcedCetCompatibleRanges`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdynamicenforcedcetcompatibleranges)
 - [`EnableProcessOptionalXStateFeatures`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-enableprocessoptionalxstatefeatures)

# See also
 - `NtOpenProcess`
 - `NtQueryInformationProcess`
