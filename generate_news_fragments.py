import os
import requests


# Constants
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "am2558"
REPO_NAME = "increment-version-number"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  
BRANCH_NAME = os.getenv('BRANCH_NAME')

# Function to get pull requests
def get_prs():
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls?state=open&head={REPO_OWNER}:{BRANCH_NAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    prs = response.json()
    return prs


def create_news_fragments(prs):
    for pr in prs:
        number = pr['number']
        title = pr['title']
        body = pr['body']
        fragment_type = determine_fragment_type(body)
        fragment_filename = f"newsfragments/{number}.{fragment_type}"
        
        with open(fragment_filename, 'w') as fragment_file:
            fragment_file.write(f"{title}\n\n{body}")


def determine_fragment_type(body):
    if "feature" in body.lower():
        return "feature"
    elif "bugfix" in body.lower():
        return "bugfix"
    else:
        return "misc"

# if __name__ == "__main__":
#     prs = get_prs()
#     create_news_fragments(prs)
