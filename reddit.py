import re
import praw
from api_keys import reddit_id, reddit_secret


class RedditHandler:
    def __init__(self, url):
        self.reddit = praw.Reddit(client_id=reddit_id,
                                  client_secret=reddit_secret,
                                  user_agent='reddit_media_to_twitter')
        self.reddit_link = url  # TODO validate link here
        self.submission_id = str()

    def download_img(self, host):
        pass

    def download_video(self, host):
        # TODO check available res
        # TODO check size of possible downloads
        # TODO crop functions (?) maybe another class
        # TODO download file
        pass

    def grab_id(self):
        submission_regex = re.search(r"comments/(.*?)/", self.reddit_link)
        if submission_regex:
            self.submission_id = submission_regex.group(1)
        else:
            self.submission_id = ''

    @staticmethod
    def check_host(submission_object):
        # TODO check if submission has media
        # TODO check if media is not 404
        # TODO check server
        pass
