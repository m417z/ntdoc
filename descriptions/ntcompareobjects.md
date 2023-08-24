Determines whether two handles point to the same kernel object.

# Parameters
 - `FirstObjectHandle` - a handle to the first object.
 - `SecondObjectHandle` - a handle to the second object.

The handles do not need to grant any specific access. Any of the handles can be a pseudo-handle to the current thread (`NtCurrentThread`) or the current process (`NtCurrentProcess`).

# Notable return values
 - `STATUS_SUCCESS` - the two handles point to the same underlying kernel object.
 - `STATUS_NOT_SAME_OBJECT` - the handles point toward different objects.

# Related Win32 API
 - [`CompareObjectHandles`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-compareobjecthandles)

# Required OS version
This function was introduced in Windows 10 TH1 (1507).

# See also
 - `NtDuplicateObject`
 - `RtlIsCurrentThread`
 - `RtlIsCurrentProcess`
