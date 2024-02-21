
import requests


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
