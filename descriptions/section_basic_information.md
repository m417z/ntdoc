Structure SECTION\_BASIC\_INFORMATION is returned as a \
result of call \
NtQuerySection with \
SectionBasicInformation information class. \
Unknown \(?\), always set \
to zero. \
SectionAttributes Can be one or \
combination of: \
SEC\_RESERVE \
SEC\_IMAGE \
SEC\_FILE \
SectionSize Size of section, in bytes. \
This value equals to section's size declared in a call to \
NtCreateSection or \
NtExtendSection.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtCreateSection \
NtExtendSection \
NtQuerySection \
SECTION\_IMAGE\_INFORMATION \
SECTION\_INFORMATION\_CLASS
