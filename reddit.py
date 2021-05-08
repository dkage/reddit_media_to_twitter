import re
import praw
from api_keys import reddit_id, reddit_secret


class RedditHandler:
    def __init__(self):
        self.reddit = praw.Reddit(client_id=reddit_id,
                             client_secret=reddit_secret,
                             user_agent='reddit_media_to_twitter')

    def check_host(self):
        pass

    def download_img(self):
        pass

    def download_video(self):
        pass

    def grab_id(self, reddit_link):
        # TODO add validation for reddit link to check if valid (is from reddit)
        submission_regex = re.search(r"comments/(.*?)/", reddit_link)
        if submission_regex:
            submission_id = submission_regex.group(1)
            submission = self.reddit.submission(id=submission_id)
            print(submission)

