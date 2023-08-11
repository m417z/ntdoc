ATOM\_BASIC\_INFORMATION structure is returned as a \
result of call NtQueryInformationAtom \
with AtomBasicInformation \
information class. \
UsageCount Internal Atom counter state. \
This value increments at every NtAddAtom \
call for current Atom, and it's decremented on every NtDeleteAtom \
function call. \
Flags \(?\), Only lowest \
bit is used. \
NameLength Size of Name array, in bytes. \
Name\[1\] Atom name.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
ATOM\_INFORMATION\_CLASS \
NtAddAtom \
NtDeleteAtom \
NtQueryInformationAtom
