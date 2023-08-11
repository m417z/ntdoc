Function NtCreateToken creates Token Object. \
TokenHandle Result of call \- pointer to \
HANDLE to Token Object. \
DesiredAccess Can be one or more of \
following: \
TOKEN\_ASSIGN\_PRIMARY \
TOKEN\_DUPLICATE \
TOKEN\_IMPERSONATE \
TOKEN\_QUERY \
TOKEN\_QUERY\_SOURCE \
TOKEN\_ADJUST\_PRIVILEGES \
TOKEN\_ADJUST\_GROUPS \
TOKEN\_ADJUST\_DEFAULT \
TOKEN\_ADJUST\_SESSIONID \
TOKEN\_ALL\_ACCESS \
ObjectAttributes Pointer to \
OBJECT\_ATTRIBUTES structure. \
TokenType \(?\), see \
TOKEN\_TYPE enumeration type. \
AuthenticationId \(?\), see \
NtAllocateLocallyUniqueId security function. \
ExpirationTime \(?\), \
pointer to LARGE\_INTEGER value contains time in \
100\-ns format. \
TokenUser \(?\), see \
TOKEN\_USER structure. \
TokenGroups \(?\), see \
TOKEN\_GROUPS structure. \
TokenPrivileges \(?\), see \
TOKEN\_PRIVILEGES \
structure. \
TokenOwner \(?\), see \
TOKEN\_OWNER structure. \
TokenPrimaryGroup \(?\), \
see TOKEN\_PRIMARY\_GROUP \
structure. \
TokenDefaultDacl \(?\), see \
TOKEN\_DEFAULT\_DACL \
structure. \
TokenSource \(?\), see \
TOKEN\_SOURCE structure.

Documented by: \
Reactos \
Requirements:

Library: ntdll.lib \
Privilege: SE\_CREATE\_TOKEN\_PRIVILEGE

See also: \
NtAllocateLocallyUniqueId \
NtDuplicateToken \
NtOpenProcessToken \
NtOpenThreadToken \
NtQueryInformationToken \
NtSetInformationToken
