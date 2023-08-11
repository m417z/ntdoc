Function NtQuerySecurityObject retrieve object's \
Security Descriptor. \
ObjectHandle HANDLE to any \
object opened with READ\_CONTROL access. \
SecurityInformationClass Can be \
combination of: \
OWNER\_SECURITY\_INFORMATION \
GROUP\_SECURITY\_INFORMATION \
DACL\_SECURITY\_INFORMATION \
SACL\_SECURITY\_INFORMATION \
DescriptorBuffer Result of call \- \
pointer to SECURITY\_DESCRIPTOR structure. \
DescriptorBufferLength Size of buffer, \
in bytes. \
RequiredLength Pointer to value \
receiving required length of buffer.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtSetSecurityObject \
SECURITY\_DESCRIPTOR
