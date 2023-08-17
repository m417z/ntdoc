This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwloaddriver).

---

### DriverServiceName

Registry path in system format. Path must begin with **"//registry//machine//SYSTEM//CurrentControlSet//Services//..."** where **"..."** is driver symbolic name. \
Key must have at least 2 values:

* **"ImagePath"** System path to file, in UNICODE format

* **"Type"** Set to 1.

# Requirements

Privilege: `SeLoadDriverPrivilege`

# See also

* `NtUnloadDriver`
