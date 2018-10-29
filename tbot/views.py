from datetime import datetime

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
                hosting_url=hosting_url,
                user_id=user_id
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


def status(bot, update, db):
    user_id = update.message.chat.id
    for network in db.get_user_networks(user_id):
        bot.send_message(
            chat_id=user_id,
            text=message[
                'STATUS_1' if network.val_loss is not None else 'STATUS_0'
            ].format(
                network_id=network.name[:-5],
                time=datetime.now().replace(microsecond=0)-network.created.replace(microsecond=0),
                epoch=network.epoch + 1,
                train_loss=network.train_loss,
                best_train_loss=network.best_train_loss,
                best_train_epoch=network.best_train_epoch+1,
                val_loss=network.val_loss,
                best_val_loss=network.best_val_loss,
                best_val_epoch=(network.best_val_epoch or -1)+1
            )
        )