Function NtCreatePagingFile is typically used by \
Control Panel's "System" applet for creating new paged \
files. \
PageFileName System path to newly \
created paged file. \
MiniumSize Minimum size of paged file, \
in bytes. This value must be multiply of page size \(0x1000 \
bytes on x86\), and must be greater then 2MB \
\(0x02000000 bytes\). \
MaxiumSize Maximum size of paged file, \
in bytes. Also this value must be multiply of page size. Minimal \
value accepted is 5MB \(0x05000000 bytes\). \
ActualSize Optional \(and currently \
unused\) parameter.

Documented by: \
Tomasz Nowak \
Reactos \
Requirements:

Library: ntdll.lib \
Privilege: SE\_CREATE\_PAGEFILE\_PRIVILEGE

See also: \
SYSTEM\_PAGEFILE\_INFORMATION
