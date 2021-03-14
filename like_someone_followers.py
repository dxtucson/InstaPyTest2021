# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from instapy import InstaPy
from instapy import smart_run
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # like someone's followers. Very sparsely.

    session = InstaPy(username="", password="",
                      headless_browser=False)
    while True:
        with smart_run(session):
            
            session.set_quota_supervisor(enabled=True,
                                         sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                         sleepyhead=True, stochastic_flow=True, notify_me=True,
                                         peak_likes_hourly=43,
                                         peak_likes_daily=None,
                                         peak_comments_hourly=21,
                                         peak_comments_daily=182,
                                         peak_follows_hourly=10,
                                         peak_follows_daily=500,
                                         peak_unfollows_hourly=35,
                                         peak_unfollows_daily=402,
                                         peak_server_calls_hourly=None,
                                         peak_server_calls_daily=None)
            
            session.set_action_delays(enabled=True, like=60, randomize=True, random_range_from=55, random_range_to=550)
            session.set_do_follow(enabled=False, percentage=70)
            session.set_do_comment(enabled=False, percentage=80)
            session.set_do_like(enabled=True, percentage=70)
            session.interact_user_followers(['intl.velvet'], amount=200, randomize=True)
            print_hi('All done. Sleep for 10 days ...')
        time.sleep(864000)
