This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenfile).

\(Also avaiable in 2000 DDK.\) \
FileHandle Result of call. \
DesiredAccess Access mask to opened \
file object. \
ObjectAttributes File name, path etc. \
See \
NtCreateFile for more information. \
IoStatusBlock Completion status of \
call. \
ShareAccess Sharing option defined as \
FILE\_SHARE\_\*. \
OpenOptions Open options.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateFile
