from flask import request, make_response
import mysql.connector
import re # Regular expressions also called Regex
from functools import wraps

##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password",
            database = "game_db"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)


##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view


##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
REGEX_USER_FIRST_NAME = f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()
    if not re.match(REGEX_USER_FIRST_NAME, user_first_name):
        raise Exception("company_exception user_first_name")
    return user_first_name


##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
REGEX_USER_LAST_NAME = f"^.{{{USER_LAST_NAME_MIN},{USER_LAST_NAME_MAX}}}$"
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name", "").strip()
    if not re.match(REGEX_USER_LAST_NAME, user_last_name):
        raise Exception("company_exception user_last_name")
    return user_last_name


##############################
REGEX_USER_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    user_email = request.form.get("user_email", "").strip()
    if not re.match(REGEX_USER_EMAIL, user_email): 
        raise Exception("company_exception user_email")
    return user_email


##############################
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception("company_exception user_password")
    return user_password

##############################

GAME_TITLE_MIN = 2
GAME_TITLE_MAX = 50
REGEX_GAME_TITLE = f"^.{{{GAME_TITLE_MIN},{GAME_TITLE_MAX}}}$"
def validate_game_title():
    game_title = request.form.get("game_title", "").strip()
    if not re.match(REGEX_GAME_TITLE, game_title):
        raise Exception("company_exception game_title")
    return game_title


##############################
GAME_PLATFORM_MIN = 2
GAME_PLATFORM_MAX = 50
REGEX_GAME_PLATFORM = f"^.{{{GAME_PLATFORM_MIN},{GAME_PLATFORM_MAX}}}$"
def validate_game_platform():
    game_platform = request.form.get("game_platform", "").strip()
    if not re.match(REGEX_GAME_PLATFORM, game_platform):
        raise Exception("company_exception game_platform")
    return game_platform

##############################

GAME_COMMENT_MIN = 2
GAME_COMMENT_MAX = 255
REGEX_GAME_COMMENT = f"^.{{{GAME_COMMENT_MIN},{GAME_COMMENT_MAX}}}$"
def validate_game_comment():
    game_comment = request.form.get("game_comment", "").strip()
    if not re.match(REGEX_GAME_COMMENT, game_comment):
        raise Exception("company_exception game_comment")
    return game_comment
##############################


REGEX_ID = "^[a-f0-9]{32}$"
def validate_id(id):
    id = id.strip()
    if not re.match(REGEX_ID, id):
        raise Exception("company_exception id")
    return id


# You know that the PK is a uuid4
# uuid4 follows certain patterns
#  TODO: replace game_pk and user_pk in the forms 

