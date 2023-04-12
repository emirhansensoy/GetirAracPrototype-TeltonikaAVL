def hex_to_dec(n):
    return int(n, 16)


IO_ELEMENTS = {
    "239": ["Ignition", "0 - Ignition Off, 1 - Ignition On"],
    "240": ["Movement", "0 - Movement Off, 1 - Movement On"],
    "80": ["Data Mode", "0 - Home On Stop, 1 - Home On Moving, 2 - Roaming On Stop, 3 - Roaming On Moving, "
                        "4 - Unknown On Stop, 5 - Unknown On Moving"],
    "21": ["GSM Signal", "Value in scale 1-5"],
    "200": ["Sleep Mode", "0 - Sleep modes disabled, 1 - GNSS sleep, 2 - Deep sleep, 3 - Online deep sleep, 4 - Ultra "
                          "deep sleep"],
    "69": ["GNSS Status", "0 - GNSS OFF, 1 - GNSS ON with fix, 2 - GNSS ON without fix, 3 - GNSS sleep"],
    "181": ["GNSS PDOP", "Probability"],
    "182": ["GNSS HDOP", "Probability"],
    "24": ["Speed", "km/h Value"],
    "205": ["GSM Cell ID", "GSM base station ID"],
    "206": ["GSM Area Code", "Location Area code (LAC), it depends on GSM operator. It provides unique number which "
                             "assigned to a set of base GSM stations."],
    "67": ["Battery Voltage", "Voltage"],
    "68": ["Battery Current", "Current"],
    "113": ["Battery Level", "Battery capacity level"],
    "66": ["External Voltage", "IO element is used to measure External Voltage, when External Voltage is < 65V."],
    "800": ["Extended External Voltage", "IO element is used to measure External Voltage, when External Voltage is > "
                                         "65 V."],
    "241": ["Active GSM Operator", "Currently used GSM Operator code"],
    "199": ["Trip Odometer", "Trip Odometer value"],
    "16": ["Total Odometer", "Total Odometer value"],
    "1": ["Digital Input 1", "Logic: 0/1"],
    "2": ["Digital Input 2", "Logic: 0/1"],
    "3": ["Digital Input 3", "Logic: 0/1"],
    "262": ["Digital Input 4", "Logic: 0/1"],
    "179": ["Digital Output 1", "Logic: 0/1"],
    "180": ["Digital Output 2", "Logic: 0/1"],
    "841": ["DOUT 1 Overcurrent", "DOUT 1 Overcurrent IO element is used to indicate overcurrent on Digital Output 1. "
                                  "When Digital Output 1 overcurrent happens, it means that current level is > 300 "
                                  "mA, value is set to 1. Value 1 holds until 5 min timeout runs out. After timeout "
                                  "value is set to 0 if current level is < 300 mA. If current level is still > 300 mA "
                                  "value remains 1."],
    "842": ["DOUT2 Overcurrent", "DOUT 2 Overcurrent IO element is used to indicate overcurrent on Digital Output 2. "
                                 "When Digital Output 2 overcurrent happens, it means that current level is > 300 mA, "
                                 "value is set to 1. Value 1 holds until 5 min timeout runs out. After timeout value "
                                 "is set to 0 if current level is < 300 mA. If current level is still > 300 mA value "
                                 "remains 1."],
    "9": ["Analog Input 1", "Voltage"],
    "6": ["Analog Input 2", "Voltage"],
    "839": ["Extended Analog Input 1", "Extended Analog Input 1 IO element is used to measure Analog Input 1 voltage, "
                                       "when Analog Input 1 voltage is > 65 V."],
    "840": ["Extended Analog Input 2", "Extended Analog Input 2 IO element is used to measure Analog Input 2 voltage, "
                                       "when Analog Input 1 voltage is > 65 V."],
    "303": ["Instant Movement", "Logic: 0/1 returns movement value"],
    "17": ["Axis X", "X axis value"],
    "18": ["Axis Y", "Y axis value"],
    "19": ["Axis Z", "Z axis value"],
    "11": ["ICCID1", "Value of SIM ICCID, MSB"],
    "14": ["ICCID2", "Value of SIM ICCID, MSB"],
    "72": ["Dallas Temperature 1", "Degrees ( °C ), -55 - +115, if 850 - Sensor not ready, if 2000 - Value read "
                                   "error, if 3000 - Not connected, if 4000 - ID failed, if 5000 - same as 850"],
    "73": ["Dallas Temperature 2", "Degrees ( °C ), -55 - +115, if 850 - Sensor not ready, if 2000 - Value read "
                                   "error, if 3000 - Not connected, if 4000 - ID failed, if 5000 - same as 850"],
    "74": ["Dallas Temperature 3", "Degrees ( °C ), -55 - +115, if 850 - Sensor not ready, if 2000 - Value read "
                                   "error, if 3000 - Not connected, if 4000 - ID failed, if 5000 - same as 850"],
    "75": ["Dallas Temperature 4", "Degrees ( °C ), -55 - +115, if 850 - Sensor not ready, if 2000 - Value read "
                                   "error, if 3000 - Not connected, if 4000 - ID failed, if 5000 - same as 850"],
    "76": ["Dallas Temperature ID 1", "Dallas sensor ID"],
    "77": ["Dallas Temperature ID 2", "Dallas sensor ID"],
    "79": ["Dallas Temperature ID 3	", "Dallas sensor ID"],
    "71": ["Dallas Temperature ID 4	", "Dallas sensor ID"],
    "78": ["iButton", "iButton ID"],
    "15": ["Eco Score", "Average amount of events on some distance"],
    "116": ["Charger Connected", "0 - charger is not connected, 1 - charger is connected"],
    "854": ["User ID", "This parameter allows to send custom number as AVL ID parameter. Configurable in Features "
                       "section."],
    "387": ["ISO6709 Coordinates", "ISO6709 Coordinates Latitude, Longitude (in Degrees, Minutes and Seconds) and "
                                   "Altitude: IO value format: ±DDMMSS.SSSS±DDDMMSS.SSSS±AAA.AAA/"],
    "288": ["GSM Cell ID 1", "Unique ID of the Cell 1"],
    "291": ["GSM Cell ID 2", "Unique ID of the Cell 2"],
    "294": ["GSM Cell ID 3", "Unique ID of the Cell 3"],
    "297": ["GSM Cell ID 4", "Unique ID of the Cell 4"],
    "287": ["GSM Cell LAC 1", "Location Area Code of the Cell 1"],
    "290": ["GSM Cell LAC 2", "Location Area Code of the Cell 2"],
    "293": ["GSM Cell LAC 3", "Location Area Code of the Cell 3"],
    "296": ["GSM Cell LAC 4", "Location Area Code of the Cell 4"],
    "1200": ["GSM Cell MNC 1", "Mobile Network Code of the Cell 1"],
    "1201": ["GSM Cell MNC 2", "Mobile Network Code of the Cell 2"],
    "1202": ["GSM Cell MNC 3", "Mobile Network Code of the Cell 3"],
    "1203": ["GSM Cell MNC 4", "Mobile Network Code of the Cell 4"],
    "286": ["GSM Signal RX 0", "GSM Signal of the Cell 0"],
    "289": ["GSM Signal RX 1", "GSM Signal of the Cell 1"],
    "292": ["GSM Signal RX 2", "GSM Signal of the Cell 2"],
    "295": ["GSM Signal RX 3", "GSM Signal of the Cell 3"],
    "298": ["GSM Signal RX 4", "GSM Signal of the Cell 4"],
    "399": ["Time To First Fix", "Amount of time it took to get first GNSS fix"],
    "20015": ["Modem Uptime", "Modem Uptime since the last wake up"],
    "155": ["Geofence zone 01", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "156": ["Geofence zone 02", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "157": ["Geofence zone 03", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "158": ["Geofence zone 04", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "159": ["Geofence zone 05", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "61": ["Geofence zone 06", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "62": ["Geofence zone 07", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "63": ["Geofence zone 08", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "64": ["Geofence zone 09", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "65": ["Geofence zone 10", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "70": ["Geofence zone 11", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "88": ["Geofence zone 12", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "91": ["Geofence zone 13", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "92": ["Geofence zone 14", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "93": ["Geofence zone 15", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "94": ["Geofence zone 16", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "95": ["Geofence zone 17", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "96": ["Geofence zone 18", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "97": ["Geofence zone 19", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "98": ["Geofence zone 20", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "99": ["Geofence zone 21", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                               "speeding start"],
    "153": ["Geofence zone 22", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "154": ["Geofence zone 23", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "190": ["Geofence zone 24", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "191": ["Geofence zone 25", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "192": ["Geofence zone 26", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "193": ["Geofence zone 27", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "194": ["Geofence zone 28", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "195": ["Geofence zone 29", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "196": ["Geofence zone 30", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "197": ["Geofence zone 31", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "198": ["Geofence zone 32", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "208": ["Geofence zone 33", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "209": ["Geofence zone 34", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "216": ["Geofence zone 35", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "217": ["Geofence zone 36", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "218": ["Geofence zone 37", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "219": ["Geofence zone 38", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "220": ["Geofence zone 39", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "221": ["Geofence zone 40", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "222": ["Geofence zone 41", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "223": ["Geofence zone 42", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "224": ["Geofence zone 43", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "225": ["Geofence zone 44", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "226": ["Geofence zone 45", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "227": ["Geofence zone 46", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "228": ["Geofence zone 47", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "229": ["Geofence zone 48", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "230": ["Geofence zone 49", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "231": ["Geofence zone 50", "0 – target left zone, 1 – target entered zone, 2 – over speeding end, 3 – over "
                                "speeding start"],
    "175": ["Auto Geofence", "0 – target left zone, 1 – target entered zone"],
    "250": ["Trip", "0 – trip stop, 1 – trip start"],
    "255": ["Overspeeding Event", "At over speeding start km/h, at over speeding end km/h"],
    "251": ["Idling", "0 – moving, 1 – idling"],
    "252": ["Unplug", "0 – battery present, 1 – battery unplug"],
    "253": ["Green driving type", "1 – harsh acceleration, 2 – harsh braking, 3 – harsh cornering"],
    "246": ["Towing", "0 – steady, 1 – towing"],
    "247": ["Crash detection", "1 – crash, 2 – limited crash trace (device not calibrated), 3 - limited crash trace ("
                               "device is calibrated), 4 - full crash trace (device not calibrated), 5 - full crash "
                               "trace (device is calibrated), 6 - crash detected (device not calibrated)"],
    "257": ["Crash trace data", "Crash trace data"],
    "248": ["Immobilizer", "0 – iButton not connected, 1 – iButton connected (Immobilizer), 2 – iButton connected ( "
                           "Authorized Driving)"],
    "254": ["Green Driving Value", "Depending on green driving type: if harsh acceleration or braking – g*100 (value "
                                   "123 -> 1.23g), if harsh cornering – degrees (value in radians)"],
    "249": ["Jamming", "0 – jamming stop, 1 – jamming start"],
    "243": ["Green driving event duration", "Duration of event that did generate Green driving"],
    "236": ["Alarm", "0 – Reserved, 1 – Alarm event occured"],
    "242": ["ManDown/FallDown", "0 – ManDown/FallDown deactivated, 1 – ManDown/FalDown is active"],
    "310": ["Movement Event", "0 - Movement event occurred, 1 - No Movement event occured"],
    "389": ["Button Click", "Button ID (X) and Action (Y) Value 0xXY, X - button ID:, 1 - alarm button, 2 - power "
                            "button, 3 - button 1, 4 - button 2, 5 - button 3, Y - action:, 1 - 1 click, "
                            "2 - 2 clicks, 3 - long click"],
    "390": ["Power Event", "1 - Device turned OFF, 0 - Device turned ON"],
    "520": ["Tamper detection Event", "0 - Tamper restore, 1 - Tamper alarm"],
    "386": ["Last Known Position", "Time in seconds has passed since last GNSS fix"],
    "400": ["Amber Alert state", "0 - Turned Off, 1 - Turned On, count down timer started, 2 - Amber Alert On button "
                                 "pressed to restart active timer, 3 - Alarm, 4 - Amber Alert turned On when timer is "
                                 "set to 0 seconds"],
    "401": ["Amber Alert timer value", "Sends Amber Alert time-out configured value"],
    "403": ["Heart Rate Alert", "Sends heart rate (BPM) from Xiaomi Mi Band 2"],
    "20012": ["Recovery mode alarm", "0 – Reserved, 1 – Reserved, 2 - Recovery alarm event occured"],
    "339": ["Serial number", "Scooter serial number"],
    "340": ["Master control FW version[1]", "Scooter's PCB and FW versions. First 4 bits (MSB) describe PCB version "
                                            "and the rest 12 bits - FW version. For example, IO value is 0x1101, "
                                            "it means PCB version is 1 and FW version V1.0.1."],
    "341": ["Error", "Scooter error code from 10 to 50."],
    "342": ["Alarm code	", "9 – alarm for being pushed in lock mode, 12 – alarm for high recoil energy during brake"],
    "344": ["Lock status", "0 - Scooter is unlocked, 1 - Scooter is locked"],
    "345": ["Buzzer alarm status", "0 - Scooter's buzzer is not active, 1 - Scooter's buzzer is active"],
    "346": ["External battery status", "0 - Scooter don't have external battery connected, 1 - Scooter has external "
                                       "battery connected"],
    "347": ["Charging status", "0 – not charging, 1 - charging"],
    "349": ["Current operation mode", "0 – NORMAL, 1 – ECO, 2 – SPORT"],
    "350": ["Internal battery voltage", "Scooter's internal battery voltage"],
    "351": ["External battery voltage", "Scooter's external battery voltage	"],
    "352": ["Battery percentage", "Battery percentage of the scooter"],
    "353": ["Actual remaining mileage", "Actual mileage with remaining battery power"],
    "354": ["Predicted remaining mileage", "Predicted mileage with remaining battery power"],
    "355": ["Speed", "Current scooter's speed"],
    "356": ["Total mileage", "Scooter's total mileage"],
    "357": ["Single mileage", "Single trip mileage"],
    "358": ["Total operation time", "Scooter's total operation time"],
    "359": ["Total riding time", "Scooter's total riding time"],
    "360": ["Single operation time", "Single operation time"],
    "361": ["Single riding time", "Single riding time"],
    "362": ["Body temperature", "Temperature inside scooter"],
    "363": ["Internal battery temperature 1", "Internal battery temperature 1"],
    "364": ["Internal battery temperature 2", "Internal battery temperature 2"],
    "365": ["External battery temperature 1", "External battery temperature 1"],
    "366": ["Supply voltage", "Supply voltage of the central control (system driving voltage)"],
    "367": ["External battery temperature 2", "External battery temperature 2"],
    "369": ["Average speed", "Average speed"],
    "370": ["External battery FW version[1]", "Scooter's external battery FW version"],
    "371": ["Internal battery FW version[1]", "Scooter's internal battery FW version"],
    "372": ["Instrument panel FW version[1]", "Scooter's Instrument panel FW version"],
    "374": ["Internal battery capacity", "Current residual capacity percentage of internal battery"],
    "375": ["External battery capacity", "Current residual capacity percentage of external battery"],
    "392": ["Normal speed limit", "Normal speed limit"],
    "393": ["Eco speed limit", "Eco speed limit"],
    "394": ["Sport speed limit", "Sport speed limit"],
    "396": ["Battery lock status", "Battery lock status"],
    "397": ["Cable lock Status", "Cable lock Status"],
    "377": ["Cable lock FW version", "Cable lock FW version"],
    "801": ["Park Brake", "Park Brake IO element is used to indicate if parking brake is active, according to CAN "
                          "signal., 0 - Disengaged, 1 - Engaged, 2 - Error, 3 - Unused"],
    "802": ["Selected", "Charger state IO element is indicaiting current charger state, according to signal on CAN "
                        "line., 0 - Disconnected, 1 - Connected, 2 - Error, 3 - Unused"],
    "803": ["Selected Charge Mode", "Selected Charge mode IO element is indicating which charge mode is currently in "
                                    "use, according to signal on CAN line., 0 - Default, 1 - Fast"],
    "804": ["Charger Voltage", "Charger Voltage Setpoint"],
    "805": ["Charger Current", "Charger Current Setpoint"],
    "806": ["Charger Control Mode", "Charger Control Mode IO element indicates which charger control mode is "
                                    "currently in use., 0-Remote Control C-V-Limiting, 1-Open Circuit"],
    "807": ["Charger BMS COM Timeout", "BMS COM Timeout IO element indicates if BMS COM Timeout has been expired., "
                                       "0-Expired, 1-Not expired"],
    "808": ["Charger CRC Violation", "Charger CRC Violation IO element indicates if charger CRC violation has "
                                     "happened., 0-No CRC Violation happened, 1-CRC Violation happened"],
    "809": ["Charger MC Violation", "Charger MC Violation IO element indicates if charger MC violation has happened. "
                                    "0-No MC Violation happened, 1-MC Violation happened"],
    "810": ["Charger Status", "Charger Status IO element indicates current charger status, according to CAN signal. "
                              "0-No Errorbr, 1-Minimal Current Limiting, 2-Reverse Polarity, 3-Reserved, "
                              "4-Cable Voltage Drop, 5-Fan Error, 6-AC Undervoltage Disconnect, 7-Not Ready For "
                              "Charging"],
    "811": ["Charger Voltage Actual", "Acctual Voltage IO element indicates measured actual charging voltage in mV, "
                                      "according to CAN signal."],
    "812": ["Charger Internal Fault", "Charger Internal Fault IO element indicates if charger internal fault "
                                      "happened, according to CAN signal. 0-Internal Fault happened, "
                                      "1-No InternalFault happened"],
    "813": ["Charger Energy", "Charger Energy IO element indicates currently measured charger energy."],
    "814": ["Charger Current Actual", "Charger Current IO element indicates currently measured charger current."],
    "815": ["Throttle Position", "Throttle Position IO element indicates currently measured throttle position."],
    "816": ["Brake Pressed", "Brake Pressed IO element indicates if brake is pressed or not. 0-Brake Pressed, "
                             "1-Brake Not Pressed"],
    "817": ["Charge Plug", "Charge Plugged IO element indicates if charger is plugged in or not. 0-Charger Plugged, "
                           "1-Charger Not Plugged"],
    "818": ["Kill Switch Active", "Kill Switch Active IO element indicates if kill switch is active or not. 0-Kill "
                                  "Switch Active, 1-Kill Switch Not Active"],
    "819": ["Kickstand Release", "Kickstand Release Status IO element indicates if kickstand released or not. "
                                 "0-Kickstand Released, 1-Kickstand Not Released"],
    "820": ["Powerstrain State", "Powertrain State IO element indicates current powertrain state. 0-Off, 1-Booting, "
                                 "2-Ready, 3-Drive, 4-Charge, 5-Shutdown, 6-Error"],
    "821": ["Malfunction Indicator", "Malfunction Indication IO element indicates if malfunction indicator is active. "
                                     "0-Malfunction Indicator Not Active, 1-Malfunction Indicator Active"],
    "822": ["Current range", "Current Range IO element indicates currently measured current range"],
    "823": ["SoH Battery", "SoH Battery IO element indicates currently measured batery SoH."],
    "824": ["SoC Battery", "SoC Battery IO element indicates currently measured batery SoC."],
    "825": ["Vehicle available", "Vehicle Available IO element indicates if vehicle is currently available or not. "
                                 "0-Vehicle Not Available, 1-Vehicle Available"],
    "826": ["Charging Active", "Charging Active IO element indicates if charging is currently active or not. "
                               "0-Charging Not Active, 1-Charging Active"],
    "827": ["Remaining Charge Time", "Remaining Charging Time IO element indicates remaining charging time until "
                                     "vehicle is fully charged."],
    "828": ["Remaining Capacity", "Remaining Capacity IO element indicates reimaining battery capacity."],
    "829": ["Full Charge Capacity", "Full Charge Capacity IO element indicates full charge battery capacity."],
    "830": ["Driving direction", "Driving Direction IO element indicates current vehicle driving direction. 0-Park, "
                                 "1-Reverse, 2-Forward, 3-Neutral"],
    "831": ["Drive Mode", "Drive Mode IO element indicates current vehicle drive mode. 0-Go, 1-Cruise, 2-Boost, "
                          "3-Reserved1"],
    "832": ["Park Brake Active", "Park Brake Active IO element indicates if park brake is currently active or not. "
                                 "0-Park Brake Not Active, 1-Park Brake Active"],
    "833": ["Total Distance", "Total Distance IO element indicates measured vehicle total traveled distance."],
    "834": ["Trip Distance", "Trip Distance IO element indicates measured vehicle traveled distance during current "
                             "trip."],
    "835": ["Vehicle speed", "Vehicle Speed IO element indicates currently measured vehicle speed in km/h."],
    "836": ["Ignition Status", "Ignition Status IO element current vehicle ignition status. 0-IGN_LOCK, 1-IGN_OFF, "
                               "2-IGN_ACC, 3-Free, 4-IGN_ON, 5-IGN_START, 6-LeM_NM:IGN_OFF, 7-LeM_NM:IGN_ON"],
    "837": ["Ignition Fast Status", "Ignition Fast Status IO element indicates if ignition is active or not. "
                                    "0-Ignition Not Active, 1-Ignition Active"],
    "838": ["Power Consumption", "Power Consumption IO element indicates currently measured vehicle power consumption "
                                 "in"],
    "1121": ["CAN Unlocked", "Defines if vehicle is unlocked"],
    "1122": ["BMS2 Temperature Current Max", None],
    "1123": ["BMS2 Temperature Current Min", None],
    "1124": ["BMS2 Voltage Cell Min", None],
    "1125": ["BMS2 Voltage Cell Max", None],
    "1100": ["BMS0 Temperature Current Max", None],
    "1101": ["BMS0 Temperature Current Min", None],
    "11002": ["BMS0 Voltage Cell Min", None],
    "11003": ["BMS0 Voltage Cell Max", None],
    "1104": ["BMS1 Temperature Current Max", None],
    "1105": ["BMS1 Temperature Current Min", None],
    "1106": ["BMS1 Voltage Cell Min", None],
    "1107": ["BMS1 Voltage Cell Max", None],
    "843": ["Helmet Status", "Indicates if Helmet is in or not. 0 – not in, 1 – in."],
    "844": ["Top Case Sensor", "Indicates if Top Case is open or closed. 0 – closed, 1 – open."],
    "845": ["Central Stand Up", "Indicates if central stand is up or down. 0 – down, 1 – up."],
    "846": ["Emergency", "Indicates if there is emergency or not. 0 – no emergency, 1 - emergency"],
    "847": ["Over-Under Temperature", "Indicates if there is battery over or under temperature warning. 0 – normal "
                                      "temperature, 1 – over-under temperature"],
    "848": ["Regeneration Disabled", "Indicates if battery regeneration is disabled. 0 – enabled, 1 – disabled."],
    "849": ["Battery On/Off", "Indicates if battery is on or off. 0 – Battery Off, 1 – Battery On"],
    "850": ["Warning UnderVoltage", "Indicates if there is battery undervoltage warning. 0 – no battery undervoltage, "
                                    "1 – battery undervoltage."],
    "851": ["Warning OverVoltage", "Indicates if there is battery overvoltage warning. 0 – No battery overvoltage, "
                                   "1 – battery overvoltage."],
    "852": ["Warning OverCurrent", "Indicates if there is battery overcurrent warning. 0 – No battery overcurrent, "
                                   "1 – battery overcurrent."],
    "853": ["Warning Short Circuit", "Indicates if there is battery short circuit warning. 0 – No battery short "
                                     "circuit, 1 – battery short circuit."],
    "900": ["Manual CAN 0", "Manual CAN0"],
    "901": ["Manual CAN 1", "Manual CAN1"],
    "902": ["Manual CAN 2", "Manual CAN2"],
    "903": ["Manual CAN 3", "Manual CAN3"],
    "904": ["Manual CAN 4", "Manual CAN4"],
    "905": ["Manual CAN 5", "Manual CAN5"],
    "906": ["Manual CAN 6", "Manual CAN6"],
    "907": ["Manual CAN 7", "Manual CAN7"],
    "908": ["Manual CAN 8", "Manual CAN8"],
    "909": ["Manual CAN 9", "Manual CAN9"],
    "910": ["Manual CAN 10", "Manual CAN10"],
    "911": ["Manual CAN 11", "Manual CAN11"],
    "912": ["Manual CAN 12", "Manual CAN12"],
    "913": ["Manual CAN 13", "Manual CAN13"],
    "914": ["Manual CAN 14", "Manual CAN14"],
    "915": ["Manual CAN 15", "Manual CAN15"],
    "916": ["Manual CAN 16", "Manual CAN16"],
    "917": ["Manual CAN 17", "Manual CAN17"],
    "918": ["Manual CAN 18", "Manual CAN18"],
    "919": ["Manual CAN 19", "Manual CAN19"],
    "920": ["Manual CAN 20", "Manual CAN20"],
    "921": ["Manual CAN 21", "Manual CAN21"],
    "922": ["Manual CAN 22", "Manual CAN22"],
    "923": ["Manual CAN 23", "Manual CAN23"],
    "924": ["Manual CAN 24", "Manual CAN24"],
    "925": ["Manual CAN 25", "Manual CAN25"],
    "926": ["Manual CAN 26", "Manual CAN26"],
    "927": ["Manual CAN 27", "Manual CAN27"],
    "928": ["Manual CAN 28", "Manual CAN28"],
    "929": ["Manual CAN 29", "Manual CAN29"],
    "930": ["Accelerator Pedal 1 Low Idle Switch", "Switch signal which indicates the state of the accelerator pedal "
                                                   "1 low idle switch. 0 - Accelerator pedal 1 not in low idle "
                                                   "condition, 1 - Accelerator pedal 1 in low idle condition, "
                                                   "2 - Error, 3 - Not available"],
    "931": ["Accelerator Pedal Kickdown Switch", "Switch signal which indicates whether the accelerator pedal "
                                                 "kickdown switch is opened or closed. 0 - Kickdown passive, "
                                                 "1 - Kickdown active, 2 - Error, 3 - Not available"],
    "932": ["Road Speed Limit Status", "Status (active or not active) of the system used to limit maximum vehicle "
                                       "velocity. 0 - Active, 1 - Not Active, 2 - Error, 3 - Not available"],
    "933": ["Accelerator Pedal 2 Low Idle Switch", "Switch signal which indicates the state of the accelerator pedal "
                                                   "2 low idle switch. 0 - Accelerator pedal 2 not in low idle "
                                                   "condition, 1 - Accelerator pedal 2 in low idle condition, "
                                                   "2 - Error, 3 - Not available"],
    "934": ["Accelerator Pedal Position 1", "This parameter is intended for the primary accelerator control in an "
                                            "application."],
    "936": ["Engine Percent Load At Current Speed", "The ratio of actual engine percent torque (indicated) to maximum "
                                                    "indicated torque available at the current engine speed, "
                                                    "clipped to zero torque during engine braking."],
    "937": ["Remote Accelerator Pedal Position", "The ratio of actual position of the remote analog engine "
                                                 "speed/torque request input device (such as an accelerator pedal or "
                                                 "throttle lever) to the maximum position of the input device."],
    "938": ["Accelerator Pedal 2 Position", "The ratio of actual position of the second analog engine speed/torque "
                                            "request input device (such as an accelerator pedal or throttle lever) to "
                                            "the maximum position of the input device. This parameter is intended for "
                                            "secondary accelerator control in an application."],
    "939": ["Vehicle Acceleration Rate Limit Status", "Status (active or not active) of the system used to limit "
                                                      "maximum forward vehicle acceleration. 0 - Limit not active, "
                                                      "1 - Limit active, 2 - Reserved, 3 - Not available"],
    "940": ["Momentary Engine Maximum Power Enable Feedback", "Momentarily requesting Engine Maximum Power Enable - "
                                                              "feature support feedback 0 - disabled, 1 - supported, "
                                                              "2 - reserved, 3 - don't care"],
    "941": ["DPF Thermal Management Active", "Indicates that the exhaust temperatures have been elevated for "
                                             "regeneration of the diesel particulate filter aftertreatment system or "
                                             "in preparation of regeneration of the diesel particulate aftertreatment "
                                             "system. 0 - DPF Thermal Management is not active, 1 - DPF Thermal "
                                             "Management is active, 2 - Reserved, 3 - Don't care"],
    "942": ["SCR Thermal Management Active", "Indicates that the exhaust temperatures have been elevated for "
                                             "regeneration of the SCR aftertreatment system or in preparation of "
                                             "regeneration of the SCR aftertreatment system. 0 - SCR Thermal "
                                             "Management is not active, 1 - SCR Thermal Management is active, "
                                             "2 - Reserved, 3 - Don't care"],
    "943": ["Actual Maximum Available Engine - Percent Torque", "This is the maximum amount of torque that the engine "
                                                                "can immediately deliver as a percentage of the "
                                                                "reference engine torque."],
    "944": ["Estimated Pumping - Percent Torque", "The calculated torque that indicates the estimated amount of "
                                                  "torque loss due to the engine air handling system."],
    "945": ["Engine Torque Mode", "State signal which indicates which engine torque mode is currently generating, "
                                  "limiting, or controlling the torque. Mode 0 - “No request”: engine torque may "
                                  "range from 0 to full load only due to low idle governor output. Modes 1 to 14 "
                                  "indicate that there is either a torque request or the identified function is "
                                  "currently controlling the engine: engine torque may range from 0 (no fueling) to "
                                  "the upper limit. Mode 15 -"],
    "946": ["Actual Engine - Percent Torque (Fractional)", "This parameter displays an additional torque in percent "
                                                           "of the reference engine torque. 0 - +0.000%, "
                                                           "1 - +0.125%...9 - +0.875%, 10 to 15 - not available"],
    "947": ["Driver’s Demand Engine - Percent Torque", "The requested torque output of the engine by the driver."],
    "948": ["Actual Engine - Percent Torque", "The calculated output torque of the engine."],
    "949": ["Engine Speed", "Actual engine speed which is calculated over a minimum crankshaft angle of 720 degrees "
                            "divided by the number of cylinders."],
    "950": ["Source Address of Controlling Device for Engine Control", "The source address of the SAE J1939 device "
                                                                       "currently controlling the engine."],
    "951": ["Engine Starter Mode", "There are several phases in a starting action and different reasons why a start "
                                   "cannot take place. 0 - start not requested, 1 - starter active but not engaged, "
                                   "2 - starter active and engaged, 3 - start finished; starter not active after "
                                   "having been actively engaged (after 50ms mode goes to 0), 4 - starter inhibited "
                                   "due to engine already running, 5 - starter inhibited due to engine not ready for "
                                   "start (preheating), 6 - starter inhibited due to driveline engaged or other "
                                   "transmission inhibit, 7 - starter inhibited due to active immobilizer, "
                                   "8 - starter inhibited due to starter over-temp, 9 - starter inhibited due to "
                                   "intake air shutoff valve being active, 10 - starter inhibited due to active "
                                   "emissions control system condition, 11 - starter inhibited due to ignition key "
                                   "cycle required, 12 - starter inhibited - reason unknown, 13 - error (legacy "
                                   "implementation only, use 14), 14 - error, 15 - not available"],
    "952": ["Engine Demand – Percent Torque", "The calculated torque that indicates the estimated amount of torque "
                                              "loss due to the engine air handling system."],
    "953": ["Aftertreatment 1 Diesel Oxidation Catalyst Intake Temperature", "Temperature of engine combustion "
                                                                             "byproducts entering the diesel "
                                                                             "oxidation catalyst in exhaust bank 1."],
    "954": ["Aftertreatment 1 Diesel Oxidation Catalyst Outlet Temperature", "Temperature of engine combustion "
                                                                             "byproducts leaving the diesel oxidation "
                                                                             "catalyst exhaust in exhaust bank 1."],
    "955": ["Aftertreatment 1 Diesel Oxidation Catalyst Differential Pressure", "Exhaust differential pressure "
                                                                                "measured between the intake and "
                                                                                "exhaust of a diesel oxidation "
                                                                                "catalyst in exhaust bank 1."],
    "956": ["Aftertreatment 1 Diesel Oxidation Catalyst Intake Temperature Preliminary FMI", "Used to identify the "
                                                                                             "applicable J1939-73 FMI "
                                                                                             "detected in the diesel "
                                                                                             "oxidation catalyst "
                                                                                             "intake temperature "
                                                                                             "sensor by the "
                                                                                             "manufacturer’s sensor "
                                                                                             "control software in "
                                                                                             "exhaust bank 1. A value "
                                                                                             "of 31 is sent to "
                                                                                             "indicate that no "
                                                                                             "failure has been "
                                                                                             "detected or this "
                                                                                             "parameter is not "
                                                                                             "supported."],
    "957": ["Aftertreatment 1 Diesel Oxidation Catalyst Outlet Temperature Preliminary FMI", "Used to identify the "
                                                                                             "applicable J1939-73 FMI "
                                                                                             "detected in the diesel "
                                                                                             "oxidation catalyst "
                                                                                             "outlet gas temperature "
                                                                                             "sensor by the "
                                                                                             "manufacturer’s sensor "
                                                                                             "control software in "
                                                                                             "exhaust bank 1. A value "
                                                                                             "of 31 is sent to "
                                                                                             "indicate that no "
                                                                                             "failure has been "
                                                                                             "detected or this "
                                                                                             "parameter is not "
                                                                                             "supported."],
    "958": ["Aftertreatment 1 Diesel Oxidation Catalyst Differential Pressure Preliminary FMI", "Used to identify the "
                                                                                                "applicable J1939-73 "
                                                                                                "FMI detected in the "
                                                                                                "diesel oxidation "
                                                                                                "catalyst "
                                                                                                "differential "
                                                                                                "pressure sensor by "
                                                                                                "the manufacturer’s "
                                                                                                "sensor control "
                                                                                                "software in exhaust "
                                                                                                "bank 1. A value of "
                                                                                                "31 is sent to "
                                                                                                "indicate that no "
                                                                                                "failure has been "
                                                                                                "detected or this "
                                                                                                "parameter is not "
                                                                                                "supported."],
    "959": ["Aftertreatment 1 Diesel Particulate Filter Soot Load Percent", "Indicates the soot load percent of "
                                                                            "diesel particulate filter 1."],
    "960": ["Aftertreatment 1 Diesel Particulate Filter Ash Load Percent", "Indicates the ash load percent of diesel "
                                                                           "particulate filter 1."],
    "961": ["Aftertreatment 1 Diesel Particulate Filter Time Since Last Active Regeneration", "Indicates the time "
                                                                                              "since the last active "
                                                                                              "regeneration event of "
                                                                                              "diesel particulate "
                                                                                              "filter 1."],
    "962": ["Aftertreatment 1 Diesel Particulate Filter Soot Load Regeneration Threshold", "This parameter indicates "
                                                                                           "the value that will first "
                                                                                           "cause DPF regeneration in "
                                                                                           "aftertreatment 1."],
    "963": ["Aftertreatment 1 Exhaust Temperature 2", "The reading from the exhaust temperature sensor located "
                                                      "midstream of the other two temperature sensors in the "
                                                      "aftertreatment system in exhaust bank 1."],
    "964": ["Aftertreatment 1 Diesel Particulate Filter Intermediate Temperature", "Temperature of engine combustion "
                                                                                   "byproducts at a mid-point in the "
                                                                                   "diesel particulate filter in "
                                                                                   "exhaust bank 1."],
    "965": ["Aftertreatment 1 Diesel Particulate Filter Differential Pressure", "Exhaust differential pressure "
                                                                                "measured between the intake and "
                                                                                "exhaust of a diesel particulate "
                                                                                "filter in exhaust bank 1."],
    "966": ["Aftertreatment 1 Exhaust Temperature 2 Preliminary FMI", "Used to identify the applicable J1939-73 FMI "
                                                                      "detected in the exhaust temperature 2 sensor "
                                                                      "by the manufacturer’s sensor control software "
                                                                      "in exhaust bank 1. In the case of multiple "
                                                                      "failures the most severe is communicated. A "
                                                                      "value of 31 is sent to indicate that no "
                                                                      "failure has been detected or this parameter is "
                                                                      "not supported."],
    "967": ["Aftertreatment 1 Diesel Particulate Filter Differential Pressure Preliminary FMI", "Used to identify the "
                                                                                                "applicable J1939-73 "
                                                                                                "FMI detected in the "
                                                                                                "diesel particulate "
                                                                                                "filter differential "
                                                                                                "pressure sensor by "
                                                                                                "the manufacturer’s "
                                                                                                "sensor control "
                                                                                                "software in exhaust "
                                                                                                "bank 1. In the case "
                                                                                                "of multiple failures "
                                                                                                "the most severe is "
                                                                                                "communicated. A "
                                                                                                "value of 31 is sent "
                                                                                                "to indicate that no "
                                                                                                "failure has been "
                                                                                                "detected or this "
                                                                                                "parameter is not "
                                                                                                "supported."],
    "968": ["Aftertreatment 1 Diesel Particulate Filter Intermediate Temperature Preliminary FMI", "Used to identify "
                                                                                                   "the applicable "
                                                                                                   "J1939-73 FMI "
                                                                                                   "detected in the "
                                                                                                   "diesel "
                                                                                                   "particulate "
                                                                                                   "filter "
                                                                                                   "intermediate "
                                                                                                   "temperature "
                                                                                                   "sensor by the "
                                                                                                   "manufacturer’s "
                                                                                                   "sensor control "
                                                                                                   "software in "
                                                                                                   "exhaust bank 1. "
                                                                                                   "In the case of "
                                                                                                   "multiple failures "
                                                                                                   "the most severe "
                                                                                                   "is communicated. "
                                                                                                   "A value of 31 is "
                                                                                                   "sent to indicate "
                                                                                                   "that no failure "
                                                                                                   "has been detected "
                                                                                                   "or this parameter "
                                                                                                   "is not "
                                                                                                   "supported."],
    "969": ["Aftertreatment 1 Exhaust Temperature 1", "The reading from the exhaust temperature sensor located "
                                                      "farthest upstream in the aftertreatment system in exhaust bank "
                                                      "1."],
    "970": ["Aftertreatment 1 Diesel Particulate Filter Intake Temperature", "Temperature of engine combustion "
                                                                             "byproducts entering the diesel "
                                                                             "particulate filter in exhaust bank 1."],
    "971": ["Aftertreatment 1 Exhaust Temperature 1 Preliminary FMI", "Used to identify the applicable J1939-73 FMI "
                                                                      "detected in the exhaust temperature 1 sensor "
                                                                      "by the manufacturer’s sensor control software "
                                                                      "in exhaust bank 1. In the case of multiple "
                                                                      "failures the most severe is communicated. A "
                                                                      "value of 31 is sent to indicate that no "
                                                                      "failure has been detected or this parameter is "
                                                                      "not supported."],
    "972": ["Aftertreatment 1 Diesel Particulate Filter Intake Temperature Preliminary FMI", "Used to identify the "
                                                                                             "applicable J1939-73 FMI "
                                                                                             "detected in the diesel "
                                                                                             "particulate filter "
                                                                                             "intake temperature "
                                                                                             "sensor by the "
                                                                                             "manufacturer’s sensor "
                                                                                             "control software in "
                                                                                             "exhaust bank 1. In the "
                                                                                             "case of multiple "
                                                                                             "failures the most "
                                                                                             "severe is communicated. "
                                                                                             "A value of 31 is sent "
                                                                                             "to indicate that no "
                                                                                             "failure has been "
                                                                                             "detected or this "
                                                                                             "parameter is not "
                                                                                             "supported."],
    "973": ["Trip Fuel (Gaseous)", "Total fuel consumed (trip drive fuel + trip PTO governor moving fuel + trip PTO "
                                   "governor non-moving fuel + trip idle fuel) since the last trip reset."],
    "974": ["Total Fuel Used (Gaseous)", "Total fuel consumed (trip drive fuel + trip PTO governor moving fuel + trip "
                                         "PTO governor non-moving fuel + trip idle fuel) over the life of the "
                                         "engine."],
    "989": ["Trip Vehicle Distance", "Distance traveled during all or part of a journey."],
    "990": ["Total Vehicle Distance", "Accumulated distance traveled by vehicle during its operation."],
    "991": ["Engine Total Hours of Operation", "Accumulated time of operation of engine."],
    "992": ["Engine Total Revolutions", "Accumulated number of revolutions of engine crankshaft during its operation."],
    "993": ["Total Vehicle Hours", "Accumulated time of operation of vehicle."],
    "994": ["Total Power Takeoff Hours", "Accumulated time of operation of power takeoff device."],
    "995": ["Engine Trip Fuel", "Fuel consumed during all or part of a journey."],
    "996": ["Engine Total Fuel Used	", "Accumulated amount of fuel used during vehicle operation."],
    "1002": ["Engine Coolant Temperature", "Temperature of liquid found in engine cooling system."],
    "1003": ["Engine Fuel 1 Temperature 1", "Temperature of fuel (or gas) of the first fuel type."],
    "1004": ["Engine Oil Temperature 1", "Temperature of the engine lubricant."],
    "1005": ["Engine Turbocharger 1 Oil Temperature", "Temperature of the turbocharger lubricant."],
    "1006": ["Engine Intercooler Temperature", "Temperature of liquid found in the intercooler located after the "
                                               "turbocharger."],
    "1007": ["Engine Charge Air Cooler Thermostat Opening", "The current position of the thermostat used to regulate "
                                                            "the temperature of the engine charge air cooler. A value "
                                                            "of 0% represents the thermostat being completely closed "
                                                            "and 100% represents the thermostat being completely "
                                                            "open."],
    "1008": ["Engine Fuel Delivery Pressure", "Gage pressure of fuel in system as delivered from supply pump to the "
                                              "injection pump."],
    "1009": ["Engine Extended Crankcase Blow-by Pressure", "Differential crankcase blow-by pressure as measured "
                                                           "through a tube with a venturi."],
    "1010": ["Engine Oil Level", "Ratio of current volume of engine sump oil to maximum required volume."],
    "1011": ["Engine Oil Pressure 1", "Gage pressure of oil in engine lubrication system as provided by oil pump."],
    "1012": ["Engine Crankcase Pressure 1", "First instance of the gage pressure inside engine crankcase."],
    "1013": ["Engine Coolant Pressure 1", "Gage pressure of liquid found in engine cooling system."],
    "1014": ["Engine Coolant Level 1", "Ratio of volume of liquid found in engine cooling system to total cooling "
                                       "system volume."],
    "1015": ["Two Speed Axle Switch", "Switch signal which indicates the current axle range. 0 - Low speed range, "
                                      "1 - High speed range, 2 - Error, 3 - Not available"],
    "1016": ["Two Speed Axle Switch", "Switch signal which indicates when the parking brake is set. 0 - Parking brake "
                                      "not set, 1 - Parking brake set, 2 - Error, 3 - Not available"],
    "1017": ["Cruise Control Pause Switch", "Switch signal which indicates the position of the Cruise Control Pause "
                                            "Switch used on Remote Cruise Control applications. The Cruise Control "
                                            "Pause Switch signal temporarily disables the Cruise Control function. 0 "
                                            "- Off, 1 - On, 2 - Error Indicator, 3 - Take No Action"],
    "1018": ["Park Brake Release Inhibit Request", "Park Brake Release Inhibit Request signals the desire that an "
                                                   "applied park brake remain applied and limit the ability of the "
                                                   "vehicle to be moved. 0 - Park Brake Release Inhibit not "
                                                   "requested, 1 - Park Brake Release Inhibit requested, "
                                                   "2 - SAE reserved, 3 - Unavailable"],
    "1019": ["Wheel-Based Vehicle Speed	", "Speed of the vehicle as calculated from wheel or tailshaft speed."],
    "1020": ["Cruise Control Active", "Cruise control is switched on. 0 - Cruise control switched off, 1 - Cruise "
                                      "control switched on, 2 - Error, 3 - Not available"],
    "1021": ["Cruise Control Enable Switch", "Switch signal which indicates that it is possible to manage the cruise "
                                             "control function. 0 - Cruise control disabled, 1 - Cruise control "
                                             "enabled, 2 - Error, 3 - Not available"],
    "1022": ["Brake Switch", "Switch signal which indicates that the driver operated brake foot pedal is being "
                             "pressed. 0 - Brake pedal released, 1 - Brake pedal depressed, 2 - Error, "
                             "3 - Not Available"],
    "1023": ["Clutch Switch", "Switch signal which indicates that the clutch pedal is being pressed. 0 - Clutch pedal "
                              "released, 1 - Clutch pedal, 2 - Error, 3 - Not available"],
    "1024": ["Cruise Control Set Switch", "Switch signal of the cruise control activator which indicates that the "
                                          "activator is in the position \"set.\" 0 - Cruise control activator not in "
                                          "the position \"set\", 1 - Cruise control activator in position \"set\", "
                                          "2 - Error, 3 - Not available"],
    "1025": ["Cruise Control Coast (Decelerate) Switch", "Switch signal of the cruise control activator which "
                                                         "indicates that the activator is in the position \"coast ("
                                                         "decelerate).\" 0 - Cruise control activator not in the "
                                                         "position \"coast\", 1 - Cruise control activator in "
                                                         "position \"coast\", 2 - Error, 3 - Not available"],
    "1026": ["Cruise Control Resume Switch", "Switch signal of the cruise control activator which indicates that the "
                                             "activator is in the position \"resume.\" 0 - Cruise control activator "
                                             "not in the position \"resume\", 1 - Cruise control activator in "
                                             "position \"resume\", 2 - Error, 3 - Not available"],
    "1027": ["Cruise Control Accelerate Switch", "Switch signal of the cruise control activator which indicates that "
                                                 "the activator is in the position \"accelerate.\" 0 - Cruise control "
                                                 "activator not in the position \"accelerate\", 1 - Cruise control "
                                                 "activator in position \"accelerate\", 2 - Error, 3 - Not available"],
    "1028": ["Cruise Control Set Speed	", "Value of set (chosen) velocity of velocity control system."],
    "1029": ["PTO Governor State", "Cruise control is switched on. It is not ensured that the engine is controlled by "
                                   "cruise control, as in the case of a large driver's demand the engine is "
                                   "controlled by the driver while cruise control is active (maximum selection of "
                                   "cruise control and driver's demand). 0 - Cruise control switched off, 1 - Cruise "
                                   "control switched on, 2 - Error, 3 - Not available"],
    "1030": ["Cruise Control States", "This parameter is used to indicate the current state or mode of operation by "
                                      "the power takeoff (PTO) governor. 0 - Off/Disabled, 1 - Hold, 2 - Remote Hold, "
                                      "3 - Standby, 4 - Remote Standby, 5 - Set, 6 - Decelerate/Coast, 7 - Resume, "
                                      "8 - Accelerate, 9 - Accelerator Override, 10 - Preprogrammed set speed 1, "
                                      "11 - Preprogrammed set speed 2, 12 - Preprogrammed set speed 3, "
                                      "13 - Preprogrammed set speed 4, 14 - Preprogrammed set speed 5, "
                                      "15 - Preprogrammed set speed 6, 16 - Preprogrammed set speed 7, "
                                      "17 - Preprogrammed set speed 8, 18 - PTO set speed memory 1, 19 - PTO set "
                                      "speed memory 2, 20 - PTO set speed memory 3, 21 - Reserved, 22 - Reserved, "
                                      "23 - Reserved, 24 - Reserved, 25 - Reserved, 26 - Reserved, 27 - Reserved, "
                                      "28 - Reserved, 29 - Reserved, 30 - Reserved, 31 - Not available"],
    "1031": ["Engine Idle Increment Switch", "This parameter is used to indicate the current state, or mode, "
                                             "of operation by the cruise control device. This is a status parameter. "
                                             "0 - Off/Disabled, 1 - Hold, 2 - Accelerate, 3 - Decelerate, 4 - Resume, "
                                             "5 - Set, 6 - Accelerator Override, 7 - Not available"],
    "1032": ["Engine Idle Decrement Switch", "Switch signal which indicates the position of the idle increment "
                                             "switch. 0 - Off, 1 - On, 2 - Error, 3 - Not available"],
    "1033": ["Engine Diagnostic Test Mode Switch", "Switch signal which indicates the position of the engine "
                                                   "diagnostic test mode switch. 0 - Off, 1 - On, 2 - Error, "
                                                   "3 - Not available"],
    "1034": ["Engine Shutdown Override Switch", "Switch signal which indicates the position of the engine shutdown "
                                                "override switch. This switch function allows the operator to "
                                                "override an impending engine shutdown. 0 - Off, 1 - On, 2 - Error, "
                                                "3 - Not available"],
    "1035": ["Engine Fuel Rate", "Amount of fuel consumed by engine per unit of time."],
    "1036": ["Engine Instantaneous Fuel Economy", "Current fuel economy at current vehicle velocity."],
    "1037": ["Engine Average Fuel Economy", "Average of instantaneous fuel economy for that segment of vehicle "
                                            "operation of interest."],
    "1038": ["Engine Throttle Valve 1 Position 1", "The position of the valve used to regulate the supply of a fluid, "
                                                   "usually air or fuel/air mixture, to an engine. 0% represents no "
                                                   "supply and 100% is full supply."],
    "1039": ["Engine Throttle Valve 2 Position", "The sensed position feedback of the valve, coming from a second "
                                                 "electrical actuator for a second throttle plate, used to regulate "
                                                 "the supply of a fluid, usually air or fuel//air mixture. 0% "
                                                 "represents no supply and 100% is full supply."],
    "1040": ["Barometric Pressure", "Absolute air pressure of the atmosphere."],
    "1041": ["Cab Interior Temperature", "Temperature of air inside the part of the vehicle that encloses the driver "
                                         "and vehicle operating controls."],
    "1042": ["Ambient Air Temperature", "Temperature of air surrounding vehicle."],
    "1043": ["Engine Intake 1 Air Temperature", "Temperature of air entering vehicle air induction system."],
    "1044": ["Road Surface Temperature", "Indicated temperature of road surface over which vehicle is operating."],
    "1045": ["Aftertreatment 1 Diesel Particulate Filter Intake Pressure", "Exhaust pressure as a result of particle "
                                                                           "accumulation on filter media placed in "
                                                                           "the exhaust stream."],
    "1046": ["Engine Intake Manifold #1 Pressure", "The gauge pressure measurement of the air intake manifold. If "
                                                   "there are multiple air pressure sensors in the intake stream, "
                                                   "this is the last one in flow direction before entering the "
                                                   "combustion chamber. This should be the pressure used to drive "
                                                   "gauges and displays."],
    "1047": ["Engine Intake Manifold 1 Temperature", "Temperature of pre-combustion air found in intake manifold of "
                                                     "engine air supply system."],
    "1048": ["Engine Intake Air Pressure", "Absolute air pressure at input port to intake manifold or air box."],
    "1049": ["Engine Air Filter 1 Differential Pressure", "Change in engine air system pressure, measured across the "
                                                          "filter, due to the filter and any accumulation of solid "
                                                          "foreign matter on or in the filter."],
    "1050": ["Engine Exhaust Temperature", "Temperature of combustion byproducts leaving the engine."],
    "1051": ["Engine Coolant Filter Differential Pressure", "Change in coolant pressure, measured across the filter, "
                                                            "due to the filter and any accumulation of solid or "
                                                            "semisolid matter on or in the filter."],
    "1052": ["SLI Battery 1 Net Current", "Net flow of electrical current into/out of the first battery or first set "
                                          "of batteries used for starting the engine, for lighting, and for ignition "
                                          "(SLI)."],
    "1053": ["Alternator Current", "Measure of electrical current flow from the alternator."],
    "1054": ["Charging System Potential (Voltage)", "Electrical potential measured at the charging system output. The "
                                                    "charging system may be any device charging the batteries. This "
                                                    "includes alternators, generators, solid state charger and other "
                                                    "charging devices."],
    "1055": ["Battery Potential / Power Input 1", "This parameter measures the first source of battery potential as "
                                                  "measured at the input of the ECU/actuator etc. coming from one or "
                                                  "more batteries, irrespective of the distance between the component "
                                                  "and the battery."],
    "1056": ["Key Switch Battery Potential", "Battery potential measured at the input of the electronic control unit "
                                             "supplied through a key switch or similar switching device."],
    "1057": ["Transmission Clutch 1 Pressure", "Gage pressure of oil within a wet clutch."],
    "1058": ["Transmission Oil Level 1", "First instance of a transmission oil level indicator. Conveys the ratio of "
                                         "volume of transmission sump oil to recommended volume."],
    "1059": ["Transmission Filter Differential Pressure", "Change in transmission fluid pressure, measured after the "
                                                          "filter, due to accumulation of solid or semisolid material "
                                                          "on or in the filter."],
    "1060": ["Transmission 1 Oil Pressure", "Gage pressure of lubrication fluid in transmission 1, measured after pump."],
    "1061": ["Transmission Oil Temperature 1", "First instance of transmission lubricant temperature."],
    "1062": ["Transmission Oil Level 1 High / Low", "First instance of a transmission oil level indicator. Conveys "
                                                    "the amount of current volume of transmission sump oil compared "
                                                    "to recommended volume. Positive values indicate overfill. Zero "
                                                    "means the transmission fluild is filled to the recommended "
                                                    "level."],
    "1063": ["Transmission Oil Level 1 Countdown Timer", "Countdown timer for the first instance of a transmission "
                                                         "oil level indicator. Once all vehicle conditions (such as "
                                                         "vehicle stopped, etc) are met, some transmissions may "
                                                         "require a 'settling time' to allow the fluid level to "
                                                         "normalize. This parameter indicates how much of the "
                                                         "required settling time remains. 0 - less than 1 minute, "
                                                         "1 - One minute, 2 - Two minutes, 3 - Three minutes, "
                                                         "4 - Four minutes, 5 - Five minutes, 6 - Six minutes, "
                                                         "7 - Seven minutes, 8 - Eight minutes, 9 - Nine minutes, "
                                                         "10 - Ten minutes, 11 - Eleven minutes, 12 - Twelve minutes, "
                                                         "13 - Thirteen minutes, 14 - Error, 15 - Not Available"],
    "1064": ["Transmission Oil Level 1 Measurement Status", "Measurement status for the first instance of a "
                                                            "transmission oil level indicator. If conditions are not "
                                                            "acceptable, this parameter conveys to the operator what "
                                                            "prevents conditions from being acceptable. 0 - "
                                                            "Conditions valid for transmission oil level measurement, "
                                                            "1 - Conditions not valid – Settling timer still counting "
                                                            "down, 2 - Conditions not valid – Transmission in gear, "
                                                            "3 - Conditions not valid – Transmission fluid "
                                                            "temperature too low, 4 - Conditions not valid – "
                                                            "Transmission fluid temperature too high, 5 - Conditions "
                                                            "not valid – Vehicle moving; output shaft speed too high, "
                                                            "6 - Conditions not valid – Vehicle not level, "
                                                            "7 - Conditions not valid – Engine speed too low, "
                                                            "8 - Conditions not valid – Engine speed too high, "
                                                            "9 - Conditions not valid – No request for reading, "
                                                            "10 - Not defined, 11 - Not defined, 12 - Not defined, "
                                                            "13 - Conditions not valid - Other, 14 - Error, "
                                                            "15 - Not available"],
    "1065": ["Washer Fluid Level", "Ratio of volume of liquid to total container volume of fluid reservoir in "
                                   "windshield wash system."],
    "1066": ["Fuel Level 1", "Ratio of volume of fuel to the total volume of fuel storage container."],
    "1067": ["Engine Fuel Filter Differential Pressure", "Change in fuel delivery pressure, measured across the "
                                                         "filter, due to accumulation of solid or semisolid matter on "
                                                         "the filter element."],
    "1068": ["Engine Oil Filter Differential Pressure", "Change in engine oil pressure, measured across the filter, "
                                                        "due to the filter and any accumulation of solid or semisolid "
                                                        "material on or in the filter."],
    "1069": ["Cargo Ambient Temperature", "Temperature of air inside vehicle container used to accommodate cargo."],
    "1070": ["Fuel Level 2", "Ratio of volume of fuel to the total volume of fuel in the second or right-side storage "
                             "container."],
    "1071": ["Engine Oil Filter Differential Pressure (Extended Range)", "Change in engine oil pressure, measured "
                                                                         "across the filter, due to the filter and "
                                                                         "any accumulation of solid or semisolid "
                                                                         "material on or in the filter."],
    "1126": ["Max Available Power", "Maximum available power"],
    "1127": ["Handlebar Lock", "Handlebar lock status"],
    "1128": ["Rear Brake Pressed", "Rear brake status"],
    "1129": ["COM Error", "COM Error"],
    "1130": ["RPM", "RPM"],
    "1131": ["Torque Current", "Torque current"],
    "1132": ["SN High", "SN High"],
    "1133": ["SN Low", "SN Low"],
    "1134": ["Lowest Battery Voltage", "Lowest battery voltage"],
    "1135": ["Lowest Battery ID", "Lowest battery ID"],
    "1136": ["Highest Battery Voltage", "Highest battery voltage"],
    "1137": ["Highest Battery ID", "Highest battery ID"],
    "1138": ["Highest Mismatch Voltage", "Highest mismatch voltage"],
    "1139": ["Highest Mismatch ID", "Highest mismatch ID"],
    "1140": ["Lowest Battery Temperature", "Lowest battery temperature"],
    "1141": ["Lowest Temperature Battery ID", "Lowest temperature battery ID"],
    "1142": ["Highest Battery Temperature", "Highest battery temperature"],
    "1143": ["Highest Temperature Battery ID", "Highest temperature battery ID"],
    "1144": ["Time To Full Load", "Time to full load"],
    "1145": ["Time To Empty", "Time to empty"],
    "1146": ["Time To Full", "Time to full"],
    "1147": ["Cluster State", "Cluster state"],
    "1148": ["Cluster SoC", "Cluster SoC"],
    "1149": ["Max Discharge Current", "Max discharge current"],
    "1150": ["Recuperation Allowed", "Recuperation status"],
    "1151": ["Switch Process Needed", "Switch process status"],
    "1152": ["SoC Switch Level", "SoC switch level"],
    "1153": ["Part Charge Capacity", "Part charge capacity"],
    "1154": ["Cluster Voltage", "Cluster voltage"],
    "1155": ["Cluster Current", "Cluster current"],
    "1156": ["Major Version", "Major version"],
    "1157": ["Minor Version", "Minor version"],
    "1158": ["Patch Version", "Patch version"],
    "1159": ["Recognized Batteries", "Recognized batteries"],
    "1160": ["Activated Batteries", "Activated batteries"],
    "1161": ["Faulty Batteries", "Faulty batteries"],
    "1162": ["Battery 1 Voltage", "Battery 1 voltage"],
    "1163": ["Battery 1 Current", "Battery 1 current"],
    "1164": ["Battery 1 State", "Battery 1 State"],
    "1165": ["Battery 1 SoC", "Battery 1 SoC"],
    "1166": ["Battery 1 Temperature 1", "Battery 1 temperature 1"],
    "1167": ["Battery 1 Temperature 2", "Battery 1 temperature 2"],
    "1168": ["Battery 1 Power Stage Temp", "Battery 1 power stage temp"],
    "1169": ["Battery 1 Remaining Capacity", "Battery 1 remaining capacity"],
    "1170": ["Battery 2 Voltage", "Battery 2 voltage"],
    "1171": ["Battery 2 Current", "Battery 2 current"],
    "1172": ["Battery 2 State", "Battery 2 state"],
    "1173": ["Battery 2 SoC", "Battery 2 SoC"],
    "1174": ["Battery 2 Temperature 1", "Battery 2 temperature 1"],
    "1175": ["Battery 2 Temperature 2", "Battery 2 temperature 2"],
    "1176": ["Battery 2 Power Stage Temp", "Battery 2 power stage temp"],
    "1177": ["Battery 2 Remaining Capacity", "Battery 2 remaining capacity"],
    "1178": ["Battery ID 0 Error Code", "Battery ID 0 error code"],
    "1179": ["Battery ID 1 Error Code", "Battery ID 1 error code"],
    "1180": ["Cluster Error Code", "Cluster error code"],
    "1181": ["Max Charge Current", "Max charge current"],
    "1182": ["Lowest Battery 2 Temperature", "Lowest battery 2 voltage"],
    "1183": ["Highest Battery 2 Temperature", "Highest battery 2 temperature"],
    "1184": ["Lowest Battery 2 Voltage	", "Lowest battery 2 voltage"],
    "1185": ["Highest Battery 2 Voltage	", "Highest battery 2 voltage"],
    "855": ["Power", "0 - Power Off, 1 - Power ON"],
    "856": ["Current Trip Range", "Current trip Range IO element indicates currently measured current range"],
    "857": ["Total Trip Range", "Total trip Range IO element indicates currently measured total range"],
    "858": ["Battery Capacity", "Battery capacity I/O element shows battery capacity left."],
    "859": ["Low Voltage", "Low Voltage status"],
    "860": ["High Temperature", "High Temperature status"],
    "861": ["Upload Time", "Upload time status"],
    "862": ["Moving Abnormal", "Moving abnormal status"],
    "863": ["Range", "Range indicator"],
    "864": ["Lock Status", "Lock status"],
    "865": ["Vehicle FW version", "Vehicle FW version"],
    "866": ["Total Range", "Total range indicator"],
    "867": ["Battery Energy", "Battery Energy indicator"],
    "868": ["Power System Error", None],
    "869": ["Power Train Error", None],
    "870": ["Instrument System Error", None],
    "25": ["BLE Temperature #1", "Degrees ( °C ), -40 - +125;"],
    "26": ["BLE Temperature #2", "Degrees ( °C ), -40 - +125;"],
    "27": ["BLE Temperature #3", "Degrees ( °C ), -40 - +125;"],
    "28": ["BLE Temperature #4", "Degrees ( °C ), -40 - +125;"],
    "29": ["BLE Battery #1", "Battery level of sensor #1"],
    "20": ["BLE Battery #2", "Battery level of sensor #2"],
    "22": ["BLE Battery #3", "Battery level of sensor #3"],
    "23": ["BLE Battery #4", "Battery level of sensor #4"],
    "86": ["BLE Humidity #1", "Humidity"],
    "104": ["BLE Humidity #2", "Humidity"],
    "106": ["BLE Humidity #3", "Humidity"],
    "108": ["BLE Humidity #4", "Humidity"],
    "331": ["BLE 1 Custom #1", "Custom IO element for BLE sensor"],
    "463": ["BLE 1 Custom #2", "Custom IO element for BLE sensor"],
    "464": ["BLE 1 Custom #3", "Custom IO element for BLE sensor"],
    "465": ["BLE 1 Custom #4", "Custom IO element for BLE sensor"],
    "466": ["BLE 1 Custom #5", "Custom IO element for BLE sensor"],
    "332": ["BLE 2 Custom #1", "Custom IO element for BLE sensor"],
    "467": ["BLE 2 Custom #2", "Custom IO element for BLE sensor"],
    "468": ["BLE 2 Custom #3", "Custom IO element for BLE sensor"],
    "469": ["BLE 2 Custom #4", "Custom IO element for BLE sensor"],
    "470": ["BLE 2 Custom #5", "Custom IO element for BLE sensor"],
    "333": ["BLE 3 Custom #1", "Custom IO element for BLE sensor"],
    "471": ["BLE 3 Custom #2", "Custom IO element for BLE sensor"],
    "472": ["BLE 3 Custom #3", "Custom IO element for BLE sensor"],
    "473": ["BLE 3 Custom #4", "Custom IO element for BLE sensor"],
    "474": ["BLE 3 Custom #5", "Custom IO element for BLE sensor"],
    "334": ["BLE 4 Custom #1", "Custom IO element for BLE sensor"],
    "475": ["BLE 4 Custom #2", "Custom IO element for BLE sensor"],
    "476": ["BLE 4 Custom #3", "Custom IO element for BLE sensor"],
    "477": ["BLE 4 Custom #4", "Custom IO element for BLE sensor"],
    "478": ["BLE 4 Custom #5", "Custom IO element for BLE sensor"],
    "385": ["Beacon ID's", "Data structure: Data part: 1 Byte, Beacon flag: 1 Byte, Beacon ID (iBeacon/Eddystone): 20 "
                           "Bytes/16 Bytes, Signal strength: 1 Byte"],
    "874": ["Bluetooth Home Zone Violation state", "Bits describe the causes of violations: 0 - None, 1 - Movement ("
                                                   "Only for Ela MOV sensor), 2 - RSSI threshold violation, "
                                                   "4 - BLE missing"],
    "889": ["Proximity Violation state", "Bits describe the causes of violations: 1 - RSSI threshold violation, "
                                         "0 - End of RSSI violation"],
    "875": ["Proximity violation source with Teltonika devices", "MAC address which violates personal space, Example "
                                                                 "of encoded HEX ASCII text: HEX: 44 35 41 34 31 42 "
                                                                 "38 42 31 30 37 35, HEX ASCII to text: D5A41B8B1075, "
                                                                 "(NOTE! From firmware version Rev.329 device sends "
                                                                 "IMEI instead of MAC address), Example:, "
                                                                 "HEX -> ASCII (String), 3031343731353942383241454643 "
                                                                 "-> 0147159B82AEFC, HEX -> DEC, 0147159B82AEFC -> "
                                                                 "359633105628924"],
    "876": ["Proximity violation source with iBeacons", "Example of UUID encoded HEX to ASCII format: HEX: 41 41 41 "
                                                        "41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 42 42 43 43 35 "
                                                        "32 36 46 36 46 36 44 33 31, HEX to ASCII format: "
                                                        "AAAAAAAAAAAAAAAAAABBCC526F6F6D31"],
    "890": ["Proximity duration", "Violation time in seconds. Included as an IO element with AVL ID 875"],
    "891": ["BLE MAC address", "BLE MAC address of device. Example of encoded HEX ASCII text: HEX: 44 35 41 34 31 42 "
                               "38 42 31 30 37 35, HEX ASCII to text: D5A41B8B1075"],
    "263": ["BT Status", "0 - BT is disabled, 1 - BT Enabled, not device connected, 2 - Device connected, BTv3 Only, "
                         "3 - Device connected, BLE only, 4 - Device connected, BLE + BT"],
    "871": ["BLE Lock Status", "0 – Unlocked, 1 – Locked On"],
    "872": ["BLE Lock Battery", "Battery level of Bluetooth lock"],
    "873": ["BLE Lock Discovered", "1 - Bluetooth lock Discovered"]
}


class AVL:
    def __init__(self):
        self.avl_data_list = []
        self.counter = None
        self.crc_16 = None
        self.n_of_data2 = None
        self.n_of_data1 = None
        self.codec_id = None
        self.data_field_length = None
        self.zero_bytes = None
        self.encoded_imei = ""
        self.imei = ""
        self.imei_length = None

    def parse_imei(self, data):
        self.encoded_imei = str(data)
        self.imei_length = data[0:4]
        temp = ""
        for i in range(len(data)):
            if i % 2 == 1:
                temp += data[i]
        self.imei = temp[2:]
        print(self.imei)

    def parse_data(self, data):
        self.avl_data_list.clear()
        self.zero_bytes = data[0:8]
        self.data_field_length = data[8:16]
        self.codec_id = data[16:18]
        self.n_of_data1 = data[18:20]
        self.counter = 20
        for n in range(hex_to_dec(self.n_of_data1)):
            self.avl_data_list.append(AVLData())
            self.avl_data_list[n].timestamp = data[self.counter:self.counter+16]
            self.avl_data_list[n].priority = data[self.counter+16:self.counter+18]
            self.avl_data_list[n].longitude = data[self.counter+18:self.counter+26]
            self.avl_data_list[n].latitude = data[self.counter+26:self.counter+34]
            self.avl_data_list[n].altitude = data[self.counter+34:self.counter+38]
            self.avl_data_list[n].angle = data[self.counter+38:self.counter+42]
            self.avl_data_list[n].satellites = data[self.counter+42:self.counter+44]
            self.avl_data_list[n].speed = data[self.counter+44:self.counter+48]
            self.avl_data_list[n].event_io_id = data[self.counter+48:self.counter+50]
            self.avl_data_list[n].n_of_total_id = data[self.counter+50:self.counter+52]
            self.counter += 52
            self.avl_data_list[n].n1_of_one_byte_io = data[self.counter:self.counter+2]
            self.counter += 2
            for i in range(hex_to_dec(self.avl_data_list[n].n1_of_one_byte_io)):
                io_id = hex_to_dec(data[self.counter:self.counter + 2])
                io_value = hex_to_dec(data[self.counter + 2:self.counter + 4])
                x = {
                    "property_name": IO_ELEMENTS[f"{io_id}"][0],
                    "description": IO_ELEMENTS[f"{io_id}"][1],
                    "value": io_value
                }
                self.avl_data_list[n].one_byte_io_list[f'{io_id}'] = x
                self.counter += 4
            self.avl_data_list[n].n2_of_two_bytes_io = data[self.counter:self.counter + 2]
            self.counter += 2
            for i in range(hex_to_dec(self.avl_data_list[n].n2_of_two_bytes_io)):
                io_id = hex_to_dec(data[self.counter:self.counter + 2])
                io_value = hex_to_dec(data[self.counter + 2:self.counter + 6])
                x = {
                    "property_name": IO_ELEMENTS[f"{io_id}"][0],
                    "description": IO_ELEMENTS[f"{io_id}"][1],
                    "value": io_value
                }
                self.avl_data_list[n].two_byte_io_list[f'{io_id}'] = x
                self.counter += 6
            self.avl_data_list[n].n4_of_four_bytes_io = data[self.counter:self.counter + 2]
            self.counter += 2
            for i in range(hex_to_dec(self.avl_data_list[n].n4_of_four_bytes_io)):
                io_id = hex_to_dec(data[self.counter:self.counter + 2])
                io_value = hex_to_dec(data[self.counter + 2:self.counter + 10])
                x = {
                    "property_name": IO_ELEMENTS[f"{io_id}"][0],
                    "description": IO_ELEMENTS[f"{io_id}"][1],
                    "value": io_value
                }
                self.avl_data_list[n].four_byte_io_list[f'{io_id}'] = x
                self.counter += 10
            self.avl_data_list[n].n8_of_eight_bytes_io = data[self.counter:self.counter + 2]
            self.counter += 2
            for i in range(hex_to_dec(self.avl_data_list[n].n8_of_eight_bytes_io)):
                io_id = hex_to_dec(data[self.counter:self.counter + 2])
                io_value = hex_to_dec(data[self.counter + 2:self.counter + 18])
                x = {
                    "property_name": IO_ELEMENTS[f"{io_id}"][0],
                    "description": IO_ELEMENTS[f"{io_id}"][1],
                    "value": io_value
                }
                self.avl_data_list[n].eight_byte_io_list[f'{io_id}'] = x
                self.counter += 18
        self.n_of_data2 = data[self.counter:self.counter + 2]
        self.crc_16 = data[self.counter + 2:self.counter + 10]

    def make_dict(self):
        x = {
            "encoded_imei": self.encoded_imei,
            "imei": self.imei,
            "zero_bytes": self.zero_bytes,
            "data_field_length": self.data_field_length,
            "codec_id": self.codec_id,
            "n_of_data1": self.n_of_data1
        }
        for i in range(len(self.avl_data_list)):
            x[f"data_packet{i+1}"] = self.avl_data_list[i].as_dict()
        x["n_of_data2"] = self.n_of_data2
        x["crc_16"] = self.crc_16

        return x

    def print_avl(self):
        print(f"Zero bytes: {self.zero_bytes}")
        print(f"Data field length: {self.data_field_length}")
        print(f"Codec ID: {self.codec_id}")
        print(f"Number of Data1: {self.n_of_data1}")
        for i in range(len(self.avl_data_list)):
            print(f"====Data Packet: {i+1}====")
            print(f"Timestamp: {self.avl_data_list[i].timestamp}")
            print(f"Priority: {self.avl_data_list[i].priority}")
            print(f"Longitude: {self.avl_data_list[i].longitude}")
            print(f"Latitude: {self.avl_data_list[i].latitude}")
            print(f"Altitude: {self.avl_data_list[i].altitude}")
            print(f"Angle: {self.avl_data_list[i].angle}")
            print(f"Satellites: {self.avl_data_list[i].satellites}")
            print(f"Speed: {self.avl_data_list[i].speed}")
            print(f"Event IO ID: {self.avl_data_list[i].event_io_id}")
            print(f"Number of Total ID: {self.avl_data_list[i].event_io_id}")
            print(f"Number1 of One Byte IO: {self.avl_data_list[i].n1_of_one_byte_io}")
            if self.avl_data_list[i].one_byte_io_list:
                print(self.avl_data_list[i].one_byte_io_list)
            print(f"Number2 of One Byte IO: {self.avl_data_list[i].n2_of_two_bytes_io}")
            if self.avl_data_list[i].two_byte_io_list:
                print(self.avl_data_list[i].two_byte_io_list)
            print(f"Number4 of One Byte IO: {self.avl_data_list[i].n4_of_four_bytes_io}")
            if self.avl_data_list[i].four_byte_io_list:
                print(self.avl_data_list[i].four_byte_io_list)
            print(f"Number8 of One Byte IO: {self.avl_data_list[i].n8_of_eight_bytes_io}")
            if self.avl_data_list[i].eight_byte_io_list:
                print(self.avl_data_list[i].eight_byte_io_list)
        print(f"Number of Data2: {self.n_of_data2}")
        print(f"CRC-16: {self.crc_16}")


class AVLData:
    def __init__(self):
        self.n8_of_eight_bytes_io = None
        self.n4_of_four_bytes_io = None
        self.n2_of_two_bytes_io = None
        self.n1_of_one_byte_io = None
        self.n_of_total_id = None
        self.event_io_id = None
        self.speed = None
        self.satellites = None
        self.angle = None
        self.altitude = None
        self.latitude = None
        self.longitude = None
        self.priority = None
        self.timestamp = None
        self.one_byte_io_list = dict()
        self.two_byte_io_list = dict()
        self.four_byte_io_list = dict()
        self.eight_byte_io_list = dict()

    def as_dict(self):
        x = {
            "timestamp": self.timestamp,
            "priority": self.priority,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "altitude": self.altitude,
            "angle": self.angle,
            "satellites": self.satellites,
            "speed": self.speed,
            "event_io_id": self.event_io_id,
            "n_of_total_id": self.n_of_total_id,
            "n1_of_one_byte_io": self.n1_of_one_byte_io,
            "one_byte_io_list": self.one_byte_io_list,
            "n2_of_two_bytes_io": self.n2_of_two_bytes_io,
            "two_byte_io_list": self.two_byte_io_list,
            "n4_of_four_bytes_io": self.n4_of_four_bytes_io,
            "four_byte_io_list": self.four_byte_io_list,
            "n8_of_eight_bytes_io": self.n8_of_eight_bytes_io,
            "eight_byte_io_list": self.eight_byte_io_list
        }
        return x
