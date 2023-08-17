Function `NtReleaseSemaphore` increments semaphore's counter, oposite to any waiting function (semaphore is signaled when semaphore's counter is greater then zero).

### SemaphoreHandle

`HANDLE` to Semaphore Object opened with `SEMAPHORE_MODIFY_STATE` access.

### ReleaseCount

Number of increments, typically set to *1*.

### PreviousCount

Optional pointer to `ULONG` value receiving semaphore's counter state before call.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateSemaphore`
* `NtOpenSemaphore`
* `NtQuerySemaphore`
