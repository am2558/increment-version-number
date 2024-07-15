import os
import re

version_file = 'code/django/version.txt'
with open(version_file, 'r') as file:
    version = file.read().strip()

match = re.match(r'(\d+)\.(\d+)\.(\d+)(-.+)?', version)
if not match:
    raise ValueError('Invalid version format')

major, minor, patch, suffix = match.groups()
major = int(major)
minor = int(minor)
patch = int(patch)

bugfix_count = 0
feature_count = 0
for root, dirs, files in os.walk('newsfragments'):
    for file in files:
        if file.endswith('.bugfix'):
            bugfix_count += 1
        elif file.endswith('.feature'):
            feature_count += 1

if feature_count > 0:
    minor += 1
    patch = 0
elif bugfix_count > 0:
    patch += 1

new_version = f'{major}.{minor}.{patch}'
if suffix:
    new_version += suffix
    
with open(version_file, 'w') as file:
    file.write(new_version)

print(f'::set-output name=new_version::{new_version}')
os.environ['NEW_VERSION'] = new_version
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f'NEW_VERSION={new_version}\n')