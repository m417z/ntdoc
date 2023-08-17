Enumeration type `SECTION_INFORMATION_CLASS` is used in a call to `NtQuerySection` function. 

This type can be one of:

### SectionBasicInformation

Result buffer contains structure `SECTION_BASIC_INFORMATION`. Buffer size shoud be set to *0x0C*.

### SectionImageInformation

Result buffer contains structure `SECTION_IMAGE_INFORMATION`. Buffer size shoud be set to *0x28*. This information class is accessable only where section was created with `HANDLE` to open executable file (see `NtCreateSection` for details).

# Documented by

* Tomasz Nowak

# See also

* `NtCreateSection`
* `NtOpenSection`
* `NtQuerySection`
* `SECTION_BASIC_INFORMATION`
* `SECTION_IMAGE_INFORMATION`
