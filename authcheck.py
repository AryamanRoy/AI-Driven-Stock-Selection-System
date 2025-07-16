import praw
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Reddit API credentials from environment variables
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")

# Create a Reddit instance
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# Check rate limit
def check_rate_limit():
    print("Rate Limit Information:")
    print(f"  - Remaining requests: {reddit.auth.limits['remaining']}")
    print(f"  - Reset time (in seconds): {reddit.auth.limits['reset']}")
    print(f"  - Total requests: {reddit.auth.limits['total']}")

try:
    # Attempt to fetch the authenticated user's information
    user = reddit.user.me()
    if user:
        print("Authenticated as:", user.name)  # This should print your Reddit username # Check rate limit after successful authentication
    else:
        print("Authentication failed: User is None.")

except Exception as e:
    print(f"Failed to authenticate: {e}")

