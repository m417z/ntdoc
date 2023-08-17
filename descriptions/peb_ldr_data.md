### Length

Size of structure, used by `ntdll.dll` as structure version ID.

### Initialized

If set, loader data section for current process is initialized.

### SsHandle

???

### InLoadOrderModuleList

Doubly linked list containing pointers to `LDR_MODULE` structure for previous and next module in load order.

### InMemoryOrderModuleList

As above, but in memory placement order.

### InInitializationOrderModuleList

As `InLoadOrderModuleList`, but in initialization order.

# Documented by

* ReactOS
* Tomasz Nowak

# See also

* `LDR_MODULE`
* `PEB`
