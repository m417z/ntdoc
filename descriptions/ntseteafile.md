This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwseteafile)

See \
NtQueryEaFile for information about EA. \
FileHandle HANDLE to File Object \
opened with FILE\_SET\_EA access. \
IoStatusBlock IO result of call. \
EaBuffer User's allocated input buffer \
containing one or more FILE\_FULL\_EA\_INFORMATION \
structures. \
EaBufferSize Size of EaBuffer, in bytes.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_FULL\_EA\_INFORMATION \
NtCreateFile \
NtQueryEaFile
