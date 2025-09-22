This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-rtltimetotimefields).

---

Function `RtlTimeToTimeFields` converts *64-bit* time to user-readable structure `TIME_FIELDS`.

### Time

Pointer to `LARGE_INTEGER` contains time to convert.

### TimeFields

Result of call - pointer to `TIME_FIELDS` structure.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `RtlTimeFieldsToTime`
* `TIME_FIELDS`
