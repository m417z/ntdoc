This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwclose).

---

### ObjectHandle

Handle to open object. \
If `ObjectHandle` is last reference to object in system, object will be removed from memory.
