### ThreadHandle

Open handle to any Thread Object, including caller's thread.

### ApcRoutine

Entry point to user *APC* routine.

### ApcRoutineContext

User defined parameter for `ApcRoutine`.

### ApcStatusBlock

???

### ApcReserved

???

---

Function adds user defined routine to thread's APC queue. This routine will be executed when thread will be signaled. You can manually empty APC queue by calling `NtTestAlert`.

# Documented by

* Tomasz Nowak

# See also

* `KiUserApcDispatcher`
* `NtTestAlert`
