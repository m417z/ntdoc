This structure describes various information about a type of kernel objects. This structure is partially [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-__public_object_type_information).

# Applicable to
 - `NtQueryObject` with `ObjectTypeInformation`.
 - `OBJECT_TYPES_INFORMATION`

# Members

## TypeName
The string containing the name unique of the type, such as `Process` or `IoCompletion`.

## TotalNumberOfObjects
The current number of objects of this type.

## TotalNumberOfHandles
The current number of handles to objects of this type.

## TotalPagedPoolUsage
The total number of paged pool bytes used by objects of this type.

## TotalNonPagedPoolUsage
The total number of non-paged pool bytes used by objects of this type.

## TotalNamePoolUsage
The total number of name pool bytes used by objects of this type.

## TotalHandleTableUsage
The total number of handle table bytes used by objects of this type.

## HighWaterNumberOfObjects
The maximum recorded number of objects of this type since boot.

## HighWaterNumberOfHandles
The maximum recorded number of handles to objects of this type since boot.

## HighWaterPagedPoolUsage
The maximum recorded number of paged pool bytes used by objects of this type.

## HighWaterNonPagedPoolUsage
The maximum recorded number of non-paged pool bytes used by objects of this type.

## HighWaterNamePoolUsage
The maximum recorded number of name pool bytes used by objects of this type.

## HighWaterHandleTableUsage
The maximum recorded number of handle table bytes used by objects of this type.

## InvalidAttributes
A bit mask of object/handle attribute flags that are not applicable to objects this type. For the list of values, see `OBJECT_ATTRIBUTES`.

## GenericMapping
A mapping between specific and generic access rights for this type.

## ValidAccessMask
A bit mask describing specific and standard access rights that are valid for objects of this type.

## SecurityRequired
Whether unnamed objects of this type maintain security descriptors.

## MaintainHandleCount
Whether the system should keep track of handles for this type.

## TypeIndex
The index of this type in the global list of kernel types. Note that the system only populates this value on Windows 8.1 and above. To infer the value on older OS versions, take the index under which the type appears in the result of `ObjectTypesInformation` enumeration (made via `NtQueryObject`) and add 2 to it.

## ReservedByte
This field in reserved for future use.

## PoolType
The type of memory pool used by this type.

## DefaultPagedPoolCharge
The default number of paged pool bytes charged for objects of this type.

## DefaultNonPagedPoolCharge
The default number of non-paged pool bytes charged for objects of this type.
