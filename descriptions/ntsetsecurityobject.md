Function NtSetSecurityDescriptor writes object's \
Security Descriptor. \
ObjectHandle HANDLE to object of \
any type. Must be opened with WRITE\_DAC or \
WRITE\_OWNER access dependly to SecurityInformationClass parameter. \
SecurityInformationClass See \
NtQuerySecurityObject for possible values. \
DescriptorBuffer Pointer to user's \
allocated SECURITY\_DESCRIPTOR to set.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQuerySecurityObject \
SECURITY\_DESCRIPTOR
