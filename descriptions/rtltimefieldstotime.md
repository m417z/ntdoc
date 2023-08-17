This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-rtltimefieldstotime).

---

Function `RtlTimeFieldsToTime` converts user-readable structure `TIME_FIELDS` to *64-bit* integer.

### TimeFields

Pointer to `TIME_FIELDS` structure containing time to convert.

### Time

Pointer to `LARGE_INTEGER` receiving converted time.

---

See also oposite function `RtlTimeToTimeFields`.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `RtlTimeToTimeFields`
* `TIME_FIELDS`
