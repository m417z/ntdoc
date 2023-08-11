FILE\_INTERNAL\_INFORMATION structure is a result of \
call \
NtQueryInformationFile with \
FileInternalInformation information class. It's not possible to \
set file unique identifier. \
IndexNumber File indentifier, unique \
for file's device.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_ALL\_INFORMATION \
FILE\_INFORMATION\_CLASS \
NtCreateFile \
NtOpenFile \
NtQueryInformationFile
