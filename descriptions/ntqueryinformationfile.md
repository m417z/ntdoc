This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryinformationfile).

\(Also avaiable in Microsoft 2000 DDK\) \
FileHandle HANDLE to File \
Object. \
IoStatusBlock Completion status of \
call. \
FileInformation Caller's allocated \
buffer for result data. \
Length Length of FileInformation buffer, in bytes. \
FileInformationClass Enumerated \
information class. See FILE\_INFORMATION\_CLASS for \
detailed information about usage.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_INFORMATION\_CLASS \
NtCreateFile \
NtOpenFile \
NtQueryAttributesFile \
NtQueryDirectoryFile \
NtSetInformationFile
