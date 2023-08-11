Function NtQueryInformationToken receives \
informations specified by information class from Token Object. See \
also Win32 API GetTokenInformation. \
TokenHandle HANDLE to Token \
Object opened with TOKEN\_QUERY access. \
TokenInformationClass Information class \
descripted in TOKEN\_INFORMATION\_CLASS \
topic. \
TokenInformation User's allocated \
buffer for output data. Format of output buffer depends on \
TokenInformationClass \
parameter. \
TokenInformationLength Length of \
TokenInformation buffer, in \
bytes. \
ReturnLength If output buffer is to \
small, value under this parameter receives required length.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateToken \
NtOpenProcessToken \
NtOpenThreadToken \
NtSetInformationToken \
TOKEN\_INFORMATION\_CLASS
