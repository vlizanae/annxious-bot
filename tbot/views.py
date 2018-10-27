from lang import message
from config import callback_url, hosting_url


def start(bot, update, db):
    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user = db.get_user(user_id)

    if user is None:
        db.add_user(user_id, user_name)
        bot.send_message(
            chat_id=user_id,
            text=message['WELCOME'].format(
                user_name=user_name,
                callback_url=callback_url,
                hosting_url=hosting_url
            )
        )
    else:
        bot.send_message(
            chat_id=user_id,
            text=message['WELCOME_BACK'].format(user_name=user_name)
        )


def help(bot, update):
    bot.send_message(
        chat_id=update.message.chat.id,
        text=message['HELP'].format(
            callback_url=callback_url,
            hosting_url=hosting_url
        )
    )


def userid(bot, update, db):
    user_id = update.message.chat.id
    user = db.get_user(user_id)

    if user is None:
        bot.send_message(
            chat_id=user_id,
            text=message['USER_NOT_FOUND']
        )
    else:
        bot.send_message(
            chat_id=user_id,
            text=message['USER_ID'].format(user_id=user_id)
        )
