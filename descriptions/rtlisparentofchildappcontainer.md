Determines if two SIDs represent a pair of related child and parent AppContainer SIDs.

# Parameters
 - `ParentAppContainerSid` - a parent AppContainer SID.
 - `ChildAppContainerSid` - a child AppContainer SID.

# Implementation details
The function verifies the types of provided SIDs using `RtlGetAppContainerSidType` and then compares their first `SECURITY_PARENT_PACKAGE_RID_COUNT` (8) sub-authorities.

# Remarks
For the structure and relation between parent and child AppContainer SIDs, see `APPCONTAINER_SID_TYPE`.

# Required OS version
This function was introduced in Windows 8.1 alongside the support for child AppContainers.

# See also
 - `NtCreateLowBoxToken`
 - `RtlGetAppContainerParent`
