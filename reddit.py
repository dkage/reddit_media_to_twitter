import re
import praw
from api_keys import reddit_id, reddit_secret


class RedditHandler:
    def __init__(self, url):
        self.reddit = praw.Reddit(client_id=reddit_id,
                             client_secret=reddit_secret,
                             user_agent='reddit_media_to_twitter')
        self.reddit_link = url  # TODO validate link here

    def check_host(self):
        # TODO check if submission has media
        # TODO check if media is not 404
        # TODO check server
        pass

    def download_img(self):
        pass

    def download_video(self):
        pass

    def grab_id(self):

        submission_regex = re.search(r"comments/(.*?)/", self.reddit_link)
        if submission_regex:
            submission_id = submission_regex.group(1)
        else:
            submission_id = ''

        return submission_id

