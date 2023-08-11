Function NtCreateNamedPipeFile creates Named \
Pipe File Object. Named Pipes are especial kind of files, so \
all functionality is provided with file's functions like \
NtReadFile, \
NtWriteFile etc. \
Named Pipes are frequently used in NT system, for example as \
stdin and stdout handles. \
NamedPipeFileHandle Result of call \- \
pointer to HANDLE to Named Pipe. \
DesiredAccess Access rights for \
object's handle. Can be one or combination of: \
FILE\_READ\_DATA \
FILE\_WRITE\_DATA \
FILE\_CREATE\_PIPE\_INSTANCE \
FILE\_READ\_ATTRIBUTES \
FILE\_WRITE\_ATTRIBUTES \
SYNCHRONIZE \
READ\_CONTROL \
WRITE\_OWNER \
WRITE\_DAC \
ACCESS\_SYSTEM\_SECURITY \
Also combination of Generic rights are supported. \
ObjectAttributes Pointer to \
OBJECT\_ATTRIBUTES structure contains name of named pipe. \
Name must begin with "\\??\\PIPE\\" string, \
that is Symbolic Link to NamedPipe device object. \
IoStatusBlock IO result of call. \
ShareAccess Can be combination of \
following: \
FILE\_SHARE\_READ \
FILE\_SHARE\_WRITE \
FILE\_SHARE\_DELETE \
CreateDisposition Use \
FILE\_CREATE, FILE\_OPEN or FILE\_OPEN\_IF. \
CreateOptions See description of \
NtCreateFile for possible creation flags. \
WriteModeMessage If set, writing to \
created pipe are processed in Message Mode. If not, all \
writes are in Byte Mode. \
ReadModeMessage The same functionality \
as WriteModeMessage parameter, \
but for reading data. \
NonBlocking If set, all operations on \
created pipe are asynchronous. \
MaxInstances Maximum number of open \
handles for Named Pipe, or FILE\_PIPE\_UNLIMITED\_INSTANCES \
constant. \
InBufferSize Input buffer size, in \
bytes. \
OutBufferSize Output buffer size, in \
bytes. \
DefaultTimeOut Pointer to \
LARGE\_INTEGER value specifing pipe's time out, in \
100\-ns units. Negative value means relative time.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
FILE\_INFORMATION\_CLASS \
FILE\_PIPE\_INFORMATION \
FILE\_PIPE\_LOCAL\_INFORMATION \
FILE\_PIPE\_REMOTE\_INFORMATION \
NtFsControlFile \
NtQueryInformationFile \
NtReadFile \
NtSetInformationFile \
NtWriteFile
