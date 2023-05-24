import requests
from datetime import datetime, timedelta

# GitHub repository information
repository_owner = "fluent"
repository_name = "fluent-bit"

# GitHub API endpoint for pull requests
api_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/pulls"

# Calculate the date range for the last week
today = datetime.now()
week_ago = today - timedelta(days=7)

# Query parameters for the GitHub API
params = {
    "state": "all",  # include all pull requests (open, closed, merged)
    "sort": "created",  # sort by creation date
    "direction": "desc",  # newest first
    "since": week_ago.isoformat()  # pull requests created since the last week
}

# Make a GET request to the GitHub API
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    pull_requests = response.json()
    opened_count = 0
    closed_count = 0
    merged_count = 0

    opened_pull_requests = []
    closed_pull_requests = []
    merged_pull_requests = []

    # Process each pull request
    for pr in pull_requests:
        pr_title = pr["title"]
        pr_state = pr["state"]

        if pr_state == "open":
            opened_count += 1
            opened_pull_requests.append(pr_title)
        elif pr_state == "closed":
            closed_count += 1
            closed_pull_requests.append(pr_title)
        elif pr_state == "merged":
            merged_count += 1
            merged_pull_requests.append(pr_title)

    print(opened_count, closed_count, merged_count)
    # exit(0)
    # Generate the email summary report
    from_email = "your_email@example.com"
    to_email = "manager@example.com"
    subject = "Pull Request Summary - Last Week"
    body = f"Hi Manager,\n\nHere is the summary of pull requests for the repository '{repository_name}':\n\n"
    body += f"Opened Pull Requests ({opened_count}):\n"
    
    for pr_title in opened_pull_requests:
        body += f"- {pr_title}\n"
    body += f"\nClosed Pull Requests ({closed_count}):\n"
    
    for pr_title in closed_pull_requests:
        body += f"- {pr_title}\n"
    body += f"\nMerged Pull Requests ({merged_count}):\n"
    
    for pr_title in merged_pull_requests:
        body += f"- {pr_title}\n"
    body += "\nPlease review the pull requests and take necessary actions.\n\n"
    body += "Best regards,\nYour Name"

    # Print the email details
    print(f"From: {from_email}")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")

else:
    print("Failed to retrieve pull requests. Please check the repository information and try again.")
