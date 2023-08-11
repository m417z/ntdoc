NtListenPort is used by LPC server. \
PortHandle HANDLE to named Port \
Object, created with \
NtCreatePort. \
ConnectionRequest Result of call \- \
pointer to structure \
LPC\_MESSAGE filled with incomming connection data. \
Server process should create new thread starting from execution of \
NtAcceptConnectPort. Main thread should call \
NtListenPort again to make possible for other \
processes to connect to port.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
LPC\_MESSAGE \
NtAcceptConnectPort \
NtConnectPort \
NtCreatePort
