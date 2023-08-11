Function NtSetInforamtionToken sets parameters of \
Token Objects. See also description of SetTokenInformation \
in Win32 API SDK. \
TokenHandle HANDLE to Token \
Object opened with TOKEN\_ADJUST\_DEFAULT access. \
TokenInformationClass Information class \
descripted in TOKEN\_INFORMATION\_CLASS \
topic. \
TokenInformation User's allocated \
buffer containing data to set to. \
TokenInformationLength Length of \
TokenInformation buffer, in \
bytes.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateToken \
NtOpenProcessToken \
NtOpenThreadToken \
NtQueryInformationToken \
TOKEN\_INFORMATION\_CLASS
