Function NtAccessCheck should be used by server \
applications working in SYSTEM context for check access to \
object for connected client's token. See similar Win32 API \
AccessCheck in Microsoft SDK. \
SecurityDescriptor Pointer to SECURITY\_DESCRIPTOR structure. \
ClientToken HANDLE to client's \
Token Object opened with TOKEN\_QUERY access. \
DesiredAccess ACCESS\_MASK \
required by client. \
GenericMapping Pointer to \
GENERIC\_MAPPING structure. Caller can take it in a call to \
NtQueryObject. \
RequiredPrivilegesBuffer Function fills \
this buffer with structure PRIVILEGE\_SET contains required \
privileges. \
BufferLength Pointer to ULONG \
value. On input this value means size of RequiredPrivilegesBuffer buffer. If buffer \
was to small, required buffer size is avaiable on output. \
GrantedAccess Pointer to \
ACCESS\_MASK value receiving granted access for object. \
AccessStatus Result of access check, in \
typical NTSTATUS format.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtImpersonateClientOfPort \
NtImpersonateThread \
NtOpenProcessToken \
NtOpenThreadToken \
NtPrivilegeCheck \
NtQueryObject \
NtQuerySecurityObject
