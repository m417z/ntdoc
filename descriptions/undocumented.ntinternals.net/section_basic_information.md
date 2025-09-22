Structure `SECTION_BASIC_INFORMATION` is returned as a result of call `NtQuerySection` with `SectionBasicInformation` information class.

### Unknown

**(?)**, always set to zero.

### SectionAttributes

Can be one or combination of:

* `SEC_RESERVE`
* `SEC_IMAGE`
* `SEC_FILE`

### SectionSize

Size of section, in bytes. This value equals to section's size declared in a call to `NtCreateSection` or `NtExtendSection`.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateSection`
* `NtExtendSection`
* `NtQuerySection`
* `SECTION_IMAGE_INFORMATION`
* `SECTION_INFORMATION_CLASS`
