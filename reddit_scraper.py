import praw
import re

def user_name_extraction(url):
    match = re.search(r'reddit\.com/user/([^/]+)/?', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid URL format. Please provide a valid Reddit user URL.")

def scrape_user_data(reddit, username):
    user = reddit.redditor(username)
    comments = []
    posts = []
    for comment in user.comments.new(limit=30):
        comments.append({
            "id": comment.id,
            "body": comment.body,
            "subreddit": comment.subreddit.display_name,
            "created_utc": comment.created_utc,
            "permalink": comment.permalink
        })
    for post in user.submissions.new(limit=15):
        posts.append({
            "id": post.id,
            "title": post.title,
            "selftext": post.selftext,
            "subreddit": post.subreddit.display_name,
            "created_utc": post.created_utc,
            "permalink": post.permalink
        })
    return {"comments": comments, "posts": posts}