#!/usr/bin/env python3

import json
import requests


def next_url(request):
    for link_dict in requests.utils.parse_header_links(request.headers["Link"]):
        if link_dict.get("rel") == "next":
            return link_dict["url"]
    return ""


url = "https://api.github.com/repos/riceissa/project-ideas/issues?state=all"

r = requests.get(url)
j = json.loads(r.content)

while next_url(r):
    r = requests.get(next_url(r))
    j.extend(json.loads(r.content))

with open("issues.json", "w") as f:
    json.dump(j, f, indent=4)
