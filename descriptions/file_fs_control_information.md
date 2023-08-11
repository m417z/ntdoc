Structure FILE\_FS\_CONTROL\_INFORMATION is user as \
input and output buffers in calls to \
NtQueryVolumeInformationFile and \
NtSetVolumeInformationFile with information class set to \
FileFsControlInformation. \
FreeSpaceStartFiltering \
FreeSpaceThreshold \
FreeSpaceStopFiltering \
DefaultQuotaThreshold \
DefaultQuotaLimit \
FileSystemControlFlags

Documented by: \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FS\_INFORMATION\_CLASS \
NtQueryVolumeInformationFile \
NtSetVolumeInformationFile
