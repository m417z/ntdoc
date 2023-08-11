PHEAP\_ENUMERATION\_ROUTINE is defined as follows: \
typedef NTSTATUS \
\(\*PHEAP\_ENUMERATION\_ROUTINE\)\( \
                IN PVOID HeapHandle, \
                IN PVOID UserParam \
                \);
