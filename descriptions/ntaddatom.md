Function `NtAddAtom` creates new Atom in Global Atom Table. If Atom with the same name already exist, internal Atom counter is incremented.

### AtomName

UNICODE Atom name.

### Atom

Result of call - pointer to `RTL_ATOM`.

# Documented by

* Tomasz Nowak

# See also

* `ATOM_BASIC_INFORMATION`
* `NtDeleteAtom`
* `NtFindAtom`
* `NtQueryInformationAtom`
