import requests

def analyze_github_profile(username):
    # Make a GET request to the GitHub API to fetch user information
    response = requests.get(f"https://api.github.com/users/{username}")
    
    if response.status_code == 200:
        user_data = response.json()
        
        # Extract relevant information from the response
        name = user_data["name"]
        bio = user_data["bio"]
        followers = user_data["followers"]
        following = user_data["following"]
        public_repos = user_data["public_repos"]
        
        # Print analyzed profile information
        print(f"Username: {username}")
        print(f"Name: {name}")
        print(f"Bio: {bio}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Public Repositories: {public_repos}")
    else:
        print("Error: Unable to fetch user information.")

# Provide the GitHub username for analysis
username = input("Enter a GitHub username: ")
analyze_github_profile(username)
