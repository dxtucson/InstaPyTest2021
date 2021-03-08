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

    # code was changed to be low-profile
    # follow is commented. only like
    session = InstaPy(username="", password="",
                      headless_browser=True)
    while True:
        with smart_run(session):
            session.set_quota_supervisor(enabled=True,
                                         sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                         sleepyhead=True, stochastic_flow=True, notify_me=True,
                                         peak_likes_hourly=30,
                                         peak_likes_daily=480,
                                         peak_comments_hourly=21,
                                         peak_comments_daily=182,
                                         peak_follows_hourly=30,
                                         peak_follows_daily=500,
                                         peak_unfollows_hourly=35,
                                         peak_unfollows_daily=402,
                                         peak_server_calls_hourly=150,
                                         peak_server_calls_daily=3000)
            # session.set_skip_users(skip_private=True)
            # session.set_do_story(enabled=True, percentage=5, simulate=True)
            # session.set_user_interact(amount=10, randomize=True, percentage=10, media='Photo')
            # session.follow_user_followers([
            #                                'twoladieskitchen',
            #                                'hideawayhilo',
            #                                'killahkalai',
            #                                'kitana.kaili',
            #                                'rayrayganiron',
            #                                'keokilxni',
            #                                'livinghilostyle',
            #                                'downtownhilohawaii', 'norishilo', 'rubmfaka808',
            #                                'hilolunchshop',
            #                                'tetsumenhawaii', 'marmaidz', 'kuiandiflorist', 'yourstrulymeri',
            #                                'kiaannii'],
            #                               amount=5, interact=False, randomize=False, sleep_delay=543)
            session.set_action_delays(enabled=True, like=10, randomize=True,
                                      random_range_from=50, random_range_to=300)
            session.like_by_locations([
                '4573910',  # Hawai`i Community College
                '214565960',  # Hawaiian Style Café - Hilo
                '652287',  # Cafe 100
                '1369906793116040',  # KTA Super Stores
                '286678182',  # Hilo High School
                '252552111906405',  # Waiakea High School
                '220719332',  # Suisan Fish Market
                '259904138',  # Waikoloa, Hawaii
                '248933518',  # Waimea Big Island
                '153047301946370',  # Downtown Hilo
                '353971',  # Big Island Candies
                '5123262',  # Waiolena
                '255285948',  # Keaau, Hawaii
                '528017',  # University of Hawaiʻi at Hilo
                '1014734662',  # Manono Street Marketplace
                '215140125',  # Liliuokalani Park and Gardens
                '7440188',  # Bayfront Beach Park
                '234437663',  # Mauna Kea
                '832944',  # Hilo Farmers Market
                '217860447',  # Hilo, HI
                '1400401506921170',  # Kamana Kitchen Indian Cuisine
                '109359892424006',  # Pepeekeo, Hawaii
                '213061859',  # Rainbow Falls
                '753431934796611',  # Hilo Volcanoes National Park and Rainbow Falls Excursion
                '1683284565326878'  # Boiling Pots, Wailuku River
            ], amount=3, skip_top_posts=True, randomize=True)
            # session.like_by_tags(['waipiovalley', 'maunakea', 'bigislandhawaii'], amount=5, interact=False)
            # session.set_do_like(enabled=True, percentage=60)
            # session.dont_include(['dingteahilo', 'teapressobarbigisland'])
            # session.dont_like(
            #     ['#photography', '#kahaluu', '#travel', '#kauai', '#kailuakona', '#maui', 'Maui', 'Mau\'i',
            #      '#Kona', '#Molokai', '#oahu', 'O\'ahu', '#Honolulu',
            #      'www.'])

            print_hi('All done. Sleep for 1 hour ...')
        time.sleep(3600)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
