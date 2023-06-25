from instapy import InstaPy
from instapy import smart_run
# from instapy import set_workspace

# set workspace folder at desired location (default is at your home folder)
# set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="dabuttadawg_dadawgwitdabutta", password="master_jules97")

with smart_run(session):
    # general settings

    # activity
    session.like_by_tags(["computer science"], amount=9, top_posts_only=True)
