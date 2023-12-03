This structure defines the extension to the basic information about the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessBasicInformation` (0)

# Members

## Size
Specifies the size in bytes of the valid portion of this structure's header.

## BasicInfo
The basic information. See `PROCESS_BASIC_INFORMATION` for more details.

## Flags
A bit mask of various flags about the process

### IsProtectedProcess
The process is full- or light-protected.

#### See also
 - `PROCESSINFOCLASS` value of `ProcessProtectionInformation` (61)
 - `PS_PROTECTION`

### IsWow64Process
Indicates that the process is 32-bit and runs under the WoW64 emulation.

#### See also
 - `PROCESSINFOCLASS` value of `ProcessWow64Information` (26)

### IsProcessDeleting
The process is terminating and its object is marked for deletion.

#### See also
 - `NtTerminateProcess`

### IsCrossSessionCreate
The process was created cross-session.

### IsFrozen
The threads in the process are suspended and cannot be resumed until the process is unfrozen.

### IsBackground
The process belongs to a background job.

### IsStronglyNamed
The process has a strong package identity.

#### See also
 - `RtlQueryPackageIdentity`

### IsSecureProcess
The process runs in Isolated User Mode (IUM).

#### Required OS version
This field was introduced in Windows 10 TH1 (1507).

### IsSubsystemProcess
The process is a Pico or a WSL process.

#### Remarks
This field was previously known as `IsPicoProcess`.

#### Required OS version
This field was introduced in Windows 10 RS1 (1607).

#### See also
 - `PROCESSINFOCLASS` value of `ProcessSubsystemInformation` (75)

# Required OS version
This structure was introduced in Windows 8.
