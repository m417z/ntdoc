This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopendirectoryobject).

---

### DirectoryObjectHandle

Pointer to `HANDLE` value representing opened Directory Object.

### DesiredAccess

Access mask. See `NtCreateDirectoryObject` for possible values.

### ObjectAttributes

Must contains valid Directory Object name.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateDirectoryObject`
* `NtQueryDirectoryObject`
