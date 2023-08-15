This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetinformationfile).

\(Description of this function is also avaiable in Win2000 \
DDK\) \
FileHandle HANDLE to File \
Object. \
IoStatusBlock IO result of call. \
FileInformation User's allocated buffer \
contains data to set to. \
Length Length of FileInformation buffer, in bytes. \
FileInformationClass See FILE\_INFORMATION\_CLASS for \
possible information classes and required contents of FileInformation buffer.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
FILE\_INFORMATION\_CLASS \
NtOpenFile \
NtQueryInformationFile \
NtSetVolumeInformationFile
