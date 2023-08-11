Function NtDeleteAtom remove Atom from Global Atom \
Table. If Atom's reference counter is greater then 1, \
function decrements this counter, but Atom stayed in Global Atom \
Table. \
Atom Atom identifier.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
ATOM\_BASIC\_INFORMATION \
NtAddAtom \
NtFindAtom \
NtQueryInformationAtom
