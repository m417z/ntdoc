This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwqueryvolumeinformationfile), [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryvolumeinformationfile), and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile).

---

### FileHandle

`HANDLE` to File Object.

### IoStatusBlock

IO result of call.

### FileSystemInformation

Caller's allocated buffer for output data.

### Length

Length of `FileSystemInformation` buffer, in bytes.

### FileSystemInformationClass

Information class descripted in `FS_INFORMATION_CLASS` topic.

---

`NtQueryVolumeInformationFile` gives information about volume (device) containing file specified as `FileHandle` parameter.

# Documented by

* Tomasz Nowak
* Bo Branten

# See also

* `FS_INFORMATION_CLASS`
* `NtOpenFile`
* `NtSetVolumeInformationFile`
