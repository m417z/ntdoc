This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushbuffersfile).

---

Function `NtFlushBuffersFile` flushes currently cashed data and write it to storage.

### FileHandle

`HANDLE` to File Object.

### IoStatusBlock

IO result of call.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtWriteFile`
