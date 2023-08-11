NtImpersonateClientOfPort is called by LPC server \
process to get security context of client. That means: client's \
Token Object is assiciated with calling server thread \(like \
NtSetInformationThread with \
ThreadImpersonationToken information class\). \
PortHandle HANDLE to Port Object \
opened with \
NtAcceptConnectPort call. \
Request Pointer to \
LPC\_MESSAGE structure contains reason of impersonation.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
LPC\_MESSAGE \
NtAcceptConnectPort \
NtOpenThreadToken \
NtQueryInformationThread \
NtSetInformationThread
