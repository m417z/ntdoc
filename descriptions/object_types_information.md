This structure defines a collection of all registered types of kernel objects.

# Applicable to
 - `NtQueryObject` with `ObjectTypesInformation`.

# Members

## NumberOfTypes
The total number of types present.

## (Variable part)
The variable part of the structure contains variable-sized `OBJECT_TYPE_INFORMATION` structures following each other. Each entry occupies `sizeof(OBJECT_TYPE_INFORMATION) + entry->TypeName.MaximumLength` bytes and is aligned up to a pointer boundary.

# Parsing
Here is an example on how to parse this structure:

```c
#define ALIGN_UP(p) ((PVOID)(((ULONG_PTR)p + sizeof(PVOID) - 1) & ~(sizeof(PVOID) - 1)))

POBJECT_TYPES_INFORMATION types = { ... };

// Locate the first entry
POBJECT_TYPE_INFORMATION entry = ALIGN_UP(((ULONG_PTR)types + sizeof(OBJECT_TYPES_INFORMATION)));

for (ULONG i = 0; i < types->NumberOfTypes; i++)
{
    // Process the entry
    wprintf_s(L"%wZ\r\n", &entry->TypeName);

    // Advance to the next one
    entry = ALIGN_UP((ULONG_PTR)entry + sizeof(OBJECT_TYPE_INFORMATION) + entry->TypeName.MaximumLength);
}
```
