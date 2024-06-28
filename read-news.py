import os
import re

def read_news_file(news_file):
    with open(news_file, 'r') as file:
        content = file.read()
    return content

def count_keywords(content, keyword):
    return content.lower().count(keyword.lower())

def get_current_version(version_file):
    with open(version_file, 'r') as file:
        version = file.readline().strip()
    match = re.match(r'(\d+)\.(\d+)\.(\d+)(-.+)?', version)
    if not match:
        raise ValueError(f"Invalid version format: {version}")
    return match.groups()

def write_new_version(version_file, new_version):
    with open(version_file, 'w') as file:
        file.write(new_version)

def main():
    version_file = 'code/django/version.txt'
    news_file = 'NEWS.rst'
    
    content = read_news_file(news_file)
    bugfix_count = count_keywords(content, 'bugfix')
    feature_count = count_keywords(content, 'feature')

    major, minor, patch, suffix = get_current_version(version_file)

    if bugfix_count >= 4:
        patch = int(patch) + 1
    if feature_count >= 4:
        minor = int(minor) + 1

    new_version = f'{major}.{minor}.{patch}'
    if suffix:
        new_version += suffix
    
    write_new_version(version_file, new_version)
    print(f'::set-output name=new_version::{new_version}')
    os.environ['NEW_VERSION'] = new_version
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write(f'NEW_VERSION={new_version}\n')

# if __name__ == "__main__":
#     main()
