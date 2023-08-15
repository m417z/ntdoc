This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)

FileHandle HANDLE to File \
Object. \
IoStatusBlock IO result of call. \
FileSystemInformation Buffer containing \
information to set, dependly to FileSystemInformationClass parameter. \
Length Length of FileSystemInformation buffer, in bytes. \
FileSystemInformationClass Class of \
information to set. See \
FS\_INFORMATION\_CLASS for valid information classes. \
NtSetVolumeInformationFile sets information to volume \
\(device\) containing file specified in FileHandle parameter.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FS\_INFORMATION\_CLASS \
NtQueryVolumeInformationFile
