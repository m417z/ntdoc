Function NtPrivilegeCheck is used to check state of \
any privileges in Token Object. It's also descripted in \
Microsoft SDK as PrivilegeCheck. \
TokenHandle HANDLE to Token \
Object opened with TOKEN\_QUERY access. \
RequiredPrivileges Pointer to PRIVILEGE\_SET structure contains \
definitions of privileges to check. \
Result Result of call \- pointer to \
BOOLEAN value containing TRUE is all asked privileges \
are enabled.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtAdjustPrivilegesToken \
NtCreateToken \
NtOpenProcessToken \
NtOpenThreadToken \
PRIVILEGE\_SET
