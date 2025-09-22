### Environment

Pointer to environment block.

### SourceString

Pointer to `UNICODE_STRING` structure with text. If text contains any environment variable name separated with **'%'** character, variable name is replaced by value of this variable.

### DestinationString

Result of above operation. At input only **MaximumLength** of `UNICODE_STRING` structure must be valid.

### DestinationBufferLength

If you don't know, how long should be result buffer, use value at `DestinationBufferLength` pointer.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `RtlQueryEnvironmentVariable_U`
* `RtlSetEnvironmentVariable`
