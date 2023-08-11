\(Avaiable also in 2000 DDK.\) \
FileHandle Result of call \- \
HANDLE to File Object. \
DesiredAccess Access mask based on \
definitions in schema FILE\_\* from \
&lt;WinNT.h&gt;. \
ObjectAttributes Name of file to create \
\(or open\), optionally path in name string. You can also define root \
directory, security descriptor and attributes \
OBJ\_CASE\_INSENSITIVE and OBJ\_INHERIT. \
IoStatusBlock Pointer to \
IO\_STATUS\_BLOCK structure, that receive final status of \
function call. Can be one of: \
FILE\_CREATED \
FILE\_OPENED \
FILE\_OVERWRITTEN \
FILE\_SUPERSEDED \
FILE\_EXISTS \
FILE\_DOES\_NOT\_EXIST \
AllocationSize File size after \
creation. \
FileAttributes Attributes for newly \
created file, as follows: \
FILE\_ATTRIBUTE\_READONLY \
FILE\_ATTRIBUTE\_HIDDEN \
FILE\_ATTRIBUTE\_SYSTEM \
FILE\_ATTRIBUTE\_ARCHIVE \
FILE\_ATTRIBUTE\_NORMAL \
FILE\_ATTRIBUTE\_TEMPORARY \
FILE\_ATTRIBUTE\_OFFLINE \
FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED \
ShareAccess Specifies share method for \
opened object. Can be set to zero or any combination of flags: \
FILE\_SHARE\_READ \
FILE\_SHARE\_WRITE \
FILE\_SHARE\_DELETE \
CreateDisposition Specifies disposition \
how to create or open object and can be one of: \
FILE\_SUPERSEDE \- If file exists, deletes it before \
creation of new one. \
FILE\_OPEN \- Fails, if file not exists. \
FILE\_CREATE \- Fails, if file exists. \
FILE\_OPEN\_IF \- If file exists, opens it. If not, creates \
new one and then open it. \
FILE\_OVERWRITE \- If file not exists, create and open it. \
If exists, open them and reset content. \
FILE\_OVERWRITE\_IF \- As FILE\_OVERWRITE, but fails \
if file not exists. \
CreateOptions Creation options. \
EaBuffer Buffer for Extended Attributes \
contains one or more of \
FILE\_FULL\_EA\_INFORMATION structures. \
EaLength Length of EaBuffer.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
FILE\_FULL\_EA\_INFORMATION \
NtDeleteFile \
NtOpenFile \
NtSetEaFile
