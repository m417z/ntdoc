Function NtQueryMultipleValueKey returns data of one \
or more values under specified Key Object. \
KeyHandle HANDLE to Key Object \
opened with KEY\_READ access. \
ValuesList Array of \
KEY\_MULTIPLE\_VALUE\_INFORMATION structures contains names of \
values to query. \
NumberOfValues Number of members in \
ValueList array. \
DataBuffer User's allocated buffer \
receiving queried value's data. \
BufferLength Pointer to value specifing \
length of DataBuffer, in \
bytes. \
RequiredLength Optionally pointer to \
value receiving required DataBuffer length, in bytes.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
KEY\_MULTIPLE\_VALUE\_INFORMATION \
NtCreateKey \
NtEnumerateValueKey \
NtOpenKey \
NtQueryValueKey
