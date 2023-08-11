NtQueryInformationAtom is used to get single Atom \
properties or to read Global Atom Table. \
Atom Atom to query. If AtomInformationClass parameter is AtomTableInformation, Atom parameter is not used. \
AtomInformationClass See ATOM\_INFORMATION\_CLASS \
enumeration type for details. \
AtomInformation Result of call \- \
pointer to user's allocated buffer for data. \
AtomInformationLength Size of \
AtomInformation buffer, in \
bytes. \
ReturnLength Pointer to ULONG \
value contains required AtomInformation buffer size.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
ATOM\_INFORMATION\_CLASS \
ATOM\_TABLE\_INFORMATION \
NtAddAtom \
NtFindAtom
