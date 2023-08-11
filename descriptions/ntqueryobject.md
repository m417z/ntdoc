Function NtQueryObject retrives some informations \
about any or all objects opened by calling process. It can be used \
with any type of object. \
ObjectHandle HANDLE to object. \
ObjectInformationClass Kind of \
information to retrive. See \
OBJECT\_INFORMATION\_CLASS for possible values list. \
ObjectInformation Output buffer \
allocated by caller. \
Length Length of ObjectInformation buffer, in bytes. \
ResultLength Pointer to ULONG \
value that contains required size of ObjectInformation buffer after function \
call.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtSetInformationObject \
OBJECT\_INFORMATION\_CLASS
