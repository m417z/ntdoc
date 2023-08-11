Structure FILE\_FULL\_DIR\_INFORMATION is returned as a \
result of call \
NtQueryDirectoryFile with \
FileFullDirectoryInformation information class. It contains \
some typical informations about directory entries, like a FILE\_DIRECTORY\_INFORMATION \
structure, but additionally contains member specifing size of \
Extended Attributes. \
NextEntryOffset Offset \(in bytes\) of \
next FILE\_FULL\_DIR\_INFORMATION structure placed in \
result buffer. If there's no more entries, NextEntryOffset is set to zero. \
FileIndex File index value, or zero, if \
directory indexing is not avaiable. \
CreationTime Time of object \
creation; \
LastAccessTime Last access time. Means \
time when last open operation was performed. \
LastWriteTime Time of last write \
data. \
ChangeTime Time of last change. \
EndOfFile Specify length of file, in \
bytes. \
AllocationSize Specify real size of \
file on device. It must be equal or greater to EndOfFile member. \
FileAttributes Attributes of file. \
FileNameLength Length of FileName array, in bytes. \
EaSize Size of Extended Attributes \
associated with file. See also FILE\_EA\_INFORMATION \
structure. \
FileName\[1\] UNICODE string specifing \
file name.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_BOTH\_DIR\_INFORMATION \
FILE\_DIRECTORY\_INFORMATION \
FILE\_INFORMATION\_CLASS \
FILE\_NAMES\_INFORMATION \
NtQueryDirectoryFile \
NtQueryOleDirectoryFile
