This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/sysinfo/ntsetsysteminformation).

---

`NtSetSystemInformation` is used to set some inaccessible *KernelMode* variables. See also `NtQuerySystemInformation`.

### SystemInformationClass

Information class described in `SYSTEM_INFORMATION_CLASS`.

### SystemInformation

Pointer to data buffer to set.

### SystemInformationLength

Length of information in `SystemInformation` buffer, in bytes.

# Documented by

* Sven B. Schreiber
* Tomasz Nowak

# See also

* `NtQuerySystemInformation`
* `SYSTEM_INFORMATION_CLASS`
