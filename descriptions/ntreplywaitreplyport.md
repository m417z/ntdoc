NtReplyWaitReplyPort sends REPLY and waits for other \
side REPLY. \
PortHandle HANDLE to Port \
Object. \
Reply There's a pointer to \
LPC\_MESSAGE structure. On input, should be filled with REPLY \
data by user. On output it contains REPLY from other side.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
LPC\_MESSAGE \
NtAcceptConnectPort \
NtConnectPort \
NtReplyPort \
NtReplyWaitReceivePort \
NtRequestWaitReplyPort
