import random
import json
import requests
import tkinter as tk

url = "https://takumin287877.github.io/illust-odai/odai.json"
odaijson = requests.get(url)
odaijson = odaijson.json()
print(odaijson)

odai1 = random.randint(1,len(odaijson))
odai2 = random.randint(1,len(odaijson))
odai3 = random.randint(1,len(odaijson))

print(odai1)
print(odaijson["odai1"][odai1-1])
print(odaijson["odai2"][odai2-1])
print(odaijson["odai3"][odai3-1])

