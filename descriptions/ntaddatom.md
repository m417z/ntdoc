Function NtAddAtom creates new Atom in Global Atom \
Table. If Atom with the same name already exist, internal Atom \
counter is incremented. \
AtomName UNICODE Atom name. \
Atom Result of call \- pointer to \
RTL\_ATOM.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
ATOM\_BASIC\_INFORMATION \
NtDeleteAtom \
NtFindAtom \
NtQueryInformationAtom
