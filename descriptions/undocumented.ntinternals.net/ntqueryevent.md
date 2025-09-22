### EventHandle

`HANDLE` to Event Object opened with `EVENT_QUERY_STATE` access.

### EventInformationClass

See `EVENT_INFORMATION_CLASS` for details.

### EventInformation

Caller's allocated buffer for result data.

### EventInformationLength

Length of `EventInformation` buffer, in bytes.

### ReturnLength

Returns required/used size of `EventInformation` buffer.

---

Currently there're only one information class for use with Event Object. See `EVENT_INFORMATION_CLASS` for details.

# Documented by

* Tomasz Nowak

# See also

* `EVENT_BASIC_INFORMATION`
* `EVENT_INFORMATION_CLASS`
* `NtCreateEvent`
* `NtOpenEvent`
