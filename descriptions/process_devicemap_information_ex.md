This structure defines information about the process's DOS Devices map.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessDeviceMap` (23)
 - `NtSetInformationProcess` with `ProcessDeviceMap` (23)

# Members

## Set

### DirectoryHandle
A handle to a directory object to set as the new device map for the process. The handle must grant `DIRECTORY_TRAVERSE` access.

#### See also
 - `NtOpenDirectoryObject`
 - `NtCreateDirectoryObject`

## Query

### DriveMap
A bit mask defining which drive letters are currently in use in the process's device map. Bit 0 corresponds to `A:`, bit 1 to `B:`, and so on.

### DriveType
An array where each element defines the type of the drive associated with the specified letter. The value is meaningful only when the corresponding bit is set in the `DriveMap` field.

#### Known values
The possible values are defined in SDK in `WinBase.h`:
 - `DRIVE_UNKNOWN` (0) - the type of the drive is unknown.
 - `DRIVE_NO_ROOT_DIR` (1) - the letter points to a directory on another drive.
 - `DRIVE_REMOVABLE` (2) - the drive is a removable media.
 - `DRIVE_FIXED` (3) - the drive is a fixed disk.
 - `DRIVE_REMOTE` (4) - the drive is a remote device.
 - `DRIVE_CDROM` (5) - the drive is a CD-ROM.
 - `DRIVE_RAMDISK` (6) - the drive is a RAM disk.

## Flags
A bit mask of flags that control the operation.

### Known flags
 - `PROCESS_LUID_DOSDEVICES_ONLY` - perform a query only for devices defined for the current process or logon session, ignoring entries from the global DOS Devices directory.

# See also
 - `PROCESS_DEVICEMAP_INFORMATION`
