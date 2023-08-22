This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntsetinformationkey).

---

### InformationClass

See `<ntddk.h>` for possible values. Currently only `KEY_WRITE_TIME_INFORMATION` is supported.

### KeyInformationData

See `<ntddk.h>` for detailed structure `KEY_WRITE_TIME_INFORMATION`.

# See also

* `NtCreateKey`
* `NtEnumerateKey`
* `NtOpenKey`
* `NtQueryKey`
