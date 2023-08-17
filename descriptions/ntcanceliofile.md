Function `NtCancelIoFile` sends cancel signal to Device Driver. If any IO operation with specified file is pending, it is immediatelly canceled.

### FileHandle

`HANDLE` to File Object.

### IoStatusBlock

IO result of call.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtFlushBuffersFile`
* `NtQueryInformationFile`
* `NtReadFile`
* `NtSetEaFile`
* `NtSetInformationFile`
* `NtWriteFile`
