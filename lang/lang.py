message = {
    'WELCOME': 'Welcome {user_name}, I\'m ANNxious to give you some results! '
               'Don\'t forget to copy my custom Keras\' callback template from '
               '{callback_url}, point its url to {hosting_url}, pass it to your '
               'model and I\'ll keep in touch.\n'
               '\n'
               'Also you user id is {user_id}, you\'ll need it to use the callback.',

    'WELCOME_BACK': 'Welcome back {user_name}, if you don\'t already know what to '
                    'do, type /help to get us started.',

    'USER_NOT_FOUND': 'I\'m sorry but I don\'t think we\'ve met, try typing /start.',

    'USER_ID': 'Your user id is {user_id}.',

    'TRAIN_BEGIN': 'I heard {network_id} started training.',

    'TRAIN_END_0': '{network_id} just told me its training is done, '
                   'after {time!s} and {epoch} epochs.\n'
                   'Final train loss: {train_loss:.5f}\n'
                   'Best train loss: {best_train_loss:.5f} at epoch {best_train_epoch}',

    'TRAIN_END_1': '{network_id} just told me its training is done, '
                   'after {time!s} and {epoch} epochs.\n'
                   'Final train loss: {train_loss:.5f}\n'
                   'Best train loss: {best_train_loss:.5f} at epoch {best_train_epoch}\n'
                   'Final val loss: {val_loss:.5f}\n'
                   'Best val loss: {best_val_loss:.5f} at epoch {best_val_epoch}',

    'NETS_NOT_FOUND': 'I haven\'t heard of any of your networks recently.',

    'STATUS_0': 'Status for {network_id}: {epoch} epochs elapsed in {time!s}.\n'
                'Train loss: {train_loss:.5f}\n'
                'Best train loss: {best_train_loss:.5f} at epoch {best_train_epoch}',

    'STATUS_1': 'Status for {network_id}: {epoch} epochs elapsed in {time!s}.\n'
                'Train loss: {train_loss:.5f}\n'
                'Best train loss: {best_train_loss:.5f} at epoch {best_train_epoch}\n'
                'Validation loss: {val_loss:.5f}\n'
                'Best val loss: {best_val_loss:.5f} at epoch {best_val_epoch}',
    
    'HELP': 'Artificial Neural Networks can take a lot of time to train, have '
            'you ever forgotten you were training networks because of that? well that\'s '
            'no longer an excuse as I\'ll get them to talk to you.\n'
            '\n'
            'How can you do that, you ask?\n'
            ' - First copy my custom Keras\' callback from {callback_url} into your project.\n'
            ' - Don\'t forget to point it towards {hosting_url}.\n'
            ' - Put the callback in your model\'s callbacks list when calling the "fit" method.\n'
            ' - You have to pass the callback your user id and a keyword to identify the model.\n'
            ' - I\'ll let you know about your model.\n'
            '\n'
            'Commands: type\n'
            ' - /start if for some reason I can\'t remember you.\n'
            ' - /help to see this message (again?).\n'
            ' - /userid in case you lost you user id.\n'
            ' - /status to check your training networks.\n'
            '\n'
            'I don\'t have any kind of access to any part of your dataset and '
            'will never have. Also I\'m open source, feel free to submit any bug '
            'report or feature request as an issue at my repo.'
}