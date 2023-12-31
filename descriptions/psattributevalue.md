This macro allows constructing a process/thread creation attribute value based on its index.

# Known values
 - `PS_ATTRIBUTE_PARENT_PROCESS` = 0x60000;
 - `PS_ATTRIBUTE_DEBUG_OBJECT` = 0x60001;
 - `PS_ATTRIBUTE_TOKEN` = 0x60002;
 - `PS_ATTRIBUTE_CLIENT_ID` = 0x10003;
 - `PS_ATTRIBUTE_TEB_ADDRESS` = 0x10004;
 - `PS_ATTRIBUTE_IMAGE_NAME` = 0x20005;
 - `PS_ATTRIBUTE_IMAGE_INFO` = 0x00006;
 - `PS_ATTRIBUTE_MEMORY_RESERVE` = 0x20007;
 - `PS_ATTRIBUTE_PRIORITY_CLASS` = 0x20008;
 - `PS_ATTRIBUTE_ERROR_MODE` = 0x20009;
 - `PS_ATTRIBUTE_STD_HANDLE_INFO` = 0x2000A;
 - `PS_ATTRIBUTE_HANDLE_LIST` = 0x2000B;
 - `PS_ATTRIBUTE_GROUP_AFFINITY` = 0x3000C;
 - `PS_ATTRIBUTE_PREFERRED_NODE` = 0x2000D;
 - `PS_ATTRIBUTE_IDEAL_PROCESSOR` = 0x3000E;
 - `PS_ATTRIBUTE_UMS_THREAD` = 0x3000F;
 - `PS_ATTRIBUTE_MITIGATION_OPTIONS` = 0x20010;
 - `PS_ATTRIBUTE_PROTECTION_LEVEL` = 0x60011;
 - `PS_ATTRIBUTE_SECURE_PROCESS` = 0x20012;
 - `PS_ATTRIBUTE_JOB_LIST` = 0x20013;
 - `PS_ATTRIBUTE_CHILD_PROCESS_POLICY` = 0x20014;
 - `PS_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY` = 0x20015;
 - `PS_ATTRIBUTE_WIN32K_FILTER` = 0x20016;
 - `PS_ATTRIBUTE_SAFE_OPEN_PROMPT_ORIGIN_CLAIM` = 0x20017;
 - `PS_ATTRIBUTE_BNO_ISOLATION` = 0x20018;
 - `PS_ATTRIBUTE_DESKTOP_APP_POLICY` = 0x20019;
 - `PS_ATTRIBUTE_CHPE` = 0x6001A;
 - `PS_ATTRIBUTE_MITIGATION_AUDIT_OPTIONS` = 0x2001B;
 - `PS_ATTRIBUTE_MACHINE_TYPE` = 0x6001C;
 - `PS_ATTRIBUTE_COMPONENT_FILTER` = 0x2001D;
 - `PS_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES` = 0x3001E;

Check the corresponding pages for more details.

# See also
 - `PS_ATTRIBUTE`
 - `PS_ATTRIBUTE_LIST`
 - `PS_ATTRIBUTE_NUM`
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`
