Structure FILE\_FULL\_EA\_INFORMATION is used for get or \
store Extended Attributes for NTFS files and directories. \
Extended Attributes \(EA\) is a list of pair \
Name\-Value. Name is capitalised ASCII string \
up to 256 characters long. Value is any data and can be up \
to 65536 bytes long. \
Structure can be used in a call to \
NtCreateFile and NtSetEaFile, or \
as a result of call NtQueryEaFile. \
NextEntryOffset Offset for next \
FILE\_FULL\_EA\_INFORMATION structure in buffer, \
relative to currently used structure. If current structure is last \
one in buffer, this field has value 0. \
Flags \- ??? \
EaNameLength Length of EA name, in \
bytes \(without leading zero\). \
EaValueLength Length of EA value, in \
bytes \(without leading zero\). \
EaName\[1\] User's allocated buffer \
contains ASCIIZ name and value. ASCII value must be finished by \
zero. \
Structure FILE\_FULL\_EA\_INFORMATION is also defined in \
Win2000 DDK.

Documented by: \
Tomasz Nowak \
Bo Branten \
Requirements:

Library: ntdll.lib

See also: \
FILE\_EA\_INFORMATION \
FILE\_GET\_EA\_INFORMATION \
NtCreateFile \
NtQueryEaFile \
NtSetEaFile
