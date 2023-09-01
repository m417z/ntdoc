This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlcompressbuffer).

---

### CompressionFormat

Only lower 2 bytes are supported. Higher byte means Compression Engine. Lower byte means Compressing Format.

**Compression format** (0-15). Bits 4-7 are unused.

In NT 4.0 sp6 only LZNT1 is supported.

```cpp
#define COMPRESSION_FORMAT_NONE     (0x0000)        // [result:STATUS_INVALID_PARAMETER]
#define COMPRESSION_FORMAT_DEFAULT  (0x0001)        // [result:STATUS_INVALID_PARAMETER]
#define COMPRESSION_FORMAT_LZNT1    (0x0002)
#define COMPRESSION_FORMAT_NS3      (0x0003)        // STATUS_NOT_SUPPORTED
#define ...                                         // STATUS_NOT_SUPPORTED
#define COMPRESSION_FORMAT_NS15     (0x000F)        // STATUS_NOT_SUPPORTED

#define COMPRESSION_FORMAT_SPARSE   (0x4000)        // ??? [result:STATUS_INVALID_PARAMETER]
```

**Compression engine**.

It's level of compression. Higher level means better results, but longer time used for compression process. \
In NT 4.0 sp6 engines works only with compression (specified in `RtlDecompressBuffer` are ignored)

```cpp
#define COMPRESSION_ENGINE_STANDARD (0x0000)        // Standard compression
#define COMPRESSION_ENGINE_MAXIMUM  (0x0100)        // Maximum (slowest but better)
#define COMPRESSION_ENGINE_HIBER    (0x0200)        // STATUS_NOT_SUPPORTED
```

### Unknown

Put 0x1000 here. Probably means page size.

### pDestinationSize

Size of data after compression.

### WorkspaceBuffer

See `RtlGetCompressionWorkSpaceSize` for more information.

# See also

* `RtlDecompressBuffer`
* `RtlGetCompressionWorkSpaceSize`
