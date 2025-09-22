Function `NtCreateSemaphore` creates Semaphore Object with or without name in Object Namespace, and sets initial and maximum releases number.

### SemaphoreHandle

Result of call - pointer to `HANDLE` to Semaphore Object.

### DesiredAccess

Access rights to Semaphore Object. Can be one of:

* `SEMAPHORE_QUERY_STATE`
* `SEMAPHORE_MODIFY_STATE`
* `SEMAPHORE_ALL_ACCESS`

### ObjectAttributes

Optional pointer to `OBJECT_ATTRIBUTES` structure containing semaphore's name.

### InitialCount

Initial state of semaphore. Typically the same as `MaximumCount`.

### MaximumCount

Maximum releases number.

# Documented by

* Tomasz Nowak

# See also

* `NtOpenSemaphore`
* `NtQuerySemaphore`
