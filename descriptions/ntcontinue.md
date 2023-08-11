ThreadContext Pointer to CONTEXT \
structure for current thread. \
RaiseAlert If set, remove \
Alerted state from current Thread Object. \
You can use NtContinue after processing exception for \
continue executing thread. System uses NtContinue \
also in APC processing.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateThread \
NtGetContextThread \
NtSetContextThread
