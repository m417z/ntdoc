The `RtlCreateAtomTable` routine creates an atom table.

# Parameters

## `NumberOfBuckets` [in]

Specifies a number of groups used to organize atom entries. Each bucket can contain multiple atoms, each having different hash value which helps minimize hash collisions.

If `NumberOfBuckets` is set to 0, the routine falls back to the default bucket count of 37.

## `AtomTableHandle` [out]

Output of the new created atom table.

**Note:** The atom table pointer must be set to `NULL` before calling  `RtlCreateAtomTable`, as it automatically allocates the atom table handle using `RtlAllocateHeap`. 

If the pointer is not `NULL`, the routine returns an invalid atom table pointer to the `AtomTableHandle`.

The `AtomTableHandle` must contain a header located at the memory address of the atom table post-routine which should be `"Atom"`.

If the `AtomTableHandle` doesn't contain this header, it indicates that the atom table was not created properly or that the routine fails to create the atom table. 

This can occur if memory for the atom table was already allocated before calling `RtlCreateAtomTable`.

This header serves as an integrity check to verify that the atom table is created properly.

# Return

Returns `STATUS_SUCCESS`. 

The routine can return the following status code:
* `STATUS_NO_MEMORY`
   * If the routine fails to initialize the atom table handle, the routine  frees the allocated atom table before returning `STATUS_NO_MEMORY`.
   * If the routine fails to allocate the atom table handle from the heap.

# See Also

- `RtlEmptyAtomTable` 
- `RtlAddAtomToAtomTable`
- `RtlDestroyAtomTable`
- `RtlQueryAtomInAtomTable`
- `RtlGetIntegerAtom`
- `RtlPinAtomInAtomTable`
- `RtlLookupAtomInAtomTable`
