Enumeration type SYSTEM\_INFORMATION\_CLASS defines \
information classes for a lot of system settings. This type is used \
with function \
NtQuerySystemInformation and \
NtSetSystemInformation. For detailed informations see \
descriptions of structures associated with information classes \
below. \
SystemBasicInformation \
Action \
: Query \
Buffer size \
: 0x02C \
Structure \
: SYSTEM\_BASIC\_INFORMATION \
SystemProcessorInformation \
Action \
: Query \
Buffer size \
: 0x00C \
Structure \
: SYSTEM\_PROCESSOR\_INFORMATION \
SystemPerformanceInformation 0x138 GET \
SystemTimeOfDayInformation 0x020 GET \
SystemPathInformation \
Action \
: Query \
Buffer size \
: ??? \
Structure \
: STATUS\_NOT\_IMPLEMENTED \
System path is avaiable via structure KUSER\_SHARED\_DATA \
SystemProcessInformation \
Action \
: Query \
Buffer size \
: 0x088\+ \
Structure \
: SYSTEM\_PROCESS\_INFORMATION \
SystemCallCountInformation \
Action \
: Query \
Buffer size \
: 0x018\+ \
Structure \
: SYSTEM\_CALL\_COUNT\_INFORMATION \
SystemDeviceInformation 0x018 GET \
SystemConfigurationInformation \
SystemProcessorPerformanceInformation \
Action \
: Query \
Buffer size \
: 0x030 \
Structure \
: SYSTEM\_PROCESSOR\_PERFORMANCE\_INFORMATION \
SystemFlagsInformation 0x004 GET SET \
SystemCallTimeInformation NOT\_IMPLEMENTED \
SystemModuleInformation \
Action \
: Query \
Buffer size \
: 0x106\+ \
Structure \
: SYSTEM\_MODULE\_INFORMATION \
SystemLocksInformation 0x028\+ GET \
SystemStackTraceInformation 0x05C GET \
SystemPagedPoolInformation 0x01C GET checked build only \
SystemNonPagedPoolInformation 0x01C GET checked build only \
SystemHandleInformation \
Action \
: Query \
Buffer size \
: 0x014\+ \
Structure \
: SYSTEM\_HANDLE\_INFORMATION \
SystemObjectInformation \
Action \
: Query \
Buffer size \
: 0x038\+ \
Structure \
: SYSTEM\_OBJECT\_INFORMATION \
SystemPageFileInformation \
Action \
: Query \
Buffer size \
: 0x018\+ \
Structure \
: SYSTEM\_PAGEFILE\_INFORMATION \
SystemVdmInstemulInformation 0x088 GET \
SystemVdmBopInformation INVALID\_INFO\_CLASS \
SystemFileCacheInformation 0x00C, 0x024 GET SET \
SystemPoolTagInformation 0x020\+ GET \
SystemInterruptInformation 0x018 GET \
SystemDpcBehaviorInformation 0x014 GET SET \
SystemFullMemoryInformation 0x014 GET checked build only \
SystemLoadGdiDriverInformation 0x018 SET \
SystemUnloadGdiDriverInformation 0x004 SET \
SystemTimeAdjustmentInformation \
Action \
: Query \
Buffer size \
: 0x00C \
Structure \
: SYSTEM\_QUERY\_TIME\_ADJUST\_INFORMATION \
Action \
: Set \
Buffer size \
: 0x008 \
Structure \
: SYSTEM\_SET\_TIME\_ADJUST\_INFORMATION \
SystemSummaryMemoryInformation 0x014 GET checked build \
only \
SystemNextEventIdInformation ???? \(C0000005\) GET checked build \
only \
SystemEventIdsInformation 0xB66 GET checked build only \
SystemCrashDumpInformation 0x004 GET \
SystemExceptionInformation 0x010 GET \
SystemCrashDumpStateInformation 0x004 GET \
SystemKernelDebuggerInformation 0x002 GET \
SystemContextSwitchInformation 0x030 GET \
SystemRegistryQuotaInformation \
Action \
: Query \
Buffer size \
: 0x00C \
Structure \
: SYSTEM\_REGISTRY\_QUOTA\_INFORMATION \
Action \
: Set \
Buffer size \
: 0x00C \
Structure \
: SYSTEM\_REGISTRY\_QUOTA\_INFORMATION \
SystemExtendServiceTableInformation \
Action \
: Set \
Buffer size \
: 0x008 \
Structure \
: SYSTEM\_LOAD\_IMAGE\_INFORMATION \
SystemPrioritySeperation 0x004 SET \
SystemPlugPlayBusInformation NOT\_IMPLEMENTED, GET \
SystemDockInformation NOT\_IMPLEMENTED, GET \
SystemPowerInformation INVALID\_INFO\_CLASS \
SystemProcessorSpeedInformation INVALID\_INFO\_CLASS \
SystemCurrentTimeZoneInformation 0x0AC GET \
SystemLookasideInformation 0x000 GET

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtQuerySystemInformation \
NtSetSystemInformation
