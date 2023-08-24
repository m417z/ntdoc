This structure controls handle inheritance and protection attributes.

# Applicable to
 - `NtQueryObject` with `ObjectHandleFlagInformation`.
 - `NtSetInformationObject` with `ObjectHandleFlagInformation`.

# Members

## Inherit
A boolean indicating whether the handle is marked as inheritable.

### See also
 - `OBJ_INHERIT`
 - `NtCreateProcess`
 - `NtCreateProcessEx`
 - `NtCreateUserProcess`

## ProtectFromClose
A boolean indicating whether the handle is marked as protected from closing.

### See also
 - `OBJ_PROTECT_CLOSE`
 - `NtClose`
