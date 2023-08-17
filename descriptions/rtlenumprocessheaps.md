`PHEAP_ENUMERATION_ROUTINE` is defined as follows:

```cpp
typedef NTSTATUS
(*PHEAP_ENUMERATION_ROUTINE)(
        IN PVOID HeapHandle,
        IN PVOID UserParam
        );
```

### HeapEnumerationRoutine

User function address.

### Param

User defined parameter, will be placed as `UserParam` in every `HeapEnumerationRoutine` calls.

# Documented by

* Tomasz Nowak

# See also

* `RtlGetProcessHeaps`
