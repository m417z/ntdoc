\(Also descripted in Win 2000 DDK\) \
FileHandle HANDLE to File Object \
opened with FILE\_WRITE\_DATA access. \
Event HANDLE to Event Object \
signaled when write finished. \
ApcRoutine User APC routine executed \
after writing is complete. \
ApcContext Parameter to ApcRoutine. \
IoStatusBlock IO result of call. \
Buffer Buffer with data to write. \
Length Length of Buffer, in bytes. \
ByteOffset Offset from begining of \
file, where write starts. \
Key \- ??? \(See \
NtReadFile\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtOpenFile \
NtReadFile
