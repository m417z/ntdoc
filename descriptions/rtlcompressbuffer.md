### CompressionFormat

Only lower 2 bytes are supported. Higher byte means Compression Engine. Lower byte means Compressing Format.

* <B>**Compression format**</B> (0-15). Bits 4-7 are unused.

In NT 4.0 sp6 only LZNT1 is supported.

<B> \
#define COMPRESSION_FORMAT_NONE		(0x0000)		<FONT COLOR="Green">*// [result:STATUS_INVALID_PARAMETER]*</FONT> \
#define COMPRESSION_FORMAT_DEFAULT	(0x0001)		<FONT COLOR="Green">*// [result:STATUS_INVALID_PARAMETER]*</FONT> \
#define COMPRESSION_FORMAT_LZNT1	(0x0002) \
#define COMPRESSION_FORMAT_NS3		(0x0003)		<FONT COLOR="Green">*// STATUS_NOT_SUPPORTED*</FONT> \
#define ...							<FONT COLOR="Green">*// STATUS_NOT_SUPPORTED*</FONT> \
#define COMPRESSION_FORMAT_NS15		(0x000F)		<FONT COLOR="Green">*// STATUS_NOT_SUPPORTED*</FONT>

#define COMPRESSION_FORMAT_SPARSE	(0x4000)		<FONT COLOR="Green">*// ??? [result:STATUS_INVALID_PARAMETER]*</FONT> \
</B>

* <B>**Compression engine**</B>.

It's level of compression. Higher level means better results, but longer time used for compression process. \
In NT 4.0 sp6 engines works only with compression (specified in `RtlDecompressBuffer` are ignored)

<B> \
#define COMPRESSION_ENGINE_STANDARD	(0x0000)		<FONT COLOR="Green">*// Standart compression*</FONT> \
#define COMPRESSION_ENGINE_MAXIMUM	(0x0100)		<FONT COLOR="Green">*// Maximum (slowest but better)*</FONT> \
#define COMPRESSION_ENGINE_HIBER	(0x0200)		<FONT COLOR="Green">*// STATUS_NOT_SUPPORTED*</FONT> \
</B>

### Unknown

Put 0x1000 here. Propably means page size.

### pDestinationSize

Size of data after compression.

### WorkspaceBuffer

See `RtlGetCompressionWorkSpaceSize` for more information.

# See also

* `RtlDecompressBuffer`
* `RtlGetCompressionWorkSpaceSize`
