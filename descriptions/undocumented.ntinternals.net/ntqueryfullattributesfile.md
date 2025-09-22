This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryfullattributesfile).

---

Function `NtQueryFullAttributesFile` is used to get information about file stored on low-speed connection device. See also description of `NtQueryAttributesFile` function.

### ObjectAttributes

Path and name of File Object to query.

### Attributes

Pointer to `FILE_NETWORK_OPEN_INFORMATION` structure.

# Documented by

* Tomasz Nowak

# See also

* `FILE_NETWORK_OPEN_INFORMATION`
* `NtQueryAttributesFile`
