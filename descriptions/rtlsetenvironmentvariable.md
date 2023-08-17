### *Environment

If `Environment` is *NULL*, current environment block is used. \
If `Environment` point to *NULL* value, new environment block is allocated and variable is set in new block. \
If you can set variable in not currently set env. block, set as `Environment` pointer to that block.

# Documented by

* Tomasz Nowak
* ReactOS

# See also

* `RtlCreateEnvironment`
* `RtlQueryEnvironmentVariable_U`
* `RtlSetCurrentEnvironment`
