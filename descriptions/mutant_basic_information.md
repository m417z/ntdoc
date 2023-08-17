Use `MUTANT_BASIC_INFORMATION` as a buffer in `NtQueryMutant` call.

### CurrentCount

If `CurrentCount` is less than zero, mutant is signaled.

### OwnedByCaller

It's *TRUE* if mutant is signaled by caller's thread.

### AbandonedState

Is set when thread terminates without call `NtReleaseMutant`.

# Documented by

* Sven B. Schreiber
* Tomasz Nowak

# See also

* `NtCreateMutant`
* `NtOpenMutant`
* `NtQueryMutant`
* `NtReleaseMutant`
