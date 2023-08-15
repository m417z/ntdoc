This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeletefile)

It's very interesting NT System Call... Normally, file deletion is realised as FileDispositionInformation class in a call to NtSetInformationFile. When you use NtDeleteFile, file will be deleted immediatly after call \(system isn't waiting for close last HANDLE to file\).
