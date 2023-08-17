This function sends `HARDERROR_MSG` *LPC* message to listener (typically *CSRSS.EXE*). See `NtSetDefaultHardErrorPort` for more information.

### ErrorStatus

Error code.

### NumberOfParameters

Number of optional parameters in `Parameters` array.

### UnicodeStringParameterMask

Optional string parameter (can be only one per error code).

### *Parameters

Array of `DWORD` parameters for use in error message string.

### ResponseOption

See `HARDERROR_RESPONSE_OPTION` for possible values description.

### Response

Pointer to `HARDERROR_RESPONSE` enumeration.

---

`NtRaiseHardError` is easy way to display message in *GUI* without loading *Win32 API* libraries.

# Documented by

* Tomasz Nowak

# See also

* `HARDERROR_MSG`
* `HARDERROR_RESPONSE`
* `HARDERROR_RESPONSE_OPTION`
* `NtSetDefaultHardErrorPort`
