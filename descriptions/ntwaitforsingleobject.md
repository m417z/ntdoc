This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwwaitforsingleobject)

ObjectHandle HANDLE to alertable \
object. \
Alertable If set, calling thread is \
signaled, so all queued APC routines are executed. \
TimeOut Time\-out interval, in \
microseconds. NULL means infinite.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtSignalAndWaitForSingleObject \
NtWaitForMultipleObjects
