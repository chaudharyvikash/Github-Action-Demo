
import os
from datetime import datetime
import requests

# get current date & time
x = datetime.now()


# with name as day-month-year-hours-minutes-seconds
var = x.strftime('%d-%m-%Y-%H-%M-%S')
with open("output.json", 'w') as fp:
    fp.write(var)


# %%
owner = "chaudharyvikash"
repo = "Github-Action-Demo"
param = {"name":"output"}

headers = {

    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"

}

res = requests.get(

    f"https://api.github.com/repos/{owner}/{repo}/actions/artifacts", headers=headers, params=param)
artifacts = res.json()

print(artifacts)
