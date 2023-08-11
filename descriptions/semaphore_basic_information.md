Structure SEMAPHORE\_BASIC\_INFORMATION is retrieved as \
a result of call \
NtQuerySemaphore with \
SemaphoreBasicInformation information class. \
CurrentCount Current state of \
semaphore's counter. \
MaximumCount Maximum counter position, \
defined with call to \
NtCreateSemaphore.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateSemaphore \
NtQuerySemaphore \
SEMAPHORE\_INFORMATION\_CLASS
