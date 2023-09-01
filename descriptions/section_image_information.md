Structure `SECTION_IMAGE_INFORMATION` is returned as a result of call `NtQuerySection` with `SectionImageInformation` information class. System automatically check type and contents of File Object passed as a parameter to function `NtCreateSection`, and sets `SEC_IMAGE` bit on Section Attributes.

This structure is very useful in process creation, because caller can check most interesting of *PE Header* fields just before call to `NtCreateProcess` and without mapping section to target process'es memory.

### EntryPoint

Image's entry point.

### StackZeroBits

Number of bits from left side of stack address must be set to zero. It means maximum stack's address in process memory.

### StackReserved

Total size of stack, in bytes.

### StackCommit

Initially committed stack's block size.

### ImageSubsystem

One of `IMAGE_SUBSYSTEM_*` descripted in *Microsoft SDK* and available in **\<winnt.h\>** header file.

### SubSystemVersionLow

Minor version number of subsystem.

### SubSystemVersionHigh

Major version number of subsystem.

### Unknown1

**(?)**

### ImageCharacteristics

DLL Characteristics.

### ImageMachineType

One of `IMAGE_FILE_MACHINE_*`.

### Unknown2[3]

**(?)**

# Documented by

* Tomasz Nowak

# See also

* `NtCreateProcess`
* `NtCreateSection`
* `NtMapViewOfSection`
* `NtOpenSection`
* `NtQuerySection`
* `SECTION_BASIC_INFORMATION`
* `SECTION_INFORMATION_CLASS`
