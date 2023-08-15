This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushvirtualmemory)

NtFlushVirtualMemory flushes mapped section view to \
file. \
ProcessHandle HANDLE of process \
containing mapped view of section to flush. \
\*BaseAddress Pointer to PVOID \
value containing address of memory area to flush. On output this \
value is rounded to Page Size \(0x1000\). \
NumberOfBytesToFlush Pointer to \
ULONG value specifing length of area to flush. On output \
this value is rounded up to Page Size \(0x1000\). \
IoStatusBlock Pointer to \
IO\_STATUS\_BLOCK structure. After call Information member \
contains the same value as NumberOfBytesToFlush parameter. \
WARNING: Two \(or more\) memory pages mapped in different \
calls of \
NtMapViewOfSection cannot be flushed in one function call, even \
if both has the same SECTION as a source.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateSection \
NtMapViewOfSection \
NtOpenSection \
NtUnmapViewOfSection
