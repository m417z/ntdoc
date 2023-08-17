Function with similar functionality as `NtReleaseKeyedEvent`. In my opinion it is not needed and exists only for future vision of `KeyedEvent` objects or just as a mistake.

### KeyedEventHandle

`HANDLE` for previously opened `KeyedEvent` object.

### Key

Value to wait for, must have lowest bit clear.

### Alertable

If set, waiting can be broken by alerting thread.

### Timeout

Optinally pointer for timing out value.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateKeyedEvent`
* `NtOpenKeyedEvent`
* `NtReleaseKeyedEvent`
