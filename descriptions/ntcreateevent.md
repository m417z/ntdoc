This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwcreateevent).

---

### EventHandle

Result of call - `HANDLE` to newly created Event Object.

### DesiredAccess

Assess rights associated with created event. Can be one of following values from **\<winnt.h\>**:

* `EVENT_QUERY_STATE`
* `EVENT_MODIFY_STATE`
* `EVENT_ALL_ACCESS`

### ObjectAttributes

Optional name of Event Object for multiprocess use.

### EventType

See `EVENT_TYPE` for details.

### InitialState

State of event immediatelly after creation.

# Documented by

* Tomasz Nowak

# See also

* `EVENT_TYPE`
* `NtOpenEvent`
