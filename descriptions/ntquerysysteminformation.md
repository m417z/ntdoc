This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntquerysysteminformation).

---

`NtQuerySystemInformation` is used to check some system information available only in *KernelMode* (above *0x80000000*). \
All available (or all known) information classes are described in `SYSTEM_INFORMATION_CLASS`.

### SystemInformationClass

Information class (see `SYSTEM_INFORMATION_CLASS`).

### SystemInformation

User-allocated buffer for results. Sometimes this parameter can be *NULL* (`OPTIONAL`), if you check required buffer size (see below).

### SystemInformationLength

Length of `SystemInformation` buffer (in bytes).

### ReturnLength

Required length of `SystemInformation` buffer.

# Documented by

* Sven B. Schreiber
* Tomasz Nowak

# See also

* `NtSetSystemInformation`
* `SYSTEM_INFORMATION_CLASS`
