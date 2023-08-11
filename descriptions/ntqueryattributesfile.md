ObjectAttributes Contains file name, in \
NT Objects Namespace format. \
FileAttributes Becouse only four bytes \
at offset 0x20 are used, this may be any buffer at least \
0x24 bytes length. Time information fields from FILE\_BASIC\_INFORMATION are \
skipped. \
Use of NtQueryAttributesFile is the easiest and the \
best way to check if file exist. \
NtOpenFile isn't good for this, becouse it modifies last access \
time for opened file. See NtQueryDirectoryFile for \
details.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
FILE\_BASIC\_INFORMATION \
NtOpenFile \
NtQueryDirectoryFile \
NtQueryFullAttributesFile \
NtQueryInformationFile
