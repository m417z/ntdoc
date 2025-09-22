`NtQueryInformationAtom` is used to get single Atom properties or to read Global Atom Table.

### Atom

Atom to query. If `AtomInformationClass` parameter is `AtomTableInformation`, `Atom` parameter is not used.

### AtomInformationClass

See `ATOM_INFORMATION_CLASS` enumeration type for details.

### AtomInformation

Result of call - pointer to user's allocated buffer for data.

### AtomInformationLength

Size of `AtomInformation` buffer, in bytes.

### ReturnLength

Pointer to `ULONG` value contains required `AtomInformation` buffer size.

# Documented by

* Tomasz Nowak

# See also

* `ATOM_INFORMATION_CLASS`
* `ATOM_TABLE_INFORMATION`
* `NtAddAtom`
* `NtFindAtom`
