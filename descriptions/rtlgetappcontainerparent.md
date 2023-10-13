Derives a parent AppContainer SID from a child AppContainer SID.

# Parameters
 - `AppContainerSid` - a child AppContainer SID.
 - `AppContainerSidParent` - a variable that receives a pointer to a system-allocated buffer that contains the parent AppContainer SID.

# Remarks
To avoid retaining unused resources, call `RtlFreeSid` to free the returned SID when it is no longer required.

For the structure and relation between parent and child AppContainer SIDs, see `APPCONTAINER_SID_TYPE`.

# Required OS version
This function was introduced in Windows 8.1 alongside the support for child AppContainers.

# See also
 - `NtCreateLowBoxToken`
 - `RtlIsParentOfChildAppContainer`
