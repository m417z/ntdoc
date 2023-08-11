NtRequestWaitReplyPort is used typically by client \
side in LPC connection. \
PortHandle HANDLE to Port \
Object. \
Request Pointer to \
LPC\_MESSAGE buffer contains request data. \
IncomingReply Pointer to \
LPC\_MESSAGE buffer filled on return with reply from other \
side.

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
NtReplyWaitReplyPort \
NtRequestPort
