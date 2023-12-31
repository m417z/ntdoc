This application compatibility flag used to be documented in early Windows 10 EWDK.

# Applicable to
 - `PEB->AppCompatFlags`

# Meaning
If set, APIs that open a docfile for writing ([`StgOpenStorageEx`](https://learn.microsoft.com/en-us/windows/win32/api/coml2api/nf-coml2api-stgopenstorageex), etc.) will revert to passing `FILE_SHARE_WRITE` when calling [`CreateFile`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew), even if the `STGM_SHARE_DENY_WRITE` flag is specified.

# Related flags
 - `KACF_OLDGETSHORTPATHNAME`
 - `KACF_VERSIONLIE_NOT_USED`
 - `KACF_GETDISKFREESPACE`
 - `KACF_FTMFROMCURRENTAPT`
 - `KACF_DISALLOWORBINDINGCHANGES`
 - `KACF_OLE32VALIDATEPTRS`
 - `KACF_DISABLECICERO`
 - `KACF_OLE32ENABLEASYNCDOCFILE`
 - `KACF_OLE32ENABLELEGACYEXCEPTIONHANDLING`
 - `KACF_RPCDISABLENDRCLIENTHARDENING`
 - `KACF_RPCDISABLENDRMAYBENULL_SIZEIS`
 - `KACF_DISABLEALLDDEHACK_NOT_USED`
 - `KACF_RPCDISABLENDR61_RANGE`
 - `KACF_RPC32ENABLELEGACYEXCEPTIONHANDLING`
 - `KACF_RPCDISABLENDRCONSTIIDCHECK`
 - `KACF_USERDISABLEFORWARDERPATCH`
 - `KACF_OLE32DISABLENEW_WMPAINT_DISPATCH`
 - `KACF_ADDRESTRICTEDSIDINCOINITIALIZESECURITY`
 - `KACF_ALLOCDEBUGINFOFORCRITSECTIONS`
 - `KACF_OLEAUT32ENABLEUNSAFELOADTYPELIBRELATIVE`
 - `KACF_ALLOWMAXIMIZEDWINDOWGAMMA`
 - `KACF_DONOTADDTOCACHE`
