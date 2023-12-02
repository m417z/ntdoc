Contains various telemetry-related information about the process. This structure is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/process_telemetry_id_information_type).

# Applicable to
 - `NtQueryInformationProcess` with `ProcessTelemetryIdInformation` (64)

# Members

## HeaderSize
The size of the header of this structure in bytes. Fields beyond this size are not populated and will contain invalid data.

## ProcessId
The PID of the process.

### See also
 - `CLIENT_ID`

## ProcessStartKey
The unique value identifying the process across reboots. In the current implementation contains `ProcessSequenceNumber | (BootId << 48)`.

## CreateTime
The number of 100-nanosecond intervals since the 1st of January 1600 to the creation of the process.

### See also
 - `PROCESSINFOCLASS` value of `ProcessTimes` (4)

## CreateInterruptTime
The number of 100-nanosecond intervals passed since boot to the creation of the process.

### See also
 - `PROCESSINFOCLASS` value of `ProcessUptimeInformation` (88)

## CreateUnbiasedInterruptTime
The number of 100-nanosecond intervals the system was active since boot to the creation of the process.

## ProcessSequenceNumber
A unique sequence number of the process.

### See also
 - `PROCESSINFOCLASS` value of `ProcessSequenceNumber` (92)

## SessionCreateTime
The number of 100-nanosecond intervals passed since boot to the creation of the process's session.

## SessionId
The ID of the process's session.

### See also
 - `PROCESSINFOCLASS` value of `ProcessSessionInformation` (24)
 - `NtQueryInformationToken` with `TOKEN_INFORMATION_CLASS` value of `TokenSessionId` (12)

## BootId
The sequence number of the current OS boot.

## ImageChecksum
The checksum value from the process's PE file header.

## ImageTimeDateStamp
The timestamp value from the process's PE file header.

## UserSidOffset
An offset from the start of this structure to the user `SID` from the process's primary token.

### See also
 - `NtOpenProcessToken`
 - `NtQueryInformationToken` with `TOKEN_INFORMATION_CLASS` value of `TokenUser` (1)

## ImagePathOffset
An offset from the start of this structure to the native filename of the process's image.

### See also
 - `PROCESSINFOCLASS` values of `ProcessImageFileName` (27) and `ProcessImageFileNameWin32` (43)

## PackageNameOffset
An offset from the start of this structure to the full package name for processes with package identity.

### See also
 - `RtlQueryPackageIdentity`

## RelativeAppNameOffset
An offset from the start of this structure to the relative application user model ID  for processes with package identity.

### See also
 - `RtlQueryPackageIdentity`

## CommandLineOffset
An offset from the start of this structure to the command line string for the process.

### See also
 - `PROCESSINFOCLASS` value of `ProcessCommandLineInformation` (60)

# Required OS version
This structure was introduced in Windows 10 TH1 (1507).