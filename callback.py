from keras.callbacks import Callback
import requests, warnings, random


class ANNxiousRemoteMonitor(Callback):
    def __init__(self, user_id, network_id,
                 url='http://localhost:8000',
                 headers=None,
                 connection_warnings=True):
        super(ANNxiousRemoteMonitor, self).__init__()

        self.user_id = user_id
        self.network_id = '{}-{}'.format(network_id, random.randint(1000, 9999))
        self.url = url
        self.headers = headers
        self.connection_warnings = connection_warnings
        self.warning_text = 'Warning: Couldn\'t connect with ANNxious at {}'.format(self.url)

        if requests is None:
            raise ImportError('RemoteMonitors require the `requests` library.')

    def __base(self, logs=None, **kwargs):
        logs = logs or {}
        send = {
            'user_id': self.user_id,
            'network_id': self.network_id
        }

        for name, param in kwargs.items():
            send[name] = param

        for name, param in logs.items():
            if isinstance(param, (np.ndarray, np.generic)):
                send[name] = param.item()
            else:
                send[name] = param

        try:
            r = requests.post(self.url, json=send, headers=self.headers)
            if r.status_code == 404:
                warnings.warn('Warning: It seems like ANNxious haven\'t heard of you. '
                              'Talk to him at https://t.me/ANNxiousBot')
        except requests.exceptions.RequestException as e:
            if self.connection_warnings:
                warnings.warn(self.warning_text)

    def on_epoch_end(self, epoch, logs=None):
        self.__base(logs=logs, kind='epoch_end', epoch=epoch)

    def on_train_begin(self, logs=None):
        self.__base(logs=logs, kind='train_begin')

    def on_train_end(self, logs=None):
        self.__base(logs=logs, kind='train_end')