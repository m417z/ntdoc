You can use `NtTestAlert` to empty *APC queue* for current thread. If *APC queue* was empty before call, `NtTestAlert` has no effect.

`NtTestAlert` is typical *ntcall* kernel routine, accessible via `int 2Eh`. It check thread *APC queue*, and call `KiUserApcDispatcher`.

# Documented by

* Tomasz Nowak

# See also

* `KiUserApcDispatcher`
* `NtQueueApcThread`
