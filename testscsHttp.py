import requests
import pandas as pd
import json

csv_csi = pd.read_csv('1_CSI.dat', skiprows=4,
                      names=['TIMESTAMP', 'RECORD', 'Temp_Enc', 'Batt_Volt', 'RH_Enc'])

csv_fws = pd.read_csv('1_FWS.dat', skiprows=4,
                      names=['TIMESTAMP', 'RECORD', 'AirTemp', 'Humidity', 'Baro', 'Lat_deg', 'Lat_min', 'Long_deg',
                             'Long_min'])

csv_sonde = pd.read_csv('1_SONDE1.dat', skiprows=4,
                        names=['TIMESTAMP', 'RECORD', 'Temp_C', 'SpCond_mS', 'Sal', 'TDS_ppt', 'pH', 'ORP_mV',
                               'DO_percent', 'DO_ppm', 'Turb_NTU', 'Chl_ppb', 'PC_ppb'])

csi = pd.DataFrame(csv_csi)

csijson = csi.to_json(orient='records', force_ascii=False)

fws = pd.DataFrame(csv_fws)

sonde = pd.DataFrame(csv_sonde)

allconcat = pd.concat([csi,fws,sonde],axis=1)

csvcsifws = pd.merge(csi, fws)
csvall = pd.merge(csvcsifws,sonde)

sizelen = [len(fws), len(csi), len(sonde)]
sizelen.sort(reverse=True)

for index, row in csi.iterrows():
    print(index, row['TIMESTAMP'], row['RECORD'])

print("csi %s" % len(csi))
print("fws %s" % len(fws))
print("sonde %s" % len(sonde))

# for index, row in csi.iterrows():
#     print(index)
#     print(row)
