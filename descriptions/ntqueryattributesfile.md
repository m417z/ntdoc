### ObjectAttributes

Contains file name, in NT Objects Namespace format.

### FileAttributes

Because only four bytes at offset *0x20* are used, this may be any buffer at least *0x24* bytes length. Time information fields from `FILE_BASIC_INFORMATION` are skipped.

---

Use of `NtQueryAttributesFile` is the easiest and the best way to check if file exist. `NtOpenFile` isn't good for this, because it modifies last access time for opened file. See `NtQueryDirectoryFile` for details.

# Documented by

* Tomasz Nowak

# See also

* `FILE_BASIC_INFORMATION`
* `NtOpenFile`
* `NtQueryDirectoryFile`
* `NtQueryFullAttributesFile`
* `NtQueryInformationFile`
