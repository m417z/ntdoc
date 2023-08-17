### CompressionFormat

See `RtlCompressBuffer` for valid `CompressionFormat` flags.

### pNeededBufferSize

You must allocate temporary compression buffer for system internal use in compression process. \
Buffer must have `pNeededBufferSize` bytes length.

### pUnknown

???, probably PageSize (0x4000).

# See also

* `RtlCompressBuffer`
* `RtlDecompressBuffer`
