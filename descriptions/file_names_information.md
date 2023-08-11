Structure FILE\_NAMES\_INFORMATION is used as a result \
of call \
NtQueryDirectoryFile with \
FileNamesInformation information class. It's shorter then other \
directory informational structures, so can be used for better \
performance, when only file names are required. \
NextEntryOffset Offset \(in bytes\) of \
next FILE\_NAMES\_INFORMATION entry, or zero if \
last. \
FileIndex Index of file, or zero if \
Directory Indexing is disabled. \
FileNameLength Length of FileName \
array, in bytes. \
FileName\[1\] Name of file, in UNICODE \
format.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_BOTH\_DIR\_INFORMATION \
FILE\_DIRECTORY\_INFORMATION \
FILE\_FULL\_DIR\_INFORMATION \
FILE\_INFORMATION\_CLASS \
NtQueryDirectoryFile
