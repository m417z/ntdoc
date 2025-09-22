This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationthread).

---

### ThreadHandle

Handle to Thread Object opened with `THREAD_QUERY_INFORMATION` access.

### ThreadInformationClass

Information class defined in `THREAD_INFORMATION_CLASS` enumerated type.

### ThreadInformation

Caller's allocated buffer for results.

### ThreadInformationLength

Length of buffer, in bytes.

### ReturnLength

Optional pointer to required buffer length.

---

See `THREAD_INFORMATION_CLASS` for more information.

# Documented by

* Tomasz Nowak

# See also

* `NtSetInformationThread`
* `THREAD_INFORMATION_CLASS`
