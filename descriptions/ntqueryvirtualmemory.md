This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryvirtualmemory) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvirtualmemory).

Function NtQueryVirtualMemory retrieves parameters of \
queried memory block. \
ProcessHandle HANDLE to process \
containing queried address in process'es address space. \
BaseAddress Virtual address to \
query. \
MemoryInformationClass Information \
class defined in MEMORY\_INFORMATION\_CLASS \
enumeration type. Currently only one class is supported. \
Buffer As long as only MemoryBasicInformation is \
supported, this value points to structure \
MEMORY\_BASIC\_INFORMATION, defined in \
&lt;WINNT.h&gt; and described in MS SDK. \
Length Length of Buffer, in bytes. \
ResultLength Optionally pointer to \
ULONG value receiving required size of Buffer, in bytes.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
MEMORY\_BASIC\_INFORMATION \
MEMORY\_INFORMATION\_CLASS \
NtAllocateVirtualMemory \
NtFreeVirtualMemory \
NtLockVirtualMemory \
NtProtectVirtualMemory
