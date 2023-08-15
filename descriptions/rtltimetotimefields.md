This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-rtltimetotimefields)

Function RtlTimeToTimeFields converts 64\-bit \
time to user\-readable structure TIME\_FIELDS. \
Time Pointer to LARGE\_INTEGER \
contains time to convert. \
TimeFields Result of call \- pointer to \
TIME\_FIELDS \
structure.

Documented by: \
Reactos \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
RtlTimeFieldsToTime \
TIME\_FIELDS
