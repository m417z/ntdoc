This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetsecurityobject) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetsecurityobject).

---

Function `NtSetSecurityDescriptor` writes object's Security Descriptor.

### ObjectHandle

`HANDLE` to object of any type. Must be opened with `WRITE_DAC` or `WRITE_OWNER` access dependly to `SecurityInformationClass` parameter.

### SecurityInformationClass

See `NtQuerySecurityObject` for possible values.

### DescriptorBuffer

Pointer to user's allocated `SECURITY_DESCRIPTOR` to set.

# Documented by

* Tomasz Nowak

# See also

* `NtQuerySecurityObject`
* `SECURITY_DESCRIPTOR`
