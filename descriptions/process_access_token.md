This structure defines a request to change the primary token of the process.

# Applicable to
 - `NtSetInformationProcess` with `ProcessAccessToken` (9)

# Members

## Token
A handle to a primary token to use. The handle must grant `TOKEN_ASSIGN_PRIMARY` access.

## Thread
This field is currently unused.
