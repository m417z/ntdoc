Determines the type of AppContainer SID.

# Parameters
 - `AppContainerSid` - the SID to classify.
 - `AppContainerSidType` - a pointer to a variable that receives the SID classification.

# Notable return values
 - `STATUS_NOT_APPCONTAINER` - the specified SID is not an AppContainer SID.

# AppContainer SID types
For the list of known AppContainer SID types, their structure, and relation, see `APPCONTAINER_SID_TYPE`.

# Remarks
If the provided SID is not an AppContainer SID, the function returns an error code in addition to setting the `AppContainerSidType` variable to `NotAppContainerSidType` (0).

# Required OS version
This function was introduced in Windows 8.1 alongside the support for child AppContainers.

# See also
 - `NtCreateLowBoxToken`
 - `RtlIsParentOfChildAppContainer`
 - `RtlGetAppContainerParent`
