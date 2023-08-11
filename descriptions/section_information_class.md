Enumeration type SECTION\_INFORMATION\_CLASS is used in \
a call to \
NtQuerySection function. \
This type can be one of: \
SectionBasicInformation Result buffer \
contains structure SECTION\_BASIC\_INFORMATION. \
Buffer size shoud be set to 0x0C. \
SectionImageInformation Result buffer \
contains structure SECTION\_IMAGE\_INFORMATION. \
Buffer size shoud be set to 0x28. This information class is \
accessable only where section was created with HANDLE to \
open executable file \(see \
NtCreateSection for details\).

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateSection \
NtOpenSection \
NtQuerySection \
SECTION\_BASIC\_INFORMATION \
SECTION\_IMAGE\_INFORMATION
