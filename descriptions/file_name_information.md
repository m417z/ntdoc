Structure FILE\_NAME\_INFORMATION contains name of \
queried file object. It's used as a result of call \
NtQueryInformationFile with \
FileNameInformation or \
FileAlternateNameInformation information class. \
FileNameLength Length of FileName, in bytes. \
FileName\[1\] UNICODE name of file. If \
caller query about \
FileNameInformation, FileName additionally contains path to file, \
and begins with '\\' \(full path to file \
relative to device\).

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_ALL\_INFORMATION \
FILE\_INFORMATION\_CLASS \
NtQueryInformationFile
