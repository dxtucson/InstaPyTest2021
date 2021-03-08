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
    session = InstaPy(username="", password="",
                      headless_browser=True)
    while True:
        with smart_run(session):
            session.set_quota_supervisor(enabled=True,
                                         sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                         sleepyhead=True, stochastic_flow=True, notify_me=True,
                                         peak_likes_hourly=57,
                                         peak_likes_daily=585,
                                         peak_comments_hourly=21,
                                         peak_comments_daily=182,
                                         peak_follows_hourly=48,
                                         peak_follows_daily=None,
                                         peak_unfollows_hourly=35,
                                         peak_unfollows_daily=402,
                                         peak_server_calls_hourly=None,
                                         peak_server_calls_daily=4700)
            session.set_skip_users(skip_private=False)
            session.set_do_story(enabled=True, percentage=10, simulate=True)
            session.set_user_interact(amount=10, randomize=True, percentage=10, media='Photo')
            session.follow_user_followers(['theyluvv.zo',
                                           'dar808dar', 'damndavea', 'coco_nail_hilo',
                                           'twoladieskitchen',
                                           'hideawayhilo',
                                           'killahkalai',
                                           'kitana.kaili',
                                           'rayrayganiron',
                                           'keokilxni',
                                           'livinghilostyle',
                                           'downtownhilohawaii', 'norishilo', 'rubmfaka808',
                                           'hilolunchshop',
                                           'tetsumenhawaii', 'marmaidz', 'kuiandiflorist', 'yourstrulymeri',
                                           'kiaannii'],
                                          amount=50, interact=False, randomize=False, sleep_delay=60)
            session.like_by_locations(['217860447',
                                       '1400401506921170',
                                       '109359892424006'],
                                      amount=100, skip_top_posts=False, randomize=True)
            session.like_by_tags(['waipiovalley', 'maunakea', 'bigislandhawaii'], amount=100, interact=False)
            session.set_do_like(enabled=True, percentage=85)
            session.dont_include(['dingteahilo', 'teapressobarbigisland'])
            session.dont_like(
                ['#photography', '#kahaluu', '#travel', '#kauai', '#kailuakona', '#maui', 'Maui', 'Mau\'i',
                 '#Kona', '#Molokai', '#oahu', 'O\'ahu', '#Honolulu',
                 'www.'])

            print_hi('All done. Sleep for 15 minutes...')
        time.sleep(15 * 60)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
