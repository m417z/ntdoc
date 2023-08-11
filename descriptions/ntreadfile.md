\(Also descripted in Win2000 DDK\) \
FileHandle HANDLE to File Object \
opened with FILE\_READ\_DATA access. \
Event Optional HANDLE to Event \
Object signaled when reading is done. \
ApcRoutine User defined APC \
routine queued for execute after reading is done. \
ApcContext User parameter to \
ApcRoutine. \
IoStatusBlock Pointer to IO\_STATUS \
structure received IO status of file reading. \
Buffer User\-allocated buffer for readed \
data. \
Length Length of Buffer, in bytes. \
ByteOffset Offset from begining of \
file, in bytes. \
Key \- ??? \(In my opinion: use this, if \
you previously lock file, and now you want read it, but without \
unlocking\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtOpenFile \
NtWriteFile
