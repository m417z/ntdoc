Structure FILE\_RENAME\_INFORMATION is used as input \
buffer for function \
NtSetInformationFile, called with \
FileRenameInformation information class. Using this structure \
caller can rename file, or move it into other directory. \
ReplaceIfExists If set, and file with \
the same name as destination exist, it will be replaced. If no, \
STATUS\_OBJECT\_NAME\_COLLISION is returned. \
RootDirectory Optional HANDLE to \
parent directory for destination file. \
FileNameLength Length of FileName array, in bytes. \
FileName\[1\] UNICODE string specifing \
destination file name. If RootDirectory is NULL, it must \
contains full system path, or only destination file name for \
in\-place rename operation.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_INFORMATION\_CLASS \
NtCreateFile \
NtNotifyChangeDirectoryFile \
NtOpenFile \
NtSetInformationFile
