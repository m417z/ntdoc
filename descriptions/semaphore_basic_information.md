Structure `SEMAPHORE_BASIC_INFORMATION` is retrieved as a result of call `NtQuerySemaphore` with `SemaphoreBasicInformation` information class.

### CurrentCount

Current state of semaphore's counter.

### MaximumCount

Maximum counter position, defined with call to `NtCreateSemaphore`.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateSemaphore`
* `NtQuerySemaphore`
* `SEMAPHORE_INFORMATION_CLASS`
