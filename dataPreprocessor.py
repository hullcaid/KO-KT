import pandas as pd

capture_34 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-34-1/bro/conn.log.labeled"
capture_43 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-43-1/bro/conn.log.labeled"
capture_44 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-44-1/bro/conn.log.labeled"
capture_49 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-49-1/bro/conn.log.labeled"
capture_52 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-52-1/bro/conn.log.labeled"
capture_20 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-20-1/bro/conn.log.labeled"
capture_21 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-21-1/bro/conn.log.labeled"
capture_42 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-42-1/bro/conn.log.labeled"
capture_60 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-60-1/bro/conn.log.labeled"
capture_17 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-17-1/bro/conn.log.labeled"
capture_36 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-36-1/bro/conn.log.labeled"
capture_33 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-33-1/bro/conn.log.labeled"
capture_8 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-8-1/bro/conn.log.labeled"
capture_35 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-35-1/bro/conn.log.labeled"
capture_48 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-48-1/bro/conn.log.labeled"
capture_39 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-39-1/bro/conn.log.labeled"
capture_7 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-7-1/bro/conn.log.labeled"
capture_9 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-9-1/bro/conn.log.labeled"
capture_3 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-3-1/bro/conn.log.labeled"
capture_1 = "./data/IoTScenarios/CTU-IoT-Malware-Capture-1-1/bro/conn.log.labeled"

column_template = ['ts',
              'uid',
              'id.orig_h',
              'id.orig_p',
              'id.resp_h',
              'id.resp_p',
              'proto',
              'service',
              'duration',
              'orig_bytes',
              'resp_bytes',
              'conn_state',
              'local_orig',
              'local_resp',
              'missed_bytes',
              'history',
              'orig_pkts',
              'orig_ip_bytes',
              'resp_pkts',
              'resp_ip_bytes',
              'label']

df34 = pd.read_table(filepath_or_buffer=capture_34, skiprows=8, nrows=100000)
df34.columns= column_template
df34.drop(df34.tail(1).index,inplace=True)

df43 = pd.read_table(filepath_or_buffer=capture_43, skiprows=8, nrows=100000)
df43.columns= column_template
df43.drop(df43.tail(1).index,inplace=True)

df44 = pd.read_table(filepath_or_buffer=capture_44, skiprows=8, nrows=100000)
df44.columns= column_template
df44.drop(df44.tail(1).index,inplace=True)

df49 = pd.read_table(filepath_or_buffer=capture_49, skiprows=8, nrows=100000)
df49.columns= column_template
df49.drop(df49.tail(1).index,inplace=True)

df52 = pd.read_table(filepath_or_buffer=capture_52, skiprows=8, nrows=100000)
df52.columns= column_template
df52.drop(df52.tail(1).index,inplace=True)

df20 = pd.read_table(filepath_or_buffer=capture_20, skiprows=8, nrows=100000)
df20.columns= column_template
df20.drop(df20.tail(1).index,inplace=True)

df21 = pd.read_table(filepath_or_buffer=capture_21, skiprows=8, nrows=100000)
df21.columns= column_template
df21.drop(df21.tail(1).index,inplace=True)

df42 = pd.read_table(filepath_or_buffer=capture_42, skiprows=8, nrows=100000)
df42.columns= column_template
df42.drop(df42.tail(1).index,inplace=True)

df60 = pd.read_table(filepath_or_buffer=capture_60, skiprows=8, nrows=100000)
df60.columns= column_template
df60.drop(df60.tail(1).index,inplace=True)

df17 = pd.read_table(filepath_or_buffer=capture_17, skiprows=8, nrows=100000)
df17.columns= column_template
df17.drop(df17.tail(1).index,inplace=True)

df36 = pd.read_table(filepath_or_buffer=capture_36, skiprows=8, nrows=100000)
df36.columns= column_template
df36.drop(df36.tail(1).index,inplace=True)

df33 = pd.read_table(filepath_or_buffer=capture_33, skiprows=8, nrows=100000)
df33.columns= column_template
df33.drop(df33.tail(1).index,inplace=True)

df8 = pd.read_table(filepath_or_buffer=capture_8, skiprows=8, nrows=100000)
df8.columns= column_template
df8.drop(df8.tail(1).index,inplace=True)

df35 = pd.read_table(filepath_or_buffer=capture_35, skiprows=8, nrows=100000)
df35.columns= column_template
df35.drop(df35.tail(1).index,inplace=True)

df48 = pd.read_table(filepath_or_buffer=capture_48, skiprows=8, nrows=100000)
df48.columns= column_template
df48.drop(df48.tail(1).index,inplace=True)

df39 = pd.read_table(filepath_or_buffer=capture_39, skiprows=8, nrows=100000)
df39.columns= column_template
df39.drop(df39.tail(1).index,inplace=True)

df7 = pd.read_table(filepath_or_buffer=capture_7, skiprows=8, nrows=100000)
df7.columns= column_template
df7.drop(df7.tail(1).index,inplace=True)

df9 = pd.read_table(filepath_or_buffer=capture_9, skiprows=8, nrows=100000)
df9.columns= column_template
df9.drop(df9.tail(1).index,inplace=True)

df3 = pd.read_table(filepath_or_buffer=capture_3, skiprows=8, nrows=100000)
df3.columns= column_template
df3.drop(df3.tail(1).index,inplace=True)

df1 = pd.read_table(filepath_or_buffer=capture_1, skiprows=8, nrows=100000)
df1.columns= column_template
df1.drop(df1.tail(1).index,inplace=True)

