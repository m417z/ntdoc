This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntquerysecurityobject) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerysecurityobject).

---

Function `NtQuerySecurityObject` retrieve object's Security Descriptor.

### ObjectHandle

`HANDLE` to any object opened with `READ_CONTROL` access.

### SecurityInformationClass

Can be combination of:

* `OWNER_SECURITY_INFORMATION`
* `GROUP_SECURITY_INFORMATION`
* `DACL_SECURITY_INFORMATION`
* `SACL_SECURITY_INFORMATION`

### DescriptorBuffer

Result of call - pointer to `SECURITY_DESCRIPTOR` structure.

### DescriptorBufferLength

Size of buffer, in bytes.

### RequiredLength

Pointer to value receiving required length of buffer.

# Documented by

* Tomasz Nowak

# See also

* `NtSetSecurityObject`
* `SECURITY_DESCRIPTOR`
