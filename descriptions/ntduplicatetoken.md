This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntduplicatetoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicatetoken).

Function NtDuplicateToken creates new Token Object \
basing on existing Token Object. \
ExistingToken HANDLE to Token \
Object opened with TOKEN\_DUPLICATE access. \
DesiredAccess Access mask for newly \
created token. Can be combination of: \
TOKEN\_ASSIGN\_PRIMARY \
TOKEN\_DUPLICATE \
TOKEN\_IMPERSONATE \
TOKEN\_QUERY \
TOKEN\_QUERY\_SOURCE \
TOKEN\_ADJUST\_PRIVILEGES \
TOKEN\_ADJUST\_GROUPS \
TOKEN\_ADJUST\_DEFAULT \
TOKEN\_ADJUST\_SESSIONID \
ObjectAttributes Optionally pointer to \
OBJECT\_ATTRIBUTES structure, containing token's name. \
ImpersonationLevel Level of \
impersonation for new token. \
TokenType Type of new token. \
NewToken Result of call \- pointer to \
HANDLE to new Token Object.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
NtCreateToken \
NtOpenProcessToken \
NtOpenThreadToken \
NtQueryInformationToken \
NtSetInformationToken
