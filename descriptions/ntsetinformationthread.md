Sets various information about the specified thread. This function is partially documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationthread).

# Parameters
 - `ThreadHandle` - a handle to the thread or the `NtCurrentThread` pseudo-handle. For most information classes, the handle must grant either `THREAD_SET_INFORMATION` or `THREAD_SET_LIMITED_INFORMATION` access.
 - `ThreadInformationClass` - the type of information to set.
 - `ThreadInformation` - a pointer to the buffer with the data specific to the request.
 - `ThreadInformationLength` - the size of the provided buffer in bytes.

# Information classes
For the list of supported info classes and required thread access, see `THREADINFOCLASS`.

# Related Win32 API
 - [`SetThreadInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadinformation)
 - [`SetThreadIdealProcessor`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessor)
 - [`SetThreadIdealProcessorEx`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessorex)
 - [`SetThreadDescription`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription)
 - [`SetThreadPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadpriorityboost)
 - [`SetThreadToken`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadtoken)
 - [`Wow64SetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-wow64setthreadcontext)

# See also
 - `NtOpenThread`
 - `NtQueryInformationThread`
 - `NtQueryInformationProcess`
 - `NtSetInformationProcess`
