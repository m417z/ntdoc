This attribute allows the caller to request the client ID of the new thread to be returned upon its creation.

# Parameters
 - `Attribute` - `PS_ATTRIBUTE_CLIENT_ID` (numeric value `0x10003`).
 - `Size` - `sizeof(CLIENT_ID)`.
 - `ValuePtr` - a pointer to a `CLIENT_ID` buffer that receives the ID of the new thread.

# Applicable to
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`

# See also
 - `CLIENT_ID`
 - `NtOpenThread`
 - `PS_ATTRIBUTE_NUM`
