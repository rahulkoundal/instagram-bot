# main file import all other files
from self_info import self_info
from get_user_info import get_user_info
from like_a_post import like_a_post
from get_user_post import get_user_post
from post_comment import post_comment
from get_own_post import get_own_post


# def function for start instabot

def init_bot():

    # this list cotain users options
    option_list = ['\t\t\t\t*************************Welcome to instabot*****************************',
                   'A.Get your own details', 'B..Get details of user by username', 'C..get your own recent post',
                   'D..get recent post of user by username ', 'E..Like most recent user post',
                   'F..make comment on user recent post ']

    # Take user choice
    select_option = raw_input("Enter your choice::")
    select_option=select_option.upper()
    if select_option == 'A':
        self_info()

    elif select_option == 'B':
        insta_username = raw_input("Enter username: ")
        get_user_info(insta_username)

    elif select_option == 'C':
        get_own_post()

    elif select_option == 'D':
        insta_username = raw_input("Enter username::")
        get_user_post(insta_username)

    elif select_option == 'E':
        insta_username = raw_input("Enter username::")
        like_a_post(insta_username)

    elif select_option == 'F':
        insta_username = raw_input("Enter username::")
        post_comment(insta_username)


# calling instagram bot function
init_bot()


