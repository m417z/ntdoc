FILE\_FS\_ATTRIBUTE\_INFORMATION is output buffer in a \
call to \
NtQueryVolumeInformationFile function with \
FileFsAttributeInformation information class. \
FileSystemAttributes \- ??? \
\(0x1F\) \
MaximumComponentNameLength Maximum \
length of file name on specified device. \
FileSystemNameLength Length of \
FileSystemName array, in \
bytes. \
FileSystemName\[1\] Name of File System \
on specified device \(ex. "NTFS"\).

Documented by: \
Bo Branten \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
FS\_INFORMATION\_CLASS \
NtQueryVolumeInformationFile
