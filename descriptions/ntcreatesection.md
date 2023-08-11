Function NtCreateSection creates Section Object \
\(virtual memory block with associated file\). \
SectionHandle Result of call \- \
HANDLE to Section Object. \
DesiredAccess Access mask. Can be \
combination of: \
SECTION\_QUERY \
SECTION\_MAP\_WRITE \
SECTION\_MAP\_READ \
SECTION\_MAP\_EXECUTE \
SECTION\_EXTEND\_SIZE \
SECTION\_ALL\_ACCESS \
ObjectAttributes Pointer to \
OBJECT\_ATTRIBUTES structure contains section name, in Object \
Namespace format. \
MaximumSize Optionally define maximum \
size of section. Must be defined when caller create section based \
on system PageFile. \
PageAttributess Can be one or \
combination of: \
PAGE\_NOACCESS \
PAGE\_READONLY \
PAGE\_READWRITE \
PAGE\_WRITECOPY \
PAGE\_EXECUTE \
PAGE\_EXECUTE\_READ \
PAGE\_EXECUTE\_READWRITE \
PAGE\_EXECUTE\_WRITECOPY \
PAGE\_GUARD \
PAGE\_NOCACHE \
PAGE\_WRITECOMBINE \
SectionAttributes Can be one or \
combination of: \
SEC\_FILE \
SEC\_IMAGE \
SEC\_RESERVE \
SEC\_COMMIT \
SEC\_NOCACHE \
FileHandle Optionally HANDLE to \
File Object opened with proper access.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile \
NtExtendSection \
NtFlushVirtualMemory \
NtMapViewOfSection \
NtOpenFile \
NtOpenSection \
NtQuerySection
