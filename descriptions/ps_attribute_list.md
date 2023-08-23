This structure defines a list of process or thread creation attributes.

# Members
 - `TotalLength` - the size of the entire structure in bytes, including the header. To store `N` attributes, the value should be `sizeof(PS_ATTRIBUTE_LIST) + (N - 1) * sizeof(PS_ATTRIBUTE)` due to the header including one attribute by default.
 - `Attributes` - the array of `PS_ATTRIBUTE` structures.

# See also
 - `PS_ATTRIBUTE`
 - `PS_ATTRIBUTE_NUM`
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`
