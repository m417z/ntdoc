Structure OBJECT\_BASIC\_INFORMATION is returned in a \
result of call \
NtQueryObject with \
ObjectBasicInformation information class. \
Attributes \
DesiredAccess \
HandleCount \
ReferenceCount \
PagedPoolUsage \
NonPagedPoolUsage \
Reserved\[3\] \
NameInformationLength \
TypeInformationLength \
SecurityDescriptorLength \
CreationTime \
Supported on system versions: \
NT 4.0,Win 2000,Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQueryObject \
OBJECT\_INFORMATION\_CLASS
