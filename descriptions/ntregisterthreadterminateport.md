PortHandle HANDLE to previously \
connected Port Object. \
Typically, NtRegisterThreadTerminatePort is used in \
CsrNewThread function, called \
before thread execution begins, but in thread context. \
Function associate PortHandle \
with thread, and sends LPC\_TERMINATION\_MESSAGE to \
specified port immediatelly after call \
NtTerminateThread.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
CsrNewThread \
LPC\_TERMINATION\_MESSAGE \
NtConnectPort \
NtTerminateThread
