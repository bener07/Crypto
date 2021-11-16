import subprocess, re

stored_wifi = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()


profile_name = (re.findall("All User Profile     : (.*)\r", stored_wifi))

wifi_list = []

if len(profile_name) != 0:
    for name in profile_name:

        wifi_profiles = {}

        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name], capture_output=True).stdout.decode()

        if re.search("Security key           : Absent", profile_info):
            continue

        else:
            wifi_profiles["ssid"] = name

            uncensored_wifi_password = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'], capture_output=True).stdout.decode()


            password = re.search("Key Content            : (.*)\r", uncensored_wifi_password)

            if password == None:
                wifi_profiles["password"]= None

            else:
                wifi_profiles["password"] = password[1]
                
            wifi_list.append(wifi_profiles)

for x in range(len(wifi_list)):
    print(wifi_list[x])