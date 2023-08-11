NtQuerySystemInformation is used to check some system \
informations avaiable only in KernelMode \(above \
0x80000000\). All avaiable \(or all known\) information classes \
are described in SYSTEM\_INFORMATION\_CLASS. \
SystemInformationClass Information \
class \(see SYSTEM\_INFORMATION\_CLASS\). \
SystemInformation User\-allocated buffer \
for results. Sometimes this parameter can be NULL \
\(OPTIONAL\), if you check required buffer size \(see \
below\). \
SystemInformationLength Length of \
SystemInformation buffer \(in \
bytes\). \
ReturnLength Required length of \
SystemInformation buffer.

Documented by: \
Sven B. Schreiber \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtSetSystemInformation \
SYSTEM\_INFORMATION\_CLASS
