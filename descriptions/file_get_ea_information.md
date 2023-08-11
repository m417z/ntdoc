Structure FILE\_GET\_EA\_INFORMATION is used in a call \
to NtQueryEaFile function. See \
FILE\_FULL\_EA\_INFORMATION for detailed information about \
EA. \
NextEntryOffset Relative offset for \
next FILE\_GET\_EA\_INFORMATION structure in \
buffer. \
EaNameLength Length of EA name, \
in bytes \(without leading zero\). \
EaName\[1\] ASCIIZ name of \
EA, case insensitive.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_FULL\_EA\_INFORMATION \
NtQueryEaFile
