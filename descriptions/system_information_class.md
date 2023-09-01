Enumeration type `SYSTEM_INFORMATION_CLASS` defines information classes for a lot of system settings
This type is used with function
`NtQuerySystemInformation` and `NtSetSystemInformation`.
For detailed information see descriptions of structures associated with information classes below.

### SystemBasicInformation

* Action: `Query`
* Buffer size: *0x02C*
* Structure: `SYSTEM_BASIC_INFORMATION`

### SystemProcessorInformation

* Action: `Query`
* Buffer size: *0x00C*
* Structure: `SYSTEM_PROCESSOR_INFORMATION`

### SystemPerformanceInformation

0x138 GET

### SystemTimeOfDayInformation

0x020 GET

### SystemPathInformation

* Action: `Query`
* Buffer size: *???*
* Structure: `STATUS_NOT_IMPLEMENTED`

System path is available via structure `KUSER_SHARED_DATA`

### SystemProcessInformation

* Action: `Query`
* Buffer size: *0x088+*
* Structure: `SYSTEM_PROCESS_INFORMATION`

### SystemCallCountInformation

* Action: `Query`
* Buffer size: *0x018+*
* Structure: `SYSTEM_CALL_COUNT_INFORMATION`

### SystemDeviceInformation

0x018 GET SystemConfigurationInformation

### SystemProcessorPerformanceInformation

* Action: `Query`
* Buffer size: *0x030*
* Structure: `SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION`

### SystemFlagsInformation

0x004 GET SET

### SystemCallTimeInformation

NOT_IMPLEMENTED

### SystemModuleInformation

* Action: `Query`
* Buffer size: *0x106+*
* Structure: `SYSTEM_MODULE_INFORMATION`

### SystemLocksInformation

0x028+ GET

### SystemStackTraceInformation

0x05C GET

### SystemPagedPoolInformation

0x01C GET checked build only

### SystemNonPagedPoolInformation

0x01C GET checked build only

### SystemHandleInformation

* Action: `Query`
* Buffer size: *0x014+*
* Structure: `SYSTEM_HANDLE_INFORMATION`

### SystemObjectInformation

* Action: `Query`
* Buffer size: *0x038+*
* Structure: `SYSTEM_OBJECT_INFORMATION`

### SystemPageFileInformation

* Action: `Query`
* Buffer size: *0x018+*
* Structure: `SYSTEM_PAGEFILE_INFORMATION`

### SystemVdmInstemulInformation

0x088 GET

### SystemVdmBopInformation

`INVALID_INFO_CLASS`

### SystemFileCacheInformation

0x00C, 0x024 GET SET

### SystemPoolTagInformation

0x020+ GET

### SystemInterruptInformation

0x018 GET

### SystemDpcBehaviorInformation

0x014 GET SET

### SystemFullMemoryInformation

0x014 GET checked build only

### SystemLoadGdiDriverInformation

0x018 SET

### SystemUnloadGdiDriverInformation

0x004 SET

### SystemTimeAdjustmentInformation

* Action: `Query`
* Buffer size: *0x00C*
* Structure: `SYSTEM_QUERY_TIME_ADJUST_INFORMATION`

<!-- -->

* Action: `Set`
* Buffer size: *0x008*
* Structure: `SYSTEM_SET_TIME_ADJUST_INFORMATION`

### SystemSummaryMemoryInformation

0x014 GET checked build only

### SystemNextEventIdInformation

???? (C0000005) GET checked build only

### SystemEventIdsInformation

0xB66 GET checked build only

### SystemCrashDumpInformation

0x004 GET

### SystemExceptionInformation

0x010 GET

### SystemCrashDumpStateInformation

0x004 GET

### SystemKernelDebuggerInformation

0x002 GET

### SystemContextSwitchInformation

0x030 GET

### SystemRegistryQuotaInformation

* Action: `Query`
* Buffer size: *0x00C*
* Structure: `SYSTEM_REGISTRY_QUOTA_INFORMATION`

<!-- -->

* Action: `Set`
* Buffer size: *0x00C*
* Structure: `SYSTEM_REGISTRY_QUOTA_INFORMATION`

### SystemExtendServiceTableInformation

* Action: `Set`
* Buffer size: *0x008*
* Structure: `SYSTEM_LOAD_IMAGE_INFORMATION`

### SystemPrioritySeperation

0x004 SET

### SystemPlugPlayBusInformation

NOT_IMPLEMENTED, GET

### SystemDockInformation

NOT_IMPLEMENTED, GET

### SystemPowerInformation

`INVALID_INFO_CLASS`

### SystemProcessorSpeedInformation

`INVALID_INFO_CLASS`

### SystemCurrentTimeZoneInformation

0x0AC GET

### SystemLookasideInformation

0x000 GET

# Documented by

* Tomasz Nowak

# See also

* `NtQuerySystemInformation`
* `NtSetSystemInformation`
