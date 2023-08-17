### Size

Size of structure, in bytes.

### ProcessHandle

*HANDLE* to newly created Process object.

### ThreadHandle

*HANDLE* to Thread object representing main thread in process.

### ClientId

Unique Id of process and thread.

### ImageInformation

Some information from *PE header*. Created in result of call `NtQuerySection` with `SectionImageInformation` class.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `NtQuerySection`
* `RtlCreateUserProcess`
* `SECTION_IMAGE_INFORMATION`
