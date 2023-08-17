`NtSetSystemInformation` is used to set some unaccessable *KernelMode* variables. See also `NtQuerySystemInformation`.

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
