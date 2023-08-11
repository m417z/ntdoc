FileHandle HANDLE to File \
Object. \
IoStatusBlock IO result of call. \
FileSystemInformation Caller's \
allocated buffer for output data. \
Length Length of FileSystemInformation buffer, in bytes. \
FileSystemInformationClass Information \
class descripted in \
FS\_INFORMATION\_CLASS topic. \
NtQueryVolumeInformationFile gives information about \
volume \(device\) containing file specified as FileHandle parameter.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FS\_INFORMATION\_CLASS \
NtOpenFile \
NtSetVolumeInformationFile
