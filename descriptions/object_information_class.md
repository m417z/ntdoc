Defines common types of information that can be queried or set for kernel handles/objects. This enumeration is partially [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ne-ntifs-_object_information_class).

# Applicable to
 - `NtQueryObject`
 - `NtSetInformationObject`

# Members


## ObjectBasicInformation (0)
Retrieves basic information about the handle and the underlying object, such as the granted access mask and handle count.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `OBJECT_BASIC_INFORMATION` | N/A
| Required access | None                       | N/A
| Optional access | `READ_CONTROL`             | N/A

## ObjectNameInformation (1)
Retrieves the name of the object in its native form.

|                 | Query                     | Set
| --------------- | ------------------------- | ---
| Type            | `OBJECT_NAME_INFORMATION` | N/A
| Required access | None                      | N/A

## ObjectTypeInformation (2)
Retrieves information about the type of the object referenced via the handle.

|                 | Query                     | Set
| --------------- | ------------------------- | ---
| Type            | `OBJECT_TYPE_INFORMATION` | N/A
| Required access | None                      | N/A

## ObjectTypesInformation (3)
Retrieves information about all types of kernel objects registered on the system. This information class does not require a handle on input.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `OBJECT_TYPES_INFORMATION` | N/A
| Required access | N/A                        | N/A

## ObjectHandleFlagInformation (4)
Controls handle inheritance and protection attributes.

|                 | Query                            | Set
| --------------- | -------------------------------- | ---
| Type            | `OBJECT_HANDLE_FLAG_INFORMATION` | `OBJECT_HANDLE_FLAG_INFORMATION`
| Required access | None                             | None

### Related Win32 API
 - [`GetHandleInformation`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-gethandleinformation)
 - [`SetHandleInformation`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-sethandleinformation)

### See also
 - `OBJ_INHERIT`
 - `OBJ_PROTECT_CLOSE`

## ObjectSessionInformation (5)

## ObjectSessionObjectInformation (6)
