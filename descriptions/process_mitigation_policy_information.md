This structure defines the state of one mitigation policy for the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessMitigationPolicy` (52)
 - `NtSetInformationProcess` with `ProcessMitigationPolicy` (52)

# Members

## Policy
On input, specifies the type of the mitigation policy to retrieve or set.

## \<unnamed union\>
A type-specific value of the mitigation defined by the `Policy` field.

# Required OS version
This structure was introduced in Windows 8.
