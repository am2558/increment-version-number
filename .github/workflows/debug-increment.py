import os
import re

issue_type = "FEATURE"
version_file = ".github/workflows/version.txt"
with open(version_file, "r") as file:
    version = file.read().strip()
match = re.match(r"(\d+)\.(\d+)\.(\d+)", version)
if match:
    major = match.group(1)
    minor = match.group(2)
    patch = match.group(3)
    print(major)
    print(minor)
    print(patch)
    print(version)
    if issue_type == "FEATURE":
        minor = int(minor) + 1
    elif issue_type == "BUGFIX":
        patch = int(patch) + 1
    new_version = f"{major}.{minor}.{patch}"
    with open(version_file, "w") as file:
        file.write(new_version)
else:
    raise ValueError("Version format not recognized " + version + ".")
