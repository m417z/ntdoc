The `RtlCreateAtomTable` function creates an atom table.

# Parameters

## `NumberOfBuckets` [in]

Specifies the number of groups used to organize atom entries. Each bucket can contain multiple atoms, each having a different hash value, which helps minimize hash collisions.

If `NumberOfBuckets` is set to 0, the function uses a default bucket count of 37.

## `AtomTableHandle` [in, out]

A pointer to a variable that receives the newly created atom table.

**Note:** The pointer referenced by `AtomTableHandle` must be set to `NULL` before calling `RtlCreateAtomTable`. If the pointer is not `NULL`, the function returns `ERROR_SUCCESS` without modifying the pointer or creating a new atom table.

# Return value

Returns `STATUS_SUCCESS` on success.

The function may return the following status code:
* `STATUS_NO_MEMORY`
  * The function failed to allocate the atom table handle from the heap.
  * The function failed to initialize the atom table handle; in this case, the allocated atom table is freed before returning.

# Remarks

After the atom table is created, the memory referenced by `AtomTableHandle` begins with the 4-byte header `"Atom"`.

# See also

- `RtlEmptyAtomTable` 
- `RtlAddAtomToAtomTable`
- `RtlDestroyAtomTable`
- `RtlQueryAtomInAtomTable`
- `RtlGetIntegerAtom`
- `RtlPinAtomInAtomTable`
- `RtlLookupAtomInAtomTable`
