import re
import praw
from prawcore import exceptions as praw_exceptions
from api_keys import reddit_id, reddit_secret


class RedditHandler:
    def __init__(self, url):
        self.reddit = praw.Reddit(client_id=reddit_id,
                                  client_secret=reddit_secret,
                                  user_agent='reddit_media_to_twitter')
        self.reddit_link = url
        self.submission_id = str()
        self.grab_id()
        self.submission = self.reddit.submission(self.submission_id)

        self.media_url = str()

    def download(self):
        self.check_link_valid()
        media_host = self.check_host()
        if media_host == 'not_mapped':
            return False
        media_type = self.check_type(media_host)

    def download_img(self, host):
        pass

    def download_video(self, host):
        # TODO check available res
        # TODO check size of possible downloads
        # TODO crop functions (?) maybe another class
        # TODO download file
        pass

    def check_type(self, host):
        if host == 'reddit_video':
            return 'Video'
        elif host == 'reddit_image':
            return 'Image'
        elif host == 'imgur':
            pass

    def grab_id(self):
        submission_regex = re.search(r"comments/(.*?)/", self.reddit_link)
        if submission_regex:
            self.submission_id = submission_regex.group(1)
        else:
            self.submission_id = ''

    def check_host(self):
        """
        Check which media hosting service is being used to given post URL.
        The common ones are imgur, reddit itself and Youtube (maybe add more later)

        :return: Host
        """

        try:
            self.media_url = str(self.submission.url)

        except praw_exceptions.NotFound:
            print("Post has no media attachment/URL. Download process finished.")
            return False

        url_no_prefix = self.media_url.removeprefix('https://').split('/')[0]
        if 'imgur' in url_no_prefix:
            host = 'imgur'
        elif 'v.redd.it' in url_no_prefix:
            host = 'reddit_video'
        elif 'i.redd.it' in url_no_prefix:
            host = 'reddit_image'
        else:
            host = 'not_mapped'
            print("Host not mapped. Cannot proceed with download. Host URL = {}".format(url_no_prefix))
            return host

        print('Host discovered. Media is using host {}'.format('host'))
        return host

    def check_link_valid(self):
        try:
            author = self.submission.author
            print('URL links to a valid post submitted by user {}.'.format(author))
            return True
        except praw_exceptions.NotFound:
            print('Received 404 HTTP response. Post deleted or wrong submission_ID/URL sent.')
            return False
