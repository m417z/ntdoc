Synchronization object called `KeyedEvent` is available in *Windows XP+* systems. It's useful when both (or more) threads have to wait for each other.

### KeyedEventHandle

`HANDLE` to newly created `KeyedEvent` object.

### DesiredAccess

The same values as for `Event` objects (typically `EVENT_ALL_ACCESS`).

### ObjectAttributes

Optionally name of object.

### Reserved

Have to be zero. Reserved for future use.

# Documented by

* Tomasz Nowak

# See also

* `NtOpenKeyedEvent`
* `NtReleaseKeyedEvent`
* `NtWaitForkeyedEvent`
