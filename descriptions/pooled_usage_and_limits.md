This structure describes the kernel pool memory usage and limits for the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessPooledUsageAndLimits` (14)

# Members

## PeakPagedPoolUsage
The historical highest size of the paged pool charge in bytes.

## PagedPoolUsage
The current size of the paged pool charge in bytes.

## PagedPoolLimit
The paged pool quota size in bytes.

## PeakNonPagedPoolUsage
The historical highest size of the non-paged pool charge in bytes.

## NonPagedPoolUsage
The current size of the non-paged pool charge in bytes.

## NonPagedPoolLimit
The non-paged pool quota size in bytes.

## PeakPagefileUsage
The historical highest usage in bytes of the pagefiles.

## PagefileUsage
The current usage in bytes of the pagefiles.

## PagefileLimit
The pagefile quota size in bytes.

# See also
 - `VM_COUNTERS`
 - `VM_COUNTERS_EX`
 