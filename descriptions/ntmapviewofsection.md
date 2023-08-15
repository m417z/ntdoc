This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)

Function NtMapViewOfSection maps specified part of \
Section Object into process memory. \
SectionHandle HANDLE to Section \
Object opened with one or more from SECTION\_MAP\_EXECUTE, \
SECTION\_MAP\_READ, SECTION\_MAP\_WRITE attributes. \
ProcessHandle HANDLE to Process \
Object opened with PROCESS\_VM\_OPERATION access. \
\*BaseAddress Pointer to variable \
receiving virtual address of mapped memory. If this value is not \
NULL, system tries to allocate memory from specified \
value. \
ZeroBits Indicates how many high bits \
must not be set in BaseAddress. \
CommitSize Size of initially commited \
memory, in bytes. \
SectionOffset Pointer to begin of \
mapped block in section. This value must be rounded up to \
X64K block size \(0x10000 on X86\). \
ViewSize Pointer to size of mapped \
block, in bytes. This value is rounded up to page size \
\(0x1000 on x86\). \
InheritDisposition How to child \
processes inherid maped section. See description of enumeration \
type \
SECTION\_INHERIT. \
AllocationType Can be one of: \
MEM\_COMMIT \
MEM\_RESERVE \
Protect Page protection. Can be one \
of: \
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
Supported on system versions: \
NT 4.0,Win 2000,Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtAllocateVirtualMemory \
NtCreateSection \
NtOpenSection \
NtUnmapViewOfSection
