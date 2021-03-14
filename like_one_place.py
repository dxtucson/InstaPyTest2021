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

    # like one single place
    session = InstaPy(username="", password="",
                      headless_browser=True)
    while True:
        with smart_run(session):
            session.set_quota_supervisor(enabled=True,
                                         sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                         sleepyhead=True, stochastic_flow=True, notify_me=True,
                                         peak_likes_hourly=44,
                                         peak_likes_daily=480,
                                         peak_comments_hourly=21,
                                         peak_comments_daily=182,
                                         peak_follows_hourly=30,
                                         peak_follows_daily=500,
                                         peak_unfollows_hourly=35,
                                         peak_unfollows_daily=402,
                                         peak_server_calls_hourly=None,
                                         peak_server_calls_daily=None)

            session.set_action_delays(enabled=True, like=10, randomize=True,
                                      random_range_from=100, random_range_to=600)
            session.like_by_locations([
                '109430532409629'  # Hilo, HI
            ], amount=300, skip_top_posts=True, randomize=True)

            print_hi('All done. Sleep for 1 hour ...')
        time.sleep(3600)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
