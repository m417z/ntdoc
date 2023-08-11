Function NtOpenSemaphore opens named Semaphore \
Object. This operation doesn't modify semaphore's internal \
counter. \
SemaphoreHandle Result of call \- \
pointer to HANDLE to Semaphore Object. \
DesiredAccess Access rights, descripted \
in \
NtCreateSemaphore. \
ObjectAttributes Pointer to \
OBJECT\_ATTRIBUTES structure containing semaphore's name.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateSemaphore
