This attribute allows the caller to request the `TEB` address of the new thread to be returned upon its creation.

# Parameters
 - `Attribute` - `PS_ATTRIBUTE_TEB_ADDRESS` (numeric value `0x10004`).
 - `Size` - `sizeof(PVOID)`.
 - `ValuePtr` - a pointer to a `PTEB` variable that receives the `TEB` address of the new thread.

# Applicable to
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`

# See also
 - `TEB`
 - `PS_ATTRIBUTE_NUM`
 - `NtCurrentTeb`
