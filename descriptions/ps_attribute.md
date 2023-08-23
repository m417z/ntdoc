This structure defines a process or thread creation attribute.

# Members
 - `Attribute` - a numerical identifier of the type of entry.
 - `Size` - the size of the value in bytes.
 - `Value`/`ValuePtr` - the additional input/output data attached to the attribute either in-place or as a pointer to a buffer.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes that has been written to the buffer (for attributes that return data).

# Known attributes
For the list of know attributes, see the documentation of `PS_ATTRIBUTE_NUM`.

# See also
 - `PS_ATTRIBUTE_LIST`
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`
