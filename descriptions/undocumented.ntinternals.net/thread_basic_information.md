### ExitStatus

Thread exit status. If thread is not terminated, it has `STATUS_PENDING` value. See also *Win32 API* `GetExitCodeThread`.

### TebBaseAddress

Address of `TEB` structure for specified thread. See also `NtCurrentTeb`.

### ClientId

Unique process id and thread id.

### AffinityMask

Thread affinity mask. There are no *Win32* call GetThreadAffinityMask, but there's function `SetThreadAffinityMask` that's use `AffinityMask` value. See also `ThreadAffinityMask` information class.

### Priority

I'm not sure...

### BasePriority

Thread base priority. Used by **Kernel32.dll** in function `GetThreadPriority`. See also `ThreadBasePriority` information class.

---

Structure is used with `ThreadBasicInformation` information class in `NtQueryInformationThread` call.

# Documented by

* Tomasz Nowak

# See also

* `NtQueryInformationThread`
* `THREAD_INFORMATION_CLASS`
