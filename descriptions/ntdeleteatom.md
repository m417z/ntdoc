Function `NtDeleteAtom` remove Atom from Global Atom Table. If Atom's reference counter is greater then *1*, function decrements this counter, but Atom stayed in Global Atom Table.

### Atom

Atom identifier.

# Documented by

* Tomasz Nowak

# See also

* `ATOM_BASIC_INFORMATION`
* `NtAddAtom`
* `NtFindAtom`
* `NtQueryInformationAtom`
