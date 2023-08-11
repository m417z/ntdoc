Function NtFsControlFile sends FSCTL\_\* code to \
File System Device Driver. See also description of \
NtDeviceIoControlFile function. \
FileHandle HANDLE to File System \
Device Object opened as a file. \
Event Optional HANDLE to Event \
Object. \
ApcRoutine Optional pointer to user's \
APC Routine. \
ApcContext Parameter for ApcRoutine. \
IoStatusBlock IO result of call. \
FsControlCode Control Code typically \
defined as FSCTL\_\*. \
InputBuffer User's allocated buffer \
contains input data. \
InputBufferLength Length of \
InputBuffer, in bytes. \
OutputBuffer User's allocated buffer \
for results of call. \
OutputBufferLength Length of \
OutputBuffer, in bytes.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtDeviceIoControlFile \
NtOpenFile
