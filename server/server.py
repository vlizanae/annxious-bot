from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from config import http_host_name, http_port
from lang import message


def get_server_handler(bot):
    class ServerHandler(BaseHTTPRequestHandler):
        tbot = bot

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(content_length))

            user = self.tbot.db.get_user(data['user_id'])
            if user:
                if data['kind'] == 'train_begin':
                    self.tbot.send_message(
                        id=data['user_id'],
                        message=message['TRAIN_BEGIN'].format(
                            network_id=data['network_id'][:-5]
                        )
                    )
                    self.tbot.db.add_network(data['user_id'], data['network_id'])

                elif data['kind'] == 'train_end':
                    self.tbot.db.deactivate_network(data['network_id'])
                    network = self.tbot.db.get_network(data['network_id'])
                    self.tbot.send_message(
                        id=data['user_id'],
                        message=message[
                            'TRAIN_END_1' if network.val_loss is not None else 'TRAIN_END_0'
                        ].format(
                            network_id=data['network_id'][:-5],
                            time=network.train_ended.replace(microsecond=0)-network.created.replace(microsecond=0),
                            epoch=network.epoch+1,
                            train_loss=network.train_loss,
                            best_train_loss=network.best_train_loss,
                            best_train_epoch=network.best_train_epoch+1,
                            val_loss=network.val_loss,
                            best_val_loss=network.best_val_loss,
                            best_val_epoch=(network.best_val_epoch or -1) + 1
                        )
                    )

                elif data['kind'] == 'epoch_end':
                    self.tbot.db.update_network(**data)

                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()

    return ServerHandler


class Server:
    def __init__(self, tbot):
        self.server = HTTPServer(
            (http_host_name, http_port),
            get_server_handler(tbot)
        )

    def run(self):
            self.server.serve_forever()
