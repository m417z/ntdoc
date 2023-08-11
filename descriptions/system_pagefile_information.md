Structure SYSTEM\_PAGEFILE\_INFORMATION is used as a \
result of call \
NtQuerySystemInformation with SystemPageFileInformation \
information class. If contains information about currently instaled \
Paged Files \(files used by system for swap paged pool memory to \
disk\). \
NextEntryOffset Offset to next \
SYSTEM\_PAGEFILE\_INFORMATION structure or zero, if \
it's last one. \
TotalSize Size of paged file, in pages \
\(Size of page depend on machine type, for x86 one \
page is 0x1000 \(4096\) bytes\). \
TotalInUse Number of currently used \
pages in paged file. \
PeakUsage Maximum number of pages used \
in this boot session. \
PageFileName System path to paged \
file.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreatePagingFile \
NtQuerySystemInformation \
SYSTEM\_INFORMATION\_CLASS
