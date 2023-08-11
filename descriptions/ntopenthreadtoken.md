ThreadHandle HANDLE to thread \
object. \
DesiredAccess Access mask for opened \
Token Object. \
OpenAsSelf \- ??? \
TokenHandle Result of call \- \
HANDLE to Token Object associated with ThreadHandle thread. \
Usually Win32 threads don't have associated Tokens. If you want to \
associate Token for Thread Object, use NtSetInformationThread \
with ThreadImpersonationToken \
information class.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateToken \
NtOpenProcessToken \
NtOpenThread \
NtSetInformationThread \
THREAD\_INFORMATION\_CLASS
