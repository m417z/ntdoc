This flags indicates that the thread should not be suspended when the system suspends or freezes the process. See [this post](https://secret.club/2021/01/04/thread-stuff.html) for more details about the flag. For the differences between suspension, freezing, and deep freezing, see [this repository](https://github.com/diversenok/Suspending-Techniques).

# Applicable to
 - `NtCreateThreadEx`

# Related flags
 - `THREAD_CREATE_FLAGS_NONE`
 - `THREAD_CREATE_FLAGS_CREATE_SUSPENDED`
 - `THREAD_CREATE_FLAGS_SKIP_THREAD_ATTACH`
 - `THREAD_CREATE_FLAGS_HIDE_FROM_DEBUGGER`
 - `THREAD_CREATE_FLAGS_LOADER_WORKER`
 - `THREAD_CREATE_FLAGS_SKIP_LOADER_INIT`

# See also
 - `NtSuspendProcess`
 - `NtResumeProcess`
