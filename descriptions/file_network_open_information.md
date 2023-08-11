FILE\_NETWORK\_OPEN\_INFORMATION structure is used with \
two file functions: \
1\) \
NtQueryFullAttributesFile, \
2\) \
NtQueryInformationFile with \
FileNetworkOpenInformation information class. \
CreationTime Indicates time of file \
creation. \
LastAccessTime Time of last open \
file. \
LastWriteTime Time of last write \
operation. \
ChangeTime Time of any last \
change. \
AllocationSize Number of bytes that \
file use on storage, equal or greater to EndOfFile. \
EndOfFile Length of file, in \
bytes. \
FileAttributes File attributes. \
Unknown \- ???

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_BASIC\_INFORMATION \
FILE\_INFORMATION\_CLASS \
FILE\_STANDARD\_INFORMATION \
NtCreateFile \
NtOpenFile \
NtQueryAttributesFile \
NtQueryFullAttributesFile \
NtQueryInformationFile \
NtWriteFile
