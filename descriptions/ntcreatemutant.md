### MutantHandle

Result of function call - handle to newly created Mutant object.

### DesiredAccess

In most cases there's `MUTANT_ALL_ACCESS`. See **\<WinNT.h\>** or **\<WinBase.h\>** for other information about Mutant objects access rights.

### ObjectAttributes

May be used to creation named Mutant objects. Named Mutant can be used by more then one process.

### InitialOwner

If *TRUE*, Mutant is created with non-signaled state. Caller should call `NtReleaseMutant` after program initialization.

---

Mutant object live in object namespace as long as at least one handle is still open. To destroy Mutant, just call `NtClose` with `MutantHandle`.

# Documented by

* Tomasz Nowak
* Sven B. Schreiber

# See also

* `NtClose`
* `NtOpenMutant`
