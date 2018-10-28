# ANNxious Telegram Bot

Get your neural network to talk to you over Telegram,
work in progress.

ANNxious is not like the other bots, one day he discovered
he could talk to Keras' Artificial Neural Networks and since
then it's the only thing he talks about. Add him on Telegram
at [ANNxiousBot](t.me/ANNxiousBot).

## How to use the bot
* Copy the custom [Keras' Callback](https://github.com/vlizanae/annxious-bot/blob/master/callback.py)
into your project.
* Talk to ANNxious to get your user id.
* Pass the callback to your model like this:
```python
log = model.fit(
    train_set_X,
    train_set_y,
    epochs=a_lot,
    callbacks=[
        ANNxiousRemoteMonitor(
            user_id=132562286,  # Some number provided by ANNxious
            network_id='MyNet', # Whatever you want to name this model
            url='http://im_not_hosting_yet.com'
        )
    ]
)
```
* That's it.

#### About your data

As data scientists we care about data. The only data coming
out of your machine are the metrics you can see in each epoch
line yielded by `model.fit`, which are completely meaningless
without context. ANNxious does not have any kind of access to
any part of your dataset.

## How to host the bot
ANNxious is written in Python 3 and uses PostgreSQL as its
backend to store the users, for the time being it is not
really necessary but it might be for some features I might
come up with. Other than setting up the database you need to
create a config module to store the credentials, install the
`requirements.txt` and you are good to go, you will need to
register the bot with Telegram's [BotFather](t.me/BotFather) to get your
own Telegram's API token.