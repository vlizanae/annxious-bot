def start(bot, update, db):
    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user = db.get_user(user_id)

    if user is None:
        db.add_user(user_id, user_name)
        user = db.get_user(user_id)
        bot.send_message(
            chat_id=user_id,
            text='Welcome {}.'.format(user_name)
        )
    else:
        bot.send_message(
            chat_id=user_id,
            text='Welcome back, {}.'.format(user_name)
        )

registry = {
    'start': start
}
