
import requests
import json

def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
