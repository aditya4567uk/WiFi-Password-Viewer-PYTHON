# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 20:15:18 2021

@author: adity
"""

import subprocess
import tableprint as tp
tp.banner("SAVED WIFI PASSWORD VIEWER")
tp.banner("BY ADITYA---KUMAR")

meta_data=subprocess.check_output(['netsh','wlan','show','profiles'])
data=meta_data.decode('utf-8',errors="backslashreplace")
data=data.split('\n')
profiles=[]
for i in data:
    if "All User Profile" in i:
        i=i.split(":")
        i=i[1]
        i=i[1:-1]
        profiles.append(i)
print("{:<30}|{:<}".format("Wi-Fi Name","Password"))
print("------------------------------------------")
for i in profiles:
    try:
        results=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear'])
        results=results.decode('utf-8',errors="backslashreplace")
        results=results.split('\n')
        results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|{:<}".format(i,results[0]))
        except IndexError:
            print("{:<30}|{:<}".format(i,""))
    except subprocess.CalledProcessError:
        print("Encoding Error")

a=input("\npress any key")