This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationthread).

---

### ThreadHandle

Handle to Thread Object opened with `THREAD_SET_INFORMATION` access.

### ThreadInformationClass

Information class to set to. See `THREAD_INFORMATION_CLASS` for detailed description of use.

### ThreadInformation

Pointer to value to set.

### ThreadInformationLength

Length of value to set.

---

See `THREAD_INFORMATION_CLASS` for more information.

# Documented by

* Tomasz Nowak

# See also

* `NtQueryInformationThread`
* `THREAD_INFORMATION_CLASS`
