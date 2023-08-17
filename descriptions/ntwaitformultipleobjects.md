### ObjectCount

Number of objects in `ObjectsArray` array.

### ObjectsArray

Pointer to array of `HANDLE`. Each must be opened with `SYNCHRONIZE` access.

### WaitType

Can be `WaitAllObjects` or `WaitAnyObject`.

### Alertable

If set, thread is signaled (*APC* routines queued for this thread are executed).

### TimeOut

Time-out interval.

---

`NtWaitForMultipleObjects` is used typically to response for notyfications. For synchronization purposes you should use `NtWaitForSingleObject`.

# Documented by

* Tomasz Nowak

# See also

* `NtSignalAndWaitForSingleObject`
* `NtWaitForSingleObject`
* `OBJECT_WAIT_TYPE`
