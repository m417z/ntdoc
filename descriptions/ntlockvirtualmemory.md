### LockOption

Can be one or both of following values:

	#define `VM_LOCK_1`		*0x0001*	<I><FONT COLOR="Green">// This is used, when calling </I>`KERNEL32.DLL`* *`VirtualLock`<I> routine</FONT> \
</I>	#define `VM_LOCK_2`		*0x0002*	<I><FONT COLOR="Green">// This require </I>**SE_LOCK_MEMORY_NAME**<I> privilege</FONT> \
</I>

# Documented by

* Tomasz Nowak
* ReactOS

# Requirements

Privilege: `SE_LOCK_MEMORY_NAME`

# See also

* `NtAllocateVirtualMemory`
* `NtFreeVirtualMemory`
* `NtUnlockVirtualMemory`
