NtQueryEaFile is used to read EA from \
NTFS file. For more information about EA see \
FILE\_FULL\_EA\_INFORMATION. \
FileHandle HANDLE to File Object \
opened with FILE\_READ\_EA access. \
IoStatusBlock IO result of call. \
Buffer Caller's allocated buffer for \
output data. See \
FILE\_FULL\_EA\_INFORMATION for detailed description of fields \
avaiable in buffer. \
Length Length of buffer, in bytes. \
ReturnSingleEntry If set, only one \
entry is returned. \
EaList Optional list of \
FILE\_GET\_EA\_INFORMATION structures containing names of \
EA. \
EaListLength Length of EaList, in bytes. \
EaIndex Pointer to ULONG value \
contains 1\-based index of queried attribute. \
RestartScan If set, result is the first \
quered EA.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
FILE\_FULL\_EA\_INFORMATION \
FILE\_GET\_EA\_INFORMATION \
NtCreateFile \
NtSetEaFile
