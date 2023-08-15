This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwallocatelocallyuniqueid)

Function allocates LUID \(Locally Unique Identifier\) \
for future use. \
LocallyUniqueId Pointer to LUID \
structure receiving new locally unique identifier.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtAllocateUuids \
NtCreateToken
