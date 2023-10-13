This enumeration defines types of AppContainer SIDs.

# Applicable to
 - `RtlGetAppContainerSidType`

# Members

## NotAppContainerSidType (0)
The SID is not an AppContainer SID since it doesn't belong to `SECURITY_APP_PACKAGE_AUTHORITY` (15) identification authority with `SECURITY_APP_PACKAGE_BASE_RID` (2) as the first sub-authority or has less than `SECURITY_BUILTIN_APP_PACKAGE_RID_COUNT` (2) sub-authorities. In other words, the SID doesn't look like `S-1-15-2-*`.

## ChildAppContainerSidType (1)
The SID is a child AppContainer. Child AppContainers belong to `SECURITY_APP_PACKAGE_AUTHORITY` (15) identification authority with the first sub-authority equal to `SECURITY_APP_PACKAGE_BASE_RID` (2) and have `SECURITY_CHILD_PACKAGE_RID_COUNT` (12) sub-authorities, `SECURITY_PARENT_PACKAGE_RID_COUNT` (8) of which come from its parent AppContainer. The values for sub-authorities come from a SHA256 hash of the downcased child/parent AppContainer moniker. In other words, the SID looks like `S-1-15-2-x-x-x-x-x-x-x-y-y-y-y` where the `x` part is inherited from the parent and the `y` part is derived from the child moniker hash.

## ParentAppContainerSidType (2)
The SID is a parent AppContainer. Child AppContainers belong to `SECURITY_APP_PACKAGE_AUTHORITY` (15) identification authority with the first sub-authority equal to `SECURITY_APP_PACKAGE_BASE_RID` (2) and have `SECURITY_PARENT_PACKAGE_RID_COUNT` (8) sub-authorities, The values for sub-authorities come from a SHA256 hash of the downcased AppContainer moniker. In other words, the SID looks like `S-1-15-2-x-x-x-x-x-x-x`.

## InvalidAppContainerSidType (3)
The SID appears similar to an AppContainer SID but has an invalid structure.

# Required OS version
This function was introduced in Windows 8.1 alongside the support for child AppContainers.

# Remarks
You can create AppContainer profiles via Win32 API [`CreateAppContainerProfile`](https://learn.microsoft.com/en-us/windows/win32/api/userenv/nf-userenv-createappcontainerprofile). The function returns a parent AppContainer when invoked outside of the AppContainer sandbox context and a child AppContainer when invoked while running as a parent AppContainer. To construct an AppContainer SID without creating an AppContainer profile, use Win32 APIs [`DeriveAppContainerSidFromAppContainerName`](https://learn.microsoft.com/en-us/windows/win32/api/userenv/nf-userenv-deriveappcontainersidfromappcontainername) or [`DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName`](https://learn.microsoft.com/en-us/windows/win32/api/userenv/nf-userenv-deriverestrictedappcontainersidfromappcontainersidandrestrictedname). Note that in Win32 terminology, child AppContainers are called restricted AppContainers.

# See also
 - `NtCreateLowBoxToken`
 - `RtlIsParentOfChildAppContainer`
 - `RtlGetAppContainerParent`
