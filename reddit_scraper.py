import praw
import json
import pandas as pd
import prawcore  # Import prawcore to handle specific exceptions

# Load the filtered CSV file containing psychiatric conditions
filtered_df = pd.read_csv('filtered_conditions.csv')

# Initialize the Reddit instance with credentials (replace with your own)
reddit = praw.Reddit(
    client_id="wGZwffGplDx3CfTr-ivI3Q",
    client_secret="JRZr87__rHWLcQFDtQlgE1btNZ9Rlw",
    user_agent="MedicationMentionsScraper 1.0 by /u/your_username"
)

# Define the list of psychiatric medications to search for
psychiatric_medications = filtered_df['drug_name'].tolist()

# Define a list of subreddits where users frequently discuss health topics
subreddits = ["AskReddit", "mentalhealth", "bipolar", "depression", "anxiety", "psychiatry", 'medication', 'antidepressants', 'askdocs']

# Function to search posts related to the medications
def search_for_posts():
    results = []

    for medication in psychiatric_medications:
        for subreddit in subreddits:
            print(f"Searching in {subreddit} for posts mentioning {medication}...")

            try:
                # Search for posts that mention the medication
                for submission in reddit.subreddit(subreddit).search(medication, limit=100):  # Adjust limit as needed
                    data = {
                        'title': submission.title,
                        'text': submission.selftext,
                        'medication': medication,
                        'subreddit': subreddit,
                        'upvotes': submission.score,
                        'author': str(submission.author)
                    }
                    results.append(data)
                    print(f"Found post: {submission.title}")

                # Search through comments in each subreddit
                for submission in reddit.subreddit(subreddit).search(medication, limit=5):  # Searching posts to find comments
                    submission.comments.replace_more(limit=0)
                    for comment in submission.comments.list():
                        data = {
                            'comment': comment.body,
                            'medication': medication,
                            'subreddit': subreddit,
                            'upvotes': comment.score,
                            'author': str(comment.author)
                        }
                        results.append(data)
                        print(f"Found comment: {comment.body[:50]}...")  # Print first 50 characters of the comment

            except prawcore.exceptions.NotFound:
                print(f"404 error encountered in {subreddit} for medication {medication}. Skipping.")
                continue
            except praw.exceptions.PRAWException as e:
                print(f"Error encountered in {subreddit} for medication {medication}: {e}")
                continue

    return results

# Call the function to search for posts and comments
medication_data = search_for_posts()

# Save the results to a JSON file
with open("medication_posts_data.json", "w") as f:
    json.dump(medication_data, f, indent=4)

print(f"Scraping complete. Found {len(medication_data)} posts/comments.")
