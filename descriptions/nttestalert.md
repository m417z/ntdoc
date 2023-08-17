You can use `NtTestAlert` to empty *APC queue* for current thread. If *APC queue* was empty before call, `NtTestAlert` has no efect.

`NtTestAlert` is typical *ntcall* kernel routine, accessable via `int 2Eh`. It check thread *APC queue*, and call `KiUserApcDispatcher`.

# Documented by

* Tomasz Nowak

# See also

* `KiUserApcDispatcher`
* `NtQueueApcThread`
