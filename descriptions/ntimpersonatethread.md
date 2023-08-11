Function NtImpersonateThread assigns one thread's \
token to another. If source thread don't have associated Token \
Object, function use process'es token to impersonate destination \
thread. \
ThreadHandle HANDLE to source \
Thread Object. \
ThreadToImpersonate HANDLE to \
destination Thread Object opened with THREAD\_IMPERSONATE \
access. \
SecurityQualityOfService Pointer to \
SECURITY\_QUALITY\_OF\_SERVICE \
structure filled by user.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateThread \
NtImpersonateClientOfPort \
NtOpenThread \
SECURITY\_QUALITY\_OF\_SERVICE
