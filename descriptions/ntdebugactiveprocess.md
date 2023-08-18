Function NtDebugActiveProcess is used to attach Debug Object to any non-debugged
process.

### ProcessHandle

HANDLE to process being debugged (opened with enough access rights
- see NtOpenProcess).

### DebugObjectHandle

HANDLE to previously created Debug Object.

# Documented by

* Tomasz Nowak

# See also

* `NtCreateDebugObject`
* `NtOpenProcess`
* `NtRemoveProcessDebug`
