`ATOM_BASIC_INFORMATION` structure is returned as a result of call `NtQueryInformationAtom` with `AtomBasicInformation` information class.

### UsageCount

Internal Atom counter state. This value increments at every `NtAddAtom` call for current Atom, and it's decremented on every `NtDeleteAtom` function call.

### Flags

**(?)**, Only lowest bit is used.

### NameLength

Size of `Name` array, in bytes.

### Name[1]

Atom name.

# Documented by

* Tomasz Nowak

# See also

* `ATOM_INFORMATION_CLASS`
* `NtAddAtom`
* `NtDeleteAtom`
* `NtQueryInformationAtom`
