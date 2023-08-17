Use for enumerate modules loaded with current process.

### BufferSize

Required minimum size is `sizeof(SYSTEM_MODULE_INFORMATION)` (4 bytes).

# Example results

|       Name       |                          Path                          |   Res01   |   Res02   |  Address  |    Size   |   Flags   |  ID  |  Rank |   w18  |
|:----------------:|:------------------------------------------------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:----:|:-----:|:------:|
|  EnumModules.exe |  D:/Program Files/Microsoft Visual Studio/MyProject... |  BAADF00D |  00000000 |  00400000 |  00016000 |  00005000 |  000 |  0006 |  65535 |
|  ntdll.dll       |  C:/WINNT/System32/ntdll.dll                           |  BAADF00D |  00000000 |  77F60000 |  0005F000 |  00004004 |  001 |  0001 |  65535 |
|  KERNEL32.dll    |  C:/WINNT/system32/KERNEL32.dll                        |  BAADF00D |  00000000 |  77F00000 |  00060000 |  000C4006 |  002 |  0002 |  65535 |
|  USER32.dll      |  C:/WINNT/system32/USER32.dll                          |  BAADF00D |  00000000 |  77E70000 |  00055000 |  00084006 |  003 |  0006 |  65535 |
|  GDI32.dll       |  C:/WINNT/system32/GDI32.dll                           |  BAADF00D |  00000000 |  77ED0000 |  0002C000 |  00004006 |  004 |  0005 |  65535 |
|  ADVAPI32.dll    |  C:/WINNT/system32/ADVAPI32.dll                        |  BAADF00D |  00000000 |  77DC0000 |  0003F000 |  000C4006 |  005 |  0004 |  65535 |
|  RPCRT4.dll      |  C:/WINNT/system32/RPCRT4.dll                          |  BAADF00D |  00000000 |  77E10000 |  00057000 |  000C4006 |  006 |  0003 |  65535 |

# See also

* `SYSTEM_MODULE`
* `SYSTEM_MODULE_INFORMATION`
