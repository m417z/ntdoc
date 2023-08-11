Function NtSignalAndWaitForSingleObject signals one \
object and wait for second object. See also Win32 API \
SignalObjectAndWait description in Microsoft SDK. \
ObjectToSignal HANDLE to object \
to signal. Possible object's types are: \
Event Object \
Semaphore Object \
Mutant Object \
WaitableObject HANDLE to object \
to wait for. Can be any waitable object. \
Alertable If set, APC Routine \
can break waiting. \
Time Optionally pointer to \
LARGE\_INTEGER value specifing time \(absolute or relative\) \
when function time outs \(in 100\-ns units\). Negative value \
means relative time.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateEvent \
NtCreateMutant \
NtCreateSemaphore \
NtWaitForMultipleObjects \
NtWaitForSingleObject
