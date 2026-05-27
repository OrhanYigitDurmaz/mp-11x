# MP-11x SIP F6.60A.332.002 INI Parameters Reference

**Source: MP11X_SIP_F6.60A.332.002.cmp (reverse engineered)**

## Firmware Format

The .cmp file uses a two-stage compression scheme:

1. **Outer layer (LZO):** Header (6-byte magic `\x00LZO\xFF\x1A` + metadata + RSA2
   signature placeholder), then independently LZO-compressed blocks (128KB uncompressed)
2. **Inner layer (LZMA):** Each decompressed LZO block contains 64KB of payload at offset
   0x1042, with the rest being zero padding. Block 0's payload begins with a 13-byte LZMA
   header (props=0x5D, dict=8MB, size=17,646,768); subsequent blocks continue the LZMA
   stream. The concatenated LZMA stream decompresses to the full firmware image
   (17,646,768 bytes of PowerPC VxWorks executable + embedded web interface + data).

- **Scalar parameters: 3165**
- **Table definitions: 90**

---

## Scalar Parameters

These parameters are set in the INI file as `ParameterName = value` within their
respective `[Section Params]` sections (e.g., `[SIP Params]`, `[Voice Engine Params]`).

| # | Parameter | Description | Enumerated Values |
|--:|-----------|-------------|-------------------|
| 1 | `0123456789` | No slic coeffcients were found, coefficients set 0 will be laoded |  |
| 2 | `0123456789012345678901234567890` | Bye Packet Sent. Channel is closed. |  |
| 3 | `0123456789ABCDEF` | Enter PEM pass phrase: |  |
| 4 | `1234` | TestCallTelLink: Receive Unknown Board Ev |  |
| 5 | `2048` | Generate self-signed |  |
| 6 | `3GDelErrorSDU` | 3G - Delivery of erroneus SDU's |  |
| 7 | `3GLocalRate` | 3G - Local Rate (AMR rate) |  |
| 8 | `3GPCMCoderType` | 3G - G. 711 Coder Type |  |
| 9 | `3GPDUType` | 3G - PDU type |  |
| 10 | `3GRFCIVX` | 3G - RFCI AMR valid/invalid |  |
| 11 | `3GRFCIVXValue` | 3G - RFCI AMR value |  |
| 12 | `3GRemoteRate` | 3G - Remote Rate (AMR rate) |  |
| 13 | `3GSupportModeType` | 3G - UP Interface (Iu/Nb) |  |
| 14 | `3GUPInitAckTimeout` | 3G - Init Ack timeout / 20ms |  |
| 15 | `3GUPRateControlAckTimeout` | 3G - Rate control Ack timeout / 20ms |  |
| 16 | `3GUPTransportMode` | 3G - Support or Transparent mode |  |
| 17 | `3GUPVersionMask` | 3G - 3GPP UP Version (release 99,4,...) |  |
| 18 | `3LevelNamingBChannelStartNum` | Defines the starting number for the B channel level when 3 level termination naming used. |  |
| 19 | `3WAYCONFERENCEMODE` | Conference mode 0/1 : configure ConfID on setup, 2: set Inboard 3w conference, 3:Huawei Media Server |  |
| 20 | `3WayConfNoneAllocateablePorts` | Define the Ports that are not hit by 3w conf feature |  |
| 21 | `3XXBEHAVIOR` | 3xx response behavior mode |  |
| 22 | `65535` | Duplicate Rule |  |
| 23 | `89kS` | Tj 6/kR |  |
| 24 | `8cvDK` | 8cy K |  |
| 25 | `AAAINDICATIONS` | Which Authentication, Authorization and Accounting indications to use | None /0,Accounting Only /3 |
| 26 | `AASPackagesProfile` | Selects the profile for the Advanced Audio Syntax specification. | td51/0,h2489/1,mgcp/2,mscl/3 |
| 27 | `ACCESSLIST_Allow_Type` | Allow or block traffic matching this rule |  |
| 28 | `ACCESSLIST_Byte_Burst` | Allowed traffic burst in bytes (0 = unused) |  |
| 29 | `ACCESSLIST_Byte_Rate` | Allowed traffic in bytes per second (0 = unused) |  |
| 30 | `ACCESSLIST_End_Port` | Port range - end |  |
| 31 | `ACCESSLIST_Interface_ID` | Interface Name (none for ALL) |  |
| 32 | `ACCESSLIST_MatchCount` | Statistics: number of matched packets |  |
| 33 | `ACCESSLIST_Net_Mask` | OBSOLETE - Mask for this access rule (bitwise ANDed with the source IP of the packet) |  |
| 34 | `ACCESSLIST_Packet_Size` | Maximum packet size (0 = unused) |  |
| 35 | `ACCESSLIST_PrefixLen` | Prefix length of source IP address (defining a subnet) |  |
| 36 | `ACCESSLIST_Protocol` | IP user-level protocol (TCP, UDP, ICMP, ESP, SIP, MGCP, TPNCP, ANY or numeric value) |  |
| 37 | `ACCESSLIST_Source_IP` | Source IP for access rule |  |
| 38 | `ACCESSLIST_Source_Port` | Source Port (0 for ALL) |  |
| 39 | `ACCESSLIST_Start_Port` | Port range - start |  |
| 40 | `ACCESSLIST_Use_Specific_Interface` | Use the rule for specific interface or for all the interfaces | Disable/0,Enable/1 |
| 41 | `ACOUSTICECHOSUPPATTENUATIONINTENSITY` | Acoustic echo suppressor signals identified as echo attenuation intensity. |  |
| 42 | `ACOUSTICECHOSUPPCOMFORTNOISEGENERATION` | Comfort Noise Generation (CNG)- Values: Enable, Disable |  |
| 43 | `ACOUSTICECHOSUPPECHOGAPTIMEXMS` | Echo hang-over time value in ms, range  0 |  |
| 44 | `ACOUSTICECHOSUPPINITIALREFDELAYx10MS` | Acoustic echo suppressor intial reference delay [10 ms] |  |
| 45 | `ACOUSTICECHOSUPPMAXECHOLEVEL` | Maximal Echo Level in |  |
| 46 | `ACOUSTICECHOSUPPMAXERLTHRESHOLD` | Acoustic echo suppressor max ratio between signal level and retruned echo from phone [dB]. |  |
| 47 | `ACOUSTICECHOSUPPMAXNOISELEVEL` | Acoustic echo suppressor max noise level. Maximal Noise Level expected in the system in |  |
| 48 | `ACOUSTICECHOSUPPMAXREFDELAYx10MS` | Acoustic echo suppressor max reference delay [10 ms]. |  |
| 49 | `ACOUSTICECHOSUPPMINATTENUATIONGAINDB` | Min attenuation applied in dB [0 - 35]. 35 means maximal attenuation applied. | DENIAL_OF_SERVICE_WINDOW_SIZE__100_msec/0,DENIAL_OF_SERVICE_WINDOW_SIZE__300_msec/1,DENIAL_OF_SER... |
| 50 | `ACOUSTICECHOSUPPMINREFDELAYx10MS` | Acoustic echo suppressor min reference delay [10 ms]. |  |
| 51 | `ACOUSTICECHOSUPPRESSORSUPPORT` | Enable support of network acoustic echo suppressor. |  |
| 52 | `ACOUSTICECHOSUPPSILENCEGAPTIMEXMS` | Silence hang-over time value in ms, range 0 |  |
| 53 | `ACOUSTICECHOSUPPSPEECHGAPTIMEXMS` | Near end speech hang-over time value in ms, range 0 |  |
| 54 | `ACTIVESPEAKERSNOTIFICATIONMININTERVAL` | Minimum interval between Active Speaker Notification (ASN) events [100 ms]. |  |
| 55 | `ADDCICASPREFIX` | If add carrier identification code as prefix |  |
| 56 | `ADDCPCPREFIX2BRAZILCALLERID` | Enable Interworking of Calling Party Category (cpc) from sip INVITE to FXS Caller ID first digit for Brazil Telecom |  |
| 57 | `ADDIEINSETUP` | Additional information element to send in ISDN Setup message |  |
| 58 | `ADDITIONALOUTOFBANDDTMFFORMAT` | Additional DTMF Out-of-Band transport method |  |
| 59 | `ADDNPIANDTON2CALLEDNUMBER` | Add NPI and TON as prefix to called number |  |
| 60 | `ADDNPIANDTON2CALLINGNUMBER` | Add NPI and TON as prefix to calling number |  |
| 61 | `ADDNPIANDTON2REDIRECTNUMBER` | Add NPI and TON as prefix to Redirect number |  |
| 62 | `ADDPORTASPREFIX` | Add port number (Analog gateway) / Trunk ID (Digital gateway) as called number prefix |  |
| 63 | `ADDTON2RPI` | Add Number Type and Plan to Remote-Party-ID header |  |
| 64 | `ADDTRUNKGROUPASPREFIX` | Add Trunk Group ID on which the call was received as the called number prefix |  |
| 65 | `ADDTRUNKGROUPASPREFIXTOSOURCE` | Add Trunk Group ID on which the call was received as the calling number prefix |  |
| 66 | `AES_CM_256_` | Illegal Tag value |  |
| 67 | `AGCDisableFastAdaptation` | Disables the AGC (Automatic Gain Control) FastAdaptation mode. |  |
| 68 | `AGCGainSlope` | Determines the AGC convergence rate. configuration values are explained in the User Manual. |  |
| 69 | `AGCMaxGain` | Defines the maximum signal gain of the AGC [dB]. |  |
| 70 | `AGCMinGain` | Defines the minimum signal gain of the AGC [dB]. |  |
| 71 | `AGCRedirection` | Redirects the AGC output towards the TDM instead of towards the network. |  |
| 72 | `AGCTargetEnergy` | Determines the target signal energy level of the AGC [-dBm] |  |
| 73 | `ALLOC` | ERR: Memory was already allocated !!! |  |
| 74 | `ALLOWUNCLASSIFIEDCALLS` | Allow unclassified incoming calls. | Reject/0,Allow/1 |
| 75 | `ALTROUTINGTEL2IPCONNMETHOD` | Tel to IP Alternative Routing Connectivity Method. | ICMP Ping /0,SIP OPTIONS /1 |
| 76 | `ALTROUTINGTEL2IPENABLE` | Enable Tel to IP Alternative Routing. Can be enabled for status only without affecting routing | Disable /0,Enable /1,Status Only /2 |
| 77 | `ALTROUTINGTEL2IPKEEPALIVETIME` | Time interval between OPTIONS Keep-Alive messages for IP connectivity (seconds) |  |
| 78 | `ALTROUTINGTEL2IPMODE` | Methods used for Alternative Routing operation | None /0,Connectivity /1,Qos /2,Both /3 |
| 79 | `ALTROUTINGTONEDURATION` | Alternative Routing Tone Duration (milliseconds) |  |
| 80 | `ALWAYSSENDTOPROXY` | Send all messages to Proxy server |  |
| 81 | `ALWAYSUSEROUTETABLE` | Always use routing table even though proxy is available |  |
| 82 | `AMDBeepDetectionSensitivity` | Determines the AMD (Answering Machine Detector) Beep detection sensitivity. |  |
| 83 | `AMDBeepDetectionTimeout` | Determines the AMD (Answering Machine Detector) Beep detection timeout [100 ms]. |  |
| 84 | `AMDDecisionCurveACoefficient` | Answer machine detector (AMD) decision curve A coefficient (parameter no' 8) |  |
| 85 | `AMDDecisionCurveBCoefficient` | Answer machine detector (AMD) decision curve B coefficient (parameter no' 1) |  |
| 86 | `AMDDecisionCurveCCoefficient` | Answer machine detector (AMD) decision curve C coefficient (parameter no' 2) |  |
| 87 | `AMDDecisionParam5` | Answer machine detector (AMD) decision parameter no'5 |  |
| 88 | `AMDDecisionParam6` | Answer machine detector (AMD) decision parameter no' 6 |  |
| 89 | `AMDDecisionParam7` | Answer machine detector (AMD) decision parameter no' 7 |  |
| 90 | `AMDDetectionDirection` | Determines the AMD (Answering Machine Detector) detection direction. | acAMD_TDMDetection/0,acAMD_NetworkDetection/1 |
| 91 | `AMDDetectionSensitivity` | Determines the AMD (Answer Machine Detector) detection sensitivity. |  |
| 92 | `AMDMAXGREETINGTIME` | Answer machine detector (AMD) max greeting time |  |
| 93 | `AMDMAXPOSTSILENCEGREETINGTIME` | Answer machine detector (AMD) max post silence greeting time |  |
| 94 | `AMDMODE` | 0 -  not affected,1 - disconnect IP2TEL call on Answering Machine detection | Don't disconnect/0,Disconnect on Answering Machine detection/1 |
| 95 | `AMDMinimumVoiceLength` | AMD (Answer Machine Detector) minimum voice length in 5ms units |  |
| 96 | `AMDSensitivityLevel` | Determines the AMD (Answering Machine Detector) level of detection sensitivity. |  |
| 97 | `AMDSensitivityParameterSuit` | Determines the serial number of the AMD (Answering Machine Detector) sensitivity suit. |  |
| 98 | `AMDTIMEOUT` | Amd Detection Timeout <mSec> |  |
| 99 | `AMDdebugger` | AMD Debugger control |  |
| 100 | `AMRCODERHEADERFORMAT` | Determine the payload format when using AMR & AMR-WB. | CE_AMR_DEFAULT_FORMAT/0,CE_AMR_RFC_3267_BUNDLING/1,CE_AMR_RFC_3267_INTERLEAVING/2,CE_AMR_IF2/3 |
| 101 | `AMRFECDELAYHYSTERESIS` | Defines the hysteresis of the Delay Threshold for AMR Hand-out events (in msec). |  |
| 102 | `AMRFECDELAYTHRESHHOLD` | Defines the one-way delay value (in msec) that may cause the AMR Hand Out report. |  |
| 103 | `AMRFECNUMBEROFCODECMODES` | Sets the number of entries to be defined at the AMR management policy table. |  |
| 104 | `AMRFECREDUNDANCYDEPTH` | Sets the AMR / AMR-WB Redundancy depth according to RFC 3267. | CE_AMR_FEC_REDUNDANCY_LEVEL__NONE /0,CE_AMR_FEC_REDUNDANCY_LEVEL__1 /1,CE_AMR_FEC_REDUNDANCY_LEVE... |
| 105 | `AMRPAYLOADTYPE` | Payload type for AMR coders family |  |
| 106 | `AMRPayloadFormat` | Bandwidth Efficient | /VEGeneralSettings@50,100,0 |
| 107 | `AMRSENDRATE` | Rate of Amr packets for sending: 4_75=0,5_15=1,5_90=2,6_70=3,7_40=4,7_95=5,10_2=6,12_2=7 |  |
| 108 | `AMSALLOWURLASALIAS` | Indicates if play requests for remote URLs should first be checked for local segments with the same alias as the URL. |  |
| 109 | `AMSEnbaleBundleBurning` | Indicates whether VP and XML files (audio bundle) are allowed to be burnt to the board. {@}{@}This parameter is only ... |  |
| 110 | `AMSForceRepositoryUpdateEnabled` | Indicates that a new audio repository is uploaded to the board even if this action prevents playing signals on the ol... |  |
| 111 | `AMSPrimaryLanguage` | Defines the Primary Language for the AMS. |  |
| 112 | `AMSProfile` | Enable/Disable Advanced IVR play functionality. |  |
| 113 | `AMSSecondaryLanguage` | Defines the Secondary Language for the AMS. |  |
| 114 | `ANALOGPORTINFO` | Analog Port Info |  |
| 115 | `ANAT` | SDPBody::RemoveIrrelevantMediaFromMatch - removing media mid=%d in %s group |  |
| 116 | `ANNEXB` | Illegal redundancy format |  |
| 117 | `ANNEXDOLCDELAY` | Set parameter to positive delay for Master to send OLC during Annex D procedure |  |
| 118 | `ANNOUNCEMENTID` | Identification of a play voice prompt call (To be used by SIP INVITE) |  |
| 119 | `ANONYMOUSMODE` | Defines the source IP in the FROM header. 0-anonymous.invalid, 1-GW IP address | anonymous-invalid /0,IP address /1 |
| 120 | `ANSWERDETECTORCMD` | Configuration::InsertIntVal- illegal value %s=%d |  |
| 121 | `APPLICATIONPROFILE` | ApplicationProfile, read it later for validating that the board is theirs. |  |
| 122 | `APPROVED` | All default parameters will be loaded. the board will be restarted... |  |
| 123 | `APSEnabled` | Indicates if the system should expect to use APS bundle (vp.dat and segments.xml files), or use local audio in the vp... | disable/0,enable/1 |
| 124 | `APSSegmentsFileUrl` | Provides a link to an XML segments file, to be downloaded from a remote server. |  |
| 125 | `ARPTableMaxEntries` | Sets maximum number of entries in the ARP table. |  |
| 126 | `ASSERTEDIDMODE` | Select Asserted Identity header method | Disabled /0,Add P-Asserted-Identity /1,Add P-Preferred-Identity /2 |
| 127 | `ASSUBSCRIBEIPGROUPID` | IPGroup ID for AS subscribe purposes |  |
| 128 | `ASYNC` | This board does not support asynchronous queries. |  |
| 129 | `ATM_BIT_FIELD_SIZE` | Defines the bit field size for for each ATM termination name level (for binary MEGACO) . |  |
| 130 | `ATM_Num` | Defines the starting number for each ATM termination level name. |  |
| 131 | `AUDIODSPEVENTSVIAUTOPIA` | Enable DSP events over UTOPIA. |  |
| 132 | `AUMO` | Per Endpoint |  |
| 133 | `AUPDCheckIfIniChanged` | Performs CRC checking to determine if the INI file has changed prior to processing. | off/0,regular/1,voice-conf-ordered/2 |
| 134 | `AUPDDigestPassword` | Set password for Digest authentication in Automatic Update. |  |
| 135 | `AUPDDigestUsername` | Set username for Digest authentication in Automatic Update. |  |
| 136 | `AUPDHTTPUSERAGENT` | Configure the User-Agent HTTP header in the Auto-Update HTTP requests. |  |
| 137 | `AUPDLastIniCRC` | Keep the last INI CRC in flash. |  |
| 138 | `AUPDRedirectedServerIp` | Defines the redirected HTTP server IP address to be used by automatic update. Set/reset by HTTP 301 response/fallback... |  |
| 139 | `AUPDRedirectedServerPort` | Defines the redirected HTTP server TCP Port number to be used by automatic update. Set/reset by HTTP 301 response/fal... |  |
| 140 | `AUPDResetURLOnWebConfig` | Enables to reset the ini file url when configuration is altered via WEB |  |
| 141 | `AUPDRetryTime` | Defines the default number of seconds to wait for automatic update retry upon a TCP/HTTP failure. |  |
| 142 | `AUPDVerifyCertificates` | Configures the AutoUpdate facility to verify server certificates when using HTTPS. |  |
| 143 | `AUTHCHALLENGEMETHOD` | Set to 0 to use a www-authenticate header or 1 to send a proxy-authenticate header in the message |  |
| 144 | `AUTHENTICATIONMODE` | Authentication mode | Per Endpoint /0,Per Gateway /1,Per FXS Only /3 |
| 145 | `AUTHNONCEDURATION` | Lifetime of the nonce in seconds. |  |
| 146 | `AUTHQOP` | Set to 0 to offer auth, 1 to offer auth-int or 2 to offer auth, auth-int, or 3 to not offer anu QOP. |  |
| 147 | `AcSIPCall` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 148 | `AcSIPCallAPI` | CHashMap::CHashMap - Allocation Exception |  |
| 149 | `AcSIPDialog` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 150 | `AcSIPDialogAPI` | CHashMap::CHashMap - Allocation Exception |  |
| 151 | `AcSIPParser` | Parse error: |  |
| 152 | `AccessList` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Firewall Settings' page. |  |
| 153 | `ActivateallChannelsOnBoardInit` | Activates or deactivates all DSPs when the board is initialized. |  |
| 154 | `Active` | Not In Service |  |
| 155 | `ActiveAlarmTableMaxSize` | Determines the maximum number of rows in the Active Alarm Table. |  |
| 156 | `ActiveBoardIPAddress` | Defines the IP Addresses of the active boards, from which the redundant board receives state DB packets. |  |
| 157 | `ActiveSpeakerEnergyThreshold` | Minimum energy level for a user to be included in Active Speaker Notification (ASN) events [-dBm]. |  |
| 158 | `ActivityListToLog` | Defines what activities are to be reported by the device in the form of a log message. |  |
| 159 | `AddCIDTraceRule` | Trace criteria CID |  |
| 160 | `AddChannelIdTrace` | Trace by Channel Id |  |
| 161 | `AddDSPTraceRule` | Trace criteria DSP core/channel |  |
| 162 | `AddFileTarget` | Add an Internal pCap File debug recording target |  |
| 163 | `AddIPControlTrace` | Trace IP control |  |
| 164 | `AddIPTLSPtrace` | Trace TLS Peek by IP/port |  |
| 165 | `AddIPTLSTrace` | Trace TLS by IP/port |  |
| 166 | `AddIPTraceRule` | Trace criteria IP/port |  |
| 167 | `AddIPTrafficTrace` | Trace by IP Addr/Port |  |
| 168 | `AddIpTarget` | Add a IP debug recording target |  |
| 169 | `AddMegacoTraceRule` | Trace according to Megaco context/termination |  |
| 170 | `AddNextCallTrace` | Trace the next media calls |  |
| 171 | `AddPrefix2ExtLine` | FXS: If enabled (1) and Prefix2ExtLine is detected, it is added to the dial number as prefix |  |
| 172 | `AddPstnSignalingTrace` | Trace Pstn Signaling |  |
| 173 | `AddSystemTraceRule` | Trace criteria System debug |  |
| 174 | `AddTBTraceRule` | Trace criteria Trunk/Bchannel |  |
| 175 | `AddTrunkBchannelTrace` | Trace by Trunk/Bchannel |  |
| 176 | `AdditionalInputReseed` | ReturnedBits = %s |  |
| 177 | `Admin` | DHCP Activated by ACLEtherDiscover. |  |
| 178 | `AdminAccessLevel` | No Access |  |
| 179 | `AdminState` | Determines the media gateway's initial administrative state. |  |
| 180 | `AdminStateLockControl` | Defines the time remaining for the shutdown to complete (in sec). |  |
| 181 | `Administrator` | Security Administrator |  |
| 182 | `AggressiveDTMFErasure` | Internal parameter. |  |
| 183 | `AggressiveNLPmode` | Defines operation mode of EC NLP: 0 - Active at beginning of call. 1 - Always Active. | ECAggNLPActiveAtBeginning/0,ECAggNLPAlwaysActive/1 |
| 184 | `AlarmHistoryTableMaxSize` | Determines the maximum number of rows in the Alarm History Table. |  |
| 185 | `AllowWanHttp` | Enables or disables WAN access to the management interface via HTTP. |  |
| 186 | `AllowWanHttps` | Enables or disables WAN access to the management interface via HTTPS. |  |
| 187 | `AllowWanSSH` | Enables or disables WAN access to the management interface via SSH. |  |
| 188 | `AllowWanSnmp` | Enables or disables WAN access to the management interface via SNMP. |  |
| 189 | `AllowWanTelnet` | Enables or disables WAN access to the management interface via Telnet. |  |
| 190 | `AlwaysUseRouteTable` | Always Use Route Table |  |
| 191 | `AmdBeepDetectionMode` | Set the AMD beep detection mod, | Disabled /0,Start After AMD/1,Start immediately/2 |
| 192 | `AmdSensitivityFileName` | Name of the AMD Sensitivity auxiliary file. |  |
| 193 | `AmdSensitivityFileUrl` | Provides a link to the AMD Sensitivity file to be downloaded from a remote server. |  |
| 194 | `AmrOctetAlignedEnable` | Defines AMR payload format: 0 = Bandwidth-Efficient; 1 = Octet-Aligned | Bandwidth Efficent /0,Octet Aligned /1 |
| 195 | `AnalogCallerIDTimingMode` | Defines the Analog CallerID Timing Mode. | first-option/0,second-option/1 |
| 196 | `AnalogChannel` | Error. Illegal CID value. CID should be in the range [0-%d] |  |
| 197 | `AnalogLineTest` | Board name: %s |  |
| 198 | `AnalogSignalTransportType` | Determines the analog signal transport type. | Ignore Analog Signals/0,RFC 2833 Analog Signal Relay/1 |
| 199 | `AnswerDetectorRedirection` | Redirects the AD (Answer Detector) towards the network instead of TDM. |  |
| 200 | `AnswerDetectorSensitivity` | Controls the AD (Answer Detector) sensitivity. lowest value matches highest sensitivity, and vice versa. |  |
| 201 | `AnswerDetectorSilenceTime` | Controls the Answer Detector's silence time period from no speech input until sending the End Of Speech event [100 ms]. |  |
| 202 | `Applied` | Not Applied |  |
| 203 | `ApplyIniMethod` | Enable/Disable INI parsing. |  |
| 204 | `AriaProtocolSupport` | Enables Aria media encryption algorithm support. |  |
| 205 | `Ascending` | Cyclic Descending |  |
| 206 | `AudioStagingAutoSwitchoverEnabled` | Indicates if audio repository is to  be automatically activated after APS bundle downloading. |  |
| 207 | `AudioTermPattern` | Defines the name pattern of an audio termination. |  |
| 208 | `Authenticated` | SIPCallAuthenticatedState::Failed to allocate SIPMessage |  |
| 209 | `Authenticating` | SIPCallAuthenticatingState::Failed to allocate SIPMessage |  |
| 210 | `Authentication` | Automatic Dialing |  |
| 211 | `AuthorizedTPNCPServers` | Sets the IP address of TPNCP authorized servers. |  |
| 212 | `AutoClockTrunkPriority` | Sets the trunk priority for auto-clock fallback. |  |
| 213 | `AutoUpdate` | AutoUpdateTask(HTTP/HTTPS): Failed Creating socket. Error %d (URL=%s). |  |
| 214 | `AutoUpdateCmpFile` | Enables / disables the automatic update mechanism for the cmp file. | disabled/0,enabled/1 |
| 215 | `AutoUpdateFrequency` | Determines the number of minutes the gateway waits between automatic updates. |  |
| 216 | `AutoUpdatePredefinedRandomTime` | Determines the maximum randomization interval, after AutoUpdatePredefinedTime (in second unit). |  |
| 217 | `AutoUpdatePredefinedTime` | Schedules an automatic update to a predefined time of the day. |  |
| 218 | `Automatic` | Dest: %s/%d, gateway: %s, IF index: %d, state: %s |  |
| 219 | `AutomaticEchoCanceller` | Enables the Automatic Echo Canceller feature. |  |
| 220 | `AutonomousDUStateChangeComplete` | Message of type %d not found |  |
| 221 | `BASIC` | DSP Basic Statistics: |  |
| 222 | `BCHANNELNEGOTIATION` | ISDN B-Channel negotiation mode | Preferred /0,Exclusive /1,Any /2 |
| 223 | `BCHANNELNEGOTIATIONFORTRUNK` | ISDN B-Channel negotiation mode for trunk{@}put  MODE_NOT_SET (-1) to use BCHANNELNEGOTIATION per Gateway | Not Set /-1,Preferred /0,Exclusive /1,Any /2 |
| 224 | `BCTTermPattern` | Defines the name pattern of a BCT termination. |  |
| 225 | `BChannelAlarms` | When set to 1 B-Channels Alarms will be sent. |  |
| 226 | `BChannelStartNum` | Defines the starting number for the B channel level. |  |
| 227 | `BELLCORE_CALLERID_TIME_BETWEEN_CID_TO_RING` | The time between the FSK Caller ID signal and the ring which follows it, in the Bellcore Caller ID with ringing. |  |
| 228 | `BELLCORE_CALLERID_TIME_BETWEEN_OSI_TO_CID` | The time between the end of the OSI and the FSK Caller ID signal in the Bellcore Caller ID, without ringing. |  |
| 229 | `BELLCORE_CALLERID_TIME_BETWEEN_RING_TO_CID` | The time between the ring and the FSK Caller ID signal in the Bellcore Caller ID, without ringing. |  |
| 230 | `BELLCORE_CALLERID_TIME_DATA_TRANSMISSION_DURATION` | The duration of data transmission (FSK signal) in the Bellcore Caller ID type. |  |
| 231 | `BELLCORE_CALLERID_TIME_OF_OSI` | The duration of the OSI (Open Circuit) while generating the Bellcore Caller ID without ringing, in msec. |  |
| 232 | `BELLCORE_CALLERID_TIME_OF_RING_PULSE` | The time of the ring pulse in the Bellcore Caller ID before the ring. |  |
| 233 | `BIPONCONFERENCE` | Beep when a new participant joins a conference | disable/0,enable/1 |
| 234 | `BIT_ELEMENT_ID_DSP_DDR_TEST` | N/A Diagnostics Bit |  |
| 235 | `BIT_RESULT_FAILED` | Notification on the board HW elements being tested and their status. |  |
| 236 | `BIT_TYPE_PERIODIC` | Envoke VoicePath BIT commands |  |
| 237 | `BKGImageFIleName` | Changes AudioCodes Web background image to the user background image by loading GIF/JPEG file. |  |
| 238 | `BLINDTRANSFERDISCONNECTTIMEOUT` | Maximum time (milliseconds) to wait for disconnect from tel before performing blind transfer |  |
| 239 | `BLOCK` | AccessList_ValidateCB: Illegal Action Upon Match: %s |  |
| 240 | `BOOT` | Send file |  |
| 241 | `BOOTPDisable` | Enable/Disable BOOTP support. |  |
| 242 | `BRAZILIAN_CID_TIME_BETWEEN_CID_TO_RING` | The time between an FSK Caller ID signal and the ring which follows it, in the Brazilian Caller ID, with ringing. |  |
| 243 | `BRAZILIAN_CID_TIME_BETWEEN_RING_TO_CID` | The time between a ring and an FSK Caller ID signal, in the Brazilian Caller ID, with ringing. |  |
| 244 | `BRAZILIAN_CID_TIME_DATA_TRANSMISSION_DURATION` | The duration of data transmission (FSK signal), in the Brazilian Caller ID type. |  |
| 245 | `BRONZESERVICECLASSDIFFSERV` | Sets the DiffServ for the Bronze service class content. |  |
| 246 | `BT_CALLERID_TIME_BETWEEN_CID_TO_HOOK_MASK` | The time between a Caller ID signal (FSK) and the masking offhook interrupt, in the BT Caller ID type. |  |
| 247 | `BT_CALLERID_TIME_BETWEEN_CID_TO_RING` | The time between a Caller ID signal (FSK) and the start of the ring, in the BT Caller ID type. |  |
| 248 | `BT_CALLERID_TIME_BETWEEN_HOOK_MASK_TO_HOOK_UNMASK` | The time between masking the offhook interrupt and unmasking the offhook interrupt, in the BT Caller ID type. |  |
| 249 | `BT_CALLERID_TIME_BETWEEN_LINE_REVERSAL_TO_CID` | The time between line reversal and a Caller ID signal (FSK), in the BT Caller ID type. |  |
| 250 | `BURN` | NOTICE:  burning of configurations to Flash causes to stop the activation of AutomaticUpdate feature |  |
| 251 | `BV_16` | AMRWB starting rate 6_6 |  |
| 252 | `BadDigest` | DigestData::FailureCode2Str - Reason is %s |  |
| 253 | `Base` | CHashMap::CHashMap - Allocation Exception |  |
| 254 | `BaseCallState` | Illegal State (%s) to handle Ev: %s |  |
| 255 | `BaseHeader` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 256 | `BaseState` | CHashMap::CHashMap - Allocation Exception |  |
| 257 | `BaseUDPPort` | Defines the lower boundary of UDP ports to be used by the board. |  |
| 258 | `Basic` | Unknown auth method |  |
| 259 | `BasicRTPPacketInterval` | Selects the RTP packet rate for sample based coders (such as G.711, G.726, G.727). | Default/0,5 Msec/1,10 Msec/2 |
| 260 | `BehaviorUponRadiusTimeout` | Defines device behavior upon a RADIUS timeout. |  |
| 261 | `BellModemTransportType` | Sets the Bell modem transport over the network method. | Disable/0,ByPassEnable/2,EventsOnly/3 |
| 262 | `BellcoreCallerIDTypeOneSubStandard` | Selects the sub-standard of the Bellcore Caller ID type. | Bellcore_Between_Rings/0,Bellcore_Not_Ring_Related/1,Bellcore_Before_Ring_RP_AS/2 |
| 263 | `BellcoreCallerIdNoneStandard` | Enables use Bellcore Caller ID none standard mode (for working with Avaya PBX). |  |
| 264 | `BellcoreVMWITypeOneStandard` | Defines the Bellcore VMWI standard. | Bellcore_VMWI_Between_Rings/0,Bellcore_VMWI_Not_Ring_Related/1 |
| 265 | `Bits` | Network B |  |
| 266 | `BlindTransferMngr` | Illegal State (%s) to handle Ev |  |
| 267 | `BoardQueue` | GW STACK QUE OVERLOAD:%s |  |
| 268 | `Body` | Body here |  |
| 269 | `BootPDelay` | Defines the delay before start BootP. |  |
| 270 | `BootPRetries` | Defines the number of BootP retries that the board sends during start-up. |  |
| 271 | `BootPSelectiveEnable` | Configures board so will only accept BootP replies from AudioCodes proprietary BootP-TFTP Software. |  |
| 272 | `Boundary` | Boundary is too long. Truncated to %d chars |  |
| 273 | `BriLayer2Mode` | Sets the ISDN layer2 mode. Applicable to BRI trunks only. | BRI L2 MODE P2P/0,BRI L2 MODE P2MP/1 |
| 274 | `BrokenConnectionDuringSilence` | Enables generate BrokenConnection event during silence period if channel stop recieve NoOp packets. |  |
| 275 | `BrokenConnectionEventActivationMode` | Determines if Broken Connection timer is active before or after receiving the first RTP packet. | acActivateBrokenConnectionAfterFirstIncomingRTPPacket/0,acActivateBrokenConnectionOnRTPStreamActi... |
| 276 | `BrokenConnectionEventTimeout` | Determines how long the RTP connection should be broken before the Broken Connection event is issued [100ms]. |  |
| 277 | `BspDebugLevel` | Sets the output level of BSP debug messages sent by the Gateway. |  |
| 278 | `BufferSDPBody` | CHashMap::CHashMap - Allocation Exception |  |
| 279 | `Bypass` | Events only |  |
| 280 | `CACompromise` | Affiliation Changed |  |
| 281 | `CALEA` | Cid can be between 0 and %d |  |
| 282 | `CALLERID` | Caller-ID length is limited to %d |  |
| 283 | `CALLERIDTYPE` | Standard Bellcore |  |
| 284 | `CALLFORWARDRINGTONEID` | Ringtone type for Call forward notification |  |
| 285 | `CALLINGNUMBERPLAYBACKID` | Calling Number Play Back ID |  |
| 286 | `CALLINGPARTYCATEGORYMODE` | Calling Party Category Mode | None /0,Brazil R2 /1,Argentina R2 /2 |
| 287 | `CALLPRIORITYMODE` | Priority mode | Disable /0,MLPP /1,Emergency /2 |
| 288 | `CALLREROUTINGMODE` | Call Rerouting Mode for Trunk.  Set to 1 to enable ISDN call rerouting | None/0,ISDN Rerouting Enabled/1 |
| 289 | `CALLSMANB` | Manual Disconnect primary call of Trunk<0,1,2...>:%d Channel<0,1,2...>:%d |  |
| 290 | `CALLSNOW` | Current active Channels: %d |  |
| 291 | `CANMAPALIASES` | If enabled, Gatekeeper can change gateway destination number using the Alias parameter in ACF message |  |
| 292 | `CASDelimitersPaddingUsage` | Defines the digits string delimiter padding usage for the specific trunk. |  |
| 293 | `CASSENDHOOKFLASH` | 0 (default): Hookflash not forwarded 1:HookFlash forwarded - Testing |  |
| 294 | `CASTableIndex` | Indicates the CAS Protocol file to be used on the specific Trunk. |  |
| 295 | `CASTransportType` | Controls the ABCD signaling transport type over IP. | CASEventsOnly/0,CASRFC2833Relay/1 |
| 296 | `CDRREPORTLEVEL` | CDR reports timing | None /0,End Call /1,Start & End Call /2,Connect & End Call /3,Start & End & Connect Call /4 |
| 297 | `CDRSYSLOGSERVERIP` | Syslog server IP address for sending CDRs |  |
| 298 | `CEDEBUG` | Enable the MEM and engines debug value. |  |
| 299 | `CEDTransferMode` | 0-transfer CED using T38. 1-transfer CED over VBD(some Vxx=2) or VoIP(Vxx=0). 2-transfer CED using RFC, and block CED... | T38-or-VBD/0,Voice-or-VBD/1,RFC4733-Blocking-RTP-VBD/2,RFC4733-Along-With-RTP-VBD/3 |
| 300 | `CHANNELSELECTMODE` | Default method to use for trunk B-channel allocation (IP to Tel calls) | By Dest Phone Number /0,Cyclic Ascending /1,Ascending /2,Cyclic Descending /3,Descending /4,Dest ... |
| 301 | `CHANTOUSE` | COLON is missing after CHANTOUSE |  |
| 302 | `CHARGEINDICATORMODE` | Charge Indicator Mode | Disabled /0,R2 Charge Info Interworking /1 |
| 303 | `CHRRTIMEOUT` | Call hold reminder ring maximum ringing time (in seconds) |  |
| 304 | `CIDNOTIFICATION` | If NO PRESENTATION arrived from PSTN and this parameter enabled,than the presentation will be allowed. If this parame... |  |
| 305 | `CLEAR` | Number Timers allocated %d, max allowed %d, current Timer timestamp %u, Timer debug is active %d |  |
| 306 | `CLIENTDEFAULT` | Failed to get Config File from Flash |  |
| 307 | `CLISCRIPT` | Load File |  |
| 308 | `CLISTARTUPSCRIPT` | Load CLI Startup Script |  |
| 309 | `CMAC` | OpenSSL CMAC method |  |
| 310 | `CMDSHELL` | WatchDog CmdShell format is CmdShell |  |
| 311 | `CNGDetectorMode` | Determines the fax CNG tone detector mode. | Disable/0,Relay/1,Event Only/2 |
| 312 | `CNONCE` | Cnonce parameter used for authentication |  |
| 313 | `CODERPRIORITYNEGOTIATION` | Defines the coder priority in SDP negotiation. Default: according remote SDP |  |
| 314 | `CODERTBLFILENAME` | Coders table file name |  |
| 315 | `CONFERENCECODE` | Control Key activation of the 3 way conference |  |
| 316 | `CONFERENCEID` | Identification of conference call (To be used by SIP INVITE) |  |
| 317 | `CONFUSERTYPE` | Illegal ConfUserType value |  |
| 318 | `CONNECT` | Test is busy. connect command ignored |  |
| 319 | `CONNECTEDNUMBERPLAN` | Connected Number Plan |  |
| 320 | `CONNECTONPROGRESSIND` | FXS:generate CallerId siganls during ringing FXO:collect CallerId and use it in Setup message. |  |
| 321 | `CONSIDERREMOTEPACKETINTERVAL` | Remote Packet Interval |  |
| 322 | `CONTROL` | Illegal media |  |
| 323 | `CONTROLPROTOCOL` | CID [%d] NOT Opened ! |  |
| 324 | `COPYDEST2REDIRECTNUMBER` | 0 - Redirect N not affected,1- Called N after manipulation from TEL2IP call will also be used as Redirect N,2 - the C... | Don't copy/0,Copy after phone number manipulation/1,Copy before phone number manipulation/2 |
| 325 | `COPYDESTONEMPTYSOURCE` | In case there is empty source number from PSTN the source number will be the same as the destination |  |
| 326 | `CPCipherSuiteType` | Defines the default cipher type for the control protocol: 0 = none ,1 = TGCP , 2 = SRTP | cpNoCipher /0,cpCableCypherType/1,cpSRTPCypherType /2 |
| 327 | `CPConnectionStatistics` | Used to enable/disable print of statistical information regarding a connections for digital boards. |  |
| 328 | `CPPlayAnnouncementToNetworkSide` | Forces announcements to be played towards network side (MGCP). |  |
| 329 | `CPPlayDigitalVMWI` | Selects the method used for VMWI. |  |
| 330 | `CPSDPPROFILE` | This parameter is a bit mask which defines the functionality of SDP negotiation. See the user manual for details. |  |
| 331 | `CPSDPSESSIONOWNER` | Defines the owner/creator of the session. |  |
| 332 | `CPSERVICECHANGEPROFILE` | Specifies the Profile (if any) of the supported protocol. |  |
| 333 | `CPTDETECTORFREQUENCYDEVIATION` | Defines the frequency deviation allowed for the detection of CPT (Call Progress Tones). [Hz]. |  |
| 334 | `CPTransportType` | Defines the transport type for the control protocol. | acCPTransport_UDP_IP/0,acCPTransport_TCP_IP/1,acCPTransport_SCTP_IP/2 |
| 335 | `CPTrunkIdOffset` | Sets the trunk numbering offset. |  |
| 336 | `CREATEENDPOINT` | CreateEndpoint Fail. error=%d |  |
| 337 | `CRLReason` | X509v3 CRL Reason Code |  |
| 338 | `CRPGATEWAYFALLBACK` | Enable fallback route from Proxy to Gateway |  |
| 339 | `CRPSURVIVABILITYMODE` | Defines the CRP functionality modes: (0)Normal, (1)Always  Emergency, (2)Auto answer to registrations | Standard Mode /0,Always Emergency Mode /1,Auto-answer REGISTER /2 |
| 340 | `CRYPTOBYSW` | This parameter is used force using SW crypto engine - relevant in 6310/8410 boards |  |
| 341 | `CSPName` | Microsoft CSP Name |  |
| 342 | `CSRFPROTECTION` | Enable or disable the CSRF Protection |  |
| 343 | `CURRENT` | Invalid TraceType parameter |  |
| 344 | `CUTTHROUGH` | Enable call connection without On-Hook/Off-Hook process 'Cut-Through' |  |
| 345 | `CUTTHROUGHTIMEFORREORDERTONE` | Duration of reorder tone played after release from IP side for CutThrogh application |  |
| 346 | `CacHeStatistics` | Streaming Cache Cleared |  |
| 347 | `CallAgentDomainName` | Defines a domain name to be used to connect with the Call Agent. |  |
| 348 | `CallAgentIP` | MGCP Call Agent IP address used for initial RSIP message. |  |
| 349 | `CallAgentPort` | UDP Port of MGCP Call Agent. |  |
| 350 | `CallMachine` | Call::StartCommonTimer for reason %d failed as timer with reason %d is running |  |
| 351 | `CallProgressDetectorEnable` | Enables or disables detection of Call Progress Tones. |  |
| 352 | `CallProgressTonesFilename` | Defines Call Progress Tone filenames. |  |
| 353 | `CallWaitingToneDuration` | Changes the call waiting tones family duration (in msec). |  |
| 354 | `CallerIDGeneration` | Defines the type of Caller ID. |  |
| 355 | `CallerIDTransportType` | Defines the Caller ID Transport type. | Disable/0,Relay/1,Mute/3 |
| 356 | `CallerIDType` | Defines the Caller ID standard. | Standard Bellcore /0,Standard ETSI /1,Standard NTT /2,Standard BT /4,Standard DTMF Based ETSI /16... |
| 357 | `Calls` | SUBSCRIBE Dialogs |  |
| 358 | `Cancel` | CMP buffer creation error |  |
| 359 | `Cancelling` | SIPCallCancellingState::Failed to allocate SIPMessage |  |
| 360 | `CasChannelIndex` | Sets the CAS Protocol Table index per channel. |  |
| 361 | `CasFileUrl` | Provides a link to a Channel Associated Signaling (CAS) file to be downloaded from a remote server. |  |
| 362 | `CasTrunkDialPlanName` | Sets the Dial Plan name that will be used on the specific trunk. |  |
| 363 | `CdrSyslogSeqNum` | Enables Sequence Numbering of SIP CDR Syslog Messages. |  |
| 364 | `CertificateMgmt` | CertificateMgmt - Manage TLS certificates. |  |
| 365 | `Certificates` | Web User Accounts |  |
| 366 | `ChangePassword` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Change Password' page. |  |
| 367 | `ChangeSignalState` | SM INFO: SignalManager MaxSigNum=%d MaxChanNum=%d |  |
| 368 | `ChannelErrCountersThresholds` | Enable to define up to 8 Channel Error Counters with Threshold. |  |
| 369 | `ChannelSelectMode` | Channel Select Mode | Not Configured /255,By Dest Phone Number /0,Channel Cyclic Ascending /1,Always Ascending /2,Cycli... |
| 370 | `Charging` | Charge Codes |  |
| 371 | `ChassisPhysicalAlias` | Physical alias of the Mediant 1000 Chassis. |  |
| 372 | `CheckIpProfileCallsLimit` | CheckIpProfileCallsLimit:Profile:%d Invalid Value:%d |  |
| 373 | `ClassificationInput` | IP only | /ProxySetsTable@50,100,0 |
| 374 | `ClassifyByProxySet` | Classify By Proxy Set |  |
| 375 | `ClearRequestBuffer` | Determines when signals and events are cleared. |  |
| 376 | `ClearStreamingCache` | Clears Streaming Cache |  |
| 377 | `CliDbg` | SocketsDebug: create socket failed. |  |
| 378 | `CliDbg_Recv` | SocketsDebug: create recv socket failed. |  |
| 379 | `CliDbg_Send` | SocketsDebug: create send socket failed. |  |
| 380 | `CliSctpTst` | CreateAssociation Fail. error=%d |  |
| 381 | `Client` | Socket error to RTSP %s: error number = %d |  |
| 382 | `ClockMaster` | Selects the trunk clock source. | acCLOCK_MASTER_OFF/0,acCLOCK_MASTER_ON/1 |
| 383 | `Close` | ResetSocket failed: error=%d |  |
| 384 | `CloseChannel` | SetDetectorsFields with fax from IP |  |
| 385 | `CmdShellAutoBuffering` | Enables or disables automatic MORE prompts in CLI. |  |
| 386 | `CmdShellFront` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Command Shell' page. |  |
| 387 | `CmpFileURL` | Provides a link to a software image (cmp file) to be downloaded from a remote server. |  |
| 388 | `CoderName` | No valid Cid [row %d] |  |
| 389 | `CoderTableFileUrl` | Provides a link to a coder table file that is to be downloaded from a remote server. |  |
| 390 | `Coders` | Coders Group Settings |  |
| 391 | `ConfNewAdminPW` | Change Password |  |
| 392 | `ConfNewUserPW` | Change Password |  |
| 393 | `ConfResourceEndPointRsrc` | ConfResourceEndPoint::Init, VCID Allocation failed |  |
| 394 | `ConferenceMaxSimultaneousSpeakers` | Number of users that can speak together in a conference. |  |
| 395 | `ConferenceMaxUsers` | Defines the maximal number of users to reserve for a new conference. |  |
| 396 | `ConferenceSignalGenerationEnable` | Defines if a BEEP tone is generated when a user enters or leaves the conference. |  |
| 397 | `ConferenceTermPattern` | Defines the name pattern of a conference termination. |  |
| 398 | `Configuration` | Invalid upload file type |  |
| 399 | `ConfigurationFile` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Configuration File' page. |  |
| 400 | `ConfigureDeadPeerDetection` | Configure IPsec Dead Peer Detection |  |
| 401 | `Connected` | SIPCallConnectedState:Disconnect #%d Fatal error in sending 500 response |  |
| 402 | `ConnectionEstablishmentNotificationMode` | Determines if Connection Establishment notification is sent after Broken Connection or from call startup. | acNotifyConnectionEstablishedAfterBrokenConnection/0,acNotifyConnectionEstablishedUponFirstRTPFra... |
| 403 | `ConnectionIDBase` | Defines the lowest number for the Connection ID values assigned by the gateway. |  |
| 404 | `ConnectionIDRange` | Defines the range for the Connection ID values assigned by the gateway. |  |
| 405 | `Constructor` | Tr069 Main Task Id %d |  |
| 406 | `ContactUser` | Contact User |  |
| 407 | `ContextEngineID` | Context Engine ID - at start up set to the MAC address. |  |
| 408 | `Control` | OAMP & Media |  |
| 409 | `ControlCidTraceData` | Control trace data for CID |  |
| 410 | `ControlDiffServ` | Defines the value of the 'DiffServ' field in the IP header for control traffic. |  |
| 411 | `CopyConfigurationFile` | AUPD: File download retry failed, Redirected Server Ip = %x. |  |
| 412 | `CopyDest2RedirectNumber` | After Manipulation |  |
| 413 | `CoreDumpDestIP` | Defines the IP address where a core-dump will be sent upon exception. |  |
| 414 | `CountryCoefficients` | Allows the user to modify the line characteristic (AC and DC) according to country. | Argentina /0,Australia /1,Austria /2,Bahrain /3,Belgium /4,Brazil /5,Bulgaria /6,Canada /7,Chile ... |
| 415 | `CptFileUrl` | Provides a link to a Call Progress Tones (CPT) file to be downloaded from a remote server. |  |
| 416 | `CrAccessIPAddr` | Add New Entry |  |
| 417 | `CreateTransport` | Device:1.0[](Baseline:1), ABCService:1.0[1](Baseline:1) |  |
| 418 | `Critical` | Non Critical |  |
| 419 | `CurrentDisconnectDefaultThreshold` | Sets the voltage threshold for the current disconnect detection. |  |
| 420 | `CurrentDisconnectDuration` | Defines the current-disconnect duration (in msec). |  |
| 421 | `DANISH_CALLERID_TIME_BEFORE_CID` | The time before a Caller ID signal (DTMF based), in the Danish Caller ID type. |  |
| 422 | `DANISH_CALLERID_TIME_BETWEEN_CID_TO_RING` | The time between a Caller ID signal (DTMF based) and the start of a ring, in the Danish Caller ID type. |  |
| 423 | `DCHConfig` | Sets the ISDN NFAS D-channel type. | acDCH_CONFIG_PRIMARY/0,acDCH_CONFIG_BACKUP/1,acDCH_CONFIG_NFAS/2 |
| 424 | `DEBUG` | SocketsDebug: Receive failed. Got error code %d |  |
| 425 | `DEBUGLEVELHIGHTHRESHOLD` | Threshold for auto-switching of debug level. 5-1 is at value, 1-0 is value + 5, 0-1 is value - 5, 1-5 is value - 20 |  |
| 426 | `DECLAREAUDCCLIENT` | 0 (default): Disable 1:Add special header with capabilities for Lync |  |
| 427 | `DEFAULT` | Scenario step %s has been modified. |  |
| 428 | `DEFAULTCAUSEMAPISDN2IP` | Common cause value to use for most ISDN release causes |  |
| 429 | `DEFAULTNUMBER` | Default dest number is used only if received SETUP message doesn't contain called party number |  |
| 430 | `DEFAULTRECORDURI` | Default record location URI used by Media Ctrl |  |
| 431 | `DEFAULTRELEASECAUSE` | The release cause that will be sent to IP or to Tel when gateway initiates release by itself |  |
| 432 | `DELAYED_INVITE_EXPIRED_EV` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 433 | `DEST` | Dest phone number = %s. |  |
| 434 | `DESTADDR` | Bad command! SIP interface not entered. |  |
| 435 | `DESTENCODTYPE` | Called number coding type in Setup message |  |
| 436 | `DESTNUMBERPLAN` | Dest Number Plan |  |
| 437 | `DETFAXONANSWERTONE` | Start T.38 fax procedure after fax answer tone detection or after HDLC preamble signal detection | Initiate T.38 on Preamble /0,Initiate T.38 on CED /1 |
| 438 | `DEVICES` | DSP Device Statistics: |  |
| 439 | `DEbug` | TACACS+ login (ADD user password, DEL #, or LIST) |  |
| 440 | `DHCP120OptionMode` | Sets mode of DHCP 120 Option. 0 means not supported. 1 means supported (SIP parameter). |  |
| 441 | `DHCPClnt` | Cannot register vlan tag information for dhcp |  |
| 442 | `DHCPDuplicateAddressDetection` | Enables or disables DHCP duplicate address detection using ARP. |  |
| 443 | `DHCPEnable` | Enable/Disable DHCP support. |  |
| 444 | `DHCPHostnameFormat` | DHCP hostname (option 12) format selection: ACL_n or IADA24x |  |
| 445 | `DHCPHostnamePrefix` | DHCP hostname (option 12) format prefix. |  |
| 446 | `DHCPInformSupport` | Enable DHCP INFORM support for SIP application discovery. |  |
| 447 | `DHCPRebootWhenLeaseExpires` | Forces reboot if the DHCP lease expires. |  |
| 448 | `DHCPRequestTftpParams` | Determines if DHCP option 55 should contain TFTP provisioning values (66 and 67). |  |
| 449 | `DHCPSpeedFactor` | Controls the DHCP renewal speed. |  |
| 450 | `DIAG` | Diagnostic Channels/ |  |
| 451 | `DIALPLANINDEX` | Dial Plan Index |  |
| 452 | `DIGITALOOSBEHAVIOR` | Digital OOS Behavior | Default /0,Service /1,D-Channel /2,Alarm /3,Block /4 |
| 453 | `DIGITALOOSBEHAVIORFORTRUNK` | Digital OOS Behavior for trunk put  OOS_NOT_SET (-1) to use DIGITALOOSBEHAVIOR per Gateway | Not configured/-1,Default/0,Service/1,D-Channel/2,Alarm/3,Block/4 |
| 454 | `DIGITMAPPING` | The digit map patterns separated by a vertical bar (/), as defined in the MEGACO RFC. |  |
| 455 | `DISABLE` | Disable certificate verification error messages |  |
| 456 | `DISABLEAUTODTMFMUTE` | Disables inband auto mute of DTMFs when signalling is used for sending DTMFs |  |
| 457 | `DISABLECRYPTOLIFETIMEINSDP` | Disable Crypto Life Time In SDP |  |
| 458 | `DISABLED` | Dumped E911 table. Refer to Syslog. |  |
| 459 | `DISABLEFALLBACKTRANSFERTOTDM` | Disable fallback from ISDN Call Transfer to TDM |  |
| 460 | `DISABLEREMINDERRING` | Reminder Ring | Enable /0,Disable /1 |
| 461 | `DISABLESTRICTDIALPLAN` | Disable Strict Dial Plan |  |
| 462 | `DISCONNECT` | Test is idle. Release command is ignored |  |
| 463 | `DISCONNECTCALLWITHPIIFALT` | If set to 1 and ISDN DISCONNECT with PI is received, 183 with SDP will be sent toward IP only if no IP-to-Tel alterna... |  |
| 464 | `DISCONNECTONBROKENCONNECTION` | Disconnect calls on receiving RTP broken notification |  |
| 465 | `DISCONNECTONBUSYTONE` | Release call if gateway receives busy or fast busy tone before the call is answered |  |
| 466 | `DISCONNECTONDIALTONE` | Releases a call on detection of dial tone from PSTN side |  |
| 467 | `DISPLAY` | The following fax/modem debug msg options are set: |  |
| 468 | `DISPLAYDEFAULTSIPPORT` | When it is enabled and the headers have been manipulated the default port 5060 is shown in the headers. |  |
| 469 | `DISTHROTTLING` | The Error 0x%x generated on Cid %d %d times (Time Duration = %d.%d ms) OverRun = %d |  |
| 470 | `DIS_PING_LOST` | Stop ping lost simulation |  |
| 471 | `DIS_RESET` | Disable network watchdog reset in failure |  |
| 472 | `DIS_TRACE` | Disabling network watchdog trace |  |
| 473 | `DJBufMinDelay` | Defines the Dynamic Jitter Buffer Minimum Delay [msec] |  |
| 474 | `DJBufOptFactor` | Defines the Dynamic Jitter Buffer attack/decay performance. |  |
| 475 | `DMDynDSPAllocNotSupport` | QA Only |  |
| 476 | `DNSPriServerIP` | Defines the DNS Primary server IP address. |  |
| 477 | `DNSQUERYTYPE` | DNS Query Type: 0-ARecord, 1-SRV, 2-NAPTR . Has effect on every DNS query in the system | A-Record /0 ,SRV /1,NAPTR /2 |
| 478 | `DNSRetries` | Number of times to retransmit DNS requests. |  |
| 479 | `DNSSecServerIP` | Defines the DNS Secondary server IP address. |  |
| 480 | `DNSTimeout` | Amount of time (in seconds) to wait before retransmitting a DNS request. |  |
| 481 | `DOWN` | Oper Status of PPP Interface is %s |  |
| 482 | `DROP` | Sent Release event |  |
| 483 | `DS3AlarmConsolidation` | When SET to 1 trunks |  |
| 484 | `DSPINFO` | Error Handler print DSP info - was set to %d |  |
| 485 | `DSPVersionTemplateNumber` | Selects the DSP s/w load number. |  |
| 486 | `DTMFDetectorEnable` | Enables or disables detection of DTMF signals. |  |
| 487 | `DTMFDetectorSensitivity` | Sensitivity of DTMF detector |  |
| 488 | `DTMFDialOffTime` | Analog DTMF Dial off time |  |
| 489 | `DTMFDialOntime` | Analog DTMF dial on time |  |
| 490 | `DTMFDigitLength` | Defines the time to play DTMF (in msec). |  |
| 491 | `DTMFGenerationTwist` | Defines a delta between the high and low frequency components in the DTMF signal [db]. |  |
| 492 | `DTMFInterDigitInterval` | Defines the time between DTMFs played (in msec). |  |
| 493 | `DTMFInterDigitThreshold` | Threshold of received DTMF InterDigitTime in milli seconds. DTMF with shorter InterDigitTime is ignored! |  |
| 494 | `DTMFS` | DTMF string is limited to %d |  |
| 495 | `DTMFTransportType` | Defines the way DTMFs are transported over the network. | RFC 2833 Relay Decoder Mute/7,RFC 2833 Relay DTMF/3,Transparent DTMF/2,Mute DTMF/0 |
| 496 | `DTMFVolume` | Defines the DTMF generation volume [-dbm]. |  |
| 497 | `DUALIPSTACKSDPMETHOD` | Method to offer two media IP addresses within SDP - one for IPv4 and another for IPv6. | None /0,ANAT /1 |
| 498 | `DYNADD` | Added dyn rule #%d |  |
| 499 | `DayLightSavingTimeEnable` | Enable or disable the day light saving time |  |
| 500 | `DayLightSavingTimeEnd` | Defines the Day Light Saving Time End in format mo:dd:hh:mm or mo:wday/week:hh:mm where week of month is 1-4, or 5 fo... |  |
| 501 | `DayLightSavingTimeMode` | Day of year |  |
| 502 | `DayLightSavingTimeOffset` | Day light saving time offset in minutes: 0-120 |  |
| 503 | `DayLightSavingTimeStart` | Defines the Day Light Saving Time Start in format mo:dd:hh:mm or mo:wday/week:hh:mm where week of month is 1-4, or 5 ... |  |
| 504 | `DeActivate` | Add Index |  |
| 505 | `Deactivate` | On busy |  |
| 506 | `Debug` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Debug Recording' page. |  |
| 507 | `DebugCertVerfication` | DebugCertVerfication - Enable/Disable printing the error in case the certificate verfication fails |  |
| 508 | `DebugRecordTrigger` | Define Trigger to activate Debug Record on certain CID |  |
| 509 | `DebugRecordingDestIP` | Defines the destination IP address for Debug Recording default target |  |
| 510 | `DebugRecordingDestPort` | Defines the destination UDP Port for Debug Recording default target |  |
| 511 | `DebugRecordingEnableOptimized` | Enable Optimized mode control |  |
| 512 | `DebugRecordingStatus` | Determines if Debug Recording should be Stopped (0) or Started (1) | Stop/0,Start/1 |
| 513 | `Default` | 32 msec |  |
| 514 | `DefaultAccessLevel` | Defines the default access level for the device. |  |
| 515 | `DefaultPacketizationPeriod` | Default packetization period for control protocols. |  |
| 516 | `DefaultSecretKeyMethod` | Set RTP RTCP default method of key generation ,base64 = 0 (default) clear = 1 |  |
| 517 | `Delay` | Remote Delay |  |
| 518 | `Delete` | Make Rule Editable |  |
| 519 | `DeleteCallsOnStopTrunk` | Delete Calls On Stop Trunk |  |
| 520 | `DeleteResourceEvent` | CList::CIterator Node = NULL |  |
| 521 | `DeleteScenario` | AuxFilesBurning FAILURE | /login@100,200,0 |
| 522 | `DenialOfServiceRtpMaxBandWidth` | Define the DSP DOS feature bandwidth threshold for RTCP port . |  |
| 523 | `DenialOfServiceT38MaxBandWidth` | Define the DSP DOS feature bandwidth threshold for RTP port . |  |
| 524 | `DenialOfServiceWindowSize` | Define the DSP DOS feature bandwidth threshold for T38 port . | DENIAL_OF_SERVICE_BANDWIDTH__0_KBPS/0,DENIAL_OF_SERVICE_BANDWIDTH__100_KBPS/1,DENIAL_OF_SERVICE_B... |
| 525 | `DenyAccessOnFailCount` | Defines the number of attempts where, afterwards, the requesting IP will be blocked. |  |
| 526 | `DenyAuthenticationTimer` | Defines a period of time where, following failed login attempts, the relevant ip will be denied, in seconds. 0 Means ... |  |
| 527 | `DepopulatedchannelsNumber` | Enables the Call Agent to access only a subset of the on-board channel bank. |  |
| 528 | `Descending` | Dest Number + Cyclic Ascending |  |
| 529 | `Destination` | Destination Phone Number |  |
| 530 | `DhcpOption66WasUsed` | Determines if DHCP option 66 was already used. |  |
| 531 | `DiagBitFailed` | N/A Diagnostics Bit return code |  |
| 532 | `DialPlan` | CList::CIterator Node = NULL |  |
| 533 | `DialPlanFileName` | This parameter is used to indicate the name of the file containing the Dial Plan. |  |
| 534 | `DialPlanFileUrl` | URL for downloading a Dial Plan file. |  |
| 535 | `DialPlanHandler` | DPLN: finished decommission process |  |
| 536 | `DialToneDuration` | Defines the timeout (in seconds) for the dial tone signal. |  |
| 537 | `DialedStringPrefix` | Defines a prefix to add to the dialed string. |  |
| 538 | `DigitDelivery2IPMngr` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 539 | `DigitMapName` | Name of the provisioned digit map. |  |
| 540 | `DigitMapTimeoutTimer` | Defines the timeout value (T symbol) in a digit map. |  |
| 541 | `DigitPatternDigitToIgnore` | A digit (0-9,A-D,* or #) that if received as Src (S) or Redirect (R), the digit is ignored and not added to that numb... |  |
| 542 | `DigitPatternExternalCall` | Digit pattern used to indicate external call (PBX to VoiceMail) |  |
| 543 | `DigitPatternForwardNoReason` | Digit pattern used to indicate Call Forward with no reason (PBX to VoiceMail) |  |
| 544 | `DigitPatternForwardNoReasonExt` | Forward on No Reason Digit Pattern (External) |  |
| 545 | `DigitPatternForwardOnBusy` | Digit pattern used to indicate Call Forward on busy (PBX to VoiceMail) |  |
| 546 | `DigitPatternForwardOnBusyExt` | Forward on Busy Digit Pattern (External) |  |
| 547 | `DigitPatternForwardOnDND` | Digit pattern used to indicate Call Forward on Do Not Disturb (PBX to VoiceMail) |  |
| 548 | `DigitPatternForwardOnDNDExt` | Forward on Do Not Disturb Digit Pattern (External) |  |
| 549 | `DigitPatternForwardOnNoAnswer` | Digit pattern used to indicate Call Forward on no answer (PBX to VoiceMail) |  |
| 550 | `DigitPatternForwardOnNoAnswerExt` | Forward on No Answer Digit Pattern (External) |  |
| 551 | `DigitPatternInternalCall` | Digit pattern used to indicate internal call (PBX to VoiceMail) |  |
| 552 | `DisIPAddr` | Delete Selected Addresses | /WebAccessList@200,200,0 |
| 553 | `Disable` | CNSL msg too long: %d |  |
| 554 | `DisableAnalogAutoCalibration` | Determines whether to enable the analog Autocalibration in the DAA. | disable/0,enable/1 |
| 555 | `DisableDLCXByGW` | Enable or disable the generation of DLCX from the gateway side. |  |
| 556 | `DisableH100ClocksOnTrunkFailure` | Disables H100 clock output when PSTN reference trunk fails. |  |
| 557 | `DisableICMPRedirects` | Disable handling of ICMP redirect messages. |  |
| 558 | `DisableNetRefOnTrunkFailure` | Disables the NETREF signal when PSTN reference trunk fails. |  |
| 559 | `DisableRS232` | Enables or disables the RS-232 port. |  |
| 560 | `DisableRTCPRandomize` | Controls whether RTCP report intervals are randomized, or whether each report interval accords to RTCPMeanTxInterval ... |  |
| 561 | `DisableSNMP` | Determines whether to enable SNMP. | no/0,yes/1 |
| 562 | `DisableTPNCPEvent` | Disables events reporting of a specific Event (see enum acTEvent). |  |
| 563 | `DisableWebConfig` | Enables or disables Web Configuration. |  |
| 564 | `DisableWebtask` | Enables or disables Web Server Tasks. |  |
| 565 | `Disabled` | Illegal webs columns order init. |  |
| 566 | `DisconnectBehavior` | Determines PBX behavior upon losing connectivity with H.248 Call agent or TPNCP. | NoActionOnDisconnect/1,DisableTrunksOnDisconnect/2,ResetBoardOnDisconnect/3,ActivateLifeLineOnDis... |
| 567 | `DisconnectToneType` | Defines the type of call progress tone for disconnection. |  |
| 568 | `Disconnected` | SIPCallDisconnectedState::Failed to allocate SIPMessage |  |
| 569 | `DisconnectingState` | ControlCallT38Support for State (%s) ignored. |  |
| 570 | `DispWebUsers` | Displays the current web users |  |
| 571 | `DisplayIniCfg` | INI Configuration |  |
| 572 | `DisplayLoginInformation` | Displays the web server' login information . |  |
| 573 | `DisplayString` | Display String | Allowed /0,Restricted /1 |
| 574 | `DistinctiveRingFreq0` | Defines the Distinctive Ringing Frequency, in units of 10 msec. |  |
| 575 | `DistinctiveRingFreq1` | Defines the Distinctive Ringing Frequency. |  |
| 576 | `DistinctiveRingFreq2` | Distinctive Ringing Freq |  |
| 577 | `DistinctiveRingTimeOut0` | Defines the Distinctive Ringing Time Out period. |  |
| 578 | `DistinctiveRingTimeOut1` | Distinctive Ringing time out |  |
| 579 | `DiversionBuffer` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 580 | `Dns1` | DNS Name 1 |  |
| 581 | `Dns2` | DNS Name 2 |  |
| 582 | `Dns3` | DNS Name 3 |  |
| 583 | `DoReboot` | Board reset error |  |
| 584 | `Done` | Interface Table configured successfully. The new configuration will be applied at the next start-up. |  |
| 585 | `Double` | Wink & Polarity |  |
| 586 | `DspCoreDumpUrl` | Provides link for external HTTP server for send DSP Core Dump files. |  |
| 587 | `DspsMiiEnable` | Enables/Disables Dsps MII Interface. |  |
| 588 | `DstHostBeforeMap` | IPG (description) |  |
| 589 | `DstPort` | VQBuildAndSendMEStat:cannot find interface name %d |  |
| 590 | `DtmfGenerationMaxDuration` | Sets the maximum duration for DTMF generated by IBS packet in unit of 100 ms. 0 value (default) means there is no lim... |  |
| 591 | `DummySRDSet` | IP Group Status Table | /SRDTableIFrame@50,100,0 |
| 592 | `DynamicRsrcContainer` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 593 | `E911CALLBACKTIMEOUT` | Maximum time for an E911 ELIN callback to be valid (minutes) |  |
| 594 | `E911GATEWAY` | Enables E911 to NG911 gateway and ELIN handling | None/0,NG911 Callback Gateway/1,Location Based Manipulations/2 |
| 595 | `E911MLPPBEHAVIOR` | Defines the MLPP E911 Preemption mode: (0)-Standard Mode (ets calls will have the highest priority and can preemt any... | Standard Mode /0,Treat As Routine Mode /1 |
| 596 | `EARLYANSWERTIMEOUT` | Max time (in seconds) to wait from sending setup message to PSTN to receiving connect message from PSTN. |  |
| 597 | `ECDCRemoval` | Enables the DC removal feature of the Echo Canceler. |  |
| 598 | `ECEnable` | Display Fax Call Data Record |  |
| 599 | `ECEnableComfortNoiseGeneration` | Use this parameter to enable or enable Echo Canceler Comfort Noise Generation, which generates comfort noise when the... |  |
| 600 | `ECEnableToneDetector` | Used to configure the Echo Canceler Tone Detector. Detects a 2100 Hz tone at the input signal to the TDM (received si... |  |
| 601 | `ECFreeze` | Freezes echo canceller internal state and avoids additional adaptations |  |
| 602 | `ECHOCANCELLERTYPE` | Echo Canceller type. Line echo canceller for TDM Side or acoustic echo suppressor on network side. | Line echo canceller /0,Acoustic Echo suppressor - network /1 |
| 603 | `ECHybridLoss` | Sets worst case ratio between signal level transmitted to hybrid & echo level returning from hybrid. | ECHybridLoss6DBM/0,ECHybridLoss0DBM/2,ECHybridLoss3DBM/3 |
| 604 | `ECNLPMode` | Defines the echo cancellation non-linear processing mode. | ECAdaptiveNlp/0,ECDisableNlp/1,ECSilenceOutputNlp/2 |
| 605 | `ECNLPThreshold` | Define the NLP Threshold, by dafault it's adaptive . |  |
| 606 | `ECNlpMode` | Adaptive NLP |  |
| 607 | `ECNlpSensitivity` | Define the NLP sensitivity if EC NLP mode is Adaptive. |  |
| 608 | `ECNoiseEnvironmentMode` | ENABLE / DISABLE Noisy Environment Mode |  |
| 609 | `ECResidualOverwrite` | Defines if Echo Canceller perform Residual Overwrite. 0 - Disable  1 - Enable |  |
| 610 | `EMERGENCYSPECIALRELEASECAUSE` | MS LDAP Settings |  |
| 611 | `EMPTYAUTHORIZATIONHEADER` | If empty Authorization header should be added into Register request |  |
| 612 | `ENABLE` | Enable certificate verification error messages |  |
| 613 | `ENABLE3WAYCONFERENCE` | Enable 3 way conference feature |  |
| 614 | `ENABLE911LOCATIONIDIP2TEL` | Enable 911 Location Id in NI2 protocol |  |
| 615 | `ENABLE911PSAP` | Enable the PSAP Call flow (Relevant to FXO) |  |
| 616 | `ENABLEALTMAPTEL2IP` | Enables different number manipulation rulse for redundant calls |  |
| 617 | `ENABLEAOC` | Enable AoC-D and AoC-E from ISDN to SIP |  |
| 618 | `ENABLEBINARYREDIRECT` | Search for Redirect number coded in binary 4 bit style |  |
| 619 | `ENABLEBUSYOUT` | Take trunks out of service in case of LAN down |  |
| 620 | `ENABLECALLERID` | FXS: Generate Caller ID; FXO: Collect Caller ID information | Disable/0,Enable/1 |
| 621 | `ENABLECALLINGPARTYCATEGORY` | Enables NI2 calling party category translation to SIP |  |
| 622 | `ENABLECALLTRANSFERUSINGREINVITES` | Enable Call Transfer using re-INVITEs |  |
| 623 | `ENABLECALLWAITING` | Enable Call Waiting service |  |
| 624 | `ENABLECIC` | Enables CIC -> ISDN TNS IE interworking |  |
| 625 | `ENABLECLIRREASON` | Enable sending of Reason for Non Notification of Caller Id |  |
| 626 | `ENABLECOMFORTTONE` | Enable Comfort Tone for playing a patience comfort tone between Invite and 18x response |  |
| 627 | `ENABLECONTACTRESTRICTION` | Hides the user part of the URI in the Contact Header |  |
| 628 | `ENABLECRPAPPLICATION` | Enables CRP (Cloud Resilience Package) functionality |  |
| 629 | `ENABLECURRENTDISCONNECT` | Disconnect call upon detection of current disconnect signal |  |
| 630 | `ENABLEDELAYEDOFFER` | Send INVITE message with/without sdp offer. |  |
| 631 | `ENABLEDID` | Enable DID support |  |
| 632 | `ENABLEDIDWINK` | Enable support for DID lines using Wink | Disable /0,Single /1,Double Wink /2,Wink & Polarity /3 |
| 633 | `ENABLEDIGITDELIVERY` | Enable automatic digit delivery to Tel side after line is off-hooked or seized |  |
| 634 | `ENABLEDIGITDELIVERY2IP` | Enable automatic digit delivery to IP side after call is connected |  |
| 635 | `ENABLEEARLY183` | Enable Early 183 |  |
| 636 | `ENABLEEARLYAMD` | If set to 1 AMD detection will be started on pstn alerting otherwise on connect |  |
| 637 | `ENABLEEARLYMEDIA` | Enable Early Media |  |
| 638 | `ENABLEETSIDIVERSION` | Use suplumentary service Etsi Diverting Leg Information 2 to send redirct number |  |
| 639 | `ENABLEFAXREROUTING` | Enable rerouting of FAX calls to FAX destination |  |
| 640 | `ENABLEFORWARD` | Enable Call Forward service |  |
| 641 | `ENABLEGRUU` | Obtain and use GRUU (Global Routable UserAgentURIs) |  |
| 642 | `ENABLEGWAPPSWWD` | Controls weather to use the software watchdog for GWAPP task |  |
| 643 | `ENABLEH235SECURITY` | Enable H.235 security |  |
| 644 | `ENABLEHISTORYINFO` | Enable History-Info header support |  |
| 645 | `ENABLEHOLD` | Enable Call Hold service |  |
| 646 | `ENABLEHOLD2ISDN` | Enable Hold/retrieve from and to ISDN |  |
| 647 | `ENABLEIMMEDIATETRYING` | If set to 1 - immediate trying will be sent upon INVITE recieve{@}If set to 0 - trying will be sent after PSTN Procee... |  |
| 648 | `ENABLEIP2IPAPPLICATION` | Enables IP2IP functionality |  |
| 649 | `ENABLEIPSEC` | This parameter is used for Secure Internet Protocol (IPsec) Policy Enable flag. |  |
| 650 | `ENABLEISDNTUNNELINGIP2TEL` | Enable ISDN tunneling to pass Setup and Facility messages from IP to ISDN |  |
| 651 | `ENABLEISDNTUNNELINGTEL2IP` | Enable ISDN tunneling to pass Setup and Facility messages from ISDN to IP | Disable /0,Using Header /1,Using Body /2 |
| 652 | `ENABLEMEDIACONTROL` | Enables media control functionality |  |
| 653 | `ENABLEMEDIASECURITY` | Enables the Media Security protocol (SRTP) | Disable/0,Enable/1 |
| 654 | `ENABLEMICROSOFTEXT` | Enables modifying the called number to the number appears in the Microsoft proprietary 'ext=xxx' parameter in INVITE ... |  |
| 655 | `ENABLEMWI` | Enable MWI support (Message Waiting Indicator) |  |
| 656 | `ENABLEMWISUBSCRIPTION` | Enable subscription for Message Waiting Indicator service |  |
| 657 | `ENABLENAMEIDENTIFICATION` | Enable Name Identification service |  |
| 658 | `ENABLENETWORKPHYSICALSEPARATION` | Enables Network Physical Separation in Supported Hardware. | UTOPIA_PROM_LOAD/0,UTOPIA_DYNAMIC_LOAD/1,UTOPIA_TFTP/2,UTOPIA_AUTOMATIC/3 |
| 659 | `ENABLENORTELHEADER` | 0 (default): No special header for Nortel 1:Add special header for Nortel |  |
| 660 | `ENABLENRTSUBSCRIPTION` | Enable subscription for Call forward ringtone indicator services |  |
| 661 | `ENABLEPARAMETERSMONITORING` | Enables monitoring of on-the-fly parameter changes via Syslog messages. |  |
| 662 | `ENABLEPASSOCIATEDURIHEADER` | Handles the P-Associated-URI  header in a 200OK response for a REGISTER request |  |
| 663 | `ENABLEPATCH` | Enables the Patch apply (if patch is loaded). |  |
| 664 | `ENABLEPCHARGINGVECTOR` | Generate P-Charging-Vector header |  |
| 665 | `ENABLEPREGRANTARQ` | ARQ message won't be sent if the Gatekeeper has pre-granted admission |  |
| 666 | `ENABLEPROXYKEEPALIVE` | Enable Proxy Keep-Alive over OPTIONS method or REGISTER method | Disable /0,Using OPTIONS /1,Using REGISTER /2 |
| 667 | `ENABLEPROXYSRVQUERY` | Enable DNS SRV queries for Proxy domain name |  |
| 668 | `ENABLEQ931CAUSE` | H.225 Reason / Q.931 Cause is sent in H.323 Release Complete message |  |
| 669 | `ENABLEQ931MULTIPLEXING` | Use same socket for all H.225 messages |  |
| 670 | `ENABLEQSIGTRANSFERUPDATE` | Enable QSIG Transfer Update |  |
| 671 | `ENABLEQSIGTUNNELING` | Enables QSIG Tunneling over SIP |  |
| 672 | `ENABLER2CATEGORYFORBRAZILTELECOM` | Enable Interworking of Calling Party Category (cpc) from sip INVITE to MFCR2 category for Brazil Telecom |  |
| 673 | `ENABLERAI` | Enables Resource Available Indication (RAI) alarm generation if the device's busy endpoints exceed a user-defined thr... |  |
| 674 | `ENABLEREANSWERINGINFO` | FXS: Enables INFO while reanswering occurs |  |
| 675 | `ENABLEREASONHEADER` | Enable Reason header in the outgoing messages |  |
| 676 | `ENABLEREKEYAFTER181` | Send Reinvite after 181 with new SRTP keys |  |
| 677 | `ENABLERESTARTSAFTERSO` | Enable/Disable Sending Restarts to PSTN on channels exeirienced mismatch in CONNID usage |  |
| 678 | `ENABLEREVERSALPOLARITY` | FXO: Connect/Disconnect calls upon detection of polarity reversal signal. FXS: generate the signal |  |
| 679 | `ENABLERFC4117TRANSCODING` | Enable transcoding call  RFC4117 |  |
| 680 | `ENABLERPIHEADER` | Enable Remote-Party-ID header |  |
| 681 | `ENABLERPORT` | Enables Rport option in VIA header |  |
| 682 | `ENABLERTCPATTRIBUTE` | Enable RCTP attribute in the SDP |  |
| 683 | `ENABLERTCPSTATISTICSFORCDR` | Enable RTCP statistics for CDR |  |
| 684 | `ENABLERTPREDUNDANCYNEGOTIATION` | Enable RTP Redundancy negotiation |  |
| 685 | `ENABLESAS` | Enables SAS functionality |  |
| 686 | `ENABLESBC` | Enables SBC functionality |  |
| 687 | `ENABLESBCMEDIASYNC` | Enables SBC media sync process. It is possible that a call will be established with the media not synced between the ... | Avoid/0,Enable/1,Never/2 |
| 688 | `ENABLESEMIATTENDEDTRANSFER` | Semi-Attended Transfer when the session to the Target is not established |  |
| 689 | `ENABLESILENCEDISCONNECT` | Disconnect calls on a configured silence timeout |  |
| 690 | `ENABLESILENCESUPPINSDP` | SilenceSupp in SDP used for fax VBD |  |
| 691 | `ENABLESINGLEDSPTRANSCODING` | Enable/Disable using single DSP for g711 <--> LBR coder |  |
| 692 | `ENABLESIPREMOTERESET` | Enables resetting the GW by receiving Notify request with 'Check-Sync' event type. |  |
| 693 | `ENABLESIPS` | Enable SIP secured URI usage |  |
| 694 | `ENABLESRVQUERY` | Enable DNS SRV queries for |  |
| 695 | `ENABLESTUN` | Enables the STUN module, used for NAT traversal of UDP packets. |  |
| 696 | `ENABLESYMMETRICMKI` | Enable symmetric MKI negotiation | 0/0,1/1 |
| 697 | `ENABLETCPCONNECTIONREUSE` | Enable reuse of TCP connection |  |
| 698 | `ENABLETDMOVERIP` | Enable gateway to maintain a permanent RTP connection |  |
| 699 | `ENABLETLSHW` | Used to enable hardware acceleration for TLS (SIPS/HTTPS...). Note: enabling this parameter may result in channel cap... |  |
| 700 | `ENABLETRANSFER` | Enable Call Transfer service |  |
| 701 | `ENABLETRANSFERCAP` | Select Transfer Capabilities method between H.323/Q.931 and ISDN/Q.931 |  |
| 702 | `ENABLEUSERINFOUSAGE` | 0 = Disable, use existing mechanism 1 = Enable usage of the data in the User Information file |  |
| 703 | `ENABLEUUIIP2TEL` | Enable User-User IE to pass in Setup from IP to ISDN |  |
| 704 | `ENABLEUUITEL2IP` | Enable User-User IE to pass in Setup from ISDN to IP |  |
| 705 | `ENABLEVMURI` | Enable VoiceMail URI |  |
| 706 | `ENABLEVOICEDETECTION` | On FXO GWs enables sending of connect/200 OK message on speech/fax/modem detection [default 0]. In order to activate ... |  |
| 707 | `ENCRYPTED` | TLS ERROR: Cannot read encrypted private key. The passphrase is incorrect. |  |
| 708 | `ENDPOINTCALLPRIORITY` | Set Ports call priority |  |
| 709 | `ENERGYDETECTORCLOSINGDELAY` | Energy detector closing delay in 30 ms units. |  |
| 710 | `ENTER` | CPU overload status not updated for %d msec, OVERLOAD! |  |
| 711 | `ENTRIES` | Invalid Voice Prompt Index!! |  |
| 712 | `ENUMSERVICE` | Specifies ENUM domain using for ENUM resolution. Default is e164.arpa |  |
| 713 | `EN_PING_LOST` | Start ping lost simulation |  |
| 714 | `EN_RESET` | Enable network watchdog reset in failure |  |
| 715 | `EN_TRACE` | Enabling network watchdog trace |  |
| 716 | `EP_BIT_Field_Size` | Defines the bit field size for each name level (for BINARY MEGACO). |  |
| 717 | `EP_Max` | Maximal number for each name level (level 0 is the left one, i.e Trunk number) |  |
| 718 | `EP_Min` | Minimal number for each name level (level 0 is the left one, i.e Trunk number) |  |
| 719 | `EP_Num` | Defines the starting number for each name level. |  |
| 720 | `ERROR` | Telenet command %s is not active now |  |
| 721 | `ETHERDISCOVERMODE` | Controls EtherDiscover mode of operation. | Always Disable /0,Unconfigured Device Only /1,Always Enable /2 |
| 722 | `ETSICallerIDTypeOneSubStandard` | Selects the number denoting the ETSI CallerID Type 1 sub-standard. | ETSI_Between_Rings/0,ETSI_Before_Ring_DT_AS/1,ETSI_Before_Ring_RP_AS/2,ETSI_Before_Ring_LR_DT_AS/... |
| 723 | `ETSIVMWITypeOneStandard` | Selects the number denoting the ETSI VMWI Type 1 Standard. | ETSI_VMWI_Between_Rings/0,ETSI_VMWI_Before_Ring_DT_AS/1,ETSI_VMWI_Before_Ring_RP_AS/2,ETSI_VMWI_B... |
| 724 | `ETSI_CALLERID_TIME_BEFORE_CID_WITHOUT_RING` | The time before a Caller ID signal (FSK) in the ETSI Caller ID before a ring / not associated with the ring. |  |
| 725 | `ETSI_CALLERID_TIME_BETWEEN_CID_TO_RING` | The time between the Caller ID signal (FSK) and the ring that follows it, in the ETSI Caller ID type. |  |
| 726 | `ETSI_CALLERID_TIME_BETWEEN_LINE_RVRESAL_TO_CID` | The time between a line reversal and a Caller ID signal (FSK) in the ETSI Caller ID before the ring / not associated ... |  |
| 727 | `ETSI_CALLERID_TIME_BETWEEN_RING_PULSE_TO_CID` | The time between the ring pulse and the Caller ID signal (FSK) in the ETSI Caller ID before the ring / not associated... |  |
| 728 | `ETSI_CALLERID_TIME_BETWEEN_RING_TO_CID` | The time between a ring and the Caller ID signal (FSK) in the ETSI Caller ID, during ringing. |  |
| 729 | `ETSI_CALLERID_TIME_DATA_TRANSMISSION_DURATION` | Data transmission duration (FSK signal) in the ETSI Caller ID type. |  |
| 730 | `ETSI_CALLERID_TIME_OF_RING_PULSE` | The time of the ring pulse in the ETSI Caller ID before the ring / not associated with the ring. |  |
| 731 | `ETSI_DTMF_CID_TIME_BETWEEN_CID_2_NORMAL_LINE_REV` | The time between a Caller ID signal (DTMF based) and line reversal back to normal, in the ETSI Caller ID type. |  |
| 732 | `ETSI_DTMF_CID_TIME_BETWEEN_LINE_REV_2_CID` | The time between a line reversal and a Caller ID signal (DTMF based) in the ETSI Caller ID type. |  |
| 733 | `ETSI_DTMF_CID_TIME_BETWEEN_NORMAL_LINE_REV_2_RING` | The time between line reversal back to normal and the start of the ring, in the ETSI Caller ID type. |  |
| 734 | `EVENT` | Erorr: event is not valid (range: 1 to %d) |  |
| 735 | `EVRCDTXMax` | EVRC VAD maximum Gap between two Silence frames. |  |
| 736 | `EVRCDTXMin` | EVRC VAD minimum Gap between two Silence frames. |  |
| 737 | `EVRCPAYLOADTYPE` | Transparent payload type |  |
| 738 | `EVRCRate` | Configures the EVRC coder bit rate. | variable/0,1-kbps/1,4-kbps/2,8-kbps/3 |
| 739 | `EXTLineMngr` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 740 | `EarlyMedia` | SIPStackSession#%d::HandleResolutionFailEV - ResolveDNS: failed to resolve %s , disconnecting call |  |
| 741 | `EchoCancelerReconvergenceEnable` | Defines if enable the Echo Canceller Reconvergence feature or not. |  |
| 742 | `EchoCancellerAggressiveNLP` | Enables Aggressive Echo Canceller NLP at first 0.5 second of the call. |  |
| 743 | `EchoCancellerAutomaticToneResetMode` | Whether to enable the Automatic Echo Canceller reset after tone detection from IP network. |  |
| 744 | `EchoCancellerDebugger` | Echo Canceller Debugger control |  |
| 745 | `EchoCancellerHPFE` | Enables the Echo Canceller HPF. |  |
| 746 | `EchoCancellerLength` | Length of Echo Canceller Tail to be used. According acTECLength enum. | CE_EC_LENGTH_DEFAULT/0,CE_EC_LENGTH_15MSEC/1,CE_EC_LENGTH_20MSEC/2,CE_EC_LENGTH_25MSEC/3,CE_EC_LE... |
| 747 | `EmergencyNumbers` | Emergency numbers |  |
| 748 | `Empty` | Length = %d Run = %d Type = %d Ptr = 0x%08x IpAdd = 0x%08x DPort = %d SPort = %d |  |
| 749 | `EmptyUser` | AcSIPParser: Unrecognized Header '%s' was detected at line: %d |  |
| 750 | `EnMCountryCoefficients` | EnM Country Coefficients | usa/0,europe/1 |
| 751 | `EnMCountryCoefficientsFromIni` | Load EnM Country Coefficients From Ini |  |
| 752 | `EnMOffHookGlareEnable` | Protect the EnM port from Rx and Tx hook collision |  |
| 753 | `EnMPortRXGain` | Rx Gain |  |
| 754 | `EnMPortTXGain` | Tx Gain |  |
| 755 | `EnMSignalingType` | Set E&M standatd signaling types are described in TIA/EIA-464C |  |
| 756 | `EnMSystemType` | E&M Signaling Type - Trunking or Signaling | Signaling/0,Trunking/1 |
| 757 | `EnMVoiceType` | E&M Voice Configuration Type 2 or 4 wire | TwoWire/0,FourWire/1 |
| 758 | `EnMhookDebounceTiming` | Sets the on E&M hook detection debounce timing. |  |
| 759 | `Enable` | Ericsson SMDI |  |
| 760 | `EnableADLowEnergyDetection` | Defines if enable Low Energy Answer Detection or not. |  |
| 761 | `EnableAGC` | Activates the AGC (Automatic Gain Control). |  |
| 762 | `EnableARPTableSmartOption` | Controls the SMART option used by the IP stack to manage the ARP cache. |  |
| 763 | `EnableARPaging` | 1=Enable Aging of ARP table entries. |  |
| 764 | `EnableAllChassisTraps` | Enables-disables the traps from all types of chassis. |  |
| 765 | `EnableAnalogDCRemover` | Determines whether to enable the analog DC remover in the DAA. |  |
| 766 | `EnableAnswerDetector` | Enables the AD (Answer Detector). |  |
| 767 | `EnableBitTask` | Enables the bit task. |  |
| 768 | `EnableCASAlternatingBitDetector` | CAS Alternating Bit Detector Control (1=Enable,0=Disbale) |  |
| 769 | `EnableCallerIDTypeTwo` | Enables or disables Caller ID Type 2. |  |
| 770 | `EnableCellularWan` | Enable/disable cellular modem WAN access |  |
| 771 | `EnableConferenceDTMFClamp` | EnableConferenceDTMFClamp - if enable remove detected DTMF digits from the audio stream on simple conference particip... |  |
| 772 | `EnableConferenceDTMFReporting` | EnableConferenceDTMFReporting- if enable report in out of band  format about  detected DTMF digits (values 1-Report,0... |  |
| 773 | `EnableContinuityTones` | Enables COT (Continuity Tones) detection and generation. |  |
| 774 | `EnableCoreDump` | This parameter enables a core dump in the case of an exception. It is used for debugging purposes only. |  |
| 775 | `EnableDHCPLeaseRenewal` | Enables/disables DHCP renewal support. |  |
| 776 | `EnableDNSasOAM` | Sets the location of the DNS. | Disable/0,Enable/1 |
| 777 | `EnableDSPAGC` | Enables DSP AGC. |  |
| 778 | `EnableDSPIPMDetectors` | Enables DSP IP Media Detectors. | #if /TP_IPM260 // TP_IPM260_RT //  TP_IPM260_UN_RT //  TP_IPM1610 // TP_IPM1610_400 $ 1 $#else$ 0... |
| 779 | `EnableDetectRemoteMACChange` | Allows for the detection of an incoming RTP stream from a changed remote MAC address. |  |
| 780 | `EnableDiagnostics` | Checks the correct functionality of different board hardware components. | acDiagnostics_Disabled/0,acDiagnostics_BuiltInTest/1,acDiagnostics_BuiltInTestwithPartialFlash/2,... |
| 781 | `EnableDspDDRTest` | 0 - disable, 1- enable internal DDR test, 2 - enable internal DDR test + HPI Access timing test |  |
| 782 | `EnableDspInternalWD` | Enable the DSP Internal Watchdog detection. |  |
| 783 | `EnableEVRCVAD` | Enables the EVRC Voice Activity detector. |  |
| 784 | `EnableEchoCanceller` | Enables the Echo Canceller. |  |
| 785 | `EnableEnergyDetector` | Activates the Energy Detector. |  |
| 786 | `EnableErrorThrottling` | Enable the error throttling mechanism |  |
| 787 | `EnableFXOCurrentLimit` | Allows the user to enable loop current limit to a maximum of 60mA (TBR21)or to disable the FXO line current limit. | enable/1,disable/0 |
| 788 | `EnableFaxModemInbandNetworkDetection` | Enables or disables inband network detection related to fax/modem. |  |
| 789 | `EnableFxsDynamicBatterySwitch` | Enables FXS battery switch for long and short line dynamicly |  |
| 790 | `EnableG729BackwardCompatibleSIDTransmission` | 0 = Transmit the SID frame separated from Voice frame; 1 = SID frame may be concatenated to a Voice frame |  |
| 791 | `EnableH24871` | Enables H.248.71 statistics. |  |
| 792 | `EnableHDConference` | Enable/Disable  HD Conference. |  |
| 793 | `EnableHighPassFilter` | Enables 360 Hz high pass filter. |  |
| 794 | `EnableICMPUnreachableReport` | Enables ICMP Destination Unreachable Report mechanism. |  |
| 795 | `EnableIDS` | Enables the Intrusion Detection System (IDS) |  |
| 796 | `EnableIPAddrTranslation` | 0=Disable NAT on IP level.  1=Enable NAT in IP level - RTP, RTCP, T38.  2=Enable NAT in IP level - Aggregation.  3=En... |  |
| 797 | `EnableIPMediaChannels` | Enable DSP channels reservation for IP media application. |  |
| 798 | `EnableLANWatchdog` | Detects LAN failures on the board. |  |
| 799 | `EnableLLDP` | Enable LLDP. |  |
| 800 | `EnableMOH` | FXS: enable playing Music On Hold |  |
| 801 | `EnableMRDCAS` | Enable/Disable MRD CAS behavior |  |
| 802 | `EnableMediaUDPChecksum` | Determines whether to enable the UDP checksum calculation for RTP media TX over IPv4. |  |
| 803 | `EnableMgmtTwoFactorAuthentication` | Enables the managment two factor authentication. Requires secure connection. |  |
| 804 | `EnableMultipleIPs` | Enables the multiple IPs feature. |  |
| 805 | `EnableNTPasOAM` | Sets NTP on the OAM network |  |
| 806 | `EnableNoiseReductionSupport` | Enables or disables Noise Reduction. |  |
| 807 | `EnableNonInvite408Reply` | Enable sending 408 responses for non-INVITE transactions. Disable this parameter to comply to RFC 4320. |  |
| 808 | `EnableOnHookActiveMode` | Enables the Duslic active mode in onhook state |  |
| 809 | `EnablePPPoE` | This parameter is used to enable the PPPoE feature. |  |
| 810 | `EnablePatternDetector` | Enables or disables activation of the PD (Pattern Detector). |  |
| 811 | `EnablePiggyBacking` | This parameter configures the option to send piggy backed commands while RSIPS are sent. |  |
| 812 | `EnablePostFilter` | Enables the post filter |  |
| 813 | `EnableProxyKeepAlive` | Enable Proxy Keep Alive | Disable /0,Using OPTIONS /1,Using REGISTER /2 |
| 814 | `EnablePulseDialDetection` | Enables Pulse Dial detection |  |
| 815 | `EnablePulseDialGeneration` | Enables Pulse Dial generation |  |
| 816 | `EnableRADIUS` | Enable/disable the RADIUS App. |  |
| 817 | `EnableSCTPasControl` | Sets the location of the Stream Control Transmission Protocol (SCTP). |  |
| 818 | `EnableSDPVersionNegotiation` | Handle SDP offer/answer if SDP version was increased, otherwise takes SDP offer/answer parameters from last agreement... |  |
| 819 | `EnableSTUModemDetection` | Enables or disables detection of two tones required for an STU modem. |  |
| 820 | `EnableSecSyslog` | Enables the Security Syslog message  (of the firewall and login). |  |
| 821 | `EnableSecureStartup` | Whether to enable secure startup mode. |  |
| 822 | `EnableSidWithNonePayloadType13` | For coders that don't support the SID in their main standard (such as G.711), it defines if we handle RTP packets wit... |  |
| 823 | `EnableSilenceCompression` | Determines the Silence Suppression Mode. | Disable/0,Enable/1,Enable Without Adaptation/2 |
| 824 | `EnableSnmpAlternateWanIfAccess` | Enables-disables SNMP access from alternate voip interface |  |
| 825 | `EnableSnmpTraps2TpNcpEvents` | Enables the module that converts traps into TpNcp events. |  |
| 826 | `EnableStandardSIDPayloadType` | Determines whether Silence Indicator (SID) packets that are sent and received are according to RFC 3389. |  |
| 827 | `EnableSurvivability` | Enable Survivability | Disable /0,Enable if Necessary /1,Always Enable /2,Always Terminate Register /3 |
| 828 | `EnableSyslog` | Enables the Syslog message system | disable/0,enable/1 |
| 829 | `EnableTPNCPSecurity` | Secures TPNCP by accepting only pre-determined servers via AuthorizedTPNCPServers parameter.{@} |  |
| 830 | `EnableTPNCPasOAM` | Sets the TPNCP location on the OAM network, when operating in multiple IPs mode.{@} |  |
| 831 | `EnableTrunkTestingTones` | Enables/Disables trunk testing tones. |  |
| 832 | `EnableUDPPortTranslation` | Specifies the type of compare operation performed on the UDP ports. |  |
| 833 | `EnableV150ModemRelaySupport` | Determines whether to enable V.150.1 modem relay support. |  |
| 834 | `EnableVLANSandMIwithTFTP` | Enables advanced networking features, such as IP separation and VLANs, after TFTP download. |  |
| 835 | `EnableVXML` | Enables/disables the VXML stack. | Disable/0,Enable/1 |
| 836 | `EnableVoicePathBITTest` | Enables the voice path bit test. |  |
| 837 | `EnableVoiceStreaming` | Enables/disables the Voice Streaming application. |  |
| 838 | `Enabled` | Failed disabling PPPoE. |  |
| 839 | `EndTime1` | End Time 1 |  |
| 840 | `EndTime2` | End Time 2 |  |
| 841 | `EndTime3` | End Time 3 |  |
| 842 | `EndTime4` | End Time 4 |  |
| 843 | `EndpointName` | Gateway's end point name. |  |
| 844 | `EndpointPREFIX` | Together with 'TrunkName' field, generates local endpoint name on trunk enabled gateways. |  |
| 845 | `EnergyDetectorQualityFactor` | Determines the Energy Detector's sensitivity. |  |
| 846 | `EnergyDetectorRedirection` | Redirect the Energy Detector towards the network instead of TDM. |  |
| 847 | `EnergyDetectorThreshold` | Defines the ED's (Energy Detector's) threshold according to the formula: -44 + (EDThreshold * 6) [- dBm]. |  |
| 848 | `EnterCpuOverloadPercent` | Defines the CPU Utilization percent that enters CPU Overload condition. |  |
| 849 | `Entrust` | Entrust Version Extension |  |
| 850 | `ErrorMsgInterval` | The Interval of the Voice Engine error counters report in [msec] |  |
| 851 | `ErrorReportInterval` | The JB and SRTP error reporting interval [10ms] |  |
| 852 | `ErrorThrottlingTimeThreshold` | The time interval threshold of the error throttling mechanism |  |
| 853 | `EthernetCleanUpTx` | Start=0x%x  Recv=0x%x  Refill=0x%x  Isr=0x%x  UserBuf=0x%x  UserRef=0x%x |  |
| 854 | `EthernetPhyConfiguration` | Controls the Ethernet connection mode type. |  |
| 855 | `EtsiCallerIdShortMarkSignal` | Enables use Etsi Caller ID with short Mark Signal. |  |
| 856 | `ExitCpuOverloadPercent` | Defines the CPU Utilization percent that exits CPU Overload condition. |  |
| 857 | `ExpandableArrayItem` | SIPOrigHeaderTemplate: Resource %s Header deleted - #%d |  |
| 858 | `ExtBootPReqEnable` | Enables extended information to be sent in the BootP reqeuest. |  |
| 859 | `FACILITYTRACE` | Enable ISDN Facility Trace |  |
| 860 | `FACILITY_ADMIN_WAIT_FOR_IP_STATE` | Endpoint UnKnown State: %d |  |
| 861 | `FAIL` | RoutingInstance (#%d) UseProxyForFwdXfer: No route to ProxyIpGroupId %d |  |
| 862 | `FAKERETRYAFTER` | 0 - disabled. Any positive value - when the GW receives 503 without Retry-After response-header, it will behave as th... |  |
| 863 | `FAKETCPALIAS` | VI 101470 - force to reuse TCP/TLS connection (even if the VIA doesn't include the alias parameter) |  |
| 864 | `FALSE` | Dns query was sent, get the address later using the Database API. |  |
| 865 | `FARENDDISCONNECTTYPE` | Silence Detection activated |  |
| 866 | `FAXCNGMODE` | 0-Does not send a SIP re-INVITE, 1-Sends T.38 re-INVITE upon detection of fax CNG tone, 2-Sends T.38 re-INVITE upon d... | Doesn't send T.38 re-INVITE/0,Sends on CNG tone /1,Sends on CNG or v8-cn /2 |
| 867 | `FAXDETECTTIMEOUTSINCECONNECT` | Defines period of time (in msec) after connect for fax detection. The fax event, detected after that interval expired... |  |
| 868 | `FAXREROUTINGDELAY` | Defines the time interval (in sec) to wait for CNG detection in order to re-route call to fax destinations |  |
| 869 | `FAXREROUTINGMODE` | Enables the detection of the fax CNG tone  in incoming calls, before sending  the INVITE | Disable /0,Rerouting without delay /1,Progress and delay /2,Connect and delay /3 |
| 870 | `FILTERCALLS2IP` | When Gatekeeper/Proxy is enabled, do not start session if called number is not listed or restricted in Tel to IP rout... | Don't Filter /0,Filter /1 |
| 871 | `FIRSTTXDTMFOPTION` | Not Supported |  |
| 872 | `FMTP` | Illegal PayloadNum value |  |
| 873 | `FORCE` | Warning: maximum of %d requests reached |  |
| 874 | `FORCERUNALL` | InitialShellCommandString does not support more than %d commands |  |
| 875 | `FORKINGDELAYTIMEFORINVITE` | Delay time (in seconds) to wait before sending Invite of 2nd forking call. |  |
| 876 | `FORKINGHANDLINGMODE` | Decides the handling method to 18X response to forking | Parallel handling /0,Sequential handling /1 |
| 877 | `FORKINGTIMEOUT` | Defines how much time to wait for 2xx responses after the first 2xx has been received. |  |
| 878 | `FORMAT` | Table %s Generation to INI: Table NOT generated. failed to get first line index attributes. |  |
| 879 | `FORMATDESTPHONENUMBER` | Format Dest Phone Number | Trasparent /0,Remove Params /1 |
| 880 | `FREE` | ERR: ED isn't stopped !!! |  |
| 881 | `FULL` | Full Option is %s |  |
| 882 | `FULLCONFIG` | PCI Set Bootp And Reset Board failed (Error = %d) |  |
| 883 | `FXOAutoDialPlayBusyTone` | Only for FXO, Tel2IP calls: If enable (1) - On receiving release, if autodial is used, the FXO seize the line and pla... |  |
| 884 | `FXOBETWEENRINGTIME` | Timeout for releasing FXO to IP call, if FXO port doesn't detect ringing signal for this timeout |  |
| 885 | `FXOCoeffFileUrl` | Provides a link to an FXO coefficients file, to be downloaded from a remote server. |  |
| 886 | `FXODCTermination` | Allows the user to set the FXO line DC termination (0 - 50 Ohm, 1 - 800 Ohm) only effect the On-Hook to Off-Hook tran... | off/0,on/1 |
| 887 | `FXOLoopCharacteristicsFilename` | Defines the FXO loop coefficient filename. |  |
| 888 | `FXONumberOfRings` | Number of rings that the FXO wait before initiating call |  |
| 889 | `FXORINGTIMEOUT` | Defines the delay (in 100 msec) for generating INVITE after RING_START detection. The valid range is 0 to 50 |  |
| 890 | `FXORxGainControl` | Sets gain |  |
| 891 | `FXOSEIZELINE` | If not set, the FXO will not seize the line |  |
| 892 | `FXOTxGainControl` | Sets gain |  |
| 893 | `FXOWAITFORDIALTIME` | Obsolete. Use WaitForDialTime instead.;Time delay between seizing the line and start dialing. only if ISWAITFORDIALTO... |  |
| 894 | `FXSCoeffFileUrl` | Provides a link to an FXS coefficients file, to be downloaded from a remote server. |  |
| 895 | `FXSLoopCharacteristicsFilename` | Defines the FXS loop coefficient filename. |  |
| 896 | `FXSOOSBEHAVIOR` | 0:none 1:reorder tone 2:reverse polarity 3:reorder tone+reversal polarity | None/0,! Reorder Tone/1,! Polarity Reversal/2,! Reorder Tone + Polarity Reversal/3,! Current Disc... |
| 897 | `FXSRxGainControl` | Sets gain |  |
| 898 | `FXSTxGainControl` | Sets gain |  |
| 899 | `Fail` | QoS Disable |  |
| 900 | `Failed` | GET Column %d - Web Display Unknown. |  |
| 901 | `FarEndDisconnectSilenceMethod` | Defines the FarDisconnect silence detection method. |  |
| 902 | `FarEndDisconnectSilencePeriod` | Defines the Silence period to be detected. |  |
| 903 | `FarEndDisconnectSilenceThreshold` | Defines the threshold (in percentages) of the packets to be considered as Silence. |  |
| 904 | `FarEndDisconnectType` | Sets the source for the acEV_FAR_END_DISCONNECTED event. |  |
| 905 | `FaultCode` | Fault Code is %d |  |
| 906 | `FaxBypassOutputGain` | Defines the fax bypass output gain [dB]. |  |
| 907 | `FaxBypassPayloadType` | Fax Bypass (VBD) Mode payload type. |  |
| 908 | `FaxModemBypasDJBufMinDelay` | Determines the Jitter Buffer constant delay during a Fax & Modem Bypass session [msec]. |  |
| 909 | `FaxModemBypassBasicRTPPacketInterval` | Sets the basic Fax/Modem bypass RTP packet packing time. | default/0,5msec/1,10msec/2,20msec/3 |
| 910 | `FaxModemBypassCoderType` | Sets the Fax/Modem bypass coder. | G711Alaw_64/0,G711Mulaw/1 |
| 911 | `FaxModemBypassM` | Defines the number of 20 msec payloads to be generated in a single RTP fax/modem bypass packet. |  |
| 912 | `FaxModemNTEMode` | Defines the modes for handling Fax Modem Telephony Events. | disable/0,ANS-tones-over-telephony-events/1 |
| 913 | `FaxModemRelayVolume` | Determines the signal output level during T.38 Fax Relay session [dBm]. |  |
| 914 | `FaxRelayECMEnable` | Enables ECM (Error Correction Mode) during T.38 Fax Relay. |  |
| 915 | `FaxRelayEnhancedRedundancyDepth` | Determines number of repetitions to be applied to control packets when using T.38 standard. |  |
| 916 | `FaxRelayJitterBufferLength` | The length of the internal |  |
| 917 | `FaxRelayMaxRate` | Limits the maximum transfer rate of the fax during T38 Fax Relay session. | 2400bps/0,4800bps/1,7200bps/2,9600bps/3,12000bps/4,14400bps/5,16800bps/6,19200bps/7,21600bps/8,24... |
| 918 | `FaxRelayRedundancyDepth` | Determines the depth of redundancy for non-V.21 T.38 fax packets. |  |
| 919 | `FaxTransportMode` | Sets the Fax over IP transport method. | Disable/0,T.38 Relay/1,Bypass/2,Events Only/3 |
| 920 | `FaxVbdBehaivior` | Fax Vbd Behavior | Bypass/0,Relay/1 |
| 921 | `FeatureKeyURL` | Provides a link to a Feature Key (FK) file to be downloaded from a remote server. |  |
| 922 | `File` | PM_Status" target="main" class="head4"> |  |
| 923 | `FileSystemStatus` | Display File System Status |  |
| 924 | `FipsLoadTest` | FIPS RSA Test. Usage: FipsLoadTest [server ip] |  |
| 925 | `FirstDspTemplateCommonCodersPercent` | Mixed DSP templates: defines the desirable percent of busy channels in first template (relevant only for common coder... |  |
| 926 | `FirstIpAddress` | First IP Address |  |
| 927 | `Flash` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Flash Configuration' page. |  |
| 928 | `FlashCmpCheck` | Validate the firmware stored in flash |  |
| 929 | `FlashHookPeriod` | Defines the flashhook detection & generation period (in msec). |  |
| 930 | `FlashKeysSequenceStyle` | Flash Keys Sequence Style{@}0: FlashHook{@}1: FlashHook + Digit (1/2/3){@}2: FlashHook + Digit (-/2/4/3){@} | Flash hook /0,Sequence 1 /1,Sequence 2 /2 |
| 931 | `FlashKeysSequenceTimeout` | Flash Keys Sequence Timeout |  |
| 932 | `FlashTime` | Adjust time between on hook and off hook that follows it |  |
| 933 | `ForceExceptionDump` | Forces an exception dump that is sent every time the board restarts. {@}{@} |  |
| 934 | `ForceIKE` | Init IKE to a peer |  |
| 935 | `ForkingController` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 936 | `FourthIpAddress` | Fourth IP Address |  |
| 937 | `FramingMethod` | Selects the physical framing method to be used for this trunk. | acEXTENDED_SUPER_FRAME /'0',acSUPER_FRAME /'1',acE1_FRAMING_DDF /'a',acE1_FRAMING_MFF_CRC4 /'b',a... |
| 938 | `FreeResource` | RegisterForBaseEvent: %s#%d is already registered for key %d, requested by %s#%d |  |
| 939 | `FreezEchoCancellerDuringDtmfDetection` | Define if Echo Canceller should be freez during DTMF detction from TDM side.  0 - Disable  1 - Enable |  |
| 940 | `FtpClient` | FtpClient: Tcp construct child data socket failed |  |
| 941 | `FtpClientData` | FtpClient: Tcp client data socket failure |  |
| 942 | `FutureNAS` | RADIUS-DUMP Active Session ID=%d Ch=%d |  |
| 943 | `Fxs60mACurrentLimit` | Enables 60mA current limitation on FXS port (enabled by default for MP124E). |  |
| 944 | `FxsFaultCurrentDetection` | Enable detection of TipRing short to ground. |  |
| 945 | `G722` | XMLString: Unknown coder type received: %s, setting to default coder: PCMA |  |
| 946 | `G729` | Microsoft-RTA (NB) |  |
| 947 | `G729EVLocalMBS` | Determines the maximum generation bitrate of the G729EV coder for a specific channel. | Undefined /15,8 Kbps /0,12 Kbps/1,14 Kbps/2,16 Kbps /3,18 Kbps /4,20 Kbps /5,22 Kbps /6,24 Kbps /... |
| 948 | `G729EVMaxBitRate` | Determines the maximum generation bitrate for all participants in a session using G729EV coder. | Undefined /15,8 Kbps /0,12 Kbps /1,14 Kbps /2,16 Kbps /3,18 Kbps /4,20 Kbps /5,22 Kbps /6,24 Kbps... |
| 949 | `G729EVReceiveMBS` | Determines the maximum generation bitrate of the G729EV coder to be requested from the other party. | Undefined /15,8 kbps /0,12 kbps /1,14 kbps /2,16 kbps /3,18 kbps /4,20 kbps /5,22 kbps /6,24 kbps... |
| 950 | `GATEWAYVERSION` | H.323/SIP internal version |  |
| 951 | `GENERATEDREGISTERSINTERVAL` | Defines the time unit interval in seconds for generate registers |  |
| 952 | `GENERATESRTPKEYS` | Generate SRTP Keys |  |
| 953 | `GETVPBUFFERINFO` | VP Buffer: Start %x  End %x |  |
| 954 | `GOLDSERVICECLASSDIFFSERV` | Sets the DiffServ for the Gold service class content. |  |
| 955 | `GOST89` | OPENSSL_malloc Error |  |
| 956 | `GRACEFULBUSYOUTTIMEOUT` | Graceful Busy Out Timeout in seconds |  |
| 957 | `GROUPS` | DSP Group Statistics: |  |
| 958 | `GUARDTIMEBETWEENCALLS` | Guard time between calls in the same EP (FXO only) |  |
| 959 | `GWAPP` | Core::Start - RedundantMode: %d, UpgradeType: %d |  |
| 960 | `GWAPPDELAYTIME` | Gateway delay time after reset (seconds) |  |
| 961 | `GWAPPGLOBALDEBUGSELECTOR` | GWAPP global debug selector |  |
| 962 | `GWAPPGLOBALDEBUGVALUE` | GWAPP global debug value |  |
| 963 | `GWDEBUGLEVEL` | Configure different debug level | 0 /0,1 /1,2 /2,3 /3,4 /4,5 /5,6 /6,7 /7 |
| 964 | `GWINBOUNDMANIPULATIONSET` | Inbound manipulation set ID for GW - If configured, applies for all incoming INVITE requests. |  |
| 965 | `GWLOGGERFLAGS` | Configuration::InsertStrVal- GWLoggerFlags have ilegal value |  |
| 966 | `GWOUTBOUNDMANIPULATIONSET` | Outbound manipulation set ID for GW - If configured, applies for all outgoing INVITE requests. |  |
| 967 | `GWREGISTRATIONNAME` | Gateway registration name |  |
| 968 | `GWREGISTRTYPE` | Type of Gatekeeper registration | H.323 ID /1,Both /2,NUMBER CLASS /3,NUMBER CLASS & H.323 ID /4,E.164 /0 |
| 969 | `GWSDPCONNECTIONMODE` | 0 - Do not Care,1- UseConnection OnSession Only,2 - Use Connection On Media Only | Don't care/0,On Session Only/1,On Media Only/2 |
| 970 | `GWUserInfo` | StackEPMngr::GWUserInfoActivation Delete previous entry - PBXExt:%s |  |
| 971 | `GWVXML_tAttributes` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 972 | `GW_STUN_RESPONSE_NOT_MATCHED` | NOT ALLOWED value of GW STUN ERROR !!! |  |
| 973 | `GainSlope` | PCIIFChangeChannelParams(): Enabling Pattern Detector will be ignored due to blocking by feature key or by startup co... |  |
| 974 | `Gateway` | CALL_STATISTICS: %s, Connection deleted by %s, Coder: %s, %s, Call duration: %d seconds, |  |
| 975 | `GatewayMGCPPort` | Forces MG to listen to another UDP port instead of  original 2427 as defined in RFC 2705. |  |
| 976 | `GatewayName` | Defines the gateway's identification name towards the MGCP/MEGACO Call Agent. |  |
| 977 | `GenDetectFaxOnDSPSwitchToFaxRelay` | If set event DETECT_FAX will generated immediate if DSP switch to fax relay, otherwise DETCT_FAX will generated on V2... |  |
| 978 | `GetVeTimersInfo` | EngineId[%d] ResourceType[%d]: Total[%d], Allocated[%d], Free[%d]. Static[%c], Loop-Up[%c] |  |
| 979 | `GetnumofDspchResperGroup` | InitEchoCanceller - Failed |  |
| 980 | `Grey` | QOEAPI_CDR NO sessionId |  |
| 981 | `GroundKeyDetection` | Enables/disables the analog ground key detection. |  |
| 982 | `GsUseRegularRing` | FXO: Ground start use regular ring |  |
| 983 | `GwSendBoardCommand2DebugRecording` | GwSendBoardCommand2DebugRecording- if enable Send Board PCIIF command to debug recording as acdr packet  (values 1-En... |  |
| 984 | `H225DIALPORT` | Port on which the gateway sends H.225 Setup messages. (Usually 1720) |  |
| 985 | `H225LISTENPORT` | Port on which the gateway expects to receive H.225 Setup messages. (Usually 1720) |  |
| 986 | `H245ROUNDTRIPTIME` | Time between H.245 Round Trip Delay messages (seconds) |  |
| 987 | `H264` | Comment line |  |
| 988 | `H323BASEPORT` | Defines range for gateway H.225/H.245 local port messages |  |
| 989 | `H323IDSTRING` | Definition of Gateway H.323-ID source field |  |
| 990 | `H323PROGRESSBEHAVIOR` | Interworking behavior of Progress message (0-Alert, 1-Progress) |  |
| 991 | `HANDLEG711ASVBD` | Handle G711 as G711-VBD |  |
| 992 | `HANDLEREASONHEADER` | Handle Reason Header |  |
| 993 | `HASEM` | Lock Error:%d   Lock nesting:%d |  |
| 994 | `HEAD` | Unknown %d |  |
| 995 | `HELDTIMEOUT` | Maximum time allowed for call to be retreived from IP (seconds) |  |
| 996 | `HELP` | Valid table names are: |  |
| 997 | `HIDDEN` | Option HIDDEN is restricted |  |
| 998 | `HMAC` | OpenSSL HMAC method |  |
| 999 | `HOLD` | The waiting for connections are on hold. |  |
| 1000 | `HOLDFORMAT` | Call Hold format - Zero IP, 'sendonly' SDP attribute or Original IP and 'inactive' attribute | 0.0.0.0 /0,Send Only /1,x.y.z.t /2 |
| 1001 | `HOOKFLASHOPTION` | Detect and send Hook-Flash using the selected method | Not Supported /0,INFO /1,RFC 2833 /4,INFO &#40;Lucent&#41; /5,INFO &#40;NetCentrex&#41; /6,INFO&#... |
| 1002 | `HOTLINETONEDURATION` | Duration of played hotline tone, after the gateway seizes the line in response to ringing |  |
| 1003 | `HOTSWAPRTX` | Number of RTX Before Hot-Swap |  |
| 1004 | `HTTPONLYFLAG` | Cookie's flag HttpOnly for security |  |
| 1005 | `HTTPPort` | Determines the local HTTP port of the device. |  |
| 1006 | `HTTPSCertFileName` | Defines the name of the HTTPS server certificate file to be downloaded via TFTP. |  |
| 1007 | `HTTPSCipherString` | Cipher string for HTTPS (in OpenSSL cipher list format). |  |
| 1008 | `HTTPSOnly` | Allows only HTTPS connections (force security). |  |
| 1009 | `HTTPSPORT` | Determine the local Secure HTTPS port of the device. |  |
| 1010 | `HTTPSPkeyFileName` | Defines the name of a private key file (internal). Set to blank to regenerate the key and certificate. |  |
| 1011 | `HTTPSRequireClientCertificate` | Requires the use of client certificates for HTTPS connection |  |
| 1012 | `HTTPSRootFileName` | Defines the name of the HTTPS trusted root certificate file to be downloaded via TFTP. |  |
| 1013 | `Header` | Head here |  |
| 1014 | `HeartBeatTraceBackEnable` | Enable addting the Traceback info into HeartBeat packets with abnormal NextIntervalTime value. |  |
| 1015 | `HeartbeatDestIP` | Sets the destination IP Address for Heartbeat Packets. |  |
| 1016 | `HeartbeatDestPort` | Sets the destination UDP port to which the heartbeat packets are sent. |  |
| 1017 | `HeartbeatIntervalmsec` | Sets the interval (in MSec) of the HeartBeat Packets. |  |
| 1018 | `HeartbeatSecondaryDestIP` | Sets the secondary destination IP address to which the heartbeat packets are sent. |  |
| 1019 | `HookFlashCode` | If this code received during session, act as if hook flash received from the TEL side |  |
| 1020 | `HookFlashCodeIP` | The string represent HookFlash, when reported to or from IP. Currently used in H.323 only (H245UserOutput, H245Signal... |  |
| 1021 | `HotLineToneDuration` | HotLine Dial-Tone Duration |  |
| 1022 | `HttpClientTimeOut` | The timeout for terminating an http client side session (msec). |  |
| 1023 | `HttpHttpsSynRetrans` | Num send retrans of SYN while create connection of HTTP or HTTPS. |  |
| 1024 | `IBSDetectionRedirection` | Enables IBS (In-Band Signaling) Detection Redirection towards the network instead of TDM. |  |
| 1025 | `ICMPUnreachableReportInterval` | Sets the ICMP Destination Unreachable Report interval. |  |
| 1026 | `IDLEPERIODIC` | Idle Periodic time %d |  |
| 1027 | `IDSAlarmClearPeriod` | Sets the minimum period before IDS alarm is cleared (in seconds). |  |
| 1028 | `IFLinkUpDownTrapEnable` | Enables-disables the linkUp and linkDown traps. |  |
| 1029 | `IGNOREALERTAFTEREARLYMEDIA` | Interwork of Alert from ISDN to SIP |  |
| 1030 | `IGNOREAUTHORIZATIONSTALE` | If set ignore Stale in 401 or 407 response |  |
| 1031 | `IGNOREBRILOSALARM` | Ignore LOS alarms for BRI user side trunk |  |
| 1032 | `IGNOREISDNSUBADDRESS` | Ignore ISDN Subaddress |  |
| 1033 | `IGNOREREMOTESDPMKI` | Ignore MKI if present in the remote SDP |  |
| 1034 | `IKETable` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'IKE Table' page. |  |
| 1035 | `IKEcertificateExtValidate` | Enables or disables certificate extension checking for IKE. |  |
| 1036 | `INDIAN_CALLERID_TIME_BETWEEN_CID_TO_RING` | The time between a Caller ID signal (DTMF based) and the start of the ring, in the Indian Caller ID type. |  |
| 1037 | `INDIAN_CALLERID_TIME_BETWEEN_RING_PULSE_TO_CID` | The time between a ring pulse and a Caller ID signal (DTMF based), in the Indian Caller ID type. |  |
| 1038 | `INDIAN_CALLERID_TIME_OF_RING_PULSE` | The time of a ring pulse, in the Indian Caller ID type. |  |
| 1039 | `INIFileSource` | Internal use. This parameter is to identify the source of the ini file. |  |
| 1040 | `INIFileVersion` | Contains the INI file version number that is reported in the acEV_BOARD_STARTED event. {@} |  |
| 1041 | `INIFreeVal` | Apply New Value |  |
| 1042 | `INILoadMode` | Used to determine if INI file loading was done from auxiliary files page or configuration file page. |  |
| 1043 | `INIParamBu` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'ini Parameters' page. |  |
| 1044 | `INITIALROUTEHEADER` | If initial Route header should be added into Register request |  |
| 1045 | `INTERCEPTIONDIRECTION` | Defines the direction of interception of a BCT listener | Incoming /0,Outgoing /1 |
| 1046 | `INT_IF` | Start int. IF ping lost simulation on both sides |  |
| 1047 | `INVALID` | PSOSBoardInterface::HA_AllocateLocalAddresses failed since cpCMediaRealmMgr encountered an error |  |
| 1048 | `INVITE` | SIPProxyContext#%d::ForwardResponseStatelessly - Failed to allocate new SIPUserBuffer!!! |  |
| 1049 | `IP2CASANIDNISDELIMITERS` | IP to CAS list of ANI and DNIS delimiters |  |
| 1050 | `IP2IPRouting` | Cost Group |  |
| 1051 | `IP2IPTRANSCODINGMODE` | Transcoding mode used by ip2ip application | if-required/0,forced/1 |
| 1052 | `IP2IPTRANSFERMODE` | IP2IP Transfer Mode | Refer Termination/0,Refer Interworking/1 |
| 1053 | `IP2TELTAGGINGDESTDIALPLANINDEX` | IP to Tel Tagging Destination Dial Plan Index |  |
| 1054 | `IP2TelCutThroughCallBehavior` | NO cut through, no paging |  |
| 1055 | `IPALERTTIMEOUT` | Maximal time to wait for connect from IP (seconds) |  |
| 1056 | `IPCONNQOSMAXALLOWEDDELAY` | The maximum delay that will not prevent normal routing (msec) |  |
| 1057 | `IPCONNQOSMAXALLOWEDPL` | The maximum percentage of packet loss that will not prevent normal routing |  |
| 1058 | `IPDiffServ` | Defines the value of the 'DiffServ' field in the IP header for media traffic. |  |
| 1059 | `IPFW_RemoteIP` | IP address of remote IPFW gateway (or self, if public) |  |
| 1060 | `IPFW_RemotePort` | Port of remote IPFW gateway (or starting port, if public) |  |
| 1061 | `IPGroupID` | Invalid FORMAT token: %s in |  |
| 1062 | `IPNetworking` | Debug DHCP States: START, LIST, SET <statenum>, STOP, PrintState <0 or 1> |  |
| 1063 | `IPPrecedence` | Sets value of IP precedence field in IP header for packets generated from the channel. |  |
| 1064 | `IPProCoderGroup` | Default Coder Group |  |
| 1065 | `IPProIsFaxUsed` | No Fax |  |
| 1066 | `IPProVxxTransportType` | Enable Bypass |  |
| 1067 | `IPProfileEnableSymmetricMKI` | Not Configured |  |
| 1068 | `IPProfileProgressIndicator2IP` | No PI |  |
| 1069 | `IPProfileSBCRemoteReinviteSupport` | Supported only with SDP |  |
| 1070 | `IPProfileSBCRemoteUpdateSupport` | Supported Only After Connect |  |
| 1071 | `IPSECDPDMODE` | IPsec Dead Peer Detection (RFC 3706) - Mode of Operation. One of the following values: '0' -  Disabled (Default); '1'... | Disabled/0,Periodic/1,On Demand/2 |
| 1072 | `IPSecTable` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'IPSec Table' page. |  |
| 1073 | `IPTOS` | Sets value of IP TOS field in IP header for all packets to be generated from the channel. |  |
| 1074 | `IPsec` | Audio Staging |  |
| 1075 | `IPv6` | SIPSDPSession::CheckMediaMatch - match is found for several media with different IP versions. This is not supported yet |  |
| 1076 | `IS931MSGUSED` | 0 (default): out of band digit is dent by H.245 1:by q931MessageInfo |  |
| 1077 | `ISCISCOSCEMODE` | In use with G.729 - if enabled and SCE=2 then AnnexB=no |  |
| 1078 | `ISDNDISCONNECTONBUSYTONE` | 1 - Release call if gateway receives busy or fast busy tone. 0 - don't release |  |
| 1079 | `ISDNGeneralCCBehavior` | Sets the ISDN Call Control Layer (Layer 4) behavior options. |  |
| 1080 | `ISDNIBehavior` | Sets the ISDN Network Layer (Layer 3) behavior options. |  |
| 1081 | `ISDNInCallsBehavior` | Sets the ISDN incoming calls behavior options. |  |
| 1082 | `ISDNNFASInterfaceID` | Sets the ISDN NFAS Interface ID. Applicable only if the NS_EXPLICIT_INTERFACE_ID behavior bit is set. | ac0DB/0,ac7_5DB/1,ac15DB/2,ac22_5DB/3 |
| 1083 | `ISDNNSBehaviour2` | Sets additional ISDN Network Layer (Layer 3) behavior options. |  |
| 1084 | `ISDNOutCallsBehavior` | Sets the ISDN outgoing calls behavior options. |  |
| 1085 | `ISDNRXOVERLAP` | Select reception type of overlap dialing from ISDN side | None/0,Local Receiving/1,Through SIP/2 |
| 1086 | `ISDNSUBADDRESSFORMAT` | ISDN SubAdress format | ASCII /0,BCD /1,User Specified /2 |
| 1087 | `ISDNTRANSFERCAPABILITY` | Send transfer capability to ISDN side on setup message  -1:Do not Overwrite 0:Audio 3.1 1:Speech 2:Data 3:Audio | Not Configured /-1,Audio 3.1 /0,Speech /1,Data /2,Audio 7 /3{@} |
| 1088 | `ISDNTRANSFERCOMPLETECAUSE` | If such a cause received in ISDN DISCONNECT message of the first leg  NOTIFY 200 is sent toward IP |  |
| 1089 | `ISDNTRANSFERCOMPLETETIMEOUT` | Max time (in seconds) to wait for transfer response from PSTN |  |
| 1090 | `ISDNTXOVERLAP` | Enable ISDN Overlap IP to Tel Dialing |  |
| 1091 | `ISDTMFUSED` | Send DTMFs on the Signaling path (not on the Media path) |  |
| 1092 | `ISFALLBACKUSED` | Allow fallback to internal Tel to IP routing table if Proxy is not responding |  |
| 1093 | `ISFAXUSED` | Use H.323/Annex D procedure for real time FAX relay. To use this feature, disable inband DTMF by setting the FaxTrans... | No Fax /0,T.38 Relay /1,G.711 Transport /2,Fax Fallback /3 |
| 1094 | `ISFSMEDIAINFOSENDONCONNECT` | Is Fast start Media sent in in Connect or in Alert |  |
| 1095 | `ISFSOPENMEDIAONCONNECT` | Open voice channel afer sending Connect or after sending Alert |  |
| 1096 | `ISHOOKFLASHUSED` | Detect and send Hook-Flash as Out-of-Band message |  |
| 1097 | `ISINFOUSED4DTMF` | Use INFO for Out-Of-Band DTMFs |  |
| 1098 | `ISO8859CHARACTERSET` | ISO 8859 Character Set Part | No Accented /0,Western European /1,Central European /2,South European /3,North European /4,Cyrill... |
| 1099 | `ISOVERLAPUSED` | Is overlap mode is used. refer to manual for gateway overlap behavior |  |
| 1100 | `ISPARALLELUSED` | Enable/Disable H323 Parallel Support (0-Disable/1-Enable) |  |
| 1101 | `ISPRACKREQUIRED` | Enable PRACK mechanism for 1xx reliable responses |  |
| 1102 | `ISPROXYHOTSWAP` | Enable Proxy Hot-Swap mode |  |
| 1103 | `ISPROXYUSED` | Is SIP Proxy used | Don't Use Proxy /0,Use Proxy /1 |
| 1104 | `ISREGISTERNEEDED` | Is Proxy registration necessary |  |
| 1105 | `ISSETUPACKUSED` | Enable SetupAck messages for overlap mode |  |
| 1106 | `ISSETUPINCLUDENUM` | Setup message contains called party number |  |
| 1107 | `ISSPECIALDIGITS` | When disabled, pressing special digits (* or #) will terminate digit collection. When enabled, special digits can be ... |  |
| 1108 | `ISTERMINAL` | The gateway registers as a H.323 terminal with multiple aliases. Otherwise, the gateway behaves as an H.323 gateway |  |
| 1109 | `ISTRUSTEDPROXY` | Determine whether the proxy is a trusted node |  |
| 1110 | `ISTWOSTAGEDIAL` | Dialing Mode - One-Stage (PBX Pass-thru) or Two-Stage | One Stage /0,Two Stages /1 |
| 1111 | `ISUBNUMBEROFDIGITS` | Number of digits that will be taken from end of phone number as Subaddress |  |
| 1112 | `ISUSEFREECHANNEL` | Selects the next available (free) Gateway port, FXO/PSTN: affects outgoing calls chanel selection FXS:affects incomin... |  |
| 1113 | `ISUSERPHONE` | Add User=Phone parameter to SIP URL |  |
| 1114 | `ISUSERPHONEINFROM` | Add 'User=Phone' to From header |  |
| 1115 | `ISUSETOHEADERASCALLEDNUMBER` | Use the user part of To header URL as called number (IP->TEL) |  |
| 1116 | `ISWAITFORDIALTONE` | Wait for dial tone before initiating an outgoing call to PBX/PSTN (FXO one-stage dialing mode) |  |
| 1117 | `Idle` | SIPCallIdleState::HandleInvite - Failed to allocate SIPMessage!!! |  |
| 1118 | `IdlePCMPattern` | Defines the PCM pattern applied to the E1/T1 timeslot (B-channel) when the channel is closed and during silence perio... |  |
| 1119 | `InValidCoder` | TR104_Coder_data::UpdateLineCodersData CoderGroupID = %d CoderName =%s, CoderRate=%d, PriorityInCG = %d |  |
| 1120 | `Inactive` | Number debug recording tapped connections: %d |  |
| 1121 | `InboundManSet` | Inbound Message Manipulation Set |  |
| 1122 | `InboundMediaLatchMode` | Determines the way of handling incoming  media packets from non-expected address/port. | strict/0,dynamic/1,dynamic-strict/2,strict-on-first/3 |
| 1123 | `Incoming` | MediaBufferOverrun Wr=%d, Rd=%d, Overrun=%d, LanRcv=%d, CPEn=%d, CIdl=%d |  |
| 1124 | `Index` | Add line failed -wrong index |  |
| 1125 | `InformResponse` | Inform failure. Got %s as response |  |
| 1126 | `IniFileLastUpdateTime` | This parameter saves the HTTP update time of the ini file (internal). |  |
| 1127 | `IniFileTemplateUrl` | Provides a link to an ini file to be downloaded from a remote server, in addition to IniFileUrl. |  |
| 1128 | `IniFileURL` | Provides a link to an ini file to be downloaded from a remote server. |  |
| 1129 | `InitialShellCommand` | Command Shell command to be executed during initialization. |  |
| 1130 | `Initiated` | Setup Recv |  |
| 1131 | `InputGain` | Defines the TDM input gain [dB]. |  |
| 1132 | `InputGainLocation` | Define if Input gain is function before or after the EC. |  |
| 1133 | `InterfaceTable` | Interface Table is empty (or missing). |  |
| 1134 | `InternalDomain` | Domain Name | UDP /0,TCP /1,TLS /2 |
| 1135 | `IntraSRDMediaAnchoring` | Anchor Media |  |
| 1136 | `Invalid` | RFC 2833 Relay Decoder Mute |  |
| 1137 | `InvalidCoder` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 1138 | `Invited` | SIPCallInvitedState::Alert failed setup transaction is NULL |  |
| 1139 | `Inviting` | SIPCallInvitingState::Handle1XXResponse failed not for setup transaction |  |
| 1140 | `IpAddress` | Proxy Address |  |
| 1141 | `IpGroup` | CHashMap::CHashMap - Allocation Exception |  |
| 1142 | `IsAdditionalManipulation` | Additional Manipulation |  |
| 1143 | `IsEnabled` | Caller ID | Not-configured /255,disable /0,enable /1 |
| 1144 | `IsProxyHotSwap` | Is Proxy Hot Swap |  |
| 1145 | `IsRealmDefined` | PrintThresholds - prints the QOE profile thesholds |  |
| 1146 | `IsdnReleaseCause` | Q.850 Causes |  |
| 1147 | `JBSMode` | 0 - the Dsp reports about over-run/under-run when it occured. 1 - JB status is reported every ErrorReportInterval*10 ms |  |
| 1148 | `Jitter` | Remote Jitter |  |
| 1149 | `JitterBufferMaxDelay` | Defines the maximum delay and length of Jitter Buffer into DSP [msec] |  |
| 1150 | `JustForIdentation` | Fill in the following 3 fields to change the password |  |
| 1151 | `KEEPISDNCALLONDISCONNECTWITHPI` | Enable ignoring of ISDN Disconnect messages with PI 1 or 8 |  |
| 1152 | `KEYBLINDTRANSFER` | Keying sequence for performing blind transfer |  |
| 1153 | `KEYBLINDTRANSFERADDPREFIX` | Add keying sequence for performing blind transfer as transfer number prefix |  |
| 1154 | `KEYCALLPICKUP` | Keying sequence for performing call pickup |  |
| 1155 | `KEYCALLWAITING` | Keying sequence for activating call waiting |  |
| 1156 | `KEYCALLWAITINGDEACT` | Keying sequence for deactivating call waiting |  |
| 1157 | `KEYCFBUSY` | Keying sequence for activating Call Forward on busy |  |
| 1158 | `KEYCFBUSYORNOANSWER` | Keying sequence for activating Call Forward on busy or no answer |  |
| 1159 | `KEYCFDEACT` | Keying sequence for deactivating Call Forward |  |
| 1160 | `KEYCFDONOTDISTURB` | Keying sequence for activating Do Not Disturb |  |
| 1161 | `KEYCFNOANSWER` | Keying sequence for activating Call Forward on no answer |  |
| 1162 | `KEYCFUNCOND` | Keying sequence for activating immediate Call Forward |  |
| 1163 | `KEYCLIR` | Keying sequence for activating restricted Caller ID |  |
| 1164 | `KEYCLIRDEACT` | Keying sequence for deactivating restricted Caller ID |  |
| 1165 | `KEYHOTLINE` | Keying sequence for activating delayed Hot-line |  |
| 1166 | `KEYHOTLINEDEACT` | Keying sequence for deactivating delayed Hot-line |  |
| 1167 | `KeepAliveEnabled` | Enables a proprietary keep-alive mechanism, in which a serviceChange is send with UNDEFINED as the termination ID and... |  |
| 1168 | `KeepAliveInterval` | Defines the interval in seconds of a KeepAlive message. |  |
| 1169 | `KeepAliveTrapPort` | The port to which the keep alive traps are sent to./ |  |
| 1170 | `KeyFeature` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Feature Key' page. |  |
| 1171 | `KeyRejectAnonymousCall` | Key pad pattern for rejecting anonymous call |  |
| 1172 | `KeyRejectAnonymousCallDeact` | Key pad pattern for accepting anonymous call |  |
| 1173 | `L1L1ComplexRxUDPPort` | The UDP port for the incoming (from the remote side) and the outgoing (destination UDP) packets, for Complex Multiple... |  |
| 1174 | `L1L1ComplexTxUDPPort` | The Source UDP port for the outgoing UDP Multiplexed RTP packets, for Complex-Multiplex RTP mode |  |
| 1175 | `L1L1LEN2LifetimeNumOfRows` | The number of the entries in the L1L1PacketLength2LifeTimeTicks table |  |
| 1176 | `L1L1SimpleRxUDPPort` | The UDP port for the incoming (from the remote side) and the outgoing (destination UDP) packets, for Simple-Multiplex... |  |
| 1177 | `L1L1SimpleTxUDPPort` | The Source UDP port for the outgoing UDP Multiplexed RTP packets, for Simple-Multiplex RTP packets mode |  |
| 1178 | `L1L2ComplexRxUDPPort` | Description N/A |  |
| 1179 | `LAST` | Cannot allocate SMDI feature no more resources!!!! |  |
| 1180 | `LATCH` | NE latching/ |  |
| 1181 | `LDAPAUTHFILTER` | The filter is used for searching the given user during the authentication process. |  |
| 1182 | `LDAPBINDDN` | This parameter is used to indicate the of LDAP server bind DN |  |
| 1183 | `LDAPCACHEENTRYREMOVALTIMEOUT` | The time (in hours) that an entry in the LDAP cache is removed from cache |  |
| 1184 | `LDAPCACHEENTRYTIMEOUT` | The time (in mintues) that an entry in the LDAP cache is valid |  |
| 1185 | `LDAPCACHESIZE` | The number of entries in cache |  |
| 1186 | `LDAPDEBUGMODE` | Determines whether to enable the LDAP task debug messages. |  |
| 1187 | `LDAPINTERFACETYPE` | Determines what VLAN interface should be used. |  |
| 1188 | `LDAPPASSWORD` | This parameter is used to indicate the user password of LDAP server. |  |
| 1189 | `LDAPSEARCHDN` | This parameter is obsolete and used for backward compatibiliy only. Please use  to the search-dns  parameter |  |
| 1190 | `LDAPSEARCHDNSINPARALLEL` | Determines (in case there is more than 1 search DN) the DNs should be checked in parallel or sequentially |  |
| 1191 | `LDAPSERVERDOMAINNAME` | This parameter is used to indicate the name of LDAP server. |  |
| 1192 | `LDAPSERVERIP` | Defines the LDAP server IP address in dotted format notation. e.g., 192.10.1.255 |  |
| 1193 | `LDAPSERVERMAXRESPONDTIME` | Defines the period of time the module  will wait for LDAP server response (seconds) |  |
| 1194 | `LDAPSERVERPORT` | Defines the port number for LDAP server |  |
| 1195 | `LDAPSERVICEENABLE` | Determines whether to enable the LDAP service |  |
| 1196 | `LENGTH` | Erorr: MaxBytes  is not valid (range: 1 to 500) |  |
| 1197 | `LINE` | Line number should not be negative |  |
| 1198 | `LINEECADDATTENUATEDREFERENCE` | This field enables adding attenuated reference signal to the input signal. For line echo canceler | ATTENUATED_REFERENCE_DISABLE/0,ATTENUATED_REFERENCE_MINUS_10_DB /1,ATTENUATED_REFERENCE_MINUS_16_... |
| 1199 | `LIST` | L#  Source IP       PrefixLen Src Port Port Range  Protocol Interface Action Count |  |
| 1200 | `LOCAL` | Illegal nettype |  |
| 1201 | `LOCALISDNRBSOURCE` | If the ringback tone source is not IP, who should supply the Ringback tone. 0 - PBX/PSTN (default) ; 1- GW | PBX /0,Gateway /1 |
| 1202 | `LOCALSIPPORT` | Local SIP port used for signaling |  |
| 1203 | `LONGINTERVAL` | Changing Diag Bit Interval To 1 hour . |  |
| 1204 | `LOOKUP` | Invalid IF index: %s |  |
| 1205 | `LdapConfiguration_useTLS` | Determines if to use SSL for the communication or not. | no/0,yes/1 |
| 1206 | `LdapSearchServerMethod` | Determines the search method at the ldap servers in case more than one ldap server was configured: PARALLEL search (=... | LDAP Search Sequentially/0,LDAP Search In Parallel/1 |
| 1207 | `LdapServersSearchDNs_Base_Path` | Base Path |  |
| 1208 | `LeaveFromRight` | Leave From Right |  |
| 1209 | `LibClnt` | SendRestartPacketToLib socket creation error |  |
| 1210 | `LifeLineType` | Defines the Lifeline phone type. |  |
| 1211 | `LineCode` | Selects the line code type to be used for this trunk. | acB8ZS/0,acAMI/1,acHDB3/2 |
| 1212 | `LineNum` | Add Index | /MultipleInterfaceTable@100,200,0 |
| 1213 | `LineTransferMode` | LineTransferMode: 0-ip 1-pbx blind transfer 2-pbx semi supv transfer 3-supervised transfer (also known as warm transf... | None /0,Blind /1,Semi Supervised /2,Supervised /3 |
| 1214 | `LinearPCM` | AMR starting rate 4_75 |  |
| 1215 | `LinkUpDownTrapIfIndexSuffixEnable` | Enables-disables the If Index in the linkUp and linkDown traps. |  |
| 1216 | `ListTargets` | List all debug recording targets |  |
| 1217 | `ListTraceRules` | List all traces |  |
| 1218 | `Llgr_flow` | BuffersFactory::NewBuffer Allocated <%d> |  |
| 1219 | `LocalControlDefaultGW` | Defines the default gateway of the Control when operating in a multiple IP mode. |  |
| 1220 | `LocalControlIPAddress` | Defines the IP address of the Control when operating in a multiple IP mode. |  |
| 1221 | `LocalControlSubnetMask` | Defines the Subnet Mask of the Control when operating in a multiple IP mode. |  |
| 1222 | `LocalKeySet` | Microsoft Local Key set |  |
| 1223 | `LocalMediaDefaultGW` | Defines the default gateway for the media interface, when operating in a multiple IPs mode. |  |
| 1224 | `LocalMediaIPAddress` | Defines the IP address of the Media when operating in multiple IP mode. |  |
| 1225 | `LocalMediaSubnetMask` | Defines the Subnet Mask for the media interface when operating in a multiple IP mode. |  |
| 1226 | `LocalOAMDefaultGW` | Sets the Default gateway for the OAM interface when operating in multiple IPs mode. |  |
| 1227 | `LocalOAMIPAddress` | Sets the IP address of the OAM  when operating in multiple IPs mode. |  |
| 1228 | `LocalOAMSubnetMask` | Sets the Subnet Mask for the OAM interface, when operating in multiple IPs mode. |  |
| 1229 | `Locked` | Shutting Down |  |
| 1230 | `Logging` | Logging Settings |  |
| 1231 | `LogicalATMTermPattern` | Defines the name pattern of an ATM termination. |  |
| 1232 | `LogicalRTPTermPattern` | Defines the name pattern of an RTP termination. |  |
| 1233 | `LogoFileName` | Changes the AudioCodes Web logo to the user logo by loading a GIF/JPEG file. |  |
| 1234 | `LogoWidth` | Defines the logo image width in pixel units. |  |
| 1235 | `LongDurationEventTime` | Defines the default time to trigger the long duration event (in sec). |  |
| 1236 | `LowDSPResourcesEventHyst` | Determines the space between Low and Hi watermarks of DSP resource notifications. |  |
| 1237 | `LowDSPResourcesEventThreshold` | Determines when a notification indicating  a 'low number of DSP resources' is issued. |  |
| 1238 | `M3KGlobalIpAddr` | Not in use any more, for sw upgrade, defines the OAMP IP address to be used by the active module in HA system. |  |
| 1239 | `M3KHAEnabled` | Enable/disable the HA subsystem module in TP6310/8410 running in M3K case. |  |
| 1240 | `M3KHAINTERNALNETWORKPREFIX` | This parameter indicate the prefix of the internal network for the M3K HA to be used, by default it is 11 (11.x.x.x). |  |
| 1241 | `M3KHASwUpgradeMode` | Defines the type of SW upgrade in M3K HA system (Hitless or system reset) |  |
| 1242 | `MAX491TIMER` | The maximum possible timer for next request transmission after 491 Response |  |
| 1243 | `MAXACTIVECALLS` | Limit the number of calls that the gateway can handle at the same time |  |
| 1244 | `MAXBUNDLESYSLOGLENGTH` | Maximum length used for bundling syslog at debug level 7. |  |
| 1245 | `MAXCALLDURATION` | Limit the call time duration (minutes); 0 = no limit |  |
| 1246 | `MAXCONFUSERS` | Illegal MaxConfUsers value |  |
| 1247 | `MAXDIGITS` | Maximum number of digits before dialing starts |  |
| 1248 | `MAXGENERATEDREGISTERSRATE` | Defines the Max. generated Register requests per interval |  |
| 1249 | `MAXPREPAREDDURATION` | Maximum prepared duration for an IVR Dialog |  |
| 1250 | `MAXPTIME` | Illegal Maxptime value |  |
| 1251 | `MAXRECORDDURATION` | Maximum record duration supported by MS |  |
| 1252 | `MAXRETRIES` | Maximum number of retransmissions of RAS messages to Gatekeeper |  |
| 1253 | `MAXSIPMESSAGELENGTH` | Limit the maximum length in KB for SIP message |  |
| 1254 | `MAXTIMERS` | ERR: valid range for MaxTimers is from 50 to 1000 |  |
| 1255 | `MDBG` | Tbl Start %x, End %x |  |
| 1256 | `MEDIACDRREPORTLEVEL` | Media CDR reports | None /0,End Media /1,Start & End Media /2,Update & End Media /3,Start & End & Update Media /4 |
| 1257 | `MEDIACHANNELS` | Number of channels associated with media services (announcements, conferencing) |  |
| 1258 | `MEDIAIPVERSIONPREFERENCE` | Select the preference of Media IP version | Only IPv4 /0,Only IPv6 /1,Prefer IPv4 /2,Prefer IPv6 /3 |
| 1259 | `MEDIASECURITYBEHAVIOUR` | Gateway behavior when recieving offer/response for media encryption. (0)-Preferable; (1)-Mandatory; (3)-Preferable-Si... | Preferable /0,Mandatory /1,Preferable - Single media /3 |
| 1260 | `MEDIASTREAMINGID` | Media Streaming ID |  |
| 1261 | `MEGACO` | NumBlocks should be in this range: 1 to %d |  |
| 1262 | `MEGACOASN1Profile` | Used to profile the binary ASN.1 encoding. |  |
| 1263 | `MEGACOCOTTESTTYPE` | The continuity test type (Set per trunk). One of the following values: 0 - THRH, 1 - THRL, 2 -TLRH |  |
| 1264 | `MEGACOCheckLegalityOfMGC` | Specified if the MEGACO rejects commands from an MGC not in the provisioned list. |  |
| 1265 | `MEGACOContextIDOffset` | Offset for the context ID generated by the gateway. |  |
| 1266 | `MEGACOEncoding` | Sets the MEGACO Coding method. |  |
| 1267 | `MEGACOHangTermTimeout` | Default timeout for sending Hanging Termination event. |  |
| 1268 | `MEGACOProvisionedAudioSize` | Provisioned audio size shown by the X-PtEngr parameter. |  |
| 1269 | `MEGACOProvisionedBCTSize` | Provisioned BCT size shown by the X-PtEngr parameter. |  |
| 1270 | `MEGACOProvisionedConfSize` | Provisioned conference size shown by the X-PtEngr parameter. |  |
| 1271 | `MEGACOProvisionedTrunkTestingSize` | Provisioned trunk testing size shown by the X-PtEngr parameter. |  |
| 1272 | `MEGACOTerminationIDOffset` | Offset for the ephemeral termination IDs in the gateway. |  |
| 1273 | `MEGACOTrunkIDOffset` | Sets the offset to the Trunk numbering. |  |
| 1274 | `MEGACO_MID` | Defines the media gateway's MID towards the MEGACO Call Agent. |  |
| 1275 | `MESSAGEPOLICYREJECTRESPONSETYPE` | The response type returned when a message is rejected according to the message policy. |  |
| 1276 | `MFCR2DEBUG` | Enable MFC-R2 protocol debug |  |
| 1277 | `MFR1DetectorEnable` | Enables or disables detection of MFR1 signaling |  |
| 1278 | `MFR2BackwardDetectorEnable` | Enables or disables detection of MFR2 backward signaling |  |
| 1279 | `MFR2ForwardDetectorEnable` | Enables or disables detection of MFR2 forward signaling |  |
| 1280 | `MFSS5DetectorEnable` | Enables or disables detection of MF SS5 line signaling. |  |
| 1281 | `MFTransportType` | Defines the way MFs are transported over the network. | Mute MF/0,Transparent MF/2,RFC2833 Relay MF/3 |
| 1282 | `MGCExecutionTime` | Defines the estimated execution time of the MGC (in msec). |  |
| 1283 | `MGCPActiveEndPoints` | Defines a list of active endpoints, separated by commas. |  |
| 1284 | `MGCPClearEventsWithDLCX` | Causes DLCX commands to clear the requested events string. |  |
| 1285 | `MGCPCommunicationLayerTimeout` | Assumed delay of the communication layer (in sec). |  |
| 1286 | `MGCPCompatibilityProfile` | Controls protocol behaviour, for vendor specific compatibility. |  |
| 1287 | `MGCPDIGESTPASSWORD` | Defines the MGCP Digest security password. |  |
| 1288 | `MGCPDIGESTUSERNAME` | Defines the MGCP Digest security user name. |  |
| 1289 | `MGCPDTMFDetectionPoint` | Defines if the detection of DTMF events is notified at the end of DTMF or at the start. |  |
| 1290 | `MGCPDebugMode` | Sets the output level of MGCP/MEGACO debug messages sent by the Gateway. |  |
| 1291 | `MGCPDefaultCoder` | The default coder used for channel opening. |  |
| 1292 | `MGCPEndPointNumberingOffset` | Sets the offset to the endpoint numbering . |  |
| 1293 | `MGCPEndpointNamingPattern` | Defines the endpoint naming pattern for the gateway. |  |
| 1294 | `MGCPPersistantEvents` | Allows the configuration of persistent MGCP Events. |  |
| 1295 | `MGCPPersistentEvents` | Allows the configuration of persistent MGCP events. |  |
| 1296 | `MGCPRetransmissionTimeout` | Controls protocols retransmission timeout (in msec). |  |
| 1297 | `MGCPRetransmitionTimeout` | Controls protocols retransmission timeout. |  |
| 1298 | `MGCPSendDigitmapMismatchNotification` | Determines whether to send a notification even if a dialed string does not match the digitmap. |  |
| 1299 | `MGCPSendMACWithRSIP` | Determines whether to include the MAC address in MGCP extension format. |  |
| 1300 | `MGCPTrunkNamingPattern` | Defines the trunk and B-channel naming pattern used by the gateway. |  |
| 1301 | `MGCPUseAudioPortForT38` | Defines that T.38 packets will be received on the RTP port. |  |
| 1302 | `MGCPVersion` | Defines the MGCP protocol version. |  |
| 1303 | `MGCPXUAMAKE` | Defines the make part of x-ua response according to RFC3149. |  |
| 1304 | `MGCPXUAMODEL` | Defines the model part of x-ua response according to RFC3149. |  |
| 1305 | `MGCProvisionalResponseTime` | Defines the provisional response timer for the MGC (in msec). |  |
| 1306 | `MGControlProtocolType` | Defines the control protocol type. |  |
| 1307 | `MGEOL` | Sets the characters that constitute the EOL in mgcp messages |  |
| 1308 | `MGExecutionTime` | Defines the estimated execution time of the media gateway (in msec). |  |
| 1309 | `MGHistoryBufferTimeLim` | Defines the time that a transaction is kept in the history buffer. |  |
| 1310 | `MGMTBEHAVIORONTIMEOUT` | Defines whether device searches in its local users table if Authentication server is not accessible. |  |
| 1311 | `MGMTLDAPLOGIN` | Defines whether device uses LDAP for authenticating management interfaces (0-not use, 1-use). |  |
| 1312 | `MGMTLOGINCACHEMODE` | Defines whether password local cache timeout is reset after successful authorization. |  |
| 1313 | `MGMTLOGINCACHETIMEOUT` | Defines expiry time [sec] of locally stored login password. When expired, the request to Authentication server is rep... |  |
| 1314 | `MGMTUSELOCALUSERSDATABASE` | Defines when to use local users database in addition to Authentication server. | When No Auth Server Defined/0,Always/1 |
| 1315 | `MGProvisionalResponseTime` | Defines the provisional response timer for the media gateway (in msec). |  |
| 1316 | `MGmt` | Call duration history: no records yet. System uptime is less than 1 hour. |  |
| 1317 | `MINCALLDURATION` | Extend call duration to a minimum time (seconds); 0 = no extend |  |
| 1318 | `MINOVERLAPDIGITSFORROUTING` | Minimum number of overlap digits before routing |  |
| 1319 | `MINSE` | Minimal value for session refresh |  |
| 1320 | `MLPPDEFAULTNAMESPACE` | MLPP Default Namespace | Interworking Namespace/-1,User Defined 0/0,DSN/1,DOD/2,DRSN/3,User Defined 4/4,UC/5,User Defined ... |
| 1321 | `MLPPDIFFSERV` | DiffServ value for MLPP calls |  |
| 1322 | `MLPPDefaultServiceDomain` | MLPP Default Service Domain String (6 Hex Digits) |  |
| 1323 | `MLPPFLASHOVEROVERRTPDSCP` | RTP DSCP for MLPP Flash-Override-Override |  |
| 1324 | `MLPPFLASHOVERRTPDSCP` | RTP DSCP for MLPP Flash Override |  |
| 1325 | `MLPPFLASHRTPDSCP` | RTP DSCP for MLPP Flash |  |
| 1326 | `MLPPIMMEDIATERTPDSCP` | RTP DSCP for MLPP Immediate |  |
| 1327 | `MLPPNETWORKIDENTIFIER` | Sets the Network identifier value which is represented as the first 2 octets in the MLPP service domain field. values... |  |
| 1328 | `MLPPNormalizedServiceDomain` | MLPP Normalized Service Domain String (6 Hex Digits) |  |
| 1329 | `MLPPPRIORITYRTPDSCP` | RTP DSCP for MLPP Priority |  |
| 1330 | `MLPPROUTINERTPDSCP` | RTP DSCP for MLPP Routine |  |
| 1331 | `MONITORID` | Identification of Calea call (To be used by SIP INVITE) |  |
| 1332 | `MPTIME` | First MPTime cannot be hyphen |  |
| 1333 | `MPVQMONENABLE` | Enable / disable voice quality monitoring and RTCP xr reports for MP1xx products. |  |
| 1334 | `MSBGShdslLineMode` | Select SHDSL line mode: ATM or EFM. |  |
| 1335 | `MSCMLID` | Identification of HTTP played voice prompt using mscml(To be used by SIP INVITE) |  |
| 1336 | `MSLDAPDISPLAYNAMEATTRIBUTENAME` | The name of the attribute which represents the user display name in the Microsoft AD data base |  |
| 1337 | `MSLDAPMOBILENUMATTRIBUTENAME` | The name of the attribute which represents the user Mobile number in the Microsoft AD data base |  |
| 1338 | `MSLDAPMngr` | MSLDAPMngr deleted |  |
| 1339 | `MSLDAPOCSNUMATTRIBUTENAME` | The name of the attribute which represents the user OCS number in the Microsoft AD data base |  |
| 1340 | `MSLDAPPBXNUMATTRIBUTENAME` | The name of the attribute which represents the user PBX number in the Microsoft AD data base |  |
| 1341 | `MSLDAPPRIMARYKEY` | The name of the query primary key in the Microsoft AD data base |  |
| 1342 | `MSLDAPPRIVATENUMATTRIBUTENAME` | The name of the attribute which represents the user Private number in the Microsoft AD data base |  |
| 1343 | `MSLDAPSECONDARYKEY` | The name of the query secondary key in the Microsoft AD data base |  |
| 1344 | `MSRTAForwardErrorCorrectionEnable` | Determines the Microsoft RTA coder forward error correction mode. |  |
| 1345 | `MSRTATxBitRate` | Determines the Microsoft RTA coder transmitted  bit rate [bps]. |  |
| 1346 | `MULTIPTIMEFORMAT` | Format of multiple ptime (ptime per coder) in outgoing SDP | None /0,PacketCable /1 |
| 1347 | `MUTEDTMFINOVERLAP` | In overlap mode if set mute in-band DTMF till Desination Number is received |  |
| 1348 | `MUTUALAUTHENTICATIONMODE` | Mutual Authentication Mode: 0 - Optional, 1 - Mandatory | Optional /0,Mandatory /1 |
| 1349 | `MWIANALOGLAMP` | Enable MWI support using an analog lamp (110 Volt) |  |
| 1350 | `MWIDISPLAY` | Enable MWI support using Caller ID interface |  |
| 1351 | `MWIEXPIRATIONTIME` | MWI service subscription expiration time (seconds) |  |
| 1352 | `MWIInterrogationType` | MWI Interrogation Type | Not Configured/255,None/0,Use Activate Only/1,Result Not Used/2,Use Result/3 |
| 1353 | `MWIOffCode` | Digit pattern used to notify PBX about no messages waiting for extension (added as prefix) |  |
| 1354 | `MWIOnCode` | Digit pattern used to notify PBX about messages waiting for extension (added as prefix) |  |
| 1355 | `MWIQSIGMSGCENTRELDIDPARTYNUMBER` | Party Number from msgCentreId in MWIactivate and MWIdeactivate |  |
| 1356 | `MWISERVERIP` | MWI server IP address |  |
| 1357 | `MWISERVERTRANSPORTTYPE` | MWI server transport type |  |
| 1358 | `MWISOURCENUMBER` | The phone number sent as source number toward PSTN for MWI setup |  |
| 1359 | `MWISUBSCRIBEIPGROUPID` | IPGroup ID for MWI subscribe purposes |  |
| 1360 | `MWISuffixCode` | MWI suffix code used to notify PBX about messages waiting for extension (added as suffix to the extention number) |  |
| 1361 | `MWIndicationType` | Defines the type of (MWI) Message Waiting Indicator (for FXS only). |  |
| 1362 | `Maintenance` | Maintenance Actions |  |
| 1363 | `Management` | CTree::CIterator Node = NULL |  |
| 1364 | `Mandatory` | Preferable - Single Media |  |
| 1365 | `ManipulatedURI` | Manipulated URI | Source/0,Destination/1 |
| 1366 | `ManipulationPurpose` | Manipulation Purpose | Normal/0,Routing input only/1,Shared Line/2 |
| 1367 | `Manipulations` | General Configuration |  |
| 1368 | `MatrixView_SelLineNum` | IP Interfaces Table |  |
| 1369 | `MaxDTMFDigitsInCIDString` | Determines the maximum number of DTMF digits in a DTMF-based Caller ID string. |  |
| 1370 | `MaxEchoCancellerLength` | Defines the maximum EC (Echo Canceller) length capability. | ECLengthDefault/0,ECLength15MSec/1,ECLength20MSec/2,ECLength25MSec/3,ECLength30MSec/4,ECLength35M... |
| 1371 | `MaxInBoardConferenceCalls` | Max InBoard Conference Calls | Conference mode 0/1 : configure ConfID on setup, 2: set Inboard 3w conference, 3:Huawei Media Server |
| 1372 | `MaxRADIUSSessions` | Maximum Radius simultaneous sessions. |  |
| 1373 | `MaxRTPTerminations` | Max number of RTP Terminations |  |
| 1374 | `MeasPersistence` | Time (in msec) that passes from the time of detection until the interrupt signal. |  |
| 1375 | `Media` | Voice Settings |  |
| 1376 | `MediaEnhancement` | Key Expire Date %d.%d.%d |  |
| 1377 | `MediaIPVersionPreference` | Only IPv4 |  |
| 1378 | `MediaSecurity` | Voice_Engine_errors_time_interval = %d(seconds) |  |
| 1379 | `MediaServerID` | Media Server ID |  |
| 1380 | `MediationTranscodingMode` | The transcoding mode for mediation between two endpoints that are connected in full transcoding level. | TDM_TRANCODING/1,RTP_SYNC_TRANCODING/2,RTP_ASYNC_TRANCODING/3,DEFAULT_TRANSCODING_SMART/0 |
| 1381 | `MegacoCALEAPackageID` | Internal parameter used to determine which package is used for CALEA |  |
| 1382 | `MegacoVersion` | Determines the maximum Megaco Version number that is supported by the board. |  |
| 1383 | `MemorySnoop` | 0=Normal mode 1=Debug running- enables memory snooping |  |
| 1384 | `MessageHeaderArrayItem` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 1385 | `MeteringOffTime` | This parameter shouldn't be used |  |
| 1386 | `MeteringType` | Sets the metering method for charging pulses. | 12 kHz sinusoidal bursts/0,16 kHz sinusoidal bursts/1,Polarity Reversal pulses/2 |
| 1387 | `MgcpFxoDiscPortsAlarm` | Determines whether to send alarm on FXO ports that are disconnected from the PBX. |  |
| 1388 | `MinDTMFDigitsInCIDString` | Determines the mimumum number of DTMF digits in a DTMF-based Caller ID string. |  |
| 1389 | `MinFlashHookTime` | Sets the minimal time (in msec) for detection of a flash hook event (for FXS only). |  |
| 1390 | `MinOffTimeDtmfRelay` | Sets the minimum delay between two RFC2833 DTMFs that are played to TDM side, in units of 10ms. |  |
| 1391 | `ModemBypassOutputGain` | Defines the modem bypass output gain [dB]. |  |
| 1392 | `ModemBypassPayloadType` | Modem Bypass (VBD) Payload type. |  |
| 1393 | `MsServiceDebugMode` | Determines whether to enable the streaming of MS task debug messages. |  |
| 1394 | `MwiResumeTime` | Time elapsed between ring stop and MWI resume. |  |
| 1395 | `NATBINDINGDEFAULTTIMEOUT` | Defines the NAT binding lifetime (in seconds). |  |
| 1396 | `NETANNANNCID` | NetAnn Announcement ID |  |
| 1397 | `NETWORKSERVICECLASSDIFFSERV` | Sets the DiffServ for Network service class content. |  |
| 1398 | `NFASGroupNumber` | Indicates the group number of the ISDN NFAS group. |  |
| 1399 | `NFSBasePort` | Start of the range of numbers used for local UDP ports used by the NFS client. |  |
| 1400 | `NFSClientMaxRetransmission` | The maximum number of retransmission of NFS commands from the board to the NFS server. |  |
| 1401 | `NFSSERVERS` | Buffer Overflow by 1 during acMatrix_CmdShellHandler |  |
| 1402 | `NOAUDIO` | SDPMediaPayloadsList::AddCoder() #%d:Failed to allocate new coder for payload id = %d |  |
| 1403 | `NOAUDIOPAYLOADTYPE` | NoAudio payload type - default:don't offer NoAudio coder |  |
| 1404 | `NOBUS` | BOARDINFO command has no any parameter |  |
| 1405 | `NONE` | SYS_HA: Can't update active module feature key without redundant key, please use web access to upload License Key Fil... |  |
| 1406 | `NORMAL` | DuSLICIFReversalPolarity (Wink) (ChannelNum=%d) |  |
| 1407 | `NORTELFIREWALLNAME` | Nortel Firewall Name |  |
| 1408 | `NOTACTIVE` | DebugIsActive=%d  CurrentTimerTimestamp=%u  MaxTimersToPrint=%u |  |
| 1409 | `NOTIFICATIONIPGROUPID` | IPGroup ID for notification purposes |  |
| 1410 | `NOTIP` | DebugRecordingDestIP_SpecialFunc - failed with EC= %d |  |
| 1411 | `NO_MORE_VCID_RESOURCES` | Total Virtual CIDs allocated : %d |  |
| 1412 | `NRTSUBSCRIBERETRYTIME` | NRT service subscription retry time after last subscription failure (seconds) |  |
| 1413 | `NSEMode` | Enables Cisco's NSE fax/modem automatic pass-through mode. |  |
| 1414 | `NSEPayloadType` | NSE Payload type. |  |
| 1415 | `NTEMaxDuration` | Maximal time for sending NTE (Named Telephony Events) to the network [ms]. |  |
| 1416 | `NTPClnt` | NTP UDP: socket() Can't create UDP Socket: %d |  |
| 1417 | `NTPSecondaryServerIP` | Defines the NTP Secondary FQDN or Server IP address. |  |
| 1418 | `NTPSecondaryServerIP_abs` | Defines the NTP Secondary Server IP address. |  |
| 1419 | `NTPServerIP` | Defines the NTP Server FQDN or IP address. |  |
| 1420 | `NTPServerIP_abs` | Defines the NTP Server IP address. |  |
| 1421 | `NTPServerUTCOffset` | Defines the NTP time to offset in seconds. |  |
| 1422 | `NTPTIME` | Current Time Milli %d |  |
| 1423 | `NTPUpdateInterval` | Activity Log: User Name: %s ,Parameter %s was set to %s. |  |
| 1424 | `NTTDIDSignallingForm` | Configures the signalling format used when generating an NTT DID. | NTT_DID_FSK_SIGNALLING /0,NTT_DID_DTMF_BASED_SIGNALLING /1 |
| 1425 | `NTT_CID_TIME_BETWEEN_CID_TO_DC_LOOP_DISCONNECT` | The time between a Caller ID signal (FSK) and DC loop disconnect detection in the NTT Caller ID type. |  |
| 1426 | `NTT_CID_TIME_BETWEEN_DC_LOOP_DISCONNECT_TO_RING` | The time between DC loop disconnect detection and ring start in the NTT Caller ID type. |  |
| 1427 | `NTT_CID_TIME_BETWEEN_DC_LOOP_TO_CID` | The time between DC loop detection and a Caller ID signal (FSK) in the NTT Caller ID type. |  |
| 1428 | `NTT_CID_TIME_BETWEEN_DID_CID_2_DC_LOOP_DISCONNECT` | The time between a DID signal (modem based) and DC loop disconnect detection in the NTT Caller ID/DID type. |  |
| 1429 | `NTT_CID_TIME_BETWEEN_LINE_REVERSAL_TO_CAR` | The time between a line reversal and a CAR signal in the NTT Caller ID type. |  |
| 1430 | `NTT_CID_TIME_BETWEEN_LINE_REVERSAL_TO_DC_LOOP` | The time between a line reversal and DC loop detection in the NTT Caller ID type. |  |
| 1431 | `NTT_CID_TIME_CAR_OFF` | The CAR signal Off time in the NTT Caller ID type. |  |
| 1432 | `NTT_CID_TIME_CAR_ON` | The CAR signal On time in the NTT Caller ID type. |  |
| 1433 | `NULLCMD` | Fail to allocate Command# %d |  |
| 1434 | `NUMBEROFACTIVEDIALOGS` | Limit the number of concurrent non responded dialogs |  |
| 1435 | `NUMBEROFWAITINGINDICATIONS` | Number of Call Waiting indications to be played to the user |  |
| 1436 | `NUMOFANNOUNCENDPOINTS` | Number of Annuncment endpoints |  |
| 1437 | `NUMOFENTRIES` | First Used VoicePrompt Index: %d  First Free VoicePrompt Index: %d |  |
| 1438 | `NUMOFSTREAMINGENDPOINTS` | Number of Streaming  endpoints |  |
| 1439 | `NUMOFSUBSCRIBES` | Active SUBSCRIBE sessions limit. Set to -1 for automatic maximum. Maximum value for this parameter can be increased b... |  |
| 1440 | `NUMOFVXMLENDPOINTS` | Number of VXML endpoints |  |
| 1441 | `Name` | Interface Name |  |
| 1442 | `NaptrDNSResolver` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 1443 | `NatMode` | Determines the mode of NAT feature:{@}0 = NAT is optional.{@}1 = NAT is disable.{@}2 = NAT is forced. | ENABLE_NAT_OPTION/0,DISABLE_NAT/1,FORCE_NAT/2 |
| 1444 | `Netscape` | Netscape Communications Corp. |  |
| 1445 | `Network` | IP Interfaces Table |  |
| 1446 | `NewAdminUN` | Change User Name |  |
| 1447 | `NewKey` | Add Key |  |
| 1448 | `NewRtpStreamPackets` | Minimal number of continuous RTP packets, allowing latching an incoming RTP stream. |  |
| 1449 | `NewSRTPStreamPackets` | Set Voice denial of service min threshold to throw packets, in Percentage. |  |
| 1450 | `NewUserUN` | Change User Name |  |
| 1451 | `NoOpEnable` | Enable (=1) or disable (=0) the No Operation packets sending. |  |
| 1452 | `NoOpInterval` | Sets the No Operation packets sending interval [ms]. |  |
| 1453 | `NoOpIntervalxMS` | Set mask values CID A or B (first value is CID): in following order : |  |
| 1454 | `NoReplyTime` | No Reply Time |  |
| 1455 | `No_modify_in_PacketCable` | No modify SRTP parameters. |  |
| 1456 | `NoiseReductionActivationDirection` | Defines the Noise Reduction activation direction. |  |
| 1457 | `NoiseReductionFineTuning` | Fine Tuning of Noise Reduction Mechanism |  |
| 1458 | `NoiseReductionIntensity` | Defines the Noise Reduction Intensity. |  |
| 1459 | `Nonce` | OCSP Nonce |  |
| 1460 | `None` | GET Column ActionRes failed |  |
| 1461 | `NumberPlan` | Number Plan |  |
| 1462 | `NumberType` | Number Type | Not Supported /0,Info NORTEL /1,NOTIFY /2,Info Cisco /3,RFC 2833 /4,Info KOREA /5,Not Set /-1 |
| 1463 | `NvMu` | NV Create Mutex error 0x%x |  |
| 1464 | `OCSP` | OCSP - Manage OCSP communication. |  |
| 1465 | `OCSPSigning` | OCSP Signing |  |
| 1466 | `OFFERUNENCRYPTEDSRTCP` | If set to 1, the 'crypto' attribute includes the UNENCRYPTED_SRTCP parameter. If set to 1, the UNENCRYPTED_SRTCP para... |  |
| 1467 | `OOSONREGISTRATIONFAIL` | Should deactivate endpoint service on registration failure |  |
| 1468 | `OPENH245ONFS` | Open H.245 when using Fast Start call setup procedure |  |
| 1469 | `OPTIONS` | Possible options are (first 3 letters enough for each to input): |  |
| 1470 | `OPTIONSUSERPART` | Allow to configure the OPTIONS userpart string for all gateways. |  |
| 1471 | `OUTOFBANDDTMFFORMAT` | DTMF Out-of-Band transport method | Unknown /0,Nortel /1,Cisco /2,Threecom /3,Korea /4 |
| 1472 | `OUTSIDE_DSP_CHANNEL` | TDM Encoder record Location is: %d (%s) |  |
| 1473 | `OcspDefaultResponse` | Determines the default OCSP behavior when the server cannot be contacted. allow / reject peer certificate. | Reject/0,Allow/1 |
| 1474 | `OcspEnable` | Enables / disables certificate checking via OCSP. |  |
| 1475 | `OcspSecondaryServerIP` | Defines the IP address of the OCSP secondary server.(Optional) |  |
| 1476 | `OcspServerIP` | Defines the IP address of the OCSP server. |  |
| 1477 | `OcspServerPort` | Defines the TCP port number of the OCSP server. |  |
| 1478 | `OffhookDebounceTiming` | Sets the off hook detection debounce timing. |  |
| 1479 | `OpenDiagBitDebugMode` | Wrong num of parameters passed. |  |
| 1480 | `OpenSslSyslog` | OpenSslSyslog - Enable/Disable Syslog for OpenSSL |  |
| 1481 | `Other` | Tx/Rx bytes:            %d/%d |  |
| 1482 | `OutboundManSet` | Outbound Message Manipulation Set |  |
| 1483 | `OverFl` | VQChagneParamValue: RemoteRTCPXR_Rep NOT allocated. |  |
| 1484 | `OverloadSensitivityLevel` | Defines when to enter overload state: 0:never 1:on very high utilization  2:on medium utilization |  |
| 1485 | `P2PTdmOutputMode` | Define whether to mute the TDM side when packet-to-packet mode is in use (and the current DSP TDM side isn't part of ... |  |
| 1486 | `PACKET` | Error Handler print all packet types - was set |  |
| 1487 | `PASS` | DES Test...  %s |  |
| 1488 | `PASSERTEDUSERNAME` | The user part of the user Url in the P-Asserted-Identity Header. |  |
| 1489 | `PASSWORD` | Password used for authentication |  |
| 1490 | `PATCH` | Send PATCH File | /UploadPatch@200,200,0 |
| 1491 | `PAYPHONEMETERINGMODE` | Method of automatic generation of payphone metering pulses | Disable /0,Internal Table /1,SIP Interval Provided /2,SIP RAW DATA Provided /3,SIP RAW DATA Incre... |
| 1492 | `PCATS` | Prints the Interface Table (The one that reflects in the INI File). |  |
| 1493 | `PCITS` | Sends the Interface Table statistics to the SysLog. (The same as occurs automatically in TreckBuffersAudit). |  |
| 1494 | `PCMLawSelect` | Selects the type of PCM companding law in the input/output TDM bus. | MuLaw/3,ALaw/1 |
| 1495 | `PDNSS` | Multi media |  |
| 1496 | `PDPattern` | Defines the patterns that can be detected by the Pattern Detector. |  |
| 1497 | `PDThreshold` | Defines the threshold for the pattern detection. |  |
| 1498 | `PEERHOSTNAMEVERIFICATIONMODE` | While using TLS, defines the verification behavior of the host name sent in the certificate. | Disable /0,Server Only /1,Server & Client /2 |
| 1499 | `PERFORMADDITIONALIP2TELDESTINATIONMANIPULATION` | Perform Additional IP2TEL Destination Manipulation |  |
| 1500 | `PERFORMADDITIONALIP2TELSOURCEMANIPULATION` | Perform Additional IP2TEL Source Manipulation |  |
| 1501 | `PERIODIC` | CpuUtilization PERIODIC is already running ! |  |
| 1502 | `PIFORDISCONNECTMSG` | Configure PIForDisconnectMsg in order to overwrite PI value received in ISDN Disconnect message | not-configured/-1,no-pi/0,pi-1/1,pi-8/8 |
| 1503 | `PIFORSETUPMSG` | Progress Indicator for ISDN Setup Message |  |
| 1504 | `PINGPONGKEEPALIVETIME` | The Ping Keep-Alivewill be sent (using CRLFCRLF) each time this timer expires (seconds) |  |
| 1505 | `PLAYBUSYTONE2ISDN` | 0: don't play, 1: Play Busy or Reorder tone when disconnecting ISDN Call and Send PI=8, 2:Play before disconnect | Don't Play /0,Play when Disconnecting /1,Play before Disconnect /2 |
| 1506 | `PLAYFROMID` | Identification of voice stream play location (To be used by SIP INVITE) |  |
| 1507 | `PLAYHELDTONEFORIP2IP` | Enable play tone on other IP2IP leg instead of putting it on hold |  |
| 1508 | `PLAYRBTONE2IP` | Enable ringback tone playing towards IP. Refer to User's Manual for details | Don't Play /0,Play /1 |
| 1509 | `PLAYRBTONE2TEL` | Enable ringback tone playing towards Tel side. Refer to User's Manual for details | Don't Play /0,Play on Local /1,Prefer IP /2,Play Local Until Remote Media Arrives /3 |
| 1510 | `PLAYRBTONE2TRUNK` | Enable ringback tone playing towards trunk side. Refer to User's Manual for details | Not Configured /-1,Don't Play /0,Play on Local /1,Prefer IP /2,Play Local Until Remote Media Arri... |
| 1511 | `PLAYRBTONEONXFER` | Play RB tone on transfer success |  |
| 1512 | `PLAYRBTONISDNTRANSFER` | Play local RBT on TBCT/ECT/RLT transfer | Don't play /0,Play /1 |
| 1513 | `PLBM` | Round Robin |  |
| 1514 | `PLLOutOfRange` | Determines the valid PPM range outside the Stratum 3 standard. This parameter is only relevant for the TP8410 on the ... | OOR 9.2 to 12 ppm/0,OOR 40 to 52 ppm/1,OOR 100 to 130 ppm/2,OOR 64 to 83 ppm/3,OOR 13.8 to 18 ppm... |
| 1515 | `PMCongestionHysteresis` | Controls the protocols Congestion Performance Monitoring Hysteresis Value. |  |
| 1516 | `PMDisplay_SelGroup` | Reset Statistics | /PM_Interface@50,50,0 |
| 1517 | `PM_ATMCellRx` | Performance Monitoring ATMCellRx setup |  |
| 1518 | `PM_ATMCellTx` | Performance Monitoring ATMCellTx setup |  |
| 1519 | `PM_ATMresources` | Performance Monitoring ATMresources setup |  |
| 1520 | `PM_ActiveContextCount` | Performance Monitoring ActiveContextCount setup |  |
| 1521 | `PM_Bct` | Performance Monitoring Bct setup |  |
| 1522 | `PM_BctDuration` | Performance Monitoring BctDuration setup |  |
| 1523 | `PM_BctInProgress` | Performance Monitoring BctInProgress setup |  |
| 1524 | `PM_CPCallAttemptsPerSec` | Performance Monitoring CPCallAttemptsPerSec setup |  |
| 1525 | `PM_CPConnectionState` | Performance Monitoring CPConnectionState setup |  |
| 1526 | `PM_CPRetransmissionCount` | Performance Monitoring CPRetransmissionCount setup |  |
| 1527 | `PM_CPTransactionRequestsPerSec` | Performance Monitoring CPTransactionRequestsPerSec setup |  |
| 1528 | `PM_ChannelsInMaintenance` | Performance Monitoring ChannelsInMaintenance setup |  |
| 1529 | `PM_ChannelsInService` | Performance Monitoring ChannelsInService setup |  |
| 1530 | `PM_ChannelsOutOfService` | Performance Monitoring ChannelsOutOfService setup |  |
| 1531 | `PM_Conf` | Performance Monitoring Conf setup |  |
| 1532 | `PM_ConfDuration` | Performance Monitoring ConfDuration setup |  |
| 1533 | `PM_ConfInProgress` | Performance Monitoring ConfInProgress setup |  |
| 1534 | `PM_ConferenceResources` | Performance Monitoring ConferenceResources setup |  |
| 1535 | `PM_DSPresources` | Performance Monitoring DSPresources setup |  |
| 1536 | `PM_DiscardedAtmCells` | Performance Monitoring DiscardedAtmCells setup |  |
| 1537 | `PM_ETH_RXBadOctets` | Performance Monitoring ETH_RXBadOctets setup |  |
| 1538 | `PM_ETH_RXBroadcastsPackets` | Performance Monitoring ETH_RXBroadcastsPackets setup |  |
| 1539 | `PM_ETH_RXCompressed` | Performance Monitoring ETH_RXCompressed setup |  |
| 1540 | `PM_ETH_RXDiscardPackets` | Performance Monitoring ETH_RXDiscardPackets setup |  |
| 1541 | `PM_ETH_RXDropped` | Performance Monitoring ETH_RXDropped setup |  |
| 1542 | `PM_ETH_RXErrors` | Performance Monitoring ETH_RXErrors setup |  |
| 1543 | `PM_ETH_RXFcsErroredPackets` | Performance Monitoring ETH_RXFcsErroredPackets setup |  |
| 1544 | `PM_ETH_RXFifoErrors` | Performance Monitoring ETH_RXFifoErrors setup |  |
| 1545 | `PM_ETH_RXFrameErrors` | Performance Monitoring ETH_RXFrameErrors setup |  |
| 1546 | `PM_ETH_RXGoodOctets` | Performance Monitoring ETH_RXGoodOctets setup |  |
| 1547 | `PM_ETH_RXMacErrors` | Performance Monitoring ETH_RXMacErrors setup |  |
| 1548 | `PM_ETH_RXMultiCastPackets` | Performance Monitoring ETH_RXMultiCastPackets setup |  |
| 1549 | `PM_ETH_RXMulticast` | Performance Monitoring ETH_RXMulticast setup |  |
| 1550 | `PM_ETH_RXOversizePackets` | Performance Monitoring ETH_RXOversizePackets setup |  |
| 1551 | `PM_ETH_RXPackets` | Performance Monitoring ETH_RXPackets setup |  |
| 1552 | `PM_ETH_RXUndersizePackets` | Performance Monitoring ETH_RXUndersizePackets setup |  |
| 1553 | `PM_ETH_RXUnicastsPackets` | Performance Monitoring ETH_RXUnicastsPackets setup |  |
| 1554 | `PM_ETH_TXBadPackets` | Performance Monitoring ETH_TXBadPackets setup |  |
| 1555 | `PM_ETH_TXBroadcastsPackets` | Performance Monitoring ETH_TXBroadcastsPackets setup |  |
| 1556 | `PM_ETH_TXCarrierErrors` | Performance Monitoring ETH_TXCarrierErrors setup |  |
| 1557 | `PM_ETH_TXCollisions` | Performance Monitoring ETH_TXCollisions setup |  |
| 1558 | `PM_ETH_TXCompressed` | Performance Monitoring ETH_TXCompressed setup |  |
| 1559 | `PM_ETH_TXDiscardPackets` | Performance Monitoring ETH_TXDiscardPackets setup |  |
| 1560 | `PM_ETH_TXDropped` | Performance Monitoring ETH_TXDropped setup |  |
| 1561 | `PM_ETH_TXErrors` | Performance Monitoring ETH_TXErrors setup |  |
| 1562 | `PM_ETH_TXFCSErrPackets` | Performance Monitoring ETH_TXFCSErrPackets setup |  |
| 1563 | `PM_ETH_TXFifoErrors` | Performance Monitoring ETH_TXFifoErrors setup |  |
| 1564 | `PM_ETH_TXLatePackets` | Performance Monitoring ETH_TXLatePackets setup |  |
| 1565 | `PM_ETH_TXMulticastsPackets` | Performance Monitoring ETH_TXMulticastsPackets setup |  |
| 1566 | `PM_ETH_TXOctets` | Performance Monitoring ETH_TXOctets setup |  |
| 1567 | `PM_ETH_TXPackets` | Performance Monitoring ETH_TXPackets setup |  |
| 1568 | `PM_ETH_TXUnicastPackets` | Performance Monitoring ETH_TXUnicastPackets setup |  |
| 1569 | `PM_EnableThresholdAlarms` | Enables SNMP / Syslog alarms for performance threshold crossing. |  |
| 1570 | `PM_GeneralResources` | Performance Monitoring GeneralResources setup |  |
| 1571 | `PM_IGMPGeneralQueryReceived` | Performance Monitoring IGMPGeneralQueryReceived setup |  |
| 1572 | `PM_IGMPLeaveGroupSent` | Performance Monitoring IGMPLeaveGroupSent setup |  |
| 1573 | `PM_IGMPMembershipReportsSent` | Performance Monitoring IGMPMembershipReportsSent setup |  |
| 1574 | `PM_IGMPSpecificQueryReceived` | Performance Monitoring IGMPSpecificQueryReceived setup |  |
| 1575 | `PM_IGMPv1MembershipReportsSent` | Performance Monitoring IGMPv1MembershipReportsSent setup |  |
| 1576 | `PM_IPresources` | Performance Monitoring IPresources setup |  |
| 1577 | `PM_IPsecCurrentSAs` | Performance Monitoring IPsecCurrentSAs setup |  |
| 1578 | `PM_IvrContDigitCollect` | Performance Monitoring IvrContDigitCollect setup |  |
| 1579 | `PM_IvrContDigitCollectDuration` | Performance Monitoring IvrContDigitCollectDuration setup |  |
| 1580 | `PM_IvrContDigitCollectInProgress` | Performance Monitoring IvrContDigitCollectInProgress setup |  |
| 1581 | `PM_IvrPlay` | Performance Monitoring IvrPlay setup |  |
| 1582 | `PM_IvrPlayCollect` | Performance Monitoring IvrPlayCollect setup |  |
| 1583 | `PM_IvrPlayCollectDuration` | Performance Monitoring IvrPlayCollectDuration setup |  |
| 1584 | `PM_IvrPlayCollectInProgress` | Performance Monitoring IvrPlayCollectInProgress setup |  |
| 1585 | `PM_IvrPlayDuration` | Performance Monitoring IvrPlayDuration setup |  |
| 1586 | `PM_IvrPlayInProgress` | Performance Monitoring IvrPlayInProgress setup |  |
| 1587 | `PM_IvrPlayRecord` | Performance Monitoring IvrPlayRecord setup |  |
| 1588 | `PM_IvrPlayRecordDuration` | Performance Monitoring IvrPlayRecordDuration setup |  |
| 1589 | `PM_IvrPlayRecordInProgress` | Performance Monitoring IvrPlayRecordInProgress setup |  |
| 1590 | `PM_MediaRealmBwRx` | Performance Monitoring MediaRealmBwRx setup |  |
| 1591 | `PM_MediaRealmBwTx` | Performance Monitoring MediaRealmBwTx setup |  |
| 1592 | `PM_MediaRealmBytesRx` | Performance Monitoring MediaRealmBytesRx setup |  |
| 1593 | `PM_MediaRealmBytesTx` | Performance Monitoring MediaRealmBytesTx setup |  |
| 1594 | `PM_MediaRealmPacketsRx` | Performance Monitoring MediaRealmPacketsRx setup |  |
| 1595 | `PM_MediaRealmPacketsTx` | Performance Monitoring MediaRealmPacketsTx setup |  |
| 1596 | `PM_MegacoSuccessfulAddWithLoopback` | Performance Monitoring MegacoSuccessfulAddWithLoopback setup |  |
| 1597 | `PM_MulticastIGMPPacketsReceived` | Performance Monitoring MulticastIGMPPacketsReceived setup |  |
| 1598 | `PM_MulticastIPPacketsReceived` | Performance Monitoring MulticastIPPacketsReceived setup |  |
| 1599 | `PM_MulticastRegisteredChannels` | Performance Monitoring MulticastRegisteredChannels setup |  |
| 1600 | `PM_MulticastUDPPacketsReceived` | Performance Monitoring MulticastUDPPacketsReceived setup |  |
| 1601 | `PM_MulticastUDPPacketsRejected` | Performance Monitoring MulticastUDPPacketsRejected setup |  |
| 1602 | `PM_NFSAbortDueToMaxRetriesExceeded` | Performance Monitoring NFSAbortDueToMaxRetriesExceeded setup |  |
| 1603 | `PM_NFSBytesDroppedOnRecord` | Performance Monitoring NFSBytesDroppedOnRecord setup |  |
| 1604 | `PM_NFSCreateCalls` | Performance Monitoring NFSCreateCalls setup |  |
| 1605 | `PM_NFSCurrentRequests` | Performance Monitoring NFSCurrentRequests setup |  |
| 1606 | `PM_NFSDelayedResponses` | Performance Monitoring NFSDelayedResponses setup |  |
| 1607 | `PM_NFSLookupCalls` | Performance Monitoring NFSLookupCalls setup |  |
| 1608 | `PM_NFSReadCalls` | Performance Monitoring NFSReadCalls setup |  |
| 1609 | `PM_NFSRequests` | Performance Monitoring NFSRequests setup |  |
| 1610 | `PM_NFSRetries` | Performance Monitoring NFSRetries setup |  |
| 1611 | `PM_NFSRoundTripTimeMs` | Performance Monitoring NFSRoundTripTimeMs setup |  |
| 1612 | `PM_NFSWriteCalls` | Performance Monitoring NFSWriteCalls setup |  |
| 1613 | `PM_NetConnectionState` | Performance Monitoring NetConnectionState setup |  |
| 1614 | `PM_NetUnknownUDPPortCounter` | Performance Monitoring NetUnknownUDPPortCounter setup |  |
| 1615 | `PM_NetUtilDiscardedPackets` | Performance Monitoring NetUtilDiscardedPackets setup |  |
| 1616 | `PM_NetUtilKBytes` | Performance Monitoring NetUtilKBytes setup |  |
| 1617 | `PM_NetUtilPackets` | Performance Monitoring NetUtilPackets setup |  |
| 1618 | `PM_RTPBytesRx` | Performance Monitoring RTPBytesRx setup |  |
| 1619 | `PM_RTPBytesTx` | Performance Monitoring RTPBytesTx setup |  |
| 1620 | `PM_RTPModulePacketsRx` | Performance Monitoring RTPModulePacketsRx setup |  |
| 1621 | `PM_RTPModulePacketsTx` | Performance Monitoring RTPModulePacketsTx setup |  |
| 1622 | `PM_RTPPacketLossRx` | Performance Monitoring RTPPacketLossRx setup |  |
| 1623 | `PM_RTPPacketLossTx` | Performance Monitoring RTPPacketLossTx setup |  |
| 1624 | `PM_RTPPacketsRx` | Performance Monitoring RTPPacketsRx setup |  |
| 1625 | `PM_RTPPacketsTx` | Performance Monitoring RTPPacketsTx setup |  |
| 1626 | `PM_RTPRealmBytesRx` | Performance Monitoring RTPRealmBytesRx setup |  |
| 1627 | `PM_RTPRealmBytesTx` | Performance Monitoring RTPRealmBytesTx setup |  |
| 1628 | `PM_RTPRealmPacketLossRx` | Performance Monitoring RTPRealmPacketLossRx setup |  |
| 1629 | `PM_RTPRealmPacketLossTx` | Performance Monitoring RTPRealmPacketLossTx setup |  |
| 1630 | `PM_RTPRealmPacketsRx` | Performance Monitoring RTPRealmPacketsRx setup |  |
| 1631 | `PM_RTPRealmPacketsTx` | Performance Monitoring RTPRealmPacketsTx setup |  |
| 1632 | `PM_RealmMOS` | Performance Monitoring RealmMOS setup |  |
| 1633 | `PM_RobustDiscardCounter` | Performance Monitoring RobustDiscardCounter setup |  |
| 1634 | `PM_SCTPRcvBytesLastSecond` | Performance Monitoring SCTPRcvBytesLastSecond setup |  |
| 1635 | `PM_SCTPRetransAttemptsNum` | Performance Monitoring SCTPRetransAttemptsNum setup |  |
| 1636 | `PM_SCTPRetransBytesNum` | Performance Monitoring SCTPRetransBytesNum setup |  |
| 1637 | `PM_SCTPSentBytesLastSecond` | Performance Monitoring SCTPSentBytesLastSecond setup |  |
| 1638 | `PM_StreamingCacheHitRate` | Performance Monitoring StreamingCacheHitRate setup |  |
| 1639 | `PM_StreamingCacheMissRate` | Performance Monitoring StreamingCacheMissRate setup |  |
| 1640 | `PM_StreamingCacheServerRequestsRate` | Performance Monitoring StreamingCacheServerRequestsRate setup |  |
| 1641 | `PM_TT` | Performance Monitoring TT setup |  |
| 1642 | `PM_TTDuration` | Performance Monitoring TTDuration setup |  |
| 1643 | `PM_TTInProgress` | Performance Monitoring TTInProgress setup |  |
| 1644 | `PM_TrunkActivitySeconds` | Performance Monitoring TrunkActivitySeconds setup |  |
| 1645 | `PM_TrunkUtilization` | Performance Monitoring TrunkUtilization setup |  |
| 1646 | `PM_VEChannelsPerCoder` | Performance Monitoring VEChannelsPerCoder setup |  |
| 1647 | `PM_VEDSPUtil` | Performance Monitoring VEDSPUtil setup |  |
| 1648 | `PM_VEPacketDelay` | Performance Monitoring VEPacketDelay setup |  |
| 1649 | `PM_VEPacketJitter` | Performance Monitoring VEPacketJitter setup |  |
| 1650 | `PM_VERealmPacketDelay` | Performance Monitoring VERealmPacketDelay setup |  |
| 1651 | `PM_VERealmPacketJitter` | Performance Monitoring VERealmPacketJitter setup |  |
| 1652 | `PM_VoipCPUUtilize` | Performance Monitoring VoipCPUUtilize setup |  |
| 1653 | `PM_WAN_RXDiscardPackets` | Performance Monitoring WAN_RXDiscardPackets setup |  |
| 1654 | `PM_WAN_RXErrors` | Performance Monitoring WAN_RXErrors setup |  |
| 1655 | `PM_WAN_RXMultiCastPackets` | Performance Monitoring WAN_RXMultiCastPackets setup |  |
| 1656 | `PM_WAN_RXOctets` | Performance Monitoring WAN_RXOctets setup |  |
| 1657 | `PM_WAN_RXPackets` | Performance Monitoring WAN_RXPackets setup |  |
| 1658 | `PM_WAN_TXDroppedPackets` | Performance Monitoring WAN_TXDroppedPackets setup |  |
| 1659 | `PM_WAN_TXErrors` | Performance Monitoring WAN_TXErrors setup |  |
| 1660 | `PM_WAN_TXOctets` | Performance Monitoring WAN_TXOctets setup |  |
| 1661 | `PM_WAN_TXPackets` | Performance Monitoring WAN_TXPackets setup |  |
| 1662 | `PM_analogActiveLines` | Performance Monitoring analogActiveLines setup |  |
| 1663 | `PM_dhcpRequestCounter` | Performance Monitoring dhcpRequestCounter setup |  |
| 1664 | `PM_dhcpResponseTime` | Performance Monitoring dhcpResponseTime setup |  |
| 1665 | `PM_dnsResponseTime` | Performance Monitoring dnsResponseTime setup |  |
| 1666 | `PM_gwAttemptedCalls` | Performance Monitoring gwAttemptedCalls setup |  |
| 1667 | `PM_gwBusyCalls` | Performance Monitoring gwBusyCalls setup |  |
| 1668 | `PM_gwCallDuration` | Performance Monitoring gwCallDuration setup |  |
| 1669 | `PM_gwDialogs` | Performance Monitoring gwDialogs setup |  |
| 1670 | `PM_gwEstablishedCalls` | Performance Monitoring gwEstablishedCalls setup |  |
| 1671 | `PM_gwFailCalls` | Performance Monitoring gwFailCalls setup |  |
| 1672 | `PM_gwFaxAttemptedCalls` | Performance Monitoring gwFaxAttemptedCalls setup |  |
| 1673 | `PM_gwFaxSuccessCalls` | Performance Monitoring gwFaxSuccessCalls setup |  |
| 1674 | `PM_gwForwardedCalls` | Performance Monitoring gwForwardedCalls setup |  |
| 1675 | `PM_gwINVITEDialogs` | Performance Monitoring gwINVITEDialogs setup |  |
| 1676 | `PM_gwIP2TelTrunkEstablishedCalls` | Performance Monitoring gwIP2TelTrunkEstablishedCalls setup |  |
| 1677 | `PM_gwIP2TelTrunkGroupEstablishedCalls` | Performance Monitoring gwIP2TelTrunkGroupEstablishedCalls setup |  |
| 1678 | `PM_gwIPGroupDialogs` | Performance Monitoring gwIPGroupDialogs setup |  |
| 1679 | `PM_gwIPGroupINVITEDialogs` | Performance Monitoring gwIPGroupINVITEDialogs setup |  |
| 1680 | `PM_gwIPGroupInDialogs` | Performance Monitoring gwIPGroupInDialogs setup |  |
| 1681 | `PM_gwIPGroupInINVITEDialogs` | Performance Monitoring gwIPGroupInINVITEDialogs setup |  |
| 1682 | `PM_gwIPGroupInOtherDialogs` | Performance Monitoring gwIPGroupInOtherDialogs setup |  |
| 1683 | `PM_gwIPGroupInSUBSCRIBEDialogs` | Performance Monitoring gwIPGroupInSUBSCRIBEDialogs setup |  |
| 1684 | `PM_gwIPGroupOtherDialogs` | Performance Monitoring gwIPGroupOtherDialogs setup |  |
| 1685 | `PM_gwIPGroupOutDialogs` | Performance Monitoring gwIPGroupOutDialogs setup |  |
| 1686 | `PM_gwIPGroupOutINVITEDialogs` | Performance Monitoring gwIPGroupOutINVITEDialogs setup |  |
| 1687 | `PM_gwIPGroupOutOtherDialogs` | Performance Monitoring gwIPGroupOutOtherDialogs setup |  |
| 1688 | `PM_gwIPGroupOutSUBSCRIBEDialogs` | Performance Monitoring gwIPGroupOutSUBSCRIBEDialogs setup |  |
| 1689 | `PM_gwIPGroupSUBSCRIBEDialogs` | Performance Monitoring gwIPGroupSUBSCRIBEDialogs setup |  |
| 1690 | `PM_gwInDialogs` | Performance Monitoring gwInDialogs setup |  |
| 1691 | `PM_gwInINVITEDialogs` | Performance Monitoring gwInINVITEDialogs setup |  |
| 1692 | `PM_gwInOtherDialogs` | Performance Monitoring gwInOtherDialogs setup |  |
| 1693 | `PM_gwInSUBSCRIBEDialogs` | Performance Monitoring gwInSUBSCRIBEDialogs setup |  |
| 1694 | `PM_gwNoAnswerCalls` | Performance Monitoring gwNoAnswerCalls setup |  |
| 1695 | `PM_gwNoMatchCalls` | Performance Monitoring gwNoMatchCalls setup |  |
| 1696 | `PM_gwNoResourcesCalls` | Performance Monitoring gwNoResourcesCalls setup |  |
| 1697 | `PM_gwNoRouteCalls` | Performance Monitoring gwNoRouteCalls setup |  |
| 1698 | `PM_gwOtherDialogs` | Performance Monitoring gwOtherDialogs setup |  |
| 1699 | `PM_gwOutDialogs` | Performance Monitoring gwOutDialogs setup |  |
| 1700 | `PM_gwOutINVITEDialogs` | Performance Monitoring gwOutINVITEDialogs setup |  |
| 1701 | `PM_gwOutOtherDialogs` | Performance Monitoring gwOutOtherDialogs setup |  |
| 1702 | `PM_gwOutSUBSCRIBEDialogs` | Performance Monitoring gwOutSUBSCRIBEDialogs setup |  |
| 1703 | `PM_gwSRDDialogs` | Performance Monitoring gwSRDDialogs setup |  |
| 1704 | `PM_gwSRDINVITEDialogs` | Performance Monitoring gwSRDINVITEDialogs setup |  |
| 1705 | `PM_gwSRDInDialogs` | Performance Monitoring gwSRDInDialogs setup |  |
| 1706 | `PM_gwSRDInINVITEDialogs` | Performance Monitoring gwSRDInINVITEDialogs setup |  |
| 1707 | `PM_gwSRDInOtherDialogs` | Performance Monitoring gwSRDInOtherDialogs setup |  |
| 1708 | `PM_gwSRDInSUBSCRIBEDialogs` | Performance Monitoring gwSRDInSUBSCRIBEDialogs setup |  |
| 1709 | `PM_gwSRDOtherDialogs` | Performance Monitoring gwSRDOtherDialogs setup |  |
| 1710 | `PM_gwSRDOutDialogs` | Performance Monitoring gwSRDOutDialogs setup |  |
| 1711 | `PM_gwSRDOutINVITEDialogs` | Performance Monitoring gwSRDOutINVITEDialogs setup |  |
| 1712 | `PM_gwSRDOutOtherDialogs` | Performance Monitoring gwSRDOutOtherDialogs setup |  |
| 1713 | `PM_gwSRDOutSUBSCRIBEDialogs` | Performance Monitoring gwSRDOutSUBSCRIBEDialogs setup |  |
| 1714 | `PM_gwSRDSUBSCRIBEDialogs` | Performance Monitoring gwSRDSUBSCRIBEDialogs setup |  |
| 1715 | `PM_gwSUBSCRIBEDialogs` | Performance Monitoring gwSUBSCRIBEDialogs setup |  |
| 1716 | `PM_gwTel2IPTrunkEstablishedCalls` | Performance Monitoring gwTel2IPTrunkEstablishedCalls setup |  |
| 1717 | `PM_gwTel2IPTrunkGroupEstablishedCalls` | Performance Monitoring gwTel2IPTrunkGroupEstablishedCalls setup |  |
| 1718 | `PM_stunDiscoveryCounter` | Performance Monitoring stunDiscoveryCounter setup |  |
| 1719 | `PM_stunQueryCounter` | Performance Monitoring stunQueryCounter setup |  |
| 1720 | `PM_stunResponseTime` | Performance Monitoring stunResponseTime setup |  |
| 1721 | `PM_stunRetransmissionCounter` | Performance Monitoring stunRetransmissionCounter setup |  |
| 1722 | `PM_veActiveFaxChannels` | Performance Monitoring veActiveFaxChannels setup |  |
| 1723 | `PM_veActiveModemChannels` | Performance Monitoring veActiveModemChannels setup |  |
| 1724 | `PM_veActiveModemRelayChannels` | Performance Monitoring veActiveModemRelayChannels setup |  |
| 1725 | `PM_veActiveRTPStreams` | Performance Monitoring veActiveRTPStreams setup |  |
| 1726 | `PM_veActiveSRTPStreams` | Performance Monitoring veActiveSRTPStreams setup |  |
| 1727 | `PM_veActiveTDM2IPChannels` | Performance Monitoring veActiveTDM2IPChannels setup |  |
| 1728 | `PM_veModemRelaySessionRejections` | Performance Monitoring veModemRelaySessionRejections setup |  |
| 1729 | `PM_veModemRelaySessionRequests` | Performance Monitoring veModemRelaySessionRequests setup |  |
| 1730 | `PM_veModulePacketDelay` | Performance Monitoring veModulePacketDelay setup |  |
| 1731 | `PM_veModulePacketJitter` | Performance Monitoring veModulePacketJitter setup |  |
| 1732 | `PM_veModuleRTPBytesRx` | Performance Monitoring veModuleRTPBytesRx setup |  |
| 1733 | `PM_veModuleRTPBytesTx` | Performance Monitoring veModuleRTPBytesTx setup |  |
| 1734 | `PM_veModuleRTPPacketLossRx` | Performance Monitoring veModuleRTPPacketLossRx setup |  |
| 1735 | `PM_veModuleRTPPacketLossTx` | Performance Monitoring veModuleRTPPacketLossTx setup |  |
| 1736 | `PM_veModuleRtcpXrRFactor` | Performance Monitoring veModuleRtcpXrRFactor setup |  |
| 1737 | `POCMAXNUMOFPARTICIPANTS` | Set the maximum participant in poc sessions on board |  |
| 1738 | `POCPartHndl` | BusyHourCallAttempts - Displays The current busy-hour call attempts |  |
| 1739 | `PORTPOOL` | New debug levels: %s |  |
| 1740 | `POST` | Accept: audio/wav, audio/basic |  |
| 1741 | `PPP_NO` | MRU: %s |  |
| 1742 | `PPPoE` | Multiple %s detected on Port %d. Switch to Destination Stream IP: %s, Source Port: %d. Left Stream IP: %s, Source Por... |  |
| 1743 | `PPPoELcpEchoEnable` | This parameter is used to enable or disable PPPoE disconnection auto-detection.{@} |  |
| 1744 | `PPPoEPassword` | Password for PAP or Secret for CHAP authentication. |  |
| 1745 | `PPPoERecoverDfgwAddress` | Default GW address to use when booting from the flash to non-PPPoE environment. |  |
| 1746 | `PPPoERecoverIPAddress` | IP address to use when booting from the flash to non-PPPoE environment. |  |
| 1747 | `PPPoERecoverSubnetMask` | Subnet Mask to use when booting from the flash to non-PPPoE environment. |  |
| 1748 | `PPPoEServerName` | Server Name for CHAP authentication. |  |
| 1749 | `PPPoEStaticIPAddress` | IP address to use in static configuration setup. |  |
| 1750 | `PPPoEUserName` | User Name for PAP or Host Name for CHAP authentication. |  |
| 1751 | `PRACKMODE` | PRACK mechanism mode for 1XX reliable responses: 0- Disabled , 1- Supported , 2- Required | Disable /0,Supported /1,Required /2 |
| 1752 | `PRECEDENCERINGINGTYPE` | Precedence Ringing Type |  |
| 1753 | `PREFERQ931CALLINGNUMBER` | Relevant only to H323.{@}if PreferQ931CallingNumber=1, the calling number of the  Q931 part of Setup message [if exis... |  |
| 1754 | `PREFERROUTETABLE` | Prefer Routing Table |  |
| 1755 | `PREFIX` | Max Message Length |  |
| 1756 | `PREFIX2EXTLINE` | Prefix to dial for external line |  |
| 1757 | `PREFIX2REDIRECTNUMBER` | Prefix which added to Redirect phone number |  |
| 1758 | `PREMIUMSERVICECLASSCONTROLDIFFSERV` | Sets the DiffServ for the Premium service class content and control traffic. |  |
| 1759 | `PREMIUMSERVICECLASSMEDIADIFFSERV` | Sets the DiffServ for Premium service class content and media traffic. |  |
| 1760 | `PRIMARYMEDIAINTERFACE` | Primary media interface to be used within SDP |  |
| 1761 | `PRINTSTATE` | Invalid PrintState value %d |  |
| 1762 | `PROGRESSINDICATOR2IP` | Determine whether to send the Progress Indicator to IP | Not Configured /-1,No PI /0,PI = 1 /1,PI = 8 /8 |
| 1763 | `PROGRESSINDICATOR2ISDN` | Override the value of progress indicator to ISDN side in ALERT PROGRESS and PROCEEDING messages |  |
| 1764 | `PROXYDNSQUERYTYPE` | Proxy DNS Query Type | A-Record /0,SRV /1,NAPTR /2 |
| 1765 | `PROXYHOTSWAPRTX` | Number of Rtx before Hotswap is performed |  |
| 1766 | `PROXYIPLISTREFRESHTIME` | Time interval between refresh of proxies list (seconds). For example SRV query will be done every ProxyIPListRefreshT... |  |
| 1767 | `PROXYKEEPALIVETIME` | Time interval between Proxy Keep-Alive messages (seconds) |  |
| 1768 | `PROXYLOADBALANCINGMETHOD` | Method of the proxies load balancing:{@}0 - Disabled (default){@}1 - RoundRobin{@}2 - Random SRV Weights | Disable /0,Round Robin /1,Random Weights /2 |
| 1769 | `PROXYNAME` | SIP Proxy name |  |
| 1770 | `PROXYREDUNDANCYMODE` | Redundancy Mode - Parking on active proxy or switching to main Proxy whenever online | Parking /0,Homing /1 |
| 1771 | `PSMODE` | VoIP Only |  |
| 1772 | `PSTNALERTTIMEOUT` | Max time (in seconds) to wait for connect from PSTN |  |
| 1773 | `PSTNSS7Options` | Container parameter for SS7 Internal Options. |  |
| 1774 | `PTIME` | Illegal ptime value |  |
| 1775 | `PUBLICATIONIPGROUPID` | IPGroup ID for publication purposes |  |
| 1776 | `PUBLISH` | UA Preemption |  |
| 1777 | `Party` | SIPStackSession::FillBCTPartyParams - Empty or illegal party "%s" for CALEA |  |
| 1778 | `Password` | User name already exists. |  |
| 1779 | `PatchFileName` | Indicates the name and location of the Patch file. |  |
| 1780 | `PayloadType` | Payload Type | Not Configured /-1,Disable /0,Enable /1,Enable No-Adaptation /2 |
| 1781 | `Phone` | The Entered Phone# doesn't exist: %s |  |
| 1782 | `PhoneNumber` | PrepareInfoEmptyPSTNTunnelingData: role of INFO is unknown |  |
| 1783 | `PhysTermNamePattern` | Defines the name pattern of a physical termination |  |
| 1784 | `PlayDTMFduringHold` | Enable/Disable Playing DTMF to TEL during hold |  |
| 1785 | `PlayRbToTelco` | By Dest Phone Number |  |
| 1786 | `Polarity` | Tel. Code |  |
| 1787 | `PolarityReversalType` | Type of polarity reversal signal used for network far-end answer and disconnect indications. | hard/1,soft/0 |
| 1788 | `Port1` | Port 1 |  |
| 1789 | `Port1BSpeed` | Ethernet Group 2 (Default: OAM) |  |
| 1790 | `Port2` | Port 2 |  |
| 1791 | `Port2BSpeed` | Gigabit Ethernet Group (Default: Media) | /EthernetPortInfo@50,100,0 |
| 1792 | `Port2Speed` | Ethernet Group 1 (Default: Control) |  |
| 1793 | `Port3` | Port 3 |  |
| 1794 | `PortPool` | Command has %s. |  |
| 1795 | `PortType` | Port Type | Not Configured /-1,FXO /0,FXS /1,E-M /2 |
| 1796 | `PreemptionToneDuration` | Preemption Tone Duration |  |
| 1797 | `Preference` | Restiction and Preference |  |
| 1798 | `PrerecordedTonesFileName` | Defines the name (and path) of the file containing the Prerecorded Tones. |  |
| 1799 | `PressLogOff` | 303 See Other |  |
| 1800 | `PrintHATree` | CPool::CPool - Allocation Exception |  |
| 1801 | `PrintJSbuff` | Display the current web access level |  |
| 1802 | `PrintNavigationTree` | Print all Board's pages' Paths |  |
| 1803 | `PrintPagesPath` | Print JS' buffer tree |  |
| 1804 | `Priority1` | Priority 1 |  |
| 1805 | `Priority2` | Priority 2 |  |
| 1806 | `Priority3` | Priority 3 |  |
| 1807 | `Private` | Send::CallerID Name=%s, Number=%s |  |
| 1808 | `ProIsFaxUsed` | No Fax |  |
| 1809 | `Proceeding` | SIPCallProceedingState::Disconnect failed setup transaction is NULL |  |
| 1810 | `ProfilePlayRBTone2IP` | Don't Play |  |
| 1811 | `ProgIndicToIP` | No PI |  |
| 1812 | `ProtocolType` | Sets the PSTN protocol to be used for this trunk. |  |
| 1813 | `ProvisionedCallAgents` | Defines list of call agent IP addresses. |  |
| 1814 | `ProvisionedCallAgentsPorts` | Defines UDP Ports for each Call Agent defined by  'ProvisionedCallAgents' parameter. |  |
| 1815 | `ProxyKeepAliveTime` | Proxy Keep Alive Time |  |
| 1816 | `ProxyLoadBalancingMethod` | Proxy Load Balancing Method | Disable /0,Round Robin /1,Random Weights /2 |
| 1817 | `ProxySetId` | IpProfileId (name) |  |
| 1818 | `PrtFileUrl` | Provides a link to to a prerecorded tones dat file, to be downloaded from a remote server. |  |
| 1819 | `PrvFullMtch` | No match |  |
| 1820 | `PstnTermReason` | VQString is not a valid data type for unknown key %d |  |
| 1821 | `PulseDialGenerationBreakTime` | Determines the time of Break in case of analog pulse dial generation. |  |
| 1822 | `PulseDialGenerationInterDigitTime` | Determines the Interdigit time in case of analog pulse dial generation. |  |
| 1823 | `PulseDialGenerationMakeTime` | Determines the time of Make in case of analog pulse dial generation. |  |
| 1824 | `PulseInterval1` | Pulse Interval 1 |  |
| 1825 | `PulseInterval2` | Pulse Interval 2 |  |
| 1826 | `PulseInterval3` | Pulse Interval 3 |  |
| 1827 | `PulseInterval4` | Pulse Interval 4 |  |
| 1828 | `PulsesOnAnswer1` | Pulses On Answer 1 |  |
| 1829 | `PulsesOnAnswer2` | Pulses On Answer 2 |  |
| 1830 | `PulsesOnAnswer3` | Pulses On Answer 3 |  |
| 1831 | `PulsesOnAnswer4` | Pulses On Answer 4 |  |
| 1832 | `PwAgeUnit` | Sets the password age unit. Either "Days" or "Min" |  |
| 1833 | `QCELP13Rate` | Configure the QCELP13 coder bit rate. |  |
| 1834 | `QCELP8Rate` | Configures the QCELP8  coder bit rate. |  |
| 1835 | `QOEConnectionMode` | Defines whether the module will connect to the VQMS (client) or receive connection from the server (server) | Server/0,Client/1,None/2 |
| 1836 | `QOEInformationLevel` | Defines the quantity of VQ information sent to the server | Standard/0,Enhanced/1,Debug/2 |
| 1837 | `QOEInterfaceName` | The interface to wait on in case of server (default is the default control interface) |  |
| 1838 | `QOEPort` | QOE server port number (default is 5000) |  |
| 1839 | `QOESendBufferSize` | Defines the sending buffer size of the socket |  |
| 1840 | `QOEServerIp` | In case VQM is at client configuration, this parameter defines the server IP address |  |
| 1841 | `QOEUseMosLQ` | If it is enabled the MOS LQ will be used by the board to calculate the mos status instead of the MOS CQ |  |
| 1842 | `QOSSTATISTICS` | Whether or not add statistics to call release |  |
| 1843 | `QSIGCALLTRANSFERREVERSEENDDESIGNATION` | Qsig CallTransfer Reverse EndDesignation |  |
| 1844 | `QSIGPATHREPLACEMENTMODE` | 0 - Enable IP to QSIG transfer,1 - Enable QSIG to IP Transfer | IP2QSIGTransfer/0,QSIG2IPTransfer/1 |
| 1845 | `QSIGTUNNELINGMODE` | QSIG Tunneling Mode | ASCII /0,HEX /1 |
| 1846 | `QUICK_QM3_COMMIT` | State: %s |  |
| 1847 | `QcelpCoderHeaderFormat` | Determines whether to define a separate header format for the QCELP coder (different to the header format of the EVRC... | Parameter_Is_Not_Used/-1 ,Including_RFC2658Interleaving_And_TOC/1,Including_TOC_Only/2 |
| 1848 | `QualityFac` | PCIIFChangeChannelParams(): Enabling AGC will be ignored due to blocking by feature key or by startup configuration |  |
| 1849 | `QuarantineModeState` | Sets the default quarantine handling state |  |
| 1850 | `QueryLightConference` | Query Light Conference failure - Illegal Conference handle |  |
| 1851 | `R1DetectionStandard` | This parameter determines which one of the R1 MF protocol flavors will be used for detection. | ITU /0,R1.5 /1 |
| 1852 | `R2CATEGORY` | MFC/R2 Calling Party's category |  |
| 1853 | `RADDEBLEVEL` | RadVision package debug level |  |
| 1854 | `RADIUSACCOUNTINGTYPE` | When will Radius Acounting messages be sent | At Call Release /0,At Connect & Release /1,At Setup & Release /2 |
| 1855 | `RADIUSACCPort` | Radius accounting port. |  |
| 1856 | `RADIUSACCServerIP` | Radius accounting server IP |  |
| 1857 | `RADIUSAuthPort` | RADIUS authentication port. |  |
| 1858 | `RADIUSAuthServerIP` | RADIUS authentication server IP |  |
| 1859 | `RADIUSDoubleDecodeURL` | Enable an additional decoding of authentication credentials that were sent to the RADIUS server via URL. |  |
| 1860 | `RADIUSRetransmission` | Radius packets retransmission |  |
| 1861 | `RADIUSTo` | Radius Response Time Out |  |
| 1862 | `RADLOGMODULES` | RadVision active modules for printout |  |
| 1863 | `RADLOGOUTPUT` | RadVision output type |  |
| 1864 | `RAIHIGHTHRESHOLD` | Percentage of active calls in order to send 'Almost out of resources' RAI |  |
| 1865 | `RAILOOPTIME` | Time period to check call resources (seconds) |  |
| 1866 | `RAITR` | Add PSTN Signaling Trace Usage |  |
| 1867 | `RASDESTPORT` | RAS requests destination port |  |
| 1868 | `RASSOURCEPORT` | RAS requests source port |  |
| 1869 | `RBABROKENCONNECTIONCMDSET` | The set of commands to execute when the network connection fails. |  |
| 1870 | `RBACONNECTIONESTCMDSET` | The set of commands to execute when the network connection is re-established. |  |
| 1871 | `RBADEBUGMODE` | Sets the debug Level of the RBA service |  |
| 1872 | `RBAENABLE` | Enables the RBA service. | disable/0,enable/1 |
| 1873 | `RBAINTERFACENAME` | The interface name for the RBA SSH connection |  |
| 1874 | `RBAPASSWORD` | The password for the RBA SSH connection |  |
| 1875 | `RBASERVERADDR` | The address of the RBA server. |  |
| 1876 | `RBASERVERPORT` | The port for the SSH connection,needed for the RBA. |  |
| 1877 | `RBATRACKID` | The track id for the RBA connection changes |  |
| 1878 | `RBATRANKSDISCONNECTIONOPTIONS` | Determines wether the connection is disconnected when ALL the tracks are down or where any of the connection is down. | all/0,any/1 |
| 1879 | `RBAUSERNAME` | The user name for the RBA connection |  |
| 1880 | `RD_BUSY` | This option is restricted |  |
| 1881 | `RECEIVE` | Receive Fail. error=%d bytesReceived=%d |  |
| 1882 | `RECORDSCRIPTPATH` | Identification of HTTP Record Script (To be used by FOR RECORD) |  |
| 1883 | `RECORDTOID` | Identification of voice stream recording location (To be used by SIP INVITE) |  |
| 1884 | `RECORDURITYPE` | Type of Default record URI used by Media Ctrl |  |
| 1885 | `REDUNDANTROUTINGMODE` | Mode of redundant routing. 0 - Disabled, 1 - Use routing table, 2 - Use proxies list | Disable /0,Routing Table /1,Proxy /2 |
| 1886 | `REDUNDANTSASPROXYSET` | Proxy Set Id for Redundant SAS |  |
| 1887 | `REGISTERONINVITEFAILURE` | Enable ReRegister upon INVITE transaction failure |  |
| 1888 | `REGISTRARIP` | SIP Registrar IP address |  |
| 1889 | `REGISTRARNAME` | SIP Registrar name |  |
| 1890 | `REGISTRARTRANSPORTTYPE` | Registrar transport type | Not Configured /-1,UDP /0,TCP /1,TLS /2 |
| 1891 | `REGISTRATIONRETRYTIME` | Time in which the gateway will try to register after last registration failure (seconds) |  |
| 1892 | `REGISTRATIONTIME` | Time for which registration to Gatekeeper/Proxy is valid. Causes periodic registration (seconds) |  |
| 1893 | `REGISTRATIONTIMEDIVIDER` | Percentage of RegistrationTime when the actual new REGISTER request will be sent out |  |
| 1894 | `REGISTRATIONTIMETHRESHOLD` | If (REGISTRATIONTIMETHRESHOLD > 0) and (REGISTRATIONTIMETHRESHOLD < computed registration time using existing logic) ... |  |
| 1895 | `REGRETTIME` | Time to wait between phone hang up and call termination |  |
| 1896 | `REJECTCANCELAFTERCONNECT` | Defines whether or not reject Cancel request after connect |  |
| 1897 | `REJECTED` | Illegal IPBCP value |  |
| 1898 | `RELEASECAUSEMAPPINGFORMAT` | Defines the Release cause mapping format whether according RFC3398 or ITU Q.1912.5 | RFC3398 Format /0,ITUQ1912.5 Format/1 |
| 1899 | `RELEASED` | The waiting for connections are on released. |  |
| 1900 | `RELEASEIP2ISDNCALLONPROGRESSWITHCAUSE` | Defines whether to disconnect call while receiving ISDN PROGRESS with Cause 0 -never, 1- disconnect if not Early medi... | Don't Release /0,Release if Not Early Media /1,Always Release /2 |
| 1901 | `REMOTE` | Call::ManualDisconnect Ignore: not allowed during ISDNTRANSFER (%d) |  |
| 1902 | `REMOTEBASEUDPPORT` | Remote Base UDP Port For Aggrigation |  |
| 1903 | `REMOTEX` | Invalid report type %s. |  |
| 1904 | `REMOVECALLINGNAME` | If set to 1 - Removes Calling Name  from IP->TEL calls |  |
| 1905 | `REMOVECLIWHENRESTRICTED` | Removes CLI from IP->TEL calls if received CLI is restricted |  |
| 1906 | `REMOVEPREFIX` | Remove prefix defined in IP to Trunk Group table (IP to Tel calls) |  |
| 1907 | `REMOVETOTAGINFAILURERESPONSE` | Remove to-tag in final reject response for setup INVITE transaction |  |
| 1908 | `REPLACECALLINGWITHREDIRECTNUMBER` | Replace Calling Number With Redirect Number ISDN 2 IP | Disable /0,Replace Number&Name /1,Replace Number only /2 |
| 1909 | `REPLACEEMPTYDSTWITHPORTNUMBER` | Replace empty destination number (received from Tel side) with port number |  |
| 1910 | `REPLACENUMBERSIGNWITHESCAPECHAR` | Replace the number sign (#) with the escape character %23 in outgoing SIP messages |  |
| 1911 | `REPLACETEL2IPCALLINGNUMTIMEOUT` | Maximum Time to wait between call setup and Facility with Redirecting Number for replacing calling number(msec) |  |
| 1912 | `REREGISTERONCONNECTIONFAILURE` | Enables GW to perform Re-Registeration on TCP/TLS connection failure |  |
| 1913 | `RESET` | Max Board Events and Max Stack Events were reset. prev value: %d  %d |  |
| 1914 | `RESETASSOCIATION` | ResetAssocaition Success. Now you can create another Association |  |
| 1915 | `RESETENDPOINT` | ResetEndpoint Success. Now you can create another Endpoint |  |
| 1916 | `RESETSRTPSTATEUPONREKEY` | Reset SRTP State Upon Re-key |  |
| 1917 | `RESETWEBPASSWORD` | Resets the web pasword and user name to 'Admin'. 1 - reset, 0 - don't reset |  |
| 1918 | `RESET_NOW` | The RESET_NOW option is restricted |  |
| 1919 | `RESPONSETIMEOUT` | Time in which the gateway waits for a RAS response from the Gatekeeper before retransmission (seconds) |  |
| 1920 | `RETRYAFTERTIME` | Retry After time for the proxy to be in state Unavailable |  |
| 1921 | `RFC2198PayloadType` | Sets the RTP Redundency packet's Payload Type field. |  |
| 1922 | `RFC2833RxPayloadType` | Received RFC 4733 Telephony Events Payload type. |  |
| 1923 | `RFC2833TxPayloadType` | Transmitted RFC 4733 Telephony Events Payload type. |  |
| 1924 | `RFSS` | RfsService: processed %d expired timers |  |
| 1925 | `RFSTCP` | Error creating socket, error code : %d |  |
| 1926 | `RFSUDP` | Error creating socket, error code : %d |  |
| 1927 | `RINGSBEFORECALLERID` | Number of rings after which the Caller ID is detected | 0 /0,1 /1,2 /2 |
| 1928 | `RMHandleRetransmit` | Allocation request rejected internally: unknown BCC Id - V5InterfaceId %d, V5UserPortId %d. |  |
| 1929 | `RNGT` | No Ring Tones were loaded. |  |
| 1930 | `ROOT` | ROOT Info:  Status: %x TB: %x %x %x %x %x %x %x %x %x %x |  |
| 1931 | `ROUTEMODEIP2TEL` | Defines order between routing incoming calls from IP side and performing manipulations | Route calls before manipulation /0,Route calls after manipulation /1 |
| 1932 | `ROUTEMODETEL2IP` | Defines order between routing incoming calls from Tel side and performing manipulations |  |
| 1933 | `ROUTE_BEFORE_MAP` | Call::GetEndPoint- HandlePhoneNumberMapping For Dest Number <%s> error %s |  |
| 1934 | `RPREQUIRED` | Indicates whether or not Require header is able to contain  the resource-priority tag |  |
| 1935 | `RSIPOnNetworkDisconnection` | Determines whether or not to send an RSIP when LAN is re-connected. |  |
| 1936 | `RTCPDirectionControl` | Selects which RTCP directions are enabled. | RTCPTxRx/0,RTCPTxOnly/1,RCTPRxOnly/2,RTCPInactive/3 |
| 1937 | `RTCPEncryptionDisableRx` | On a secured RTP session, determines whether to enable Encryption on received RTCP packets. |  |
| 1938 | `RTCPEncryptionDisableTx` | On a secured RTP session, determines whether to disable Encryption on transmitted RTCP packets. |  |
| 1939 | `RTCPInterval` | Time interval between the adjacent RTCP report (in msec). |  |
| 1940 | `RTCPXRESCTRANSPORTTYPE` | RtcpXrEsc transport type |  |
| 1941 | `RTPAuthenticationDisableRx` | On a secured RTP session, determines whether to enable Authentication on received RTP packets |  |
| 1942 | `RTPAuthenticationDisableTx` | On a secured RTP session, determines whether to disable Authentication on transmitted RTP packets. | Active /0,Inactive /1 |
| 1943 | `RTPDirectionControl` | Selects which RTP directions are enabled. | RTPTxRx/0,RTPTxOnly/1,RTPRxOnly/2,RTPUnactive/3,RTPRxRFC2833Tx/4 |
| 1944 | `RTPEncryptionDisableRx` | On a secured RTP session, determines whether to disable Encryption on received RTP packets. |  |
| 1945 | `RTPEncryptionDisableTx` | On a secured RTP session, determines whether to disable Encryption on transmitted RTP packets. |  |
| 1946 | `RTPFD` | RTP full data/ |  |
| 1947 | `RTPFW` | RTP forwarding and mediation/ |  |
| 1948 | `RTPNOOPPAYLOADTYPE` | Defines the transmitted No Operation packets RTP Payload type. |  |
| 1949 | `RTPONLYMODE` | On RTP only mode their is no signalling protocol (for media parameters negotiation with the remote side). The channel... | Disable /0,Transmit & Receive /1,Transmit Only /2,Receive Only /3 |
| 1950 | `RTPPackingFactor` | Defines the number of DSP payloads for generating one RTP packet. |  |
| 1951 | `RTPRedundancyDepth` | Redundancy depth of RTP redundancy packets. |  |
| 1952 | `RTPSIDCoeffNum` | Determines the number of spectral coefficients added to an SID packet being sent according to RFC 3389. | 0/0,4/4,6/6,8/8,10/10 |
| 1953 | `RTP_BIT_Field_Size` | Defines the bit field size for each RTP termination name (for binary MEGACO). |  |
| 1954 | `RTP_Num` | Defines the starting number for each name's RTP termination level |  |
| 1955 | `RTSPCONNECTIONRETRYINTERVAL` | Time in seconds the system should wait before trying to create a socket to the RTSP Server, if the socket was never c... |  |
| 1956 | `RTSPENABLED` | Enable/disable the RTSP functionality. |  |
| 1957 | `RTSPMAXPORTS` | Indicates how many channels can be simultaneously active in RTSP sessions. {@} |  |
| 1958 | `RXDTMFOPTION` | Declare support for RFC 2833 in SDP | No /0,Yes /3 |
| 1959 | `RadiusAccLocalPort` | Radius access local port. |  |
| 1960 | `RadiusAuthLocalPort` | Radius authentication local port. |  |
| 1961 | `RadiusLocalCacheMode` | Defines the ability to reset the expiry of the local RADIUS password cache: |  |
| 1962 | `RadiusLocalCacheTimeout` | Defines expiry time [sec] of locally stored RADIUS password cache. |  |
| 1963 | `RadiusVSAAccessAttribute` | Defines 'Security Access Level' attribute code in VSA section of RADIUS packet that  device should relate to. |  |
| 1964 | `RadiusVSAVendorID` | Defines the vendor ID that the device should accept when parsing a RADIUS response packet. |  |
| 1965 | `RandomizeTransactionID` | Defines if transactions produced by  board start with a fixed or random number. |  |
| 1966 | `ReSetDevice` | Reset the device |  |
| 1967 | `Reason` | CList::CIterator Node = NULL |  |
| 1968 | `Receiving` | Receiving (Calls: %d) |  |
| 1969 | `RecordPort` | Apply New Settings | /DebugRecording@200,200,0 |
| 1970 | `RecordSrtpPingPackets` | Enable record RTP and RTCP ping packets |  |
| 1971 | `RedirectNumBeforeMap` | SrdId (name) |  |
| 1972 | `RedundancyMode` | Not Configured |  |
| 1973 | `RedundantAgentIP` | Defines the redundant MGCP up to 3,  call agent IP address for initial RSIP message. |  |
| 1974 | `RedundantAgentPort` | UDP Port of Redundant MGCP call agent |  |
| 1975 | `RedundantBoardIPAddress` | Defines the IP address of the redundant board, to which state DB packets are sent. |  |
| 1976 | `RedundantCallAgentDomainName` | Redundant MGCP Call Agent Domain name. |  |
| 1977 | `RedundantMode` | This parameter is used to enable the redundancy mechanism on redundant board. 1 = Activate, 0 = Deactivate. |  |
| 1978 | `ReferController` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 1979 | `RegistrationDBEntry` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 1980 | `RegistrationMode` | Registration Mode | Not Configured /255,Per Endpoint /0,Per Gateway /1,Don't Register /4,Per Account /5 |
| 1981 | `Relay` | Events Only |  |
| 1982 | `ReleaseCause` | Release Cause |  |
| 1983 | `ReleaseVirtualCIDs` | There are no Virtual Cids |  |
| 1984 | `ReliableTransportObject` | CPool::CPool - Allocation Exception |  |
| 1985 | `ReloadPKI` | Reload Pkeys,cert,root certs if available |  |
| 1986 | `RemoteAccepted` | SIPCallRemoteAcceptedState::HandleBye : No SetupTransaction exist! |  |
| 1987 | `RemoteResetControl` | Determine the remote reset action. 1 - burn staged load image, if any, and config to flash, perform a reset, and load... |  |
| 1988 | `RemoveAllIpTraceRules` | Remove All IP trace rules |  |
| 1989 | `RemoveCallingNameForTrunk` | Remove Calling Name ForTrunk. put (-1 ) to use the global parameter {@}RemoveCallingName. | Use Global /-1,Remove /1,Don't Remove /0 |
| 1990 | `RemoveFromLeft` | Remove From Left |  |
| 1991 | `RemoveFromRight` | Remove From Right |  |
| 1992 | `RemoveSystemTraceRule` | Remove System rule |  |
| 1993 | `RemoveTarget` | Remove a debug recording target |  |
| 1994 | `RemoveTraceRule` | Remove a trace |  |
| 1995 | `RemoveWebUsers` | Remove web users. Use index or "ALL" to remove all users |  |
| 1996 | `Replaces` | AcSIPCall::HandleRefer with Replaces |  |
| 1997 | `ReportCpuUtilizationPercent` | Defines the minimum CPU Utilization percent that starts sending to SYSLOG reports about CPU Utilization. |  |
| 1998 | `ReportNodeLockComplete` | CID %d connected to CID %d successfully GEN2/GEN3/GEN5, Mediation Level:%d | CID %d connected to CID %d unsuccessfully GEN2/GEN3/GEN5, Mediation Level:%d |
| 1999 | `RequestDownloadResponse` | RequestDownload failure. Got %s as response |  |
| 2000 | `RequestType` | Request Type | All/0,INVITE/1,REGISTER/2,SUBSCRIBE/3,INVITE and REGISTER/4,INVITE and SUBSCRIBE/5,OPTIONS/6 |
| 2001 | `RequireStrictCert` | Verifies the certification strictly - for SSL |  |
| 2002 | `Rerl` | Remote Rerl |  |
| 2003 | `ResetDevice` | Reset security device |  |
| 2004 | `ResetEchoCancellerAfterDtmfGeneration` | Defines if Echo Canceller should be reset after DTMF generation to TDM direction.  0 - Disable  1 - Enable |  |
| 2005 | `ResetNow` | Invokes an immediate restart of the gateway. This option can be used to activate offline (not on-the-fly) parameters ... |  |
| 2006 | `ResourceObj` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 2007 | `ResourceObjAudit` | ResourceObjAudit:: malloc failed!! |  |
| 2008 | `RestartMaximumWaitingDelay` | Defines the Maximum Waiting Delay before restart service change when the Media Gateway is powered on (in msec). |  |
| 2009 | `RfsRead` | RfsRead url len |  |
| 2010 | `RfsServiceDebugMode` | Determines whether to enable the streaming of RFS task debug messages. |  |
| 2011 | `RfsSesIdMap` | Unable to insert message on queue |  |
| 2012 | `RfsWrite` | RfsWrite url len POST/PUT postUrl |  |
| 2013 | `RfsWriteFile` | RfsWriteFile url len |  |
| 2014 | `RingDeglitch` | Time (in msec) to prevent detection of glitch/noise as a ring. |  |
| 2015 | `RingDetectMode` | Defines the Analog Ring Detection mode. |  |
| 2016 | `RingOffPeriod` | Defines the default ringing OFF period on analog lines. |  |
| 2017 | `RingOffPeriod0` | Defines the Distinctive Ringing #0 OFF period (in msec) on analog lines. |  |
| 2018 | `RingOffPeriod1` | Defines the Distinctive Ringing #1 OFF period (in msec) on analog lines. |  |
| 2019 | `RingOffPeriod2` | Defines the Distinctive Ringing #2 OFF period (in msec) on analog lines. |  |
| 2020 | `RingOffPeriod3` | Defines the Distinctive Ringing #3 OFF period (in msec) on analog lines. |  |
| 2021 | `RingOffPeriod4` | Defines the Distinctive Ringing #4 OFF period (in msec) on analog lines. |  |
| 2022 | `RingOffPeriod5` | Defines the Distinctive Ringing #5 OFF period (in msec) on analog lines. |  |
| 2023 | `RingOffPeriod6` | Defines the Distinctive Ringing #6 OFF period (in msec) on analog lines. |  |
| 2024 | `RingOffPeriod7` | Defines the Distinctive Ringing #7 OFF period (in msec) on analog lines. |  |
| 2025 | `RingOffTime` | Ring Off duration (between two On Rings). |  |
| 2026 | `RingOnPeriod` | Defines the default ringing ON period on analog lines. |  |
| 2027 | `RingOnPeriod0` | Defines the Distinctive Ringing #0 ON period (in msec) on analog lines. |  |
| 2028 | `RingOnPeriod1` | Defines the Distinctive Ringing #1 ON period (in msec) on analog lines. |  |
| 2029 | `RingOnPeriod2` | Defines the Distinctive Ringing #2 ON period (in msec) on analog lines. |  |
| 2030 | `RingOnPeriod3` | Defines the Distinctive Ringing #3 ON period (in msec) on analog lines. |  |
| 2031 | `RingOnPeriod4` | Defines the Distinctive Ringing #4 ON period (in msec) on analog lines. |  |
| 2032 | `RingOnPeriod5` | Defines the Distinctive Ringing #5 ON period (in msec) on analog lines. |  |
| 2033 | `RingOnPeriod6` | Defines the Distinctive Ringing #6 ON period (in msec) on analog lines. |  |
| 2034 | `RingOnPeriod7` | Defines the Distinctive Ringing #7 ON period (in msec) on analog lines. |  |
| 2035 | `RingPersistence` | Time (in msec) from the ring detection to signaling the ring interrupt. |  |
| 2036 | `Routing` | Routing General Params |  |
| 2037 | `RoutingMode` | Routing Mode | Not Configured /-1,Routing Table /0,Serving IP Group /1,Request-URI /2 |
| 2038 | `RoutingTableDestinationMasksColumn` | Comprises the destination masks column of the static routing rules that users can add to |  |
| 2039 | `RoutingTableDestinationPrefixLensColumn` | The prefix length value of the destination masks column of the static routing rules. Users can add static routing rul... |  |
| 2040 | `RoutingTableDestinationsColumn` | Comprises the destinations column of the static routing rules that users can add to. |  |
| 2041 | `RoutingTableGatewaysColumn` | Comprises the gateways column of the static routing rules that users can add. |  |
| 2042 | `RoutingTableHopsCountColumn` | Comprises the Hops count column of the static routing rules that users can add. |  |
| 2043 | `RoutingTableInterfacesColumn` | Comprises the interfaces column of the static routing rules that users can add. |  |
| 2044 | `RtcpActivationMode` | Rtcp activation policy:{@}0 - always active{@}1- inactive while rtp is inactive | Active always /0,If RTP Active /1 |
| 2045 | `RtcpXrEscIP` | RTCP-XR server IP address |  |
| 2046 | `RtcpXrReportMode` | 0:rtcpxr is not sent over SIP at all{@}1:rtcpxr is sent over sip when call ended{@}2:rtcpxr is sent over sip when on ... | Disable /0,End Call /1,End Call & Periodic /2,End Call & End Segment /3 |
| 2047 | `RtpOnly_Session` | CHashMap::CHashMap - Allocation Exception |  |
| 2048 | `RtspServiceDebugMode` | Determines whether to enable RTSP debug messages. |  |
| 2049 | `Running` | Running (Calls: %d, ASR: %d%%) |  |
| 2050 | `RxDtmfHangOverTime` | PCIIFChangeChannelParams(): Enabling Answer Detector will be ignored due to blocking by feature key or by startup con... |  |
| 2051 | `S8c7` | S8c7 H |  |
| 2052 | `S8c9` | S8c9 N |  |
| 2053 | `SASBINDINGMODE` | Defines the SAS database binding mode: URI dependant (0), according to user part (1) | URI Dependant /0,User Part /1 |
| 2054 | `SASBLOCKUNREGUSERS` | Enables SAS to reject dialog-establishment requests from un-registered users | Un-Block /0,Block /1 |
| 2055 | `SASCONNECTIONREUSE` | Re-using TCP/TLS connection in SAS application |  |
| 2056 | `SASDEFAULTGATEWAYIP` | SIP SAS default IP address for incoming requests in emergency mode |  |
| 2057 | `SASEMERGENCYNUMBERS` | SAS Emergency numbers |  |
| 2058 | `SASEMERGENCYPREFIX` | Add prefix to RequestURI user for outgoing calls in emergency mode |  |
| 2059 | `SASENABLECONTACTREPLACE` | Enables SAS to set the Contact and the Upper Via headers to have the same IP address (domain part). |  |
| 2060 | `SASENABLEENUM` | Enables SAS to perform ENUM query when receiving INVITE messages in emergency mode |  |
| 2061 | `SASENABLERECORDROUTE` | Enables SAS to add record-Route header to requests |  |
| 2062 | `SASENTERINGEMERGENCYMODE` | Defines which methods cause SAS to enter EMERGENCY mode. (0)-OPTIONS only, (1)-OPTIONS/INVITE/REGISTER | OPTIONS Only /0,OPTIONS/INVITE/REGISTER /1 |
| 2063 | `SASINBOUNDMANIPULATIONMODE` | Defines the SAS inbound manipulation: (0)-None, (1)-Emergency only. Currently, applies only to INVITE requests | None /0,Emergency Only /1 |
| 2064 | `SASINDIALOGREQUESTMODE` | 0-in-dialog requests from user and not in emergency mode, send according to Request-URI.1-in-dialog requests from use... | standard/0,send-to-proxy/1 |
| 2065 | `SASLOCALSIPTCPPORT` | Local SAS SIP port used for signaling over TCP |  |
| 2066 | `SASLOCALSIPTLSPORT` | Local SAS SIP port used for signaling over TLS |  |
| 2067 | `SASLOCALSIPUDPPORT` | Local SAS SIP port used for signaling over UDP |  |
| 2068 | `SASPROXYSET` | Proxy Set Id for SAS |  |
| 2069 | `SASREGISTRATIONTIME` | SAS will send this value in expires header while working in emergency mode |  |
| 2070 | `SASRegistrationInstance` | CHashMap::CHashMap - Allocation Exception |  |
| 2071 | `SASSHORTNUMBERLENGTH` | Defines the suffix length of the compared number |  |
| 2072 | `SASSUBSCRIBERESPONSE` | SIP response for SUBSCRIBE in SAS Emergency mode |  |
| 2073 | `SASSURVIVABILITYMODE` | Defines the SAS working mode: (0)-Standard Mode (working with configured proxy set), (1)-always emergency mode (worki... | Standard Mode /0,Always Emergency Mode /1,Ignore REGISTER in normal mode /2,Auto-answer REGISTER ... |
| 2074 | `SAVE` | SYS_HA: system is in HA sync period. don't change module configuration until the HA alarm is cleared |  |
| 2075 | `SAVP` | SIPSDPSession::CheckMediaMatch - No media interface configured for %s. |  |
| 2076 | `SBC3XXBEHAVIOR` | Defines how SBC passes Contact in 3xx responses | Transparent /0,Using DB /1 |
| 2077 | `SBCALERTTIMEOUT` | Maximal time to wait for connect in SBC (seconds) |  |
| 2078 | `SBCASSERTIDENTITY` | 0 - Don't care,1- Add P-Asserted-Identity Header, 2 - Remove P-Asserted-Identity Header | Don't care /0,Always Add /1,Always remove /2 |
| 2079 | `SBCDIVERSIONURITYPE` | Which uri to use for Diversion header in SBC | Transparent /0,Sip /1,Tel /2 |
| 2080 | `SBCDirectMedia` | Disable - All cross SRD's calls via SBC are no direct media.{@}Enable - All calls via SBC are direct media.{@}{@} |  |
| 2081 | `SBCDiversionMode` | Don't Care |  |
| 2082 | `SBCENABLEBYEAUTHENTICATION` | Allows the media to remain active upon receipt of a 401/407 response by sending a releaseNackEvent, rather than relea... | 0-DisconnectthepathbysendingareleaseAckeventuponreceiptofa401/407(default){@}1-Retainthemediapath... |
| 2083 | `SBCENABLESURVIVABILITYNOTICE` | If enabled - when SBC needs to terminates a REGISTER request, it adds a body (survivability notice) to the 200OK resp... |  |
| 2084 | `SBCENFORCEMEDIAORDER` | Arrange media lines according to the previous offer-answer (required by RFC 3264) |  |
| 2085 | `SBCEXTENSIONSPROVISIONINGMODE` | Indicates how the registration database is provisioned (0) - use register request (1) - broadsoft automatic mode |  |
| 2086 | `SBCFORKINGHANDLINGMODE` | Decides the handling method to 18X response to forking.The parameter only affects the SBC behavior. | Latch On First/0,Sequential/1 |
| 2087 | `SBCFaxCodersGroupID` | Coders group 0 |  |
| 2088 | `SBCGRUUMODE` | SBC GRUU Behavior | None /0,AsProxy /1,TemporaryOnly /2,PublicOnly /3,Both /4 |
| 2089 | `SBCKEEPCONTACTUSERINREGISTER` | SBC - Keep original Contact User in REGISTER requests |  |
| 2090 | `SBCMAXFORWARDSLIMIT` | Limit the value of the Max-Forwards header. {@}If the header's value is equal or smaller than the parameter's value t... |  |
| 2091 | `SBCMINSE` | The minimum amount of time that can occur between session refresh requests in a dialog before the session will be con... |  |
| 2092 | `SBCMediaSecurityBehaviourLocal` | As Is |  |
| 2093 | `SBCPREFERENCESMODE` | Defines the coders combination in the outgoing message. (0)-doesn't include extensions, (1)-Include extensions | Doesn't Include Extensions /0,Include Extensions /1 |
| 2094 | `SBCPROXYREGISTRATIONTIME` | This parameter defines the duration (in seconds)  in which the user is registered in the proxy DB, after the REGISTER... |  |
| 2095 | `SBCREFERBEHAVIOR` | Defines how SBC passes Refer-To in REFER requests | Regular /0,Regular & Using DB /1,Set HOST part to IPGroup name /2 |
| 2096 | `SBCREGISTRATIONTIME` | Expires value SBC responds to user with. |  |
| 2097 | `SBCSENDINVITETOALLCONTACTS` | Disable-SBC sends INVITE according to the Request-URI. Enabled-if the Request-URI is of specific contact, SBC sends t... |  |
| 2098 | `SBCSESSIONEXPIRES` | SBC session refresh timer for requests in a dialog |  |
| 2099 | `SBCSHAREDLINEREGMODE` | Define the registration handling mode in case of shared line manipulation.0 - as configured, 1- terminate secondary l... | As Configured /0,Terminate Secondary Lines /1 |
| 2100 | `SBCSURVIVABILITYREGISTRATIONTIME` | Defines the duration of the periodic registrations between the user and the SBC, when the SBC is in survivability state |  |
| 2101 | `SBCTESTID` | Incoming SBC test ID (bypass TestCallID) |  |
| 2102 | `SBCTranscodingMode` | Only if Required |  |
| 2103 | `SBCUSERREGISTRATIONTIME` | SBC User Registration Time |  |
| 2104 | `SBCXFERPREFIX` | Prefix for routing and manipulations when URL DB is used |  |
| 2105 | `SCENARIO` | Send File |  |
| 2106 | `SCREENINGIND2IP` | Override screening indicator value in Setup messages to IP | Not Configured /-1,User Provided /0,User Passed /1,User Failed /2,Network Provided /3{@} |
| 2107 | `SCREENINGIND2ISDN` | Override screening indicator value in Setup messages to ISDN |  |
| 2108 | `SCTPAssociationsNum` | Defines the maximum number of SCTP associations that can be opened. |  |
| 2109 | `SCTPChecksumMethod` | Determines the Checksum method for authenticating packets on both sides. | Adler/0,Crc/1 |
| 2110 | `SCTPDNetNum` | Defines the maximum number of association transport addresses that can be active.{@} |  |
| 2111 | `SCTPHBInterval` | Defines the SCTP heartbeat interval. |  |
| 2112 | `SCTPHOSTNAME` | When set to any value other than empty string, SCTP uses it as the FQDN  parameter value. |  |
| 2113 | `SCTPISTRMNum` | Defines the maximum number of incoming streams. |  |
| 2114 | `SCTPMaxAssocInitAttempts` | Defines the maximum number of SCTP association initialization attempts. |  |
| 2115 | `SCTPMaxAssocRet` | Defines the maximum number of SCTP association retransmission attempts. |  |
| 2116 | `SCTPMaxDataChunkSize` | Defines the maximum length of SCTP data chunks. |  |
| 2117 | `SCTPOSTRMNum` | Defines the maximum number of outgoing streams. |  |
| 2118 | `SCTPOutChunksNum` | Defines the maximum number of outgoing chunks. |  |
| 2119 | `SCTPPortsNum` | Defines the maximum number of SCTP endpoints that can be opened. |  |
| 2120 | `SCTPT4SAckTimer` | Defines the SCTP T4 SACK timer interval. |  |
| 2121 | `SDPBodyMedia` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 2122 | `SDPECANFORMAT` | SDP Ecan Format - defines echo canceller format for outgoing SDP | GPMD Line /0,Separate Attribute /1,No Ecan /2,No VBD /3 |
| 2123 | `SDPMediaEncryption` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2124 | `SECONDARYMEDIAINTERFACE` | Secondary media interface to be used within SDP |  |
| 2125 | `SECURECALLSFROMIP` | Gateway will either only accept calls from IP addresses that are defined in the Tel to IP Routing table (1) or handle... | Disable /0,Secure Incoming calls /1,Secure All calls /2 |
| 2126 | `SELECTSOURCEHEADERFORCALLEDNUMBER` | Select source header for called number (IP->TEL), either from the user part of To header or the P-Called-Party-ID hea... | use RequestURI header /0,use To header /1,use P-Called-Party-ID header /2 |
| 2127 | `SEND180FORCALLWAITING` | Send 180 for call waiting. |  |
| 2128 | `SENDALARMSTOSYSLOG` | Enables the module that sends SNMP alarms to Syslog. |  |
| 2129 | `SENDALLCODERSONRETRIEVE` | Send only chosen coder (0) or all supported coders (1) |  |
| 2130 | `SENDCHANNELNONSTANDARD` | Send trunk and bchannel numbers on setup and call proceeding messages as nonStandard data |  |
| 2131 | `SENDIEONTG` | Configure trunk groups on which to send additional IE |  |
| 2132 | `SENDINVITETOPROXY` | Always send INVITE messages to Proxy server |  |
| 2133 | `SENDISDNSERVICEAFTERRESTART` | If set ISDN SERVICE message will be sent after local RESTART |  |
| 2134 | `SENDISDNTRANSFERONCONNECT` | Send TBCT/ECT/RLT request only when second leg call is connected | Alert /0,Connect /1 |
| 2135 | `SENDLOCALTIMETOISDNCONNECT` | 0 - Don't Send Local Date and Time,1 - Send Local Date and Time Only If Missing,2 - Always Send Local Date and Time | Don't Send Local Date and Time/0,Send Local Date and Time Only If Missing/1,Always Send Local Dat... |
| 2136 | `SENDMETERING2IP` | Send metering messages to IP on detection of analog metering pulses |  |
| 2137 | `SENDQSIGTRANSFERCOMPLETEONREMOTETRANSFER` | Send QSIG Facility TransferComplete on Remote Transfer |  |
| 2138 | `SEQNUM` | Old RTPSeqNum Value:%d |  |
| 2139 | `SESONE` | Bad session id |  |
| 2140 | `SESRANGE` | Bad session id range |  |
| 2141 | `SESSIONEXPIRESDISCONNECTTIME` | Defines the minimum time factor before the session expires. By achiving this time without session refresh, the sessio... |  |
| 2142 | `SESSIONEXPIRESMETHOD` | Determines the Method which the SIP session will be using to referesh the session. | re-INVITE /0,UPDATE /1 |
| 2143 | `SETDBL0TO1` | GWAPP DBL0ToDBL1:%d |  |
| 2144 | `SETDBL1TO0` | GWAPP DBL1ToDBL0:%d |  |
| 2145 | `SETDBL1TO5` | GWAPP DBL1ToDBL5:%d |  |
| 2146 | `SETDBL5TO1` | GWAPP DBL5ToDBL1:%d |  |
| 2147 | `SHELL` | Too many parameters. |  |
| 2148 | `SHORTINTERVAL` | Changing Diag Bit Interval To 5 minutes. |  |
| 2149 | `SHOULDREGISTER` | This parameter related to Register/UnRegister buttons | unreg-all-entities/0,unreg-ep/1,unreg-account/2,unreg-bri/3,reg-all-entities/16,reg-ep/17,reg-acc... |
| 2150 | `SHOULDSUBSCRIBE` | This parameter related to Subscribe/UnSubscribe buttons |  |
| 2151 | `SHow` | SHow (SH) - Display operational statistics. |  |
| 2152 | `SIP183BEHAVIOUR` | If this parameter set to 1, ALERT to ISDN will be sent upon 183 receive | Progress /0,Alert /1 |
| 2153 | `SIPAccount` | CHashMap::CHashMap - Allocation Exception |  |
| 2154 | `SIPAdditionalHeaders` | Unexpected symbol '%c'. CRLF expected |  |
| 2155 | `SIPCDR` | This is SIP CDR message |  |
| 2156 | `SIPCHALLENGECACHINGMODE` | SIP Challenge caching mode | None /0,Invite Only /1,Full /2 |
| 2157 | `SIPDEFAULTCALLPRIORITY` | SIP Default Call Priority |  |
| 2158 | `SIPDESTINATIONPORT` | Default SIP destination port (usually 5060) |  |
| 2159 | `SIPDialogInitiateData` | CHashMap::CHashMap - Allocation Exception |  |
| 2160 | `SIPEndPoint` | CHashMap::CHashMap - Allocation Exception |  |
| 2161 | `SIPExtraSmallRawUserBuffer` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2162 | `SIPFORCERPORT` | If enable, the sip responces will be send to the UDP port from where the sip Request was sent, even if RPORT paramete... |  |
| 2163 | `SIPGATEWAYNAME` | Gateway name |  |
| 2164 | `SIPGateway` | CHashMap::CHashMap - Allocation Exception |  |
| 2165 | `SIPGroupName` | SIP Group Name |  |
| 2166 | `SIPHeaderTable` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2167 | `SIPInternalUrl` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2168 | `SIPMAXRTX` | Maximum number of retransmissions |  |
| 2169 | `SIPMessage` | GeneralRsrcMngr<%s>::ReturnObject: Object %d is returned while it is stored in HA |  |
| 2170 | `SIPNATDETECTION` | If not set, the incoming request will be always processed as user NOT behind NAT |  |
| 2171 | `SIPPChargingVectorHeader` | CHashMap::CHashMap - Allocation Exception |  |
| 2172 | `SIPProxyEventResource` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2173 | `SIPProxyRequestEvent` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2174 | `SIPQueueEvent` | CHashMap::CHashMap - Allocation Exception |  |
| 2175 | `SIPREROUTINGMODE` | Defines the routing mode after receiving 3xx response or transfer: standard mode (0), send invite to proxy (1), use r... | Standard Mode /0,Send to Proxy /1,Use Routing Table /2 |
| 2176 | `SIPRawHeader` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2177 | `SIPReSetupData` | CHashMap::CHashMap - Allocation Exception |  |
| 2178 | `SIPRecordRouteHeader` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2179 | `SIPSDPSESSIONOWNER` | The SDP owner string |  |
| 2180 | `SIPSESSIONEXPIRES` | The SIP session will be refreshed (using INVITE) each time this timer expires (seconds) |  |
| 2181 | `SIPSREQUIRECLIENTCERTIFICATE` | Should require client certificate upon TLS connection request arrival |  |
| 2182 | `SIPSUBJECT` | User-defined sip subject |  |
| 2183 | `SIPServer` | CHashMap::CHashMap - Allocation Exception |  |
| 2184 | `SIPServersIPList` | CHashMap::CHashMap - Allocation Exception |  |
| 2185 | `SIPServersMngr` | CHashMap::CHashMap - Allocation Exception |  |
| 2186 | `SIPServiceRouteHeader` | Unexpected symbol '%c'. Expected end of header |  |
| 2187 | `SIPStackEndPoint` | CHashMap::CHashMap - Allocation Exception |  |
| 2188 | `SIPStackSession` | CHashMap::CHashMap - Allocation Exception |  |
| 2189 | `SIPT1RTX` | SIP T1 timeout for retransmission |  |
| 2190 | `SIPT2RTX` | SIP T2 timeout for retransmission |  |
| 2191 | `SIPT38VERSION` | SIP T.38 Version | Not Configured /-1,Version 0 /0,Version 3 /3 |
| 2192 | `SIPTCPTIMEOUT` | SIP TCP time out (influence timerB and Timer F) |  |
| 2193 | `SIPTRANSPORTTYPE` | SIP transport type | UDP /0,TCP /1,TLS /2 |
| 2194 | `SIPTUConfiguration` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2195 | `SIPTUResource` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2196 | `SIPTestEndPoint` | CHashMap::CHashMap - Allocation Exception |  |
| 2197 | `SIPTestStackEndPoint` | CHashMap::CHashMap - Allocation Exception |  |
| 2198 | `SIPTransaction` | ServerTransaction#%d::SendTUProvisionalResponse failed to send message!!! |  |
| 2199 | `SIPTranscodingStackSession` | CHashMap::CHashMap - Allocation Exception |  |
| 2200 | `SIPViaHeader` | GeneralRsrcMngr<%s>::ReturnObject: Object %d is returned while it is stored in HA |  |
| 2201 | `SIPWarningReason` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 2202 | `SIP_SESSION_INTERVAL_TOO_SMALL_EV` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2203 | `SITDetectorEnable` | Enables SIT (Special Information Tones) detection and generation. |  |
| 2204 | `SITQ850CAUSE` | Release cause for SIT |  |
| 2205 | `SITQ850CAUSEFORIC` | Release cause for SIT IC |  |
| 2206 | `SITQ850CAUSEFORNC` | Release cause for SIT NC |  |
| 2207 | `SITQ850CAUSEFORRO` | Release cause for SIT RO |  |
| 2208 | `SITQ850CAUSEFORVC` | Release cause for SIT VC |  |
| 2209 | `SId3WayConfNonAllocatablePorts` | BRI to SIP Supplementary Services Codes |  |
| 2210 | `SIdAUTHENTICATIONMODE` | Per FXS |  |
| 2211 | `SIdDayOfMonthEnd` | STUN Settings |  |
| 2212 | `SIdDefGateway` | VoIP DNS Settings |  |
| 2213 | `SIdEnableDHCP` | VoIP Monitoring Settings |  |
| 2214 | `SIdEnableEchoCanceller` | Acoustic Echo Suppressor Settings |  |
| 2215 | `SIdFXOCoefficientType` | FXS Settings |  |
| 2216 | `SIdGWDEBUGLEVEL` | Activity Types to Report via 'Activity Log' Messages |  |
| 2217 | `SIdIP2TelCutThroughCallBehavior` | Coder Group |  |
| 2218 | `SIdIPProfileName` | Common Parameters |  |
| 2219 | `SIdIdDisableNAT` | G729EV Coder Settings |  |
| 2220 | `SIdLockGraceTimeout` | Save Configuration |  |
| 2221 | `SIdMGMTBEHAVIORONTIMEOUT` | Absolute Expiry Timer |  |
| 2222 | `SIdMGMTLOGINCACHEMODE` | LDAP settings |  |
| 2223 | `SIdMGMTUSELOCALUSERSDATABASE` | Deny Access |  |
| 2224 | `SIdResetSRTPStateUponRekey` | Gateway Parameters |  |
| 2225 | `SIdSRDLineIndex` | Common Parameters |  |
| 2226 | `SIdSRDMediaRealm` | SBC Parameters |  |
| 2227 | `SIdVoiceMailInterface` | Digit Patterns |  |
| 2228 | `SMART` | Smart Option is %s |  |
| 2229 | `SMDI` | Enables the Simplified Message Desk Interface (SMDI). 0-no SMDI 1-Belcore SMDI 2-Ericsson SMDI 3-NEC (Ics) |  |
| 2230 | `SMDIInternalNumberLen` | Defines the length of PBX internal numbers. This is relevant for Ericsson SMDI only. |  |
| 2231 | `SMDILineIdLen` | Defines the line identification string length. Use 7 (default) for Bellcore SMDI, or between 2 and 5 for Ericsson SMDI. |  |
| 2232 | `SMDIMWIMinInterval` | Minimum time interval (milliseconds) between sending subsequent MWI messages over SMDI. |  |
| 2233 | `SMDIMWIQueueSize` | Queue size (number of entries) for throttling outgoing MWI messages over SMDI. |  |
| 2234 | `SMDITimeOut` | SMDI Timeout <mSec> |  |
| 2235 | `SMIB` | Result: %d |  |
| 2236 | `SNMPAlternateWanInterfaceName` | This is the name of the alternate voip interface that SNMP can be accessed from. |  |
| 2237 | `SNMPManagerIsUsed` | Enables a row in the SNMP Managers Table. |  |
| 2238 | `SNMPManagerTableIP` | Defines the SNMP manager server IP address |  |
| 2239 | `SNMPManagerTrapPort` | Sets the trap ports to be used by the different managers. |  |
| 2240 | `SNMPManagerTrapSendingEnable` | Enables the SNMP Manager's IP address for traps to be sent to it. | disable/0,enable/1 |
| 2241 | `SNMPManagerTrapUser` | SNMPv3 USM user or SNMPv2 user to associate with this trap destination. By default it is associated with the SNMPv2 u... |  |
| 2242 | `SNMPPort` | This parameter specifies the port number for SNMP requests and responses. |  |
| 2243 | `SNMPREADONLYCOMMUNITYSTRING` | Defines a read-only community string. |  |
| 2244 | `SNMPREADWRITECOMMUNITYSTRING` | Defines a read-write community string. |  |
| 2245 | `SNMPSysContact` | Defines thethe contact person for thismanaged node. |  |
| 2246 | `SNMPSysLocation` | Defines the physical location of the node. |  |
| 2247 | `SNMPSysName` | Defines the sysName as descibed in MIB-2. |  |
| 2248 | `SNMPSysOid` | Defines the base product system OID (SNMP SysOid). |  |
| 2249 | `SNMPTASKSTARTUPDELAY` | Determines  Snmp-Task's StartUp delay; mainly for MSBG-WAN become ready; in seconds. |  |
| 2250 | `SNMPTRAPCOMMUNITYSTRING` | Defines the community string used in traps. |  |
| 2251 | `SNMPTRUSTEDMGR` | Defines the IP address of a trusted SNMP manager. |  |
| 2252 | `SNMPTrapEnterpriseOid` | Defines the Trap Enterprise Oid via the INI file. |  |
| 2253 | `SNMPTrapManagerHostName` | Defines a FQDN of a remote host that is used as an SNMP Trap Manager. |  |
| 2254 | `SNMPTrapPort` | This parameter specifies the port number for SNMP Traps. {@} |  |
| 2255 | `SOURCEENCODTYPE` | Calling number coding type in Setup message |  |
| 2256 | `SOURCEIPADDRESSINPUT` | Decides the origin of the source ip address looked at when routing using the IP --> Tel table. 0 - Contact 1 - Reciev... | Not Configure /-1,SIP Contact Header /0,Layer 3 Source IP /1 |
| 2257 | `SOURCEMANIPULATIONMODE` | Describes the headers containing source number after manipulation: (0) both FROM and P-Asserted contain src number af... | FROM & P-Asserted /0 ,Only FROM /1 |
| 2258 | `SOURCENUMBERPREFERENCE` | Determines from where the source number shall be taken from (in an incoming  INVITE request) |  |
| 2259 | `SPEEX_WB` | Channel Type: |  |
| 2260 | `SRDLineIndex` | Remove Line |  |
| 2261 | `SRTP` | Unknown %d |  |
| 2262 | `SRTPOFFEREDSUITES` | Offered SRTP Cipher Suites | Not defined /0, All /15,AES-CM-128-HMAC-SHA1-80 /1,AES-CM-128-HMAC-SHA1-32 /2,ARIA-CM-128-HMAC-SH... |
| 2263 | `SRTPTunnelingValidateRTCPRxAuthentication` | SRTP Tunneling Authentication for RTCP |  |
| 2264 | `SRTPTunnelingValidateRTPRxAuthentication` | SRTP Tunneling Authentication for RTP |  |
| 2265 | `SRTPTxPacketMKISize` | Determines the size of the parameter Master Key Identifier (MKI) in transmitted SRTP packets. |  |
| 2266 | `SS5DetectorEnable` | Enables or disables detection of Line signaling |  |
| 2267 | `SS7M3BDebugFlags` | Container parameter for SS7 debug flags. Controls SS7 Debug Outputs. |  |
| 2268 | `SS7M3BRdcyXlinkTraceAll` | When set via INI-file, activates trace output for all X-links (only when SS7 redundancy is configured). |  |
| 2269 | `SS7MTP3RdcyBoardNum` | Defines the board number for the Signaling System 7 (SS7) MTP3-User Adaptation Layer redundancy mode. Each board has ... |  |
| 2270 | `SS7MTP3RdundancyMode` | Defines the Signaling System 7 (SS7) MTP3-User Adaptation Layer redundancy mode. Determines the redundancy flavor. |  |
| 2271 | `SS7MTP3RdundancyTransferType` | This is an MTP3-User Adaptation Layer parameter of the Signaling System 7 (SS7), used to define the cross-board conne... |  |
| 2272 | `SSHAdminKey` | RSA public key for SSH login. |  |
| 2273 | `SSHEnableLastLoginMessage` | Enables / disables the Last-Login message in SSH sessions. |  |
| 2274 | `SSHMaxBinaryPacketSize` | Configures the maximum packet size (in bytes) for SSH packets (possible values are between 582 and 35000). |  |
| 2275 | `SSHMaxLoginAttempts` | Configures the number of allowed SSH incorrect login attempts (possible values are between 1 and 5). |  |
| 2276 | `SSHMaxPayloadSize` | Configures the maximum uncompressed payload size for SSH packets, in bytes (possible values are between 550 and 32768). |  |
| 2277 | `SSHMaxSessions` | Configures the maximum allowed number of SSH sessions. |  |
| 2278 | `SSHRequirePublicKey` | Enables or disables RSA public keys in SSH. |  |
| 2279 | `SSHServerEnable` | Enables / disables the embedded SSH server. | Enable/1,Disable/0 |
| 2280 | `SSHServerPort` | Defines the SSH port number. |  |
| 2281 | `SSHSrv` | SSH error: can't get socket! %d |  |
| 2282 | `SSLCertificateSR` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Certificate Settings' page. |  |
| 2283 | `SSLPKEY` | Send File |  |
| 2284 | `SSLSubjectName_C` | Create CSR |  |
| 2285 | `SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA` | No Compression |  |
| 2286 | `START` | The valid range for the NUM AMD operations parameter is: 1 to %d |  |
| 2287 | `STATIC` | STATIC failed,  error = %d |  |
| 2288 | `STOP` | Audit FIFO Statistic command must have at least one parameter |  |
| 2289 | `STOPPERIODIC` | CpuUtilization PERIODIC was already stopped ! |  |
| 2290 | `STOPRECORDINGONNOSPEACHTIMEOUT` | Timeout for no speech detection used to stop recording |  |
| 2291 | `STREAMINGID` | Identification of HTTP played voice prompt (To be used by SIP INVITE) |  |
| 2292 | `STUNSERVERPRIMARYIP` | Defines the primary STUN Server IP address. |  |
| 2293 | `STUNSERVERSECONDARYIP` | Defines the secondary STUN Server IP address. |  |
| 2294 | `STUTTERTONEDURATION` | Time for playing confirmation tone before normal dial tone is played (msec) |  |
| 2295 | `SUBSCRIBERETRYTIME` | MWI service subscription retry time after last subscription failure (seconds) |  |
| 2296 | `SUBSCRIPTIONMODE` | Subscription Mode: 0 - Per Endpoint, 1 - Per Gateway | Per Endpoint /0,Per Gateway /1 |
| 2297 | `SUPPORTREDIRECTINFACILITY` | Search for Redirect number in facility IE |  |
| 2298 | `SUPPSERVCODECFB` | Supp Serv code for activating Call Forward Busy |  |
| 2299 | `SUPPSERVCODECFBDEACT` | Supp Serv code for deactivating Call Forward Busy |  |
| 2300 | `SUPPSERVCODECFNR` | Supp Serv code for activating Call Forward No Reply |  |
| 2301 | `SUPPSERVCODECFNRDEACT` | Supp Serv code for deactivating Call Forward No Reply |  |
| 2302 | `SUPPSERVCODECFU` | Supp Serv code for activating Call Forward Unconditional |  |
| 2303 | `SUPPSERVCODECFUDEACT` | Supp Serv code for deactivating Call Forward Unconditional |  |
| 2304 | `SWAPREDIRECTNUMBER` | Swap Redirect and Called numbers | No /0,Yes /1 |
| 2305 | `SXNetID` | Strong Extranet ID |  |
| 2306 | `SYSLOG` | Buffer status: %d free entries |  |
| 2307 | `SYSLOGOUTPUTMETHOD` | Defines which method controlls gwapp Syslog output | Error Handle /0,NLOG Sys /1,NLOG /2 |
| 2308 | `SYSTEM_AUDIT_FAILURE_CORE_EV` | Failed to allocate gwDeleteResourceEvent |  |
| 2309 | `SampleBasedCodersRTPPacketInterval` | MSRTATxBitRate %d. |  |
| 2310 | `SaveConfiguratioN` | Save device configuration |  |
| 2311 | `SaveConfiguration` | Determines if the device configuration is saved in flash memory. |  |
| 2312 | `ScenarioFileName` | The name of the scenario file. |  |
| 2313 | `SctpIPAddress` | Seperate source IP address for the SCTP. |  |
| 2314 | `SecondIpAddress` | Second IP Address |  |
| 2315 | `Security` | Print IPSec SPD to syslog |  |
| 2316 | `SecuritySettings` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Security Settings' page. |  |
| 2317 | `Send` | Device Certificate |  |
| 2318 | `SendKeepAliveTrap` | Invokes keep-alive trap and sends it out every 9/10 of time defined in the NatBindingDefaultTimeout parameter. |  |
| 2319 | `SendPortEvent` | AM INFO: cpAnalogChannelsManager MaxAnalogChannels=%d |  |
| 2320 | `SendRejectOnOverload` | If set to false (0), a 503 response will not be sent on overload. |  |
| 2321 | `SerialBaudRate` | Enables changes to the Serial Baud Rate for Simplified Message Desk Interface (SMDI). |  |
| 2322 | `SerialData` | Changes the serial data bit for the Simplified Message Desk Interface (SMDI). |  |
| 2323 | `SerialFlowControl` | Changes the serial flow control for the Simplified Message Desk Interface (SMDI). |  |
| 2324 | `SerialParity` | Changes the serial parity for the Simplified Message Desk Interface (SMDI). |  |
| 2325 | `SerialPortAuditIntervalMin` | Interval timeout in minutes, of the Serial Port audit. In case of 0 value, the audit isn't running. |  |
| 2326 | `SerialStop` | Changes the serial stop for the Simplified Message Desk Interface (SMDI). |  |
| 2327 | `Server` | Fault already sent |  |
| 2328 | `ServerRespondTimeout` | Defines the maximum time the board should wait for a response when working with a remote server. |  |
| 2329 | `ServiceEndPoint` | ConfParticipantEndPoint::AllocateParticipantHandle - cannot allocate Participant Handle. probably lack of resources |  |
| 2330 | `Services` | Least Cost Routing |  |
| 2331 | `ServingIPGroup` | Serving IP Group |  |
| 2332 | `SetCommunityString` | User-determined community string with access limited to INI file entered values only. |  |
| 2333 | `SetDefaultIpTarget` | Set default IP debug recording target |  |
| 2334 | `SetDefaultLinePolarityState` | Sets the default line polarity state | DEFAULT_POSITIVE_POLARITY/0,DEFAULT_NEGATIVE_POLARITY/1,DEFAULT_POLARITY_AUTO_DETECT/2 |
| 2335 | `SetDefaultOnIniFileProcess` | Determine if all parameters are set to their defaults before processing updated INI File |  |
| 2336 | `SetIp2TelRedirectReason` | Set the IP-to-TEL Redirect Reason | Not Configured /-1,Unknown /0,Busy /1,No Reply /2,NetWork Busy /3,Deflection /4,DTE out of order ... |
| 2337 | `SetIp2TelRedirectScreeningInd` | Override screening indicator value of the Redirect number in Setup messages to PSTN interface | Not Configured /-1,User Provided /0,User Passed /1,User Failed /2,Network Provided /3 |
| 2338 | `SetIpProfileCallsLimit` | SetIpProfileCallsLimit: Profile:%d Wrong Limit:%d |  |
| 2339 | `SetLimit` | ERROR: need parameter: IP or TEL |  |
| 2340 | `SetMaxLines` | Set number of lines for MORE prompts. |  |
| 2341 | `SetTel2IpRedirectReason` | Set Tel2Ip Redirect Reason | Not Configured /-1,Unknown /0,Busy /1,No Reply /2,NetWork Busy /3,Deflection /4,DTE out of order ... |
| 2342 | `SharedSecret` | Shared secret between client/server |  |
| 2343 | `ShowIPSecMMSAD` | Print ISAKMP SAD to syslog |  |
| 2344 | `ShowIPSecQMSAD` | Print IPSec SAD to syslog |  |
| 2345 | `SidAndVoiceSeparation` | Whether to enable the SID and Voice Separation feature. |  |
| 2346 | `SignalPool` | SM FATAL: Failed to allocate Pool for signals. SignalSegSize=%d |  |
| 2347 | `SilenceTime` | PCIIFChangeChannelParams(): Enabling Energy Detector will be ignored due to blocking by feature key or by startup con... |  |
| 2348 | `SilkMaxAverageBitRate` | Determines the SILK coder maximal average bit rate. |  |
| 2349 | `SilkTxInbandFEC` | Enables the SILK FEC (Forward Error Correction) |  |
| 2350 | `SimpleBuffer` | CPool::CPool - Allocation Exception |  |
| 2351 | `SingleSIDPacketWithSCEG729` | While using connection coder G729 and SCE is ON, single SID packet will be sent. |  |
| 2352 | `SipProxySession` | CHashMap::CHashMap - Allocation Exception |  |
| 2353 | `SipReRoutingMode` | SIP Re-Routing Mode | Not Configured /-1,Standard /0,Proxy /1,Routing Table /2 |
| 2354 | `SipResponse` | Sip Response |  |
| 2355 | `SnmpAccessList` | ACL identifier for SNMP access on MSBG products per a community-string. |  |
| 2356 | `SnmpEngineBoots` | The number of times that the SNMP engine has initialized or reinitialized itself since its initial configuration. |  |
| 2357 | `SnmpEngineIDString` | Snmp Engine ID - sets the SNMP EngineID. 12 HEX Octets in the following format xx:xx:...:xx |  |
| 2358 | `SnoopTask` | Which Task to snoop after memory tramp. [TASK] use to snoop after the task that tramp. [Task Name] use to snoop after... |  |
| 2359 | `SpeexNBBitRate` | Determines the bitrate of Speex NB coder. | 2.15 Kbps /1,5.95 Kbps /2,8.00 Kbps /3,11.0 Kbps /4,15.0 Kbps /5,18.2 Kbps /6,24.6 Kbps /7,3.95 K... |
| 2360 | `SpeexWBBitRate` | Determines the bitrate of Speex WB coder. | 3.95 Kbps /0,5.75 Kbps /1,7.75 Kbps /2,9.80 Kbps /3,12.8 Kbps /4,16.8 Kbps /5,20.6 Kbps /6,23.8 K... |
| 2361 | `SrtpResetWhenEncryptionIsChanged` | Reset (Roc and/or Rtcp Index) SRTP Tx and/or Rx stream, when encryption is changed in mdiddle of SRTP call. |  |
| 2362 | `SshAccessList` | ACL identifier for SSH access on MSBG products. |  |
| 2363 | `SslTls` | SslTls - Manage SSL/TLS communication. |  |
| 2364 | `StackEndPoint` | CHashMap::CHashMap - Allocation Exception |  |
| 2365 | `Standard` | Always Emergency |  |
| 2366 | `StartState` | Illegal State (%s) to handle Ev |  |
| 2367 | `StaticRouteTable` | IPForward MIB. Modification of ipCidrRoute table failed. The row for dest' IP: %x was delted |  |
| 2368 | `Statistics` | StatisticsReset: RESET TEL2ip/IP2tel statistics.  USE WITH CAUTION! |  |
| 2369 | `StorageServerNetworkAddress` | The global storage device address to be used internally by the board. |  |
| 2370 | `StorageServerSWFileName` | This parameter indicates the Storage Server software file name. |  |
| 2371 | `StreamingCacheDecisionInterval` | Defines the streaming cache decision interval in minutes. If -1 is set, decision will be made upon each cache request. |  |
| 2372 | `StreamingCacheNumOfDescriptors` | Defines the number of monitored descriptors in the streaming cache. |  |
| 2373 | `StreamingCacheRefreshTime` | Defines the streaming cache data refresh time in minutes. If -1 is set, refresh is off. |  |
| 2374 | `StreamingCacheSize` | Sets the streaming cache size in MBs. |  |
| 2375 | `StreamingPlayingUnderRunTimeout` | The maximum time an under run condition may occur on the streaming channel. |  |
| 2376 | `StreamingRecordingOverRunTimeout` | The maximum time an over run condition may occur on the streaming channel. |  |
| 2377 | `StunServerDomainName` | Defines the STUN Server's domain name. |  |
| 2378 | `Submit` | Subscribe to MWI |  |
| 2379 | `SubnetBroadcastAfterENetSOEnabled` | Enables Subnet Broadcast After Ethernet Switchover. |  |
| 2380 | `Success` | Internal error |  |
| 2381 | `Supported` | Not Supported |  |
| 2382 | `Syslog` | Cannot Register syslog socket with vlan information, error %d |  |
| 2383 | `SyslogServerIP` | Defines the Syslog server IP address |  |
| 2384 | `SyslogServerPort` | Defines the Syslog Server Port Number |  |
| 2385 | `SystemOperationStateChangeProfile` | Defines the System Operation state Change Profile. |  |
| 2386 | `T38BrokenConnectionEventTimeout` | Determines how long T38 packets aren't received before the Broken Connection event is issued. |  |
| 2387 | `T38FALLBACKTRANSPORTMODE` | Sets the fax mode when the remote fax does not indicate T.38 support. |  |
| 2388 | `T38FAXMAXBUFFERSIZE` | Defines the fax max buffer size in T.38 SDP negotiation. |  |
| 2389 | `T38FAXSESSIONIMMEDIATESTART` | T.38 Fax Session Immediate Start (Fax behind NAT) | Disable /0,Immediate Start On Fax /1,Immediate Start On Fax & Voice /2 |
| 2390 | `T38FaxMaxBuffer` | Illegal T38FaxMaxBuffer value |  |
| 2391 | `T38FaxMaxDatagram` | Illegal T38FaxMaxDatagram value |  |
| 2392 | `T38FaxVersion` | Illegal T38FaxVersion value |  |
| 2393 | `T38MAXDATAGRAMSIZE` | T.38 coder - Max Datagram Size |  |
| 2394 | `T38MaxBitRate` | Illegal T38MaxBitRate value |  |
| 2395 | `T38USERTPPORT` | T.38 packets will be received on RTP port |  |
| 2396 | `T38Version` | Sets the T.38 fax relay version. | T.38 version 0/0,T.38 version 3/3 |
| 2397 | `TAKE` | The TAKE option is restricted |  |
| 2398 | `TARGETOFCHANNEL` | ParsePrefixWorkingImage: No Working Image to start with. exit |  |
| 2399 | `TCPLOCALSIPPORT` | SIP TCP Local Port |  |
| 2400 | `TCSS` | Destination Phone Number Manipulation Table for Tel -> IP Calls | /DPNTelcoToIP@50,100,0 |
| 2401 | `TDMBITSClockReference` | Configures the BITS clock reference. |  |
| 2402 | `TDMBITSClockSource` | Configures which clock is output to the BITS card and on which output signal.{@} | Network/4,Network_B/16,ATM_OC3/17,ATM_OC3_B/18,Null/0,Network_DS3_1/19,Network_DS3_2/20,Network_D... |
| 2403 | `TDMBusClockSource` | Selects the clock source on which the board synchronizes. | acTDMBusClockSource_Internal/1,acTDMBusClockSource_MVIP/3,acTDMBusClockSource_Network/4,acTDMBusC... |
| 2404 | `TDMBusEnableFallback` | Defines the auto fallback of the clock. | Manual/0,Auto Non-Revertive/1,Auto Revertive/2 |
| 2405 | `TDMBusFallbackClock` | Selects fallback clock source on which board synchronizes in event of clock failure. | Network/4,H110_A/8,H110_B/9,NetReference1/10,NetReference2/11 |
| 2406 | `TDMBusH100TerminationEnable` | Enables or Disables H.100 TDM Bus Termination. |  |
| 2407 | `TDMBusLocalReference` | Selects the TrunkID to be used as the clock synchronization source of the board. |  |
| 2408 | `TDMBusNetrefOUTPUTMODE` | Selects the NetRef output functionality. | acNetrefOutputMode_NONE/0,acNetrefOutputMode_NETREF1/1,acNetrefOutputMode_NETREF2/2,acNetrefOutpu... |
| 2409 | `TDMBusNetrefSpeed` | Determines the NetRef frequency for generation and synchronization. | 8khz/0,1.544MHz/1,2.048MHz/2 |
| 2410 | `TDMBusOutputDisable` | 1=Disable TDM bus output and places timeslot in tri-state mode |  |
| 2411 | `TDMBusOutputPort` | Defines the SCSA/MVIP/H.100/H.110 port to be used for board's channel #0. |  |
| 2412 | `TDMBusOutputStartingChannel` | Defines the outgoing TDM Timeslot for the board's channel #0. |  |
| 2413 | `TDMBusSpeed` | Selects the TDM bus speed according to the Bus Type. | 2 Mbps/0,4 Mbps/2,8 Mbps/3,16 Mbps/4 |
| 2414 | `TDMBusType` | Selects the TDM bus interface to be used. | MVIP_BUS/0,SC_BUS/1,USE_FRAMERS/2,QSLAC_BUS/3,USE_H110_BUS/4,USE_EXT_BUS/5,ANALOG_BUS/6,USE_PSTN_... |
| 2415 | `TDMBusmasterSlaveSelection` | Sets SC/MVIP/H.100/H.110. | SlaveMode/0,MasterMode/1,SecondaryMasterMode/2 |
| 2416 | `TDMOIPINITIATEINVITETIME` | Time between first INVITE issued within the same trunk (msec) |  |
| 2417 | `TDMOIPINVITERETRYTIME` | Time between call release and new INVITE(msec) |  |
| 2418 | `TDMOVERIPMINCALLSFORTRUNKACTIVATION` | Minimum connected calls for trunk activation, if 0 - trunk is always active |  |
| 2419 | `TEL2IPCALLFORKINGMODE` | Tel2IP Call Forking Mode |  |
| 2420 | `TEL2IPDEFAULTREDIRECTREASON` | Tel2IP Default Redirect Reason | Not Configured /-1,Busy /1,No Reply /2,Deflection /4,DTE out of order /9,Systematic or Unconditio... |
| 2421 | `TEL2IPSOURCENUMBERMAPPINGDIALPLANINDEX` | Tel to IP Source Number Mapping Dial Plan Index |  |
| 2422 | `TEL2IPSOURCENUMBERMAPPINGDIALPLANMODE` | Tel to IP Source Number Mapping Dial Plan Mode. 0-number is reserved. 1-number is replaced by DialPlan manipulated nu... | reserved /0,replaced /1 |
| 2423 | `TELCONNECTCODE` | Play Code string to Tel side when connect message recieved from IP side |  |
| 2424 | `TELNETSERVERPORT` | Defines the port number for Telnet. |  |
| 2425 | `TESTCALLDTMFSTRING` | DTMF string for test calls |  |
| 2426 | `TESTCALLID` | Incoming test call prefix |  |
| 2427 | `TGRPROUTINGPRECEDENCE` | TGRP Routing Precedence |  |
| 2428 | `THIRDPARTYCALLCONTROLTRANSCODING` | Enables Third Party Call Control Transcoding functionality |  |
| 2429 | `THRMeasPersistence` | Time (in msec) that passes from when the THR INT is detected until the interrupt signal. |  |
| 2430 | `TIAS` | Unexpected symbol '%c' in SDP. Colon expected |  |
| 2431 | `TIMEBEFOREWAITINGINDICATIONS` | Time before call waiting indication is sent to a busy line (seconds) |  |
| 2432 | `TIMEBETWEENDIGITS` | Timeout in seconds between dialed digits |  |
| 2433 | `TIMEBETWEENWAITINGINDICATIONS` | Time between one call waiting indication to the next (seconds) |  |
| 2434 | `TIMEFORDIALTONE` | Duration of played dial tone after the gateway seizes the line in response to ringing |  |
| 2435 | `TIMEFORREORDERTONE` | Duration of reorder tone playing before FXO releases line |  |
| 2436 | `TIMEOUT` | Timeout must be a positive integer |  |
| 2437 | `TIMEOUTBETWEEN100AND18X` | Timer between 100 response and 18x response |  |
| 2438 | `TIMER` | LLDP: rx %d tx %d |  |
| 2439 | `TIMES` | Times parameter has to be in this range:  2..700 |  |
| 2440 | `TIMESTAMP` | Old RTPTimeStamp Value:%d |  |
| 2441 | `TIMETOWAITFORPSTNRELEASEACK` | Defines the timeout (in milliseconds) to wait for the release ACK from the PSTN before releasing the channel. |  |
| 2442 | `TLSBuf` | CPool::Free - Bad Magic (object already released) |  |
| 2443 | `TLSCertFileUrl` | URL for downloading a TLS certificate file. |  |
| 2444 | `TLSClientCipherString` | Cipher-suite selection string for TLS clients. |  |
| 2445 | `TLSExpiryCheckPeriod` | Defines how often the system will check for TLS server certificate expiry (in days). |  |
| 2446 | `TLSExpiryCheckStart` | The system will report when the TLS server certificate is about to expire within this number of days. |  |
| 2447 | `TLSExpiryTestingMode` | Hidden testing parameter: 0=normal, 1=minutes instead of days |  |
| 2448 | `TLSLOCALSIPPORT` | Local TLS SIP port used for signaling |  |
| 2449 | `TLSPkeyFileUrl` | URL for downloading a TLS private key file. |  |
| 2450 | `TLSPkeyPassphrase` | This passphrase will be used to decode encrypted keys loaded to the device. |  |
| 2451 | `TLSPkeySize` | Defines RSA key size (in bits) for newly-generated keys. |  |
| 2452 | `TLSREHANDSHAKEINTERVAL` | The interval between consequent TLS re-handshakes (Minutes). 0 - Disables re-handshakes. |  |
| 2453 | `TLSREMOTESUBJECTNAME` | OCSP Settings |  |
| 2454 | `TLSRequireRFC5746` | Require RFC 5746 support on all TLS connections |  |
| 2455 | `TLSRootFileUrl` | URL for downloading a TLS trusted root certificate file. |  |
| 2456 | `TLSVersion` | Defines the TLS version to be used (SSLv2/SSLv3 or TLSv1). | Any - Including SSLv3/0,TLSv1.0/1,TLSv1.1/2,TLSv1.0 and TLSv1.1/3,TLSv1.2/4,TLSv1.0 and TLSv1.2/5... |
| 2457 | `TLS_Fips140_ErrorInduce` | Induce errors into FIPS140 self-tests. |  |
| 2458 | `TLS_Fips140_Mode` | Determines whether to enable the FIPS140 mode for TLS. |  |
| 2459 | `TLS_Fips140_RNG` | Select random number generator (RNG) algorithm: 0 for FIPS186, 1 for SP800-90 |  |
| 2460 | `TMClockToDerive_A` | Witch Clock to use in sync mode | Derive Ref From Line Clock 1 /0x00,Derive Internal Clock /0x04,Derive None /0x07 |
| 2461 | `TMClockToDerive_B` | Timing Clock To Derive B |  |
| 2462 | `TME1LineBuildOut` | Sets the transmission power between the timing module on the SAT and the E1 external reference clock. This parameter ... | E 75 OHM Normal/0,E 120 OHM Normal/1,E 75 OHM With High Return Loss/4,E 120 OHM With High Return ... |
| 2463 | `TMExternalIFType` | Defines the external line reference (BITS) transmission format | E1_CRC4/0,E1_CAS/1,E1_FAS/2,T1_D4/3,T1_ESF/4,T12/5 |
| 2464 | `TMLoopBackExternalRef1` | Enables loopback state, by connecting Rx path towards Tx path. | Disable /0,Enable /1 |
| 2465 | `TMLoopBackExternalRef2` | Loopback External Ref 2 |  |
| 2466 | `TMMode` | Determines the Gateway-PSTN Timing Syncrhonization Mode. | TM_Standalone_MODE/0,TM_External_MODE/1,TM_LineSync_MODE/2 |
| 2467 | `TMReferenceValidationTime` | Reference validation time. Applicable for External timing and Line timing timing references. Range: 0 - 12minutes. Re... |  |
| 2468 | `TMT1LineBuildOut` | Sets the transmission power between the timing module on the SAT and the T1 external reference clock. This parameter ... | DSX 1 0 To 133 Feet 0dB CSU/0,DSX 1 133 To 266 Feet/1,DSX 1 266 To 399 Feet/2,DSX 1 399 To 533 Fe... |
| 2469 | `TMTransmitControl` | Enables loopback state, by connecting Rx path towards Tx path | SystemClock/0,AIS/1,DisableTransmit/2 |
| 2470 | `TONEID` | Identification of a play call progress tone call (To be used by SIP INVITE) |  |
| 2471 | `TP2110` | SIPProxyContext#%d::ReplaceRequestURI - Failed to get Request-URI from message |  |
| 2472 | `TP2608` | SIPProxyContext#%d::RevertMessageVersion - revert message to version (%d) |  |
| 2473 | `TPApp` | Function %s Offset 0x%x |  |
| 2474 | `TPEthDirectConnectEnable` | This parameter is used to enable or disable the DirectConnect option. |  |
| 2475 | `TPNCPConnectionTimeout` | Defines the TPNCP KeepAlive timeout (in seconds). |  |
| 2476 | `TPNCPLibSocketDelayedAck` | For TG Usage Only - Sets the value of Delayed ACK for the TCP Socket of the LIB connection. pSOS only. |  |
| 2477 | `TPOLICY_CONSTRAINTS` | Require Explicit Policy |  |
| 2478 | `TR069` | CreateSocket failed: error=%d |  |
| 2479 | `TR069ACSPASSWORD` | Sets the password to access the ACS |  |
| 2480 | `TR069ACSURL` | Sets the  ACS url |  |
| 2481 | `TR069ACSUSERNAME` | Sets the user name to access the ACS |  |
| 2482 | `TR069BOOTSTRAP` | Determines whether to enable the TR069  service |  |
| 2483 | `TR069CONNECTIONREQUESTPASSWORD` | Determines ACS connection request password |  |
| 2484 | `TR069CONNECTIONREQUESTURL` | Determines ACS connection request URL |  |
| 2485 | `TR069CONNECTIONREQUESTUSERNAME` | Determines ACS connection request usermane |  |
| 2486 | `TR069CWMPDbFILENAME` | This parameter indicates the Tr069 CWMP library data base file name. |  |
| 2487 | `TR069DEBUGMODE` | Sets the TR069 debug mode level |  |
| 2488 | `TR069HTTPPort` | Determines TR069 HTTP port of the device. |  |
| 2489 | `TR069PERIODICINFORMINTERVAL` | TR069 default periodic inform interval |  |
| 2490 | `TR069Protocol` | Determines TR069  Protocol: HTTP or HTTPS. | HTTP/0,HTTPS/1 |
| 2491 | `TR069RetryIntervalMultiplier` | Interval multiplier - The wait interval range is controlled by two parameters, the minimum wait interval and the inte... |  |
| 2492 | `TR069RetryMinimumWaitInterval` | Minimum wait interval in seconds. |  |
| 2493 | `TR069SERVICEENABLE` | Determines whether to enable the TR069  service. |  |
| 2494 | `TR069WanEnable` | Determines whether the TR069  connection is on WAN (or LAN) | LAN/0,WAN/1 |
| 2495 | `TR069_Capabilities_Codecs_IsObjectExists` | TR069_Capabilities_Codecs_IsObjectExists: Missing indeces at param name = %s. |  |
| 2496 | `TR069_Capabilities_Codecs_NextInstance` | TR069_Capabilities_Codecs_IsObjectExists: Missing indices at param name = %s. |  |
| 2497 | `TR069_Get_Capabilities_Codecs_column` | TR069_Get_Capabilities_Codecs_column: Missing indices at param name = %s. |  |
| 2498 | `TR069_Get_Line_CallingFeatures_column` | TR069_Get_Line_CallingFeatures_column: Missing indeces at param name = %s. |  |
| 2499 | `TR069_Get_Line_Codec_List_column` | TR069_Get_Line_Codec_List_column: Missing indeces at param name = %s. |  |
| 2500 | `TR069_Get_Line_Codec_column` | TR069_Get_Line_Codec_column: Missing indeces at param name = %s. |  |
| 2501 | `TR069_Get_Line_Session_column` | TR069_Get_Line_Session_column: Missing indeces at param name = %s. |  |
| 2502 | `TR069_Get_Line_VoiceProcessing_column` | TR069_Get_Line_VoiceProcessing_column: Missing indeces at param name = %s. |  |
| 2503 | `TR069_Get_VoiceProfile_Capabilities_SIP_column` | TR069_Get_VoiceProfile_Capabilities_SIP_column: Failed; parameter name=%s, pid=%d |  |
| 2504 | `TR069_Get_VoiceProfile_FaxT38_column` | TR069_Get_VoiceProfile_FaxT38_column: Missing indeces at param name = %s. |  |
| 2505 | `TR069_Get_VoiceProfile_Line_SIP_column` | TR069_Get_VoiceProfile_Line_SIP_column: Missing indeces at param name = %s. |  |
| 2506 | `TR069_Get_VoiceProfile_Line_column` | TR069_Get_VoiceProfile_Line_column: Missing indeces at param name = %s. |  |
| 2507 | `TR069_Get_VoiceProfile_NumberingPlan_column` | TR069_Get_VoiceProfile_NumberingPlan_column: Missing indices at param name = %s. |  |
| 2508 | `TR069_Get_VoiceProfile_RTP_RTCP_column` | TR069_Get_VoiceProfile_RTP_RTCP_column: Missing indices at param name = %s. |  |
| 2509 | `TR069_Get_VoiceProfile_RTP_Redundancy_column` | TR069_Get_VoiceProfile_RTP_Redundancy_column: Missing indices at param name = %s. |  |
| 2510 | `TR069_Get_VoiceProfile_RTP_SRTP_column` | TR069_Get_VoiceProfile_RTP_SRTP_column: Missing indices at param name = %s. |  |
| 2511 | `TR069_Get_VoiceProfile_RTP_column` | TR069_Get_VoiceProfile_RTP_column: Missing indices at param name = %s. |  |
| 2512 | `TR069_Get_VoiceProfile_SIP_column` | TR069_Get_VoiceProfile_SIP_column: Missing indices at param name = %s. |  |
| 2513 | `TR069_Get_VoiceProfile_TotalStats_column` | TR069_Get_VoiceProfile_TotalStats_column: Missing indices at param name = %s. |  |
| 2514 | `TR069_Get_VoiceProfile_column` | TR069_Get_VoiceProfile_column: Missing indices at param name = %s. |  |
| 2515 | `TR069_Get_VoiceService_Capabilities_column` | TR069_Get_VoiceService_Capabilities_column: Failed; no instance exist at parameter name=%s, pid=%d |  |
| 2516 | `TR069_Line_Codec_List_IsObjectExists` | TR069_Line_Codec_List_IsObjectExists: Missing indeces at param name = %s. |  |
| 2517 | `TR069_Line_Codec_List_NextInstance` | TR069_Line_Codec_List_NextInstance: Missing indeces at param name = %s. |  |
| 2518 | `TR069_Line_IsObjectExists` | TR069_Line_IsObjectExists: Missing indeces at param name = %s. |  |
| 2519 | `TR069_Line_NextInstance` | TR069_Line_NextInstance: Missing indeces at param name = %s. |  |
| 2520 | `TR069_Line_Session_IsObjectExists` | TR069_Line_Session_IsObjectExists: Missing indeces at param name = %s. |  |
| 2521 | `TR069_Line_Session_NextInstance` | TR069_Line_Session_NextInstance: Missing indeces at param name = %s. |  |
| 2522 | `TR069_Set_Line_CallingFeatures_column` | TR069_Set_Line_CallingFeatures_column: Missing indeces at param name = %s. |  |
| 2523 | `TR069_Set_Line_Codec_List_column` | TR069_Set_Line_Codec_List_column: Missing indeces at param name = %s. |  |
| 2524 | `TR069_Set_Line_VoiceProcessing_column` | TR069_Set_Line_VoiceProcessing_column: Missing indeces at param name = %s. |  |
| 2525 | `TR069_Set_VoiceProfile_FaxT38_column` | TR069_Set_VoiceProfile_FaxT38_column: Missing indeces at param name = %s. |  |
| 2526 | `TR069_Set_VoiceProfile_Line_SIP_column` | TR069_Set_VoiceProfile_Line_SIP_column: Missing indeces at param name = %s. |  |
| 2527 | `TR069_Set_VoiceProfile_Line_column` | TR069_Set_VoiceProfile_Line_column: Missing indeces at param name = %s. |  |
| 2528 | `TR069_Set_VoiceProfile_NumberingPlan_column` | TR069_Set_VoiceProfile_NumberingPlan_column: Missing indices at param name = %s. |  |
| 2529 | `TR069_Set_VoiceProfile_RTP_RTCP_column` | TR069_Set_VoiceProfile_RTP_RTCP_column: Missing indices at param name = %s. |  |
| 2530 | `TR069_Set_VoiceProfile_RTP_Redundancy_column` | TR069_Set_VoiceProfile_RTP_Redundancy_column: Missing indices at param name = %s. |  |
| 2531 | `TR069_Set_VoiceProfile_RTP_SRTP_column` | TR069_Set_VoiceProfile_RTP_SRTP_column: Missing indices at param name = %s. |  |
| 2532 | `TR069_Set_VoiceProfile_RTP_column` | TR069_Set_VoiceProfile_RTP_column: Failed; parameter name=%s, new pv=%s. |  |
| 2533 | `TR069_Set_VoiceProfile_SIP_column` | TR069_Set_VoiceProfile_SIP_column: Missing indices at param name = %s. |  |
| 2534 | `TR069_Set_VoiceProfile_column` | TR069_Set_VoiceProfile_column: Missing indices at param name = %s. |  |
| 2535 | `TR069_VoiceProfile_IsObjectExists` | TR069_VoiceProfile_IsObjectExists: Missing indices at param name = %s. |  |
| 2536 | `TR069_VoiceProfile_NextInstance` | TR069_VoiceProfile_NextInstance: Missing indices at param name = %s. |  |
| 2537 | `TR069_VoiceService_IsObjectExists` | TR069_VoiceService_IsObjectExists: No instance exists for param name = %s. |  |
| 2538 | `TR069_WAN` | TR069: wrong Interface Name = %s |  |
| 2539 | `TR104` | GWAPP Command Shell Added |  |
| 2540 | `TRACE` | Stop print trace for all error codes |  |
| 2541 | `TRANSCODINGID` | SIP Transcoding ID |  |
| 2542 | `TRANSCODINGMODE` | Transcoding mode | Only If Required /0,Force /1 |
| 2543 | `TRANSFERCAPABILITYFORDATACALLS` | 0: ISDN Transfer Capability for data calls will be 64k unrestricted (data), 1:ISDN Transfer Capability  for Data call... | 64k unrestricted /0,According to ISDNTransferCapability /1 |
| 2544 | `TRANSPARENTCODERONDATACALL` | In case the transfer capability of a call from ISDN is data open with transparent coder |  |
| 2545 | `TRANSPARENTCODERPRESENTATION` | Transparent Code Presentation | Clear Mode /0,X-CCD /1 |
| 2546 | `TRANSPARENTPAYLOADTYPE` | Transparent payload type - default:56 |  |
| 2547 | `TRANSPORT` | ERROR: Unknown transport type! |  |
| 2548 | `TRAPMANAGERHOSTNAME` | Read Only |  |
| 2549 | `TRECK` | Number of TRECK Warnings - was set |  |
| 2550 | `TRUNK` | ERROR: parameter dstObj is wrong |  |
| 2551 | `TRUNKALARMCALLDISCONNECTTIMEOUT` | Trunk alarm call disconnect timeout in seconds |  |
| 2552 | `TRUNKRESTARTMODEONPOWERUP` | Trunk Restart Mode on Power Up. | No restart/0,Per trunk/1,Per B-channel/2 |
| 2553 | `TRUNKSTATUSREPORTINGMODE` | When TrunkGroup #1 is present and active response to options and/or send keep-alive to associated proxy(ies) | Don't Care/0,Don't reply Options/1,Don't send Keep-Alive/2,Don't reply and send/3 |
| 2554 | `TRUNKTRANSFERMODE` | The type of transfer the PSTN/PBX supports | None /0,CAS NFA /1,ISDN /2,CAS Normal /3,QSIG Signal Step /4,ISDN Inband /5,AT&T OOD Blind /6 |
| 2555 | `TTYTRANSPORTTYPE` | Defines the transferring method of TTY signals over the network. | Disable /0,Inband_Relay /2 |
| 2556 | `TXRTPSEQUENCENUMBER` | Sets the starting sequence number of RTP activated channels on the board. Set to 0 to randomly set the RTP starting SN. |  |
| 2557 | `TacPlusAccountingEnable` | Enable/disable TACACS+ accounting |  |
| 2558 | `TacPlusAuthorizationEnable` | Enable/disable TACACS+ command authorization |  |
| 2559 | `TacPlusAutoAuthorization_c` | Automatically authorize the CLI session (enable mode) |  |
| 2560 | `TacPlusBehaviorUponTimeout_c` | Enable fallback to local password verification if TACACS+ does not respond. |  |
| 2561 | `TacPlusCmdAccountingEnable` | Enable/disable TACACS+ command accounting |  |
| 2562 | `TacPlusEnable` | Enable/disable TACACS+ CLI login |  |
| 2563 | `TacPlusErrorMeansFail` | Interpret TACACS+ error response as login failure |  |
| 2564 | `TacPlusLoginAccountingEnable` | Enable/disable TACACS+ session accounting |  |
| 2565 | `TacPlusLoginAuthorizationEnable` | Enable/disable TACACS+ session authorization |  |
| 2566 | `TacPlusPort` | TACACS+ authentication port |  |
| 2567 | `TacPlusSecondaryServerIp` | TACACS+ authentication server secondary IP address |  |
| 2568 | `TacPlusServerIp` | TACACS+ authentication server primary IP address |  |
| 2569 | `TacPlusSharedSecret` | TACACS+ shared secret between client and server |  |
| 2570 | `TacPlusTimeout` | TACACS+ Response Timeout, in seconds |  |
| 2571 | `TargetMG_ResponseTime` | Defines the time from the arrival of a call set-up request until the response  (in msec). |  |
| 2572 | `TdmRecordParameters` | TDM signals record parameters |  |
| 2573 | `TelDisconnectCode` | Disconnect call if digit string is received from the TEL side during session |  |
| 2574 | `TelProCoderGroup` | Default Coder Group |  |
| 2575 | `TelProfileIndex1` | Profile Parameters |  |
| 2576 | `TelnetAccessList` | ACL identifier for telnet access on MSBG products. |  |
| 2577 | `TelnetClient` | Open telnet connection |  |
| 2578 | `TelnetMaxSessions` | Configures the maximum allowed number of Telnet sessions. |  |
| 2579 | `TelnetServerEnable` | Enables / disables regular or secured embedded Telnet server. | Disable/0,Enable Unsecured/1,Enable Secured/2 |
| 2580 | `TelnetServerIdleDisconnect` | Sets the timeout for disconnection of an idle Telnet session (minutes). |  |
| 2581 | `TelnetServerVerifyPeerCertificate` | Determines whether to enable the verification of peer (client) certificates. | Disable/0,Require and verify/1 |
| 2582 | `Terminating` | Terminating (%d) |  |
| 2583 | `TerminationSide` | Sets the ISDN termination side. | acUSER_TERMINATION_SIDE/0,acNETWORK_TERMINATION_SIDE/1 |
| 2584 | `Test` | CList::CList - Allocation Exception |  |
| 2585 | `Test3` | CString::_Cat -  length error |  |
| 2586 | `TestDevice` | Test security device |  |
| 2587 | `TestEndPoint` | Service channel |  |
| 2588 | `TestMode` | Defines the type of testing mode applied. | CoderLoopback/0,PCMLoopback/1,ToneInjection/2,NoLoopback/3 |
| 2589 | `TestTelLink` | TestTelLink: Session already released. |  |
| 2590 | `TestTelLink_Session` | CHashMap::CHashMap - Allocation Exception |  |
| 2591 | `Test_Call_ActiveCalls` | Current active calls |  |
| 2592 | `Test_Call_ApplicationType` | Application type | gw-ip-to-ip/0,sbc/2 |
| 2593 | `Test_Call_AutoRegister` | Auto register |  |
| 2594 | `Test_Call_AverageCPS` | Average calls per second |  |
| 2595 | `Test_Call_CallAttempts` | Total call attempts |  |
| 2596 | `Test_Call_CallDuration` | Call duration in seconds (-1 for auto, 0 for infinite) |  |
| 2597 | `Test_Call_CallParty` | Test call party - i.e. Caller or Called | Caller/0,Called/1 |
| 2598 | `Test_Call_CalledURI` | Called URI |  |
| 2599 | `Test_Call_CallsPerSecond` | Calls per second |  |
| 2600 | `Test_Call_DestAddress` | Destination address and optional port |  |
| 2601 | `Test_Call_DestTransportType` | Destination transport type | udp/0,tcp/1,tls/2,not-configured/-1 |
| 2602 | `Test_Call_ElapsedTime` | Elapsed time since last session beginning or stats reset |  |
| 2603 | `Test_Call_EndpointURI` | Endpoint URI (can be either 'user' or 'user@host') |  |
| 2604 | `Test_Call_EstablishedCalls` | Total established calls |  |
| 2605 | `Test_Call_FailedAttempts` | Total failed attempts |  |
| 2606 | `Test_Call_IPGroupID` | IP Group ID |  |
| 2607 | `Test_Call_MaxChannels` | Maximum concurrent channels for session |  |
| 2608 | `Test_Call_MinChannels` | Minimum concurrent channels for session |  |
| 2609 | `Test_Call_Password` | Password for registration |  |
| 2610 | `Test_Call_Play` | Playback mode | Disable/0,DTMF/1 |
| 2611 | `Test_Call_RemoteDisconnects` | Remote disconnections |  |
| 2612 | `Test_Call_RouteBy` | Routing method. Affects both incoming and outgoing calls. For IP Group, calls are matched by (or routed to) IPGroupID... | GW Tel2IP/0,IP Group/1,Dest Address/2 |
| 2613 | `Test_Call_ScheduleInterval` | 0 disables scheduling, any positive number defines the inetrval between scheduled calls in minutes |  |
| 2614 | `Test_Call_TestDuration` | Test duration (minutes) |  |
| 2615 | `Test_Call_TestMode` | Test mode | Once/0,Continuous/1 |
| 2616 | `Test_Call_TestStatus` | Detailed status for current test |  |
| 2617 | `Test_Call_TestSummary` | Short summary of current test status (Idle, Running...) |  |
| 2618 | `Test_Call_UserName` | User name for registration |  |
| 2619 | `TextOverlay` | Text overlay buffer pool allocation failed. |  |
| 2620 | `TftpClnt` | TFTP Socket error %d |  |
| 2621 | `ThirdIpAddress` | Third IP Address |  |
| 2622 | `TimeBeforeReorderTone` | Delay time before playing Reorder tone |  |
| 2623 | `TimeOut` | Cancel Graceful Operation | /ResetBoard@100,100,0 |
| 2624 | `TimeToSampleAnalogLineVoltage` | Determines the time to sample the analog line voltage after offhook, for the current disconnect threshold. |  |
| 2625 | `Timeout` | ARP manager internal error |  |
| 2626 | `TimeoutToRelatchRTPMsec` | If a channel latched on an incoming RTP stream, it cannot relatch on another one until no packets of the old stream a... |  |
| 2627 | `TimeoutToRelatchSRTPMsec` | If a channel latched on an incoming SRTP stream, it cannot relatch on another one until no packets of the old stream ... |  |
| 2628 | `Timer` | Ptr:%p, Type:%d, ConfigTimeStamp:%u, ExpireFunction:%p %s |  |
| 2629 | `TimerTExpired` | AcSIPCall::HandleTimerTExpiredEvent - No relevant transactions (Reinvite or Update) |  |
| 2630 | `TlntServer` | Telnet error: can't get socket! %d |  |
| 2631 | `ToggleAutoBuffering` | Toggle automatic buffering and MORE prompts. |  |
| 2632 | `Tone` | CStreamingData::Stream Added %s %s |  |
| 2633 | `TpncpNatTraversalMode` | Indicates that the device should initiate the connection to the TPNCP host. |  |
| 2634 | `TpncpNatTraversalPassword` | Selects a password for authentication with the TPNCP host. |  |
| 2635 | `Tr069AcsUrlProvisioningMode` | Determines whether ACS URL will be acquired using DHCP option #43 or will be configured by a user. | Manual/0,Automatic/1 |
| 2636 | `TransactionIDBase` | Defines the minimum number for the transaction ID. |  |
| 2637 | `TransactionIDRange` | Defines range for the transaction ID. |  |
| 2638 | `Transcode` | PCIIFChangeChannelParams(): Enabling RTCP-XR will be ignored due to blocking by feature key or QOE server is disconne... |  |
| 2639 | `TransferringState` | BlindTransferMngr::HandleCoreEv: %s- State is:%s Call:#%d |  |
| 2640 | `Transparent` | INFO - Cisco |  |
| 2641 | `TransparentCoderPayloadType` | Alternative payload type used when using transparent coder. |  |
| 2642 | `TransportType` | Not Configured |  |
| 2643 | `TrueRandomBufferSelfTest` | TrueRandomBufferSelfTest . |  |
| 2644 | `TrunkGroupName` | Trunk Group Name |  |
| 2645 | `TrunkName` | Together with 'EndpointPrefix' field, generates local endpoint name on trunk enabled gateways. |  |
| 2646 | `TrunkTestTermPattern` | Defines the name pattern of a trunk test termination. |  |
| 2647 | `TrunkTestURL` | Defines the VXML trunk testing URL. |  |
| 2648 | `TrunkingToAnalogFunctionalityProfile` | Defines the Trunking to Analog Functionality Profile. | acTrunkingToAnalogFunctionalityProfile_Disable /0,acTrunkingToAnalogFunctionalityProfile_CASAnalo... |
| 2649 | `TxDtmfHangOverTime` | Voice Silence time on the Network side after generating DTMF or MF digits arriving from the TDM side as Telephony Eve... |  |
| 2650 | `UDTDETECTORFREQUENCYDEVIATION` | Defines the frequency deviation allowed for the detection of UDT (User Defined Tones) [Hz]. |  |
| 2651 | `UDTDETECTORSNR` | Defines the value of which UDT Signals with a Signal To Noise Ratio below this value will not be detected. Units are ... |  |
| 2652 | `UDTLowEnergyThreshold` | Minimum energy level of a single UDT component to be detected (units: -dBm). |  |
| 2653 | `UNAUTHENTICATED_SRTP` | SBCFaxCodersList::Remove failed - invalid index |  |
| 2654 | `UNKNOWN` | SIGNALS: HAL: Enabled Media Type doesn't match with the file Media Type. File Media Type is AUDIO when Enable Media T... |  |
| 2655 | `UNLOCK` | UNLOCKED action failed - graceful reset process cancelled |  |
| 2656 | `UNLOCKED` | Shutting Down |  |
| 2657 | `UNREGISTRATIONMODE` | If explicit unregister needed |  |
| 2658 | `UP_13` | ESP Processing |  |
| 2659 | `USEALTROUTEREASONSFOR3XX` | Use Alt Route Reasons Table For 3xx | No /0,No if 6xx /1,Yes /2 |
| 2660 | `USEAORINREFERTOHEADER` | If enabled, we will use URI from To/From headers in Refer-To header. If disabled, we will take the URI from Contact |  |
| 2661 | `USEBRACKETSWITHDIGITSTRING` | Enables digit map strings to be encapsulated inside brackets. |  |
| 2662 | `USEBROADSOFTDTG` | Use DTG parameter 0 - disable [Default] , 1 -Enable |  |
| 2663 | `USEDESTINATIONASCONNECTEDNUMBER` | Use Destination As Connected Number |  |
| 2664 | `USEDIFFERENTRTPPORTAFTERHOLD` | Use different RTP port after Hold |  |
| 2665 | `USEDIGITFORSPECIALDTMF` | Indicates whether a special DTMF, sent with INFO(Cisco), is sent using its digit representation or not. | Special /0,Numeric /1 |
| 2666 | `USEEPNUMASCALLINGNUMIP2TEL` | Use EndPoint Number As Calling Number IP2Tel |  |
| 2667 | `USEEPNUMASCALLINGNUMTEL2IP` | Use EndPoint Number As Calling Number Tel2IP |  |
| 2668 | `USEGATEWAYNAMEFOROPTIONS` | Use Gateway name (instead of IP address) in Keep-Alive OPTIONS messages | No /0,Yes /1,Server /2 |
| 2669 | `USEHOSTNAMEFORCONTACT` | When set, the contact header will contain Gateway name instead of IP address |  |
| 2670 | `USEPINGPONGKEEPALIVE` | Use Ping-Pong for Keep-Alive to proxy via reliable connection |  |
| 2671 | `USEPROXYIPASHOST` | Whether or not to use the Proxy IP as Host in From and To headers |  |
| 2672 | `USERADLOG` | RadVision printout tool |  |
| 2673 | `USERAGENTDISPLAYINFO` | String that will be displayed in the SIP Header 'User-Agent' or 'Server' |  |
| 2674 | `USERDEF` | Non Initialized record! |  |
| 2675 | `USERINACTIVITYTIMER` | Defines the time, in days, which afterward the user becomes inactive .Inactive user can become active only by securit... |  |
| 2676 | `USERINFOFILENAME` | The file name to be loaded using TFTP |  |
| 2677 | `USERNAME` | User Name used for authentication |  |
| 2678 | `USERSPACESIGNMODE` | Indicates whether replace space in phone number to '_'  or escape sequence %20 | Underscore/0,Escape/1 |
| 2679 | `USESIPTGRP` | Use TGRP parameter 0 - disable [Default] , 1 - send only , 2 - send and use if in the RequestURI when receiving INVITE. | Disable /0,Send Only /1,Send & Receive /2,Hotline /3,Hotline Extended /4 |
| 2680 | `USESIPURIFORDIVERSIONHEADER` | Use Tel uri or Sip uri for Diversion header |  |
| 2681 | `USETELURIFORASSERTEDID` | Use Tel uri or Sip uri forP-Asserted or P-Preferred headers |  |
| 2682 | `USETransparentCoderWithHBR` | Transparent coder with HBR. |  |
| 2683 | `Unauthorized` | Correct authorization is required for this area. Either your browser does not perform authorization, or your authoriz... |  |
| 2684 | `Unavailable` | QOS Low |  |
| 2685 | `Unconditional` | No Answer |  |
| 2686 | `Unknown` | SIPStackSession::AddDigitToBuffer - Buffer is full. Can not add digit to buffer |  |
| 2687 | `UnknownCoder` | Microsoft-RTA (WB) |  |
| 2688 | `UnknownManagedObject` | CPool::CPool - Allocation Exception |  |
| 2689 | `UnregisterAll` | UnregisterIpEntry failed: |  |
| 2690 | `Unused` | PL[percent]:%d DELAY[msec]:%d |  |
| 2691 | `UpdateMinutes` | ApplyDayLightSavingTime: Error %d |  |
| 2692 | `Upgrade` | Invalid download file type |  |
| 2693 | `Upload` | Run %s transfer %s |  |
| 2694 | `UseAccurateInternalClock` | 6310 board with ALC - if the internal clock (20ppm) is selected and this patameter is on ALC 4.6 ppm, the clock is to... |  |
| 2695 | `UseBRacketsWithGatewayName` | Determines whether the gateway name takes the board IP address with added brackets. |  |
| 2696 | `UseLogoInWeb` | Change Logo |  |
| 2697 | `UseNewFormatCoderNegotiation` | Disables the response of all coders and descriptions in CRCX/MDCX without coder and SDP. |  |
| 2698 | `UseProductName` | Activates the userProductName parameter. |  |
| 2699 | `UseRProductName` | Changes the default AudioCodes product name to a convenient user name. |  |
| 2700 | `UseRangeEndpointsWithRSIP` | Use range carding with RSIP e.g. RSIP 1234 ACGw[ep1-ep2]@AUDC.com |  |
| 2701 | `UseWeblogo` | Enables the webLogoText string to override any loaded logo image file. |  |
| 2702 | `UseWildCardWithRSIP` | When wildcard is used, RSIPs turn in a single message on EndPoint Naming configuration, and single message for each t... |  |
| 2703 | `Used` | Used      gratuitous ARP transmitted for each VLAN-IP-address pair. i.e. 3 frames. |  |
| 2704 | `User` | EEPROM: Invalid Special parameters. All Special BoardParams were taken default |  |
| 2705 | `UserAccessLevel_get` | Change Access Level |  |
| 2706 | `UserDefinedToneDetectorEnable` | Enables or disables detection of User Defined Tones. |  |
| 2707 | `UserId` | User Name |  |
| 2708 | `UserInfoFileUpdateTime` | Internal parameter |  |
| 2709 | `UserInfoFileUrl` | Provides a link to the user information file, to be downloaded using Automatic Update. |  |
| 2710 | `UserInfoResource` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 2711 | `V1501ARR` | ARR - Automatic Retrain Renegotiation control. |  |
| 2712 | `V1501AllocationProfile` | Selects the V.150.1 profile. | CE_MINUS_9_5/0,CE_MINUS_12/1,CE_MINUS_15/2,CE_MINUS_1/3 |
| 2713 | `V1501SPRTPayloadTypeTx` | Transimtted V.150.1 SPRT payload type. |  |
| 2714 | `V1501SPRTTransportChannel0MaxPayloadSize` | V.150.1 SPRT transport channel 0 max payload size. |  |
| 2715 | `V1501SPRTTransportChannel2MaxPayloadSize` | V.150.1 SPRT transport channel 2 max payload size. |  |
| 2716 | `V1501SPRTTransportChannel2MaxWindowSize` | V.150.1 SPRT transport channel 2 max window size. |  |
| 2717 | `V1501SPRTTransportChannel3MaxPayloadSize` | V.150.1 SPRT transport channel 3 max payload size. |  |
| 2718 | `V1501SSEPAYLOADTYPERX` | Configuration::InsertIntVal- Unhandled parameter %s |  |
| 2719 | `V1501SSEPayloadTypeRx` | Received V.1501.1 SSE RTP payload type. |  |
| 2720 | `V1501SSEPayloadTypeTx` | Transmitted V.150.1 SSE RTP Payload Type. |  |
| 2721 | `V1501SSERedundancyDepth` | V.150.1 SSE redundancy depth. |  |
| 2722 | `V21ModemTransportType` | Sets the V.21 modem transport method. | Disable/0,Enable Bypass/2,Events Only/3 |
| 2723 | `V22ModemTransportType` | Sets the V.22 modem transport method. |  |
| 2724 | `V23ModemTransportType` | Sets the V.23 modem transport method. |  |
| 2725 | `V32ModemTransportType` | Sets the V.32 modem transport method. | disable/0,bypass/2,events-only/3,ans-mute/4 |
| 2726 | `V34FAXTRANSPORTTYPE` | Determines the V.34 fax transport method. | Disable/0,RelayEnable/1,ByPassEnable/2,EventsOnly/3 |
| 2727 | `V34ModemTransportType` | Sets the V.34 modem transport method. | disable/0,relay/1,bypass/2,events-only/3,ans-mute/4 |
| 2728 | `V52_FILE` | Load File | /AuxilaryFilesHidden@100,100,0 |
| 2729 | `V5PortConfigurationFileName` | Indicates the name and location of the V5 Port Configuration file. |  |
| 2730 | `V5PortConfigurationFileURL` | Provides a link to a software (V5PortConfiguration file) to be downloaded from a remote server. |  |
| 2731 | `VARIABLE_WEEKDAY` | No match to any known type |  |
| 2732 | `VBRCoderHangover` | EVRC: number of silence frames at the beginning of each silence period. |  |
| 2733 | `VBRCoderHeaderFormat` | Determines the header format of the EVRC codec. | WithOut_RFC2658Interleaving_And_TOC/0,Including_RFC2658Interleaving_And_TOC/1,Including_TOC_Only/... |
| 2734 | `VBRCoderNoiseSuppressionEnable` | For activating specail VBR coder noise suppression algorithm. |  |
| 2735 | `VEDenialOfServiceMaxThresholdPercent` | Enable Voice denial of service functionality. |  |
| 2736 | `VEDenialOfServiceMinThresholdPercent` | Set Voice denial of service max threshold before give up CPU, in Percentage. |  |
| 2737 | `VERIFYRECIEVEDREQUESTURI` | Defines whether or not to verify RequestURI Header in Requests |  |
| 2738 | `VERIFYRECIEVEDVIA` | Defines whether or not to verify Source IP with IP in Topmost VIA |  |
| 2739 | `VERIFYSERVERCERTIFICATE` | Certificate validation behavior 0 - No certificate validation. 1 - Server certificate validation. |  |
| 2740 | `VLANBRONZESERVICECLASSPRIORITY` | Sets the priority for the Bronze service class content. |  |
| 2741 | `VLANCONTROLVLANID` | Sets the control VLAN identifier. |  |
| 2742 | `VLANGOLDSERVICECLASSPRIORITY` | Sets the priority for the Gold service class content. |  |
| 2743 | `VLANHEARTBEATVLANID` | Sets the  heartbeat stream VLAN identifier. |  |
| 2744 | `VLANMEDIAVLANID` | Sets the media VLAN identifier. |  |
| 2745 | `VLANMODE` | Sets the VLAN functionality. |  |
| 2746 | `VLANNATIVEVLANID` | Sets the native VLAN identifier. |  |
| 2747 | `VLANNETWORKSERVICECLASSPRIORITY` | Sets the priority for Network service class content. |  |
| 2748 | `VLANOAMVLANID` | Sets the OAMP (Operation, Administration, Management and Provisioning) VLAN identifier. |  |
| 2749 | `VLANPREMIUMSERVICECLASSCONTROLPRIORITY` | Sets the priority for the Premium service class content and control traffic. |  |
| 2750 | `VLANPREMIUMSERVICECLASSMEDIAPRIORITY` | Sets the priority for the Premium service class content and media traffic. |  |
| 2751 | `VOCONF` | Conferencing not supported on this board. |  |
| 2752 | `VPDATAENDPOINTER` | Invalid Parameter for "Set" |  |
| 2753 | `VQMONENABLE` | Sets voice quality monitoring (RTCP-XR) mode. | disable/0,full/1,calculation-only/2 |
| 2754 | `VXMLFIleName` | Indicates the name (and path) of the file containing the VXML file. |  |
| 2755 | `VXMLID` | Identification of VoiceXML call (To be used by SIP INVITE) |  |
| 2756 | `Validity` | Not Before: |  |
| 2757 | `VcidAllocationMethod` | The VCID allocation method to allocate VCID's from a FIFO and LIFO. | LIFO_ALLOCATION_METHOD/0,FIFO_ALLOCATION_METHOD/1 |
| 2758 | `Version` | 3 Vendor Configuration File |  |
| 2759 | `Versions` | Loaded Files |  |
| 2760 | `VideoFontFileUrl` | Indicates the URL for downloading a logo file for the web interface. |  |
| 2761 | `VideoGraphicsOverlayNumOfObjects` | Indicates the number of video graphics overlay objects. |  |
| 2762 | `VideoTargetBitrate` | Sets the target output bit rate. |  |
| 2763 | `Voice` | GetCallForCallIndex call:#%d |  |
| 2764 | `VoiceMailInterface` | Selects the method of communication between PBX and the Gateway, that is used instead of legacy voicemail | None /0,DTMF /1,SMDI /2,QSIG /3,SETUP Only /4,QSIG_Matra/5,QSIG_SIEMENS /6,IP2IP /7,ETSI /8,NI2/9 |
| 2765 | `VoiceMenuPassword` | Sets the password for the voice menu, used for configuration and status. |  |
| 2766 | `VoicePayloadFormat` | Sets the G.726 voice Payload Format. | VoicePayloadFormatRTP/0,VoicePayloadFormatATM/1 |
| 2767 | `VoicePromptsFileName` | Defines the name (and path) of the file containing the voice prompts. |  |
| 2768 | `VoiceStreamServerIP` | Defines the IP address of the default Web Server used for play and record of streaming audio. |  |
| 2769 | `VoiceStreamServerPort` | Port number of the default Web Server used for play and record of streaming audio. |  |
| 2770 | `VoiceStreamUploadMethod` | Defines the HTTP request type for uploading the voice stream to the file server. | post/0,put/1 |
| 2771 | `VoiceStreamUploadPostUri` | Defines URI used on  POST request, to upload voice data from  media server to a web server. |  |
| 2772 | `VoiceVolume` | Defines the voice TDM output gain [dB] |  |
| 2773 | `VpFileLastUpdateTime` | Saves the HTTP update time of the vp file (internal). |  |
| 2774 | `VpFileUrl` | Provides a link to a Voice Prompts file to be downloaded from a remote server. |  |
| 2775 | `VxmlBargeInAllowed` | VXML property that indicates if prompts can be interrupted. |  |
| 2776 | `VxmlBuiltinGrammarPath` | Defines the path on the ASR/TTS server to access the built-in grammars. |  |
| 2777 | `VxmlCompleteTimeout` | Defines the amount of silence in milliseconds to wait after a speech grammar has been matched before reporting the ma... |  |
| 2778 | `VxmlConfidenceLevel` | Defines the default speech recognition confidence threshold for VXML. |  |
| 2779 | `VxmlDefaultLanguage` | Defines the default language for speech recognition (if speech recognition is enabled). |  |
| 2780 | `VxmlIncompleteTimeout` | Defines the amount of silence in milliseconds to wait after speech that has not matched a voice grammar. |  |
| 2781 | `VxmlInterDigitTimeout` | Defines the interdigit timeout value used in DTMF input. |  |
| 2782 | `VxmlMaxActiveFiles` | Indicates the maximum number of VXML scripts that can be loaded into the system at one time. |  |
| 2783 | `VxmlMaxPorts` | Defines the number of channels on the system that can be active at once running VXML scripts. |  |
| 2784 | `VxmlMaxSpeechTimeout` | Defines the maximum time the caller can speak, in miliseconds, in attempt to match a speech grammar before a no match... |  |
| 2785 | `VxmlNoInputTimeout` | Defines the input timeout for digit collection or speech recognition. |  |
| 2786 | `VxmlSensitivityLevel` | Defines the default speech recognition sensitivity level for VXML. |  |
| 2787 | `VxmlSpeedVsAccuracy` | Hint to the speech recognition for the balance of speed vs accuracy. |  |
| 2788 | `VxmlSystemInputModes` | Indicates which input types are valid for grammars: dtmf, voice, or both. |  |
| 2789 | `VxmlTermChar` | Defines the terminating digit for DTMF input. |  |
| 2790 | `VxmlTermTimeout` | Defines the time to wait before terminating dtmf input, in milliseconds. |  |
| 2791 | `WAITFORDIALTIME` | Time delay between seizing the line and start dialing (if ISWAITFORDIALTONE disabled) or after hookflash before dialing |  |
| 2792 | `WAITINGBEEPDURATION` | Call Waiting tone beep length (msec) |  |
| 2793 | `WAITINGCALLDENYMODE` | 0 - Normal behavior: 182-Queued, 603-Decline{@}1 - Special behavior: 180-Ringing, 486-Busy | Normal-182/0,Special-180/1 |
| 2794 | `WANBaseBucket` | Defines the WAN Base Bucket for limit the Rx by the feature key. |  |
| 2795 | `WEBACCESSLIST` | Allows IP addresses to connect to the Web interface. |  |
| 2796 | `WEBAccessAction` | WEB Access action. |  |
| 2797 | `WEBAccessRowStatus` | WEB Access row-status |  |
| 2798 | `WEBAccessUserCode` | WEB Access user code |  |
| 2799 | `WEBAccessUserName` | WEB Access user name |  |
| 2800 | `WEBHOSTEDBASENAME` | Hosted TP Base NIC Name(s). |  |
| 2801 | `WEBHOSTEDPCI1NAME` | Hosted TP PCI1 NIC Name(s). |  |
| 2802 | `WEBHOSTEDPCI2NAME` | Hosted TP PCI2 NIC Name(s). |  |
| 2803 | `WEBPRODUCTDESCRIPTION` | Board product description for web homepage display. |  |
| 2804 | `WEBPasswordControlViaSNMP` | Allowing the SNMP to change the WEBs username and password |  |
| 2805 | `WEBR` | Send radius request and wait for radius response. |  |
| 2806 | `WEBRADIUSLOGIN` | Use the RADIUS for management interfaces authentication. |  |
| 2807 | `WSRegistrationMode` | Per Gateway |  |
| 2808 | `WSTxDTMF` | Not Supported |  |
| 2809 | `WaitAllTasksTerminated` | All user tasks were terminated |  |
| 2810 | `WaitForBusyTime` | Time to wait to detect busy and reorder tones. Currently used in semi supervised PBX transfer |  |
| 2811 | `WanMgmtHttpPort` | Determines the WAN HTTP port of the device. |  |
| 2812 | `WanMgmtHttpsPort` | Determines the WAN HTTPS port of the device. |  |
| 2813 | `WanMgmtSSHPort` | Determines the WAN SSH port of the device. |  |
| 2814 | `WanMgmtSnmpPort` | This parameter specifies the WAN port number for SNMP requests and responses. |  |
| 2815 | `WanMgmtTelnetPort` | Determines the WAN Telnet port of the device. |  |
| 2816 | `WarningToneDuration` | OfHook Warning Tone Duration [Sec] |  |
| 2817 | `WatchdogStatus` | Enables or disables Watch dog 0-disable 1-Enable(default) |  |
| 2818 | `WebAccessList` | Activity Log: User Name: %s, Client bearing IP address %s requests to access the 'Web Access List' page. |  |
| 2819 | `WebAudit` | Start Web Audit: take care when file transfer in progress! |  |
| 2820 | `WebAuthMode` | Selects HTTP basic (clear text) or digest (MD5) authentication for the web interface. | Basic Mode/0,Web Based Authentication/1 |
| 2821 | `WebClearUserTable` | Reverts to legacy mode from web users table. |  |
| 2822 | `WebClntSock` | ConstructChildSocket error %d |  |
| 2823 | `WebDataAccessList` | ACL identifier for web access on MSBG products. |  |
| 2824 | `WebDebugLevel` | Sets the output level of WEB debug messages sent by the Gateway. |  |
| 2825 | `WebLogoFileUrl` | URL for downloading a logo file for the web interface. |  |
| 2826 | `WebLogoText` | Replaces default AudioCodes logo image with text. |  |
| 2827 | `WebMaxSimultaneousUsers` | Max simultaneous users for the web interface, ranges 0 - 5. 0 means unlimited. |  |
| 2828 | `WebMaxUserInstances` | Max simultaneous sessions per user, ranges 0 - 3. 0 Means unlimited. |  |
| 2829 | `WebPassChangeInterval` | The time allowed between password changes, in minutes. Range is 0-100000 while 0 means no restriction. |  |
| 2830 | `WebSessionTimeout` | The number of minutes before the user will be logged off automatically. 0 means no timeout. Up to 100000. |  |
| 2831 | `WebSrv` | WebServer: CreateSocket error %d |  |
| 2832 | `WebTlsClntSock` | ConstructChildSocket TLS error %d |  |
| 2833 | `Weight1` | Weight 1 |  |
| 2834 | `Weight2` | Weight 2 |  |
| 2835 | `Weight3` | Weight 3 |  |
| 2836 | `Winktime` | Time elapsed between two consecutive polarity reversals. |  |
| 2837 | `WsLockGracefulOption` | Not Available |  |
| 2838 | `XCHANNELHEADER` | 0 (default): No special header  1:Add special header for trunk and B-Channel |  |
| 2839 | `XFERPREFIX` | Prefix added to the called number of a transferred call |  |
| 2840 | `XFERPREFIXIP2TEL` | Prefix added to the called number of a transferred call (IP2Tel) |  |
| 2841 | `XFERSUCCESSTO` | Max time (in millisec) to wait for release an original call on transfer. Value -1 means that this timer not operated. |  |
| 2842 | `XMLFileName` | This parameter is used to indicate the name  of the file containing the XML file. |  |
| 2843 | `XmlFileLastUpdateTime` | Saves the HTTP update time of the XML file (internal). |  |
| 2844 | `ZEROIZE` | FIPS140 zeroization function to clear all secrets. |  |
| 2845 | `ZEROSDPHANDLING` | Zero connection information in SDP behavior | Zero SDP /0,Board IP /1 |
| 2846 | `acRFC2833RelayDecoderMute` | DTMF Transport Type:    %d-%s |  |
| 2847 | `acUserInputAlarmDescription` | Defines the Description of the input alarm. |  |
| 2848 | `acUserInputAlarmSeverity` | Defines the severity of the input alarm. |  |
| 2849 | `acceptableResponses` | Acceptable OCSP Responses |  |
| 2850 | `ad_timestamping` | AD Time Stamping |  |
| 2851 | `anonymous` | Replace Source Number: %s By userInfo number: %s |  |
| 2852 | `anyExtendedKeyUsage` | Any Extended Key Usage |  |
| 2853 | `anyPolicy` | X509v3 Any Policy |  |
| 2854 | `archiveCutoff` | OCSP Archive Cutoff |  |
| 2855 | `arrayType` | Found arrayType Parameter '%s' => '%s' |  |
| 2856 | `authorityInfoAccess` | Authority Information Access |  |
| 2857 | `authorityKeyIdentifier` | X509v3 Authority Key Identifier |  |
| 2858 | `badAlarmState` | Administrative state is unlocked |  |
| 2859 | `base64Binary` | Validator result: %d |  |
| 2860 | `basicConstraints` | X509v3 Basic Constraints |  |
| 2861 | `basicOCSPResponse` | Basic OCSP Response |  |
| 2862 | `biometricInfo` | Biometric Info |  |
| 2863 | `cRLSign` | Encipher Only |  |
| 2864 | `caIssuers` | CA Issuers |  |
| 2865 | `caRepository` | CA Repository |  |
| 2866 | `cb6cbdaad26cd210a8b31a5d56a876ee1d51a96c` | FIPS 2.0.12 validated module 16 Nov 2015 |  |
| 2867 | `certificateHold` | Remove From CRL |  |
| 2868 | `certificateIssuer` | X509v3 Certificate Issuer |  |
| 2869 | `certificatePolicies` | X509v3 Certificate Policies |  |
| 2870 | `cessationOfOperation` | Certificate Hold |  |
| 2871 | `clientAuth` | TLS Web Client Authentication |  |
| 2872 | `codeSigning` | Code Signing |  |
| 2873 | `compatible` | SSL Client |  |
| 2874 | `configure_leg` | SIPXmlParser::Machine - %s request is not supported |  |
| 2875 | `cpDIGITMAPLONGTIMER` | Defines the value in milliseconds of the inter-digit long timer (L symbol) in a digit map. |  |
| 2876 | `cpDIGITMAPSHORTTIMER` | Defines the value in milliseconds of the short timer (S symbol) in a digit map. |  |
| 2877 | `cpDefaultMediaRealmName` | Defines the default CP media realm in the media realm table |  |
| 2878 | `cpEndOfRecordCutTime` | The max amount of audio to cut from the end of a recording  (in msec). This is used to remove the DTMF signals genera... |  |
| 2879 | `cpEvLst` | Failed initializing EventList queue |  |
| 2880 | `cpGarbageCollectionTime` | The number of  days that  invalid Megaco context can exist before auto deletion. Value 0 (the default) means no auto ... |  |
| 2881 | `cpHal_Generate_ReversalPolarity` | Debug Max Level is: |  |
| 2882 | `cpHndlr` | HP FATAL: Pool(%s) too many elements. Request: MaxNumberOfHandlers=%d |  |
| 2883 | `cpMaxPacketsPerSecond` | The maximum CPU time for Control Protocol packets processing (per second). |  |
| 2884 | `cpPlayCoder` | Determines the coder type to be used when playing a file of type .raw . |  |
| 2885 | `cpPool` | POOL WARNING: Pool(%s) Too meny elements. Request: NumberOfSegment=%d,SegSize=%d |  |
| 2886 | `cpRecordCoder` | Determines the coder used for recording to all supported file types. |  |
| 2887 | `cpSendRTCPByePacket` | Determines  sending RTCP Bye Packet according to  ini file parameter: cpSendRTCPByePacket. |  |
| 2888 | `cpVQMonitoring_TcpChild` | Server socket error %d |  |
| 2889 | `cpVQMonitoring_TlsChild` | TLSServer socket error %d |  |
| 2890 | `critical` | Unexpected symbol '%c'. End of header expected |  |
| 2891 | `crlDistributionPoints` | X509v3 CRL Distribution Points |  |
| 2892 | `crlNumber` | X509v3 CRL Number |  |
| 2893 | `ct_cert_scts` | CT Certificate SCTs |  |
| 2894 | `ct_precert_poison` | CT Precertificate Poison |  |
| 2895 | `ct_precert_scts` | CT Precertificate SCTs |  |
| 2896 | `ct_precert_signer` | CT Precertificate Signer |  |
| 2897 | `cwmp_XXXXXX` | Wrapper file_remove |  |
| 2898 | `dataEncipherment` | Key Agreement |  |
| 2899 | `deltaCRL` | X509v3 Delta CRL Indicator |  |
| 2900 | `dh_Ys` | ASN.1Cert, length=%d |  |
| 2901 | `digitalSignature` | Non Repudiation |  |
| 2902 | `direction` | Device Side/0,Remote Side/1 |  |
| 2903 | `ecdh_Yc` | Unexpected Message |  |
| 2904 | `ecdsa_fixed_ecdh` | Premaster Secret |  |
| 2905 | `emailCA` | Object Signing CA |  |
| 2906 | `emailProtection` | E-mail Protection |  |
| 2907 | `encipherOnly` | Decipher Only |  |
| 2908 | `extReq` | Extension Request |  |
| 2909 | `extendedKeyUsage` | X509v3 Extended Key Usage |  |
| 2910 | `extendedStatus` | Extended OCSP Status |  |
| 2911 | `freshestCRL` | X509v3 Freshest CRL |  |
| 2912 | `g729AnnexAwAnnexB` | Type = %s |  |
| 2913 | `generate` | This action will erase the existing private key and certificate. |  |
| 2914 | `getciphersuite` | Can't get Cipher list %s |  |
| 2915 | `gost2001cc` | GOST 34.10-2001 Cryptocom |  |
| 2916 | `gost94cc` | GOST 34.10-94 Cryptocom |  |
| 2917 | `gwDeleteResourceEvent` | CHashMap::CHashMap - Allocation Exception |  |
| 2918 | `gwEventResource` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2919 | `gwHashTableItem` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 2920 | `gwLinkedListItem` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 2921 | `gwVideoCodersList` | GeneralRsrcMngr::GetNewObject Failed, Resource: %s, m_IdsPool = 0x%p, m_Pool = 0x%p |  |
| 2922 | `haU761yJla` | No pattern set |  |
| 2923 | `hlgr_flow` | GwAlarmMngr::SetAlarm: Invalid gwSNMPMOId=%d Trap=%d ID=%d %s |  |
| 2924 | `holdInstructionCallIssuer` | Hold Instruction Call Issuer |  |
| 2925 | `holdInstructionCode` | Hold Instruction Code |  |
| 2926 | `holdInstructionNone` | Hold Instruction None |  |
| 2927 | `holdInstructionReject` | Hold Instruction Reject |  |
| 2928 | `ifAlias` | Interface's alias; ifAlias MIB object. |  |
| 2929 | `ifIkeParsePhase1Id` | Not supported ID payload |  |
| 2930 | `ifName` | Interface Alias. |  |
| 2931 | `inactive` | GeneralRsrcMngr<%s>::AllocateObjectByIndex: Illegal index %d |  |
| 2932 | `inhibitAnyPolicy` | X509v3 Inhibit Any Policy |  |
| 2933 | `initialize` | Half Duplex |  |
| 2934 | `initiate` | Initiate during reconnect, req-id=%d |  |
| 2935 | `invalidityDate` | Invalidity Date |  |
| 2936 | `ipsecEndSystem` | IPSec End System |  |
| 2937 | `ipsecTunnel` | IPSec Tunnel |  |
| 2938 | `ipsecUser` | IPSec User |  |
| 2939 | `issuerAltName` | X509v3 Issuer Alternative Name |  |
| 2940 | `issuingDistributionPoint` | X509v3 Issuing Distrubution Point |  |
| 2941 | `keyAgreement` | Certificate Sign |  |
| 2942 | `keyCertSign` | CRL Sign |  |
| 2943 | `keyCompromise` | CA Compromise |  |
| 2944 | `keyEncipherment` | Data Encipherment |  |
| 2945 | `keyUsage` | X509v3 Key Usage |  |
| 2946 | `lgr_CmdSh` | Max Board Events = %d  Max Stack Events = %d  LockErr:%d |  |
| 2947 | `lgr_PSOSsemaphore` | The name of semaphore should be at most four char(%s) |  |
| 2948 | `lgr_RingToHuntGroup` | Cannot allocate RingToHuntGroup feature no more resources!!!! |  |
| 2949 | `lgr_TrnkGrp` | TrunkGroup::TrunkGroup - failed to allocte m_TrunkInfo [%d] |  |
| 2950 | `lgr_aaa_mngr` | Cannot allocate AAA feature no more resources!!!! |  |
| 2951 | `lgr_blind_transfer_mngr` | Cannot allocate Blind Transfer feature no more resources!!!! |  |
| 2952 | `lgr_call_feature` | Cannot allocate Call feature no more resources!!!! |  |
| 2953 | `lgr_cdr_writer` | SendRadiusReportIfEnabled - failed to send Radius Accounting Request |  |
| 2954 | `lgr_coders_list` | ACCodersList::Add failed m_CodersArray is full |  |
| 2955 | `lgr_conf` | ProxyIpListRefreshTime_conditionalCheck- can not set value %ld |  |
| 2956 | `lgr_default` | In LoggingFilters, TrunkId/FXS/FXO cannot have value 0, filter ignored |  |
| 2957 | `lgr_digitmap_mngr` | No EndPoint For DigitMapMngr Cannot Activate... |  |
| 2958 | `lgr_dns_resolver` | HandleARecordQuery- can't handle 2 name resolution at the same time |  |
| 2959 | `lgr_dtmf_options_list` | ACDtmfOptionsList::Add failed m_DtmfSupportArray is full |  |
| 2960 | `lgr_endpoint` | EndPoint::MediaResourceList Perform FORCE Deallocation of port: Realm:%d port:%d current allocations:%d |  |
| 2961 | `lgr_feature_mngr` | FeatureMngr::RegisterFeature: feature index (%d) is out of bound |  |
| 2962 | `lgr_flow` | Error creating ProxyFaultCatalog |  |
| 2963 | `lgr_freeid` | Pop free id: id=%d |  |
| 2964 | `lgr_fwd_mngr` | Cannot allocate Forward feature no more resources!!!! |  |
| 2965 | `lgr_fxs_conf_mngr` | Cannot allocate FXS Conference feature no more resources!!!! |  |
| 2966 | `lgr_gw_ldap` | Cannot allocate MS LDAP Calling Name feature no more resources!!!! |  |
| 2967 | `lgr_gwapp_ha` | Invalid TranslationData! |  |
| 2968 | `lgr_hline_mngr` | Cannot allocate Hot Line feature no more resources!!!! |  |
| 2969 | `lgr_hold_mngr` | Cannot allocate Hold feature no more resources!!!! |  |
| 2970 | `lgr_ipconn` | IPConn#%d ERROR: %s Par:%d |  |
| 2971 | `lgr_join_mngr` | Cannot allocate Join feature no more resources!!!! |  |
| 2972 | `lgr_maintask` | BYE BYE - GW finished |  |
| 2973 | `lgr_manipulation` | StringManipulation::Apply - Trying to remove %d from left from string %s |  |
| 2974 | `lgr_media_service` | CStreamingData Returned to Pool ResourceID: %d |  |
| 2975 | `lgr_metering_mngr` | Cannot allocate Metering feature no more resources!!!! |  |
| 2976 | `lgr_mp100board` | MP100Board::Init- failed on IsValid |  |
| 2977 | `lgr_num2` | New Digit = %d |  |
| 2978 | `lgr_overload` | GW BOARD QUE OVERLOAD:%s |  |
| 2979 | `lgr_psbrdif` | GeneralRsrcMngr::Init - Requested too many objects of type %s |  |
| 2980 | `lgr_routing` | Failed to allocate CostGroupTimebandEntry |  |
| 2981 | `lgr_stack` | DNS resolution list is empty !!! |  |
| 2982 | `lgr_stk_mngr` | StackMngr::GetFreeSession- Base class is abstract |  |
| 2983 | `lgr_timer` | ACTimer::Start IsTimerStarted=%d, ForTime=%d, IsPeriodic=%d |  |
| 2984 | `lgr_vxml_mngr` | Cannot allocate VXML feature no more resources!!!! |  |
| 2985 | `llgr_endpoint_feature` | Cannot allocate endpoint feature no more resources!!!! |  |
| 2986 | `msCTLSign` | Microsoft Trust List Signing |  |
| 2987 | `msCodeCom` | Microsoft Commercial Code Signing |  |
| 2988 | `msCodeInd` | Microsoft Individual Code Signing |  |
| 2989 | `msEFS` | Microsoft Encrypted File System |  |
| 2990 | `msExtReq` | Microsoft Extension Request |  |
| 2991 | `msSGC` | Microsoft Server Gated Crypto |  |
| 2992 | `msSmartcardLogin` | Microsoft Smartcardlogin |  |
| 2993 | `msUPN` | Microsoft Universal Principal Name |  |
| 2994 | `nameConstraints` | X509v3 Name Constraints |  |
| 2995 | `noCheck` | OCSP No Check |  |
| 2996 | `noRevAvail` | X509v3 No Revocation Available |  |
| 2997 | `nonRepudiation` | Key Encipherment |  |
| 2998 | `notApplicable` | Not Applicable |  |
| 2999 | `nsBaseUrl` | Netscape Base Url |  |
| 3000 | `nsCaPolicyUrl` | Netscape CA Policy Url |  |
| 3001 | `nsCaRevocationUrl` | Netscape CA Revocation Url |  |
| 3002 | `nsCertExt` | Netscape Certificate Extension |  |
| 3003 | `nsCertSequence` | Netscape Certificate Sequence |  |
| 3004 | `nsCertType` | Netscape Cert Type |  |
| 3005 | `nsComment` | Netscape Comment |  |
| 3006 | `nsDataType` | Netscape Data Type |  |
| 3007 | `nsRenewalUrl` | Netscape Renewal Url |  |
| 3008 | `nsRevocationUrl` | Netscape Revocation Url |  |
| 3009 | `nsSGC` | Netscape Server Gated Crypto |  |
| 3010 | `nsSslServerName` | Netscape SSL Server Name |  |
| 3011 | `nssslserver` | S/MIME signing |  |
| 3012 | `objCA` | Digital Signature |  |
| 3013 | `ocsphelper` | Time Stamp signing |  |
| 3014 | `pmQoEQN` | Reset Counters |  |
| 3015 | `policyConstraints` | X509v3 Policy Constraints |  |
| 3016 | `policyMappings` | X509v3 Policy Mappings |  |
| 3017 | `presentation` | Allowed /0,Restricted /1 |  |
| 3018 | `privateKeyUsagePeriod` | X509v3 Private Key Usage Period |  |
| 3019 | `privilegeWithdrawn` | AA Compromise |  |
| 3020 | `proxyCertInfo` | Proxy Certificate Information |  |
| 3021 | `ramMP118_SIP` | HelpMe!! BC |  |
| 3022 | `random_bytes` | Signature Algorithm %s+%s (%d+%d) |  |
| 3023 | `received` | Test successful |  |
| 3024 | `registration` | RegistrationPackageRequestItem::Machine - cannot get AOR from list. List might be full! |  |
| 3025 | `removeFromCRL` | Privilege Withdrawn |  |
| 3026 | `response` | Unexpected symbol '%c'. Digit expected |  |
| 3027 | `serverAuth` | TLS Web Server Authentication |  |
| 3028 | `serviceLocator` | OCSP Service Locator |  |
| 3029 | `setstate` | State C=%d M=%d Plan=%d |  |
| 3030 | `sip_stack` | SIPRawBufferMngr::GetNewBuffer - m_ExtraSmallRawBufferPool is full ... |  |
| 3031 | `sip_transport` | SIPUserBufferData::Init - Failed to allocate new SIPRawBuffer |  |
| 3032 | `smimeencrypt` | CRL signing |  |
| 3033 | `smimesign` | S/MIME encryption |  |
| 3034 | `snmpTraps2TpNcpFilter` | Filters which traps do NOT get sent out as TpNcp events. These events will be sent out in Mediant/IPmedia 5000/8000 s... |  |
| 3035 | `sslclient` | SSL server |  |
| 3036 | `sslserver` | Netscape SSL server |  |
| 3037 | `subjectAltName` | X509v3 Subject Alternative Name |  |
| 3038 | `subjectDirectoryAttributes` | X509v3 Subject Directory Attributes |  |
| 3039 | `subjectInfoAccess` | Subject Information Access |  |
| 3040 | `subjectKeyIdentifier` | X509v3 Subject Key Identifier |  |
| 3041 | `superseded` | Cessation Of Operation |  |
| 3042 | `systemIdleTaskDoNothing` | Makes the IDLE task be idle, doing nothing. |  |
| 3043 | `tEXtComment` | Created with GIMPW |  |
| 3044 | `targetInformation` | X509v3 AC Targeting |  |
| 3045 | `tf4TunnelIcmpIncomingError` | Unrecognized ICMP error over tunnel |  |
| 3046 | `tf6AhExtnHeaderProcess` | No bufs |  |
| 3047 | `tf6IpIncomingPacket` | Truncated packet |  |
| 3048 | `tf6IpIncomingPolicyCheck` | Incoming IPSEC policy check failed |  |
| 3049 | `tf6IpReassemblePacket` | Empty fragment |  |
| 3050 | `tf6IpSendPacket` | Policy requires discarding |  |
| 3051 | `tf6NdIncomingPacket` | Incoming ND packet with link                                          layer address size greater than                ... |  |
| 3052 | `tfAddPolicy` | Transforms required preshared key |  |
| 3053 | `tfAhCheckPkt` | Reserved data is not zero |  |
| 3054 | `tfAhChkPkt` | Authentication header length error |  |
| 3055 | `tfAhEspCheckReplay` | Zero sequence found |  |
| 3056 | `tfAhHmac` | MAC version authentication chained data error |  |
| 3057 | `tfAsn1Enc` | OBJECT error! |  |
| 3058 | `tfAsn1ObjectDec` | OBJECT not found! |  |
| 3059 | `tfBufferDoubleMalloc` | Ran out of Simple Heap |  |
| 3060 | `tfDeviceSend` | Send Too Much Scattered Data |  |
| 3061 | `tfDeviceSendBuffer` | Corrupted transmit queue |  |
| 3062 | `tfDeviceSendFailed` | Corrupted sendQueuePtr |  |
| 3063 | `tfEspCheckPkt` | Reserved SPI used |  |
| 3064 | `tfEspPacketCbcDecrypt` | Payload length error |  |
| 3065 | `tfEtherMcast` | Corrupted device Link Mcast Pointer |  |
| 3066 | `tfFreeSharedBuffer` | Null packet pointer |  |
| 3067 | `tfGetPositionFromLink` | Chain data error |  |
| 3068 | `tfGetRawBuffer` | No Kernel Memory |  |
| 3069 | `tfIkeAggressiveInam2Outam3` | Initiator sent AM[3] // |  |
| 3070 | `tfIkeAggressiveInam3` | Next hdr not supported |  |
| 3071 | `tfIkeBuildSig` | Build Signature error |  |
| 3072 | `tfIkeGetRandomMessageId` | Cannot create a unique message ID |  |
| 3073 | `tfIkeMainIni3Outr3` | Apply encryption failed |  |
| 3074 | `tfIkeMainInr1Outi2` | Situation Not Supported |  |
| 3075 | `tfIkeMainInr2Outi3` | Apply encrption failed |  |
| 3076 | `tfIkeOut1` | Responder received AM[1] // |  |
| 3077 | `tfIkeParseCert` | Not expected next payload |  |
| 3078 | `tfIkeParseCertReq` | Parse Cert Req error |  |
| 3079 | `tfIkeParseKe` | KeyExchange dataLen not expected |  |
| 3080 | `tfIkeParseNonce` | Length error |  |
| 3081 | `tfIkeParsePhase1Hash` | Phase 1 hash is not correct |  |
| 3082 | `tfIkeParsePhase2Hash` | Next header not supported |  |
| 3083 | `tfIkeParseSig` | Parse Signature error |  |
| 3084 | `tfIkePolicyAdd` | IKE has not been started |  |
| 3085 | `tfIkePolicyAddByPriority` | NULL or invalid argument in list |  |
| 3086 | `tfIkePolicyBuild` | NULL argument in list |  |
| 3087 | `tfIkePolicyFree` | Too many tfIkePolicyFree calls |  |
| 3088 | `tfIkePolicyQuery` | IPsec has not been initialized |  |
| 3089 | `tfIkePolicyRestore` | NULL argument list |  |
| 3090 | `tfIkePolicyValidate` | Must define intiator or responder role |  |
| 3091 | `tfIkeQuickInqm1Outqm2` | Could not save previous IV |  |
| 3092 | `tfIkeQuickInqm2Outqm3` | Responder received unsupported next payload type in QM[2] // |  |
| 3093 | `tfIkeQuickInqm4` | Invalid next payload value |  |
| 3094 | `tfIkeQuickOutqm1` | Not valid parameter |  |
| 3095 | `tfIkeTransformValidate` | Invalid encryption algorithm |  |
| 3096 | `tfIkeVerifyPhase1Sa` | SA next payload invalid |  |
| 3097 | `tfInitEnhancedLogging` | FATAL: Unable to malloc enhanced logging structure |  |
| 3098 | `tfInitLoopBack` | Could not add IPv4 router reject Loop back entry |  |
| 3099 | `tfIpForwardPacket` | Null device pointer in routing entry |  |
| 3100 | `tfIpIncomingPacket` | Incoming scattered data |  |
| 3101 | `tfIpIncomingPolicyCheck` | Incoming IPSEC policy check failed |  |
| 3102 | `tfIpReassemblePacket` | Empty list after packet insertion |  |
| 3103 | `tfIpsecSendPacketMultiple` | IPSEC can't add Head/Tail to packet |  |
| 3104 | `tfKernelCreateEvent` | Unable to Create Semaphore |  |
| 3105 | `tfKernelPendEvent` | Unable to Pend on Semaphore |  |
| 3106 | `tfKernelPostIsrEvent` | Unable to Post on Semaphore |  |
| 3107 | `tfMpcInit` | Not enough memory for descriptor rings |  |
| 3108 | `tfOakleyGetProposal` | Could not find matching local certificate |  |
| 3109 | `tfPacketChecksum` | Data in Packet chain smaller than length to be checksumed |  |
| 3110 | `tfPkiOwnKeyPairAddTo` | NO file I/O |  |
| 3111 | `tfPolicyDelete` | Ipsec is not initialized yet |  |
| 3112 | `tfPolicyFree` | Too many Policy free calls |  |
| 3113 | `tfPolicyHeadTrailer` | ESP has both null authentication and null encryption algorithm |  |
| 3114 | `tfRecyleAlloc` | Could not allocate memory from system |  |
| 3115 | `tfRtAddEntry` | Duplicate head and no grandfather |  |
| 3116 | `tfRtAllocNLockNCopy` | Routing table corrupted or not initialized |  |
| 3117 | `tfRtClone` | No loop back driver configured |  |
| 3118 | `tfRtTreeWalk` | Corrupted Patricia tree |  |
| 3119 | `tfSendAppend` | Send queue corrupted |  |
| 3120 | `tfSnmpdCacheDeleteRoute` | Corrupted Pointer to last entry |  |
| 3121 | `tfSnmpdCacheInsertRoute` | Entry already in cache! |  |
| 3122 | `tfSocketAllocate` | Unable to Allocate Memory for TCP socket from Kernel/OS |  |
| 3123 | `tfSocketIncomingPacket` | Data improperly trimmed in TCP |  |
| 3124 | `tfSocketInit` | FATAL: cannot have more than 32766 sockets |  |
| 3125 | `tfSocketNotify` | Null CB function with non zero CB flags |  |
| 3126 | `tfSocketTreeDelete` | Corrupted reuseaddress list |  |
| 3127 | `tfStartEnhancedIke` | ID setting failed |  |
| 3128 | `tfStartIke` | IP addr type not supported |  |
| 3129 | `tfStartIsakmp` | IKE global variable not initialized |  |
| 3130 | `tfStartTreck` | Please call tfInitTreckOption with a non zero TM_OPTION_TICK_LENGTH value |  |
| 3131 | `tfTcpDelReXmit` | Retransmission timer should already have been deleted |  |
| 3132 | `tfTcpEstablish` | Corrupted passive socket |  |
| 3133 | `tfTcpGetTcpHeader` | Found a recycled header on closed vector! |  |
| 3134 | `tfTcpIncomingPacket` | Checksum on incoming TCP packet failed |  |
| 3135 | `tfTcpRcvAck` | Trimmed incoming data bigger than receive queue!! |  |
| 3136 | `tfTcpRcvUrgentData` | Peer follows RFC 1122, but user reset STD URG |  |
| 3137 | `tfTcpRemoveConReq` | Corruped connection request entry |  |
| 3138 | `tfTcpSackDeQueueBlocks` | Lost bytes in reassemble queue |  |
| 3139 | `tfTcpSackQueueBlock` | No memory to allocate a SEL ACK block |  |
| 3140 | `tfTcpSendPacket` | Discrepancy between SEL ACK list, and reassemble list |  |
| 3141 | `tfTcpSendQueueFree` | Socket send queue corrupted! |  |
| 3142 | `tfTcpSynData` | Receive queue full, or not initialized |  |
| 3143 | `tfTcpTimerNewTime` | Null timer pointer |  |
| 3144 | `tfTcpTmProbeWnd` | Probing window, and rexmit timer on! |  |
| 3145 | `tfTimerAdd` | No memory to allocate a timer |  |
| 3146 | `tfUdpIncoming` | Bad UDP header length |  |
| 3147 | `tfUseIke` | Could not initialize priority structures |  |
| 3148 | `tfUseIpsec` | Crypto engine initialization failed |  |
| 3149 | `tfUseIpsecLogging` | TM_IPSEC not initialized |  |
| 3150 | `tfX509ObjectInit` | OBJECT init error! |  |
| 3151 | `timeStamping` | Time Stamping |  |
| 3152 | `tm_rt_tree_search` | Null leaf in the tree |  |
| 3153 | `transport` | SIPStackMngr::GetActiveRegisteredContacts - %d active registered users were found |  |
| 3154 | `trapuser` | Error saving converted auth key for new user, index=%d |  |
| 3155 | `trustRoot` | Trust Root |  |
| 3156 | `unspecified` | Key Compromise |  |
| 3157 | `unstructuredAddress` | PKCS #9 unstructured address |  |
| 3158 | `unstructuredName` | PKCS #9 unstructured name |  |
| 3159 | `updateSnmpConfig` | TargetParams table entry not found for trap community string |  |
| 3160 | `vbdatacall` | SipStackSession::HandleCoreSetupEV: Illegal characters in Source/Dest phone number |  |
| 3161 | `vlanHeartbeatPriority` | Sets the priority value for the heartbeat Vlan tag. |  |
| 3162 | `vlanSendNonTaggedOnNative` | Specify whether to send non-tagged packets on the native vlan. |  |
| 3163 | `vlanType` | File system is in use. Remount will take place when file system is no longer in use. IP=%s root=%s |  |
| 3164 | `vmEnableWhenRTPActive` | Enables the voice menu even when RTP is active (mid-call). |  |
| 3165 | `voicexml` | SIPStackSession::UpdateNetAnnIfNeeded - Can not find voicexml=URL in URI params |  |

---

## Table Definitions

Tables are configured in the INI file with the following structure:
```ini
[ TableName ]
FORMAT TableName_Index = TableName_Col1, TableName_Col2, ...;
TableName 0 = value1, value2, ...;
TableName 1 = value1, value2, ...;
[ \TableName ]
```

### [ ACCESSLIST ]

**Columns (3):** `MatchCount`, `PrefixLen`, `Protocol`

### [ AMRFECCodecPolicies ]

**Columns (4):** `Hysteresis`, `Rate`, `RedundancyLevel`, `Threshold`

### [ Account ]

**Columns (9):** `ApplicationType`, `ContactUser`, `HostName`, `Password`, `Register`, `ServedIPGroup`, `ServedTrunkGroup`, `ServingIPGroup`, `Username`

### [ AllowedCodersGroup0 ]

**Columns (1):** `Name`

### [ AllowedCodersGroup1 ]

**Columns (1):** `Name`

### [ AllowedCodersGroup2 ]

**Columns (1):** `Name`

### [ AllowedCodersGroup3 ]

**Columns (1):** `Name`

### [ AllowedCodersGroup4 ]

**Columns (1):** `Name`

### [ AltRouteCauseIp2Tel ]

**Columns (1):** `ReleaseCause`

### [ AltRouteCauseTel2Ip ]

**Columns (1):** `ReleaseCause`

### [ Authentication ]

**Columns (6):** `IsUsed`, `Module`, `Port`, `PortType`, `UserId`, `UserPassword`

### [ BWManagement ]

**Columns (6):** `Hysteresis`, `MediaRealmIndex`, `RuleAction`, `Threshold`, `ThresholdIndex`, `ThresholdLevel`

### [ CPCallManagerGroups ]

**Columns (6):** `FourthMGCIndx`, `GroupMembersList`, `MGCType`, `PrimaryMGCIndx`, `SecondaryMGCIndx`, `ThirdMGCIndx`

### [ Call ]

**Columns (29):** `ActiveCalls`, `ApplicationType`, `AutoRegister`, `AverageCPS`, `CallAttempts`, `CallDuration`, `CallParty`, `CalledURI`, `CallsPerSecond`, `DestAddress`, `DestTransportType`, `ElapsedTime`, `EndpointURI`, `EstablishedCalls`, `FailedAttempts`, `IPGroupID`, `MaxChannels`, `MinChannels`, `Password`, `Play`, `RemoteDisconnects`, `RouteBy`, `SRD`, `ScheduleInterval`, `TestDuration`, `TestMode`, `TestStatus`, `TestSummary`, `UserName`

### [ CallWaitingPerPort ]

**Columns (5):** `IsEnabled`, `IsUsed`, `Module`, `Port`, `PortType`

### [ CallerDisplayInfo ]

**Columns (6):** `DisplayString`, `IsCidRestricted`, `IsUsed`, `Module`, `Port`, `PortType`

### [ CallingNameMapIp2Tel ]

**Columns (13):** `CallingNamePrefix`, `DestHost`, `DestinationPrefix`, `LeaveFromRight`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ CallingNameMapTel2Ip ]

**Columns (13):** `CallingNamePrefix`, `DestHost`, `DestinationPrefix`, `LeaveFromRight`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ CauseMap2IsdnLocation ]

**Columns (2):** `IsdnLocation`, `ReleaseCause`

### [ CauseMapIsdn2Isdn ]

**Columns (2):** `MapIsdnReleaseCause`, `OrigIsdnReleaseCause`

### [ CauseMapIsdn2Sip ]

**Columns (2):** `IsdnReleaseCause`, `SipResponse`

### [ CauseMapSip2Isdn ]

**Columns (2):** `IsdnReleaseCause`, `SipResponse`

### [ ChargeCode ]

**Columns (12):** `EndTime1`, `EndTime2`, `EndTime3`, `EndTime4`, `PulseInterval1`, `PulseInterval2`, `PulseInterval3`, `PulseInterval4`, `PulsesOnAnswer1`, `PulsesOnAnswer2`, `PulsesOnAnswer3`, `PulsesOnAnswer4`

### [ CodersGroup0 ]

**Columns (5):** `Name`, `PayloadType`, `Sce`, `pTime`, `rate`

### [ CodersGroup1 ]

**Columns (5):** `Name`, `PayloadType`, `Sce`, `pTime`, `rate`

### [ CodersGroup2 ]

**Columns (5):** `Name`, `PayloadType`, `Sce`, `pTime`, `rate`

### [ CodersGroup3 ]

**Columns (5):** `Name`, `PayloadType`, `Sce`, `pTime`, `rate`

### [ CodersGroup4 ]

**Columns (5):** `Name`, `PayloadType`, `Sce`, `pTime`, `rate`

### [ ConditionTable ]

**Columns (2):** `Condition`, `Description`

### [ CostGroupTable ]

**Columns (5):** `CostGroupName`, `DefaultConnectCost`, `DefaultConnectionCost`, `DefaultMinuteCost`, `DefaultTimeCost`

### [ CostGroupTimebands ]

**Columns (8):** `ConnectCost`, `ConnectionCost`, `CostGroup`, `EndTime`, `MinuteCost`, `StartTime`, `TimeCost`, `TimebandIndex`

### [ CpMediaRealm ]

**Columns (7):** `IPv4IF`, `IPv6IF`, `IsDefault`, `MediaRealmName`, `MediaSessionLeg`, `PortRangeEnd`, `PortRangeStart`

### [ DS3CONFIG ]

**Columns (8):** `AdminState`, `CircuitIdentifier`, `ClockSource`, `FramingMethod`, `LineBuildOut`, `PmOnOff`, `TappingEnable`, `TrapEnable`

### [ Dns2Ip ]

**Columns (5):** `DomainName`, `FirstIpAddress`, `FourthIpAddress`, `SecondIpAddress`, `ThirdIpAddress`

### [ DspTemplates ]

**Columns (2):** `DspResourcesPercentage`, `DspTemplateNumber`

### [ EnableCallerId ]

**Columns (5):** `IsEnabled`, `IsUsed`, `Module`, `Port`, `PortType`

### [ EnableDid ]

**Columns (5):** `IsEnable`, `IsUsed`, `Module`, `Port`, `PortType`

### [ ForwardOnBusyTrunkDest ]

**Columns (2):** `ForwardDestination`, `TrunkGroupId`

### [ FwdInfo ]

**Columns (7):** `Destination`, `IsUsed`, `Module`, `NoReplyTime`, `Port`, `PortType`, `Type`

### [ GWUserInfoTable ]

**Columns (6):** `DisplayName`, `GlobalPhoneNumber`, `PBXExtension`, `Password`, `Status`, `Username`

### [ IP2IPRouting ]

**Columns (17):** `AltRouteOptions`, `CostGroup`, `DestAddress`, `DestHost`, `DestIPGroupID`, `DestPort`, `DestSRDID`, `DestTransportType`, `DestType`, `DestUsernamePrefix`, `MessageCondition`, `ReRouteIPGroupID`, `RequestType`, `SrcHost`, `SrcIPGroupID`, `SrcUsernamePrefix`, `Trigger`

### [ IPGroup ]

**Columns (24):** `AlwaysUseRouteTable`, `AuthenticationMode`, `ClassifyByProxySet`, `ContactName`, `ContactUser`, `Description`, `DestUriInput`, `EnableSBCClientForking`, `EnableSurvivability`, `InboundManSet`, `MaxNumOfRegUsers`, `MediaRealm`, `MethodList`, `OutboundManSet`, `ProfileId`, `ProxySetId`, `RegistrationMode`, `RoutingMode`, `SIPGroupName`, `SRD`, `ServingIPGroup`, `SipReRoutingMode`, `SourceUriInput`, `Type`

### [ IPInboundManipulation ]

**Columns (14):** `DestHost`, `DestUsernamePrefix`, `IsAdditionalManipulation`, `LeaveFromRight`, `ManipulatedURI`, `ManipulationPurpose`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `RequestType`, `SrcHost`, `SrcIPGroupID`, `SrcUsernamePrefix`, `Suffix2Add`

### [ IPMediaChannels ]

**Columns (2):** `DSPChannelsReserved`, `ModuleID`

### [ IPsecProposalTable ]

**Columns (3):** `AuthenticationAlgorithm`, `DHGroup`, `EncryptionAlgorithm`

### [ IPsecSATable ]

**Columns (16):** `AuthenticationMethod`, `DPDmode`, `DestPort`, `IPsecMode`, `InterfaceIndex`, `InterfaceName`, `Phase1SaLifetimeInSec`, `Phase2SaLifetimeInKB`, `Phase2SaLifetimeInSec`, `Protocol`, `RemoteEndpointAddressOrName`, `RemoteSubnetIPAddress`, `RemoteSubnetPrefixLength`, `RemoteTunnelAddress`, `SharedKey`, `SourcePort`

### [ InterfaceTable ]

**Columns (10):** `ApplicationTypes`, `Gateway`, `IPAddress`, `IPv6InterfaceMode`, `InterfaceMode`, `InterfaceName`, `PrefixLength`, `PrimaryDNSServerIPAddress`, `SecondaryDNSServerIPAddress`, `VlanID`

### [ IpProfile ]

**Columns (76):** `AMDMaxGreetingTime`, `AMDMaxPostSilenceGreetingTime`, `AMDSensitivityLevel`, `AMDSensitivityParameterSuit`, `AddIEInSetup`, `AmdMode`, `CNGmode`, `CallLimit`, `CodersGroupID`, `CopyDest2RedirectNumber`, `DisconnectOnBrokenConnection`, `EarlyAnswerTimeout`, `EnableEarly183`, `EnableEarlyMedia`, `EnableEchoCanceller`, `EnableHold`, `EnableQSIGTunneling`, `EnableSymmetricMKI`, `FirstTxDtmfOption`, `GenerateSRTPKeys`, `IPDiffServ`, `InputGain`, `IpPreference`, `IsDTMFUsed`, `IsFaxUsed`, `JitterBufMinDelay`, `JitterBufOptFactor`, `MKISize`, `MediaIPVersionPreference`, `MediaSecurityBehaviour`, `NSEMode`, `PlayRBTone2IP`, `ProfileName`, `ProgressIndicator2IP`, `RTPRedundancyDepth`, `RemoteBaseUDPPort`, `ResetSRTPStateUponRekey`, `RxDTMFOption`, `SBC2833DTMFPayloadType`, `SBCAllowedCodersGroupID`, `SBCAllowedCodersMode`, `SBCAlternativeDTMFMethod`, `SBCAssertIdentity`, `SBCDiversionMode`, `SBCEnforceMKISize`, `SBCExtensionCodersGroupID`, `SBCFaxAnswerMode`, `SBCFaxBehavior`, `SBCFaxCodersGroupID`, `SBCFaxOfferMode`, `SBCHistoryInfoMode`, `SBCMediaSecurityBehaviour`, `SBCPlayHeldTone`, `SBCRFC2833Behavior`, `SBCReliableHeldToneSource`, `SBCRemote3xxBehavior`, `SBCRemoteCanPlayRingback`, `SBCRemoteDelayedOfferSupport`, `SBCRemoteEarlyMediaRTP`, `SBCRemoteEarlyMediaResponseType`, `SBCRemoteEarlyMediaSupport`, `SBCRemoteHoldFormat`, `SBCRemoteMultiple18xSupport`, `SBCRemoteReferBehavior`, `SBCRemoteReinviteSupport`, `SBCRemoteSupportsRFC3960`, `SBCRemoteUpdateSupport`, `SBCSessionExpiresMode`, `SBCUserRegistrationTime`, `SCE`, `SbcPrackMode`, `SecondTxDtmfOption`, `SigIPDiffServ`, `TranscodingMode`, `VoiceVolume`, `VxxTransportType`

### [ LdapConfiguration ]

**Columns (10):** `ConnectionStatus`, `LdapConfBindDn`, `LdapConfInterfaceType`, `LdapConfPassword`, `LdapConfServerDomainName`, `LdapConfServerIp`, `LdapConfServerMaxRespondTime`, `LdapConfServerPort`, `MngmAuthAtt`, `Type`

### [ LdapServersSearchDNs ]

**Columns (2):** `LdapConfigurationIndex`, `SearchDnInternalIndex`

### [ LocalSwitchingPorts ]

**Columns (1):** `PhoneNumber`

### [ LoggingFilters ]

**Columns (4):** `CaptureType`, `FilterType`, `Syslog`, `Value`

### [ M3UAROUTINGCLIST ]

**Columns (17):** `DestinationPointCode`, `LowerCICValue1`, `LowerCICValue2`, `LowerCICValue3`, `LowerCICValue4`, `NetworkAppearence`, `OPC1`, `OPC2`, `OPC3`, `OPC4`, `OwnerInterfaceGroup`, `RoutingContext`, `SeriviceIndicatorList`, `UpperCICValue1`, `UpperCICValue2`, `UpperCICValue3`, `UpperCICValue4`

### [ MegacoGtwConfigurationTable ]

**Columns (10):** `AssociatedMembersList`, `IPv4InterfaceName`, `IPv6InterfaceName`, `LoadWeight`, `LocalPort`, `MID`, `MediaRealmName`, `MegacoVersion`, `ServiceChangeProfile`, `VirtualGWName`

### [ MegacoGtwControllerLinkTable ]

**Columns (6):** `ActivityOrder`, `MGCAddressFormat`, `MGControllerAddress`, `MGControllerPort`, `TransportType`, `VirtualGWIndex`

### [ MessagePolicy ]

**Columns (10):** `BodyList`, `BodyListType`, `MaxBodyLength`, `MaxHeaderLength`, `MaxMessageLength`, `MaxNumBodies`, `MaxNumHeaders`, `MethodList`, `MethodListType`, `SendRejection`

### [ MgmntLDAPGroups ]

**Columns (4):** `Group`, `GroupIndex`, `LdapConfigurationIndex`, `Level`

### [ NATTranslation ]

**Columns (6):** `SourceEndPort`, `SourceIPInterfaceName`, `SourceStartPort`, `TargetEndPort`, `TargetIPAddress`, `TargetStartPort`

### [ NFSServers ]

**Columns (7):** `AuthType`, `GID`, `HostOrIP`, `NfsVersion`, `RootPath`, `UID`, `VlanType`

### [ NumberMapIp2Tel ]

**Columns (16):** `DestHost`, `DestIPGroupID`, `DestinationPrefix`, `IsPresentationRestricted`, `LeaveFromRight`, `NumberPlan`, `NumberType`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ NumberMapTel2Ip ]

**Columns (16):** `DestHost`, `DestIPGroupID`, `DestinationPrefix`, `IsPresentationRestricted`, `LeaveFromRight`, `NumberPlan`, `NumberType`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ PREFIX ]

**Columns (16):** `CallSetupRulesSetId`, `CostGroup`, `DestAddress`, `DestHostPrefix`, `DestIPGroupID`, `DestPort`, `DestSRD`, `DestinationPrefix`, `ForkingGroup`, `MeteringCode`, `ProfileId`, `SourcePrefix`, `SrcHostPrefix`, `SrcIPGroupID`, `SrcTrunkGroupID`, `TransportType`

### [ PhoneContext ]

**Columns (3):** `Context`, `Npi`, `Ton`

### [ PortName ]

**Columns (5):** `IsUsed`, `Module`, `Name`, `Port`, `PortType`

### [ ProxyIp ]

**Columns (3):** `IpAddress`, `ProxySetId`, `TransportType`

### [ ProxySet ]

**Columns (8):** `ClassificationInput`, `EnableProxyKeepAlive`, `IsProxyHotSwap`, `KeepAliveFailureResp`, `ProxyKeepAliveTime`, `ProxyLoadBalancingMethod`, `ProxyRedundancyMode`, `SRD`

### [ PstnPrefix ]

**Columns (11):** `CallSetupRulesSetId`, `DestHostPrefix`, `DestPrefix`, `ProfileId`, `SourceAddress`, `SourcePrefix`, `SrcHostPrefix`, `SrcIPGroupID`, `SrcSRDID`, `TrunkGroupId`, `TrunkId`

### [ QOERules ]

**Columns (13):** `Direction`, `GreenYellowHysteresis`, `GreenYellowOperation`, `GreenYellowOperationDetails`, `GreenYellowThreshold`, `MediaRealmIndex`, `MonitoredParam`, `Profile`, `RuleIndex`, `YellowRedHysteresis`, `YellowRedOperation`, `YellowRedOperationDetails`, `YellowRedThreshold`

### [ RedirectNumberMapTel2Ip ]

**Columns (15):** `DestHost`, `DestinationPrefix`, `IsPresentationRestricted`, `LeaveFromRight`, `NumberPlan`, `NumberType`, `Prefix2Add`, `RedirectPrefix`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ RegistrationPrefix ]

**Columns (3):** `NumberPlan`, `NumberType`, `Prefix`

### [ RejectAnonymousCallPerPort ]

**Columns (5):** `Enable`, `IsUsed`, `Module`, `Port`, `PortType`

### [ ResourcePriorityNetworkDomains ]

**Columns (2):** `Ip2TelInterworking`, `Name`

### [ RoutingRuleGroups ]

**Columns (3):** `LCRAverageCallLength`, `LCRDefaultCost`, `LCREnable`

### [ SASRegistrationManipulation ]

**Columns (2):** `LeaveFromRight`, `RemoveFromRight`

### [ SIPInterface ]

**Columns (11):** `ApplicationType`, `ClassificationFailureResponseType`, `MessagePolicy`, `NetworkInterface`, `PreClassificationManSet`, `SRD`, `TCPKeepaliveEnable`, `TCPPort`, `TLSMutualAuthentication`, `TLSPort`, `UDPPort`

### [ SNMPUsers ]

**Columns (6):** `AuthKey`, `AuthProtocol`, `Group`, `PrivKey`, `PrivProtocol`, `Username`

### [ SRD ]

**Columns (6):** `BlockUnRegUsers`, `EnableUnAuthenticatedRegistrations`, `IntraSRDMediaAnchoring`, `MaxNumOfRegUsers`, `MediaRealm`, `Name`

### [ SourceNumberMapIp2Tel ]

**Columns (15):** `DestHost`, `DestinationPrefix`, `IsPresentationRestricted`, `LeaveFromRight`, `NumberPlan`, `NumberType`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ SourceNumberMapTel2Ip ]

**Columns (15):** `DestHost`, `DestinationPrefix`, `IsPresentationRestricted`, `LeaveFromRight`, `NumberPlan`, `NumberType`, `Prefix2Add`, `RemoveFromLeft`, `RemoveFromRight`, `SourceAddress`, `SourcePrefix`, `SrcHost`, `SrcIPGroupID`, `SrcTrunkGroupID`, `Suffix2Add`

### [ Srv2Ip ]

**Columns (14):** `Dns1`, `Dns2`, `Dns3`, `InternalDomain`, `Port1`, `Port2`, `Port3`, `Priority1`, `Priority2`, `Priority3`, `TransportType`, `Weight1`, `Weight2`, `Weight3`

### [ StaticRouteTable ]

**Columns (5):** `Description`, `Destination`, `Gateway`, `InterfaceName`, `PrefixLength`

### [ TargetOfChannel ]

**Columns (7):** `Destination`, `HotLineToneDuration`, `IsUsed`, `Module`, `Port`, `PortType`, `Type`

### [ TelProfile ]

**Columns (35):** `CallPriorityMode`, `CodersGroupID`, `DialPlanIndex`, `DigitalCutThrough`, `DisconnectOnBusyTone`, `DtmfVolume`, `ECNlpMode`, `Enable911PSAP`, `EnableAGC`, `EnableCurrentDisconnect`, `EnableDIDWink`, `EnableDigitDelivery`, `EnableEC`, `EnableEarlyMedia`, `EnableFXODoubleAnswer`, `EnableReversePolarity`, `EnableVoiceMailDelay`, `FXORingTimeout`, `FlashHookPeriod`, `IP2TelCutThroughCallBehavior`, `IPDiffServ`, `InputGain`, `IsFaxUsed`, `IsTwoStageDial`, `JitterBufMinDelay`, `JitterBufOptFactor`, `MWIAnalog`, `MWIDisplay`, `ProfileName`, `ProgressIndicator2IP`, `SigIPDiffServ`, `SwapTelToIpPhoneNumbers`, `TelPreference`, `TimeForReorderTone`, `VoiceVolume`

### [ ToneIndex ]

**Columns (3):** `DestinationPrefix`, `PriorityIndex`, `SourcePrefix`

### [ TrunkGroup ]

**Columns (8):** `FirstBChannel`, `FirstPhoneNumber`, `FirstTrunkId`, `LastBChannel`, `LastTrunkId`, `Module`, `ProfileId`, `TrunkGroupNum`

### [ TrunkGroupSettings ]

**Columns (8):** `ChannelSelectMode`, `ContactUser`, `GatewayName`, `MWIInterrogationType`, `RegistrationMode`, `ServingIPGroup`, `TrunkGroupId`, `TrunkGroupName`

### [ TxDtmfOption ]

**Columns (1):** `Type`

### [ UserTable ]

**Columns (3):** `FullName`, `Password`, `UserName`

### [ WebUsers ]

**Columns (25):** `BlockDurationStart`, `BlockTime`, `IsInactive`, `IsOldPassword`, `LastFailIP`, `LastFailTime`, `LastFailTime2`, `LastLogin`, `LastLogin2`, `LastSuccessIP`, `LastSuccessLogin`, `LastSuccessLogin2`, `LoginFailAttempts`, `LoginFailAttempts2`, `Password`, `PasswordVal`, `PwAgeInterval`, `PwChangeTime`, `PwChangeTime2`, `PwNonce`, `SessionLimit`, `SessionTimeout`, `Status`, `UserLevel`, `Username`

### [ WelcomeMessage ]

**Columns (1):** `Text`
