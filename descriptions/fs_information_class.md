FS\_INFORMATION\_CLASS enumeration type is used in a \
call to NtQueryVolumeInformationFile \
and NtSetVolumeInformationFile. \
FileFsVolumeInformation \
Action \
: Query \
Buffer size \
: 0x18 \
Structure \
: FILE\_FS\_VOLUME\_INFORMATION \
FileFsLabelInformation \
Action \
: Set \
Buffer size \
: 0x08 \
Structure \
: FILE\_FS\_LABEL\_INFORMATION \
FileFsSizeInformation \
Action \
: Query \
Buffer size \
: 0x18 \
Structure \
: FILE\_FS\_SIZE\_INFORMATION \
FileFsDeviceInformation \
Action \
: Query \
Buffer size \
: 0x08 \
Structure \
: FILE\_FS\_DEVICE\_INFORMATION \
FileFsAttributeInformation \
Action \
: Query \
Buffer size \
: 0x10 \
Structure \
: FILE\_FS\_ATTRIBUTE\_INFORMATION \
FileFsControlInformation \
Action \
: Query, Set \
Buffer size \
: 0x30, 0x30 \
Structure \
: FILE\_FS\_CONTROL\_INFORMATION \
FileFsFullSizeInformation \
Action \
: Query \
Buffer size \
: 0x38 \
Structure \
: ??? \
FileFsObjectIdInformation \
Action \
: Set \
Buffer size \
: 0x38 \
Structure \
: ???

Documented by: \
Tomasz Nowak \
Bo Branten \
Reactos \
Requirements:

Library: ntdll.lib

See also: \
FILE\_FS\_ATTRIBUTE\_INFORMATION \
FILE\_FS\_CONTROL\_INFORMATION \
FILE\_FS\_DEVICE\_INFORMATION \
FILE\_FS\_LABEL\_INFORMATION \
FILE\_FS\_SIZE\_INFORMATION \
FILE\_FS\_VOLUME\_INFORMATION \
NtQueryVolumeInformationFile \
NtSetVolumeInformationFile
