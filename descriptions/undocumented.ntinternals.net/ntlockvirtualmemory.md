### LockOption

Can be one or both of following values:

```cpp
#define VM_LOCK_1       0x0001  // This is used, when calling KERNEL32.DLL VirtualLock routine
#define VM_LOCK_2       0x0002  // This require SE_LOCK_MEMORY_NAME privilege
```

# Documented by

* Tomasz Nowak
* ReactOS

# Requirements

Privilege: `SE_LOCK_MEMORY_NAME`

# See also

* `NtAllocateVirtualMemory`
* `NtFreeVirtualMemory`
* `NtUnlockVirtualMemory`
