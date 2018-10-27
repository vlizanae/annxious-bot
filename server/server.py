from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from config import http_host_name, http_port
from lang import message


def get_server_handler(bot):
    class ServerHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super(ServerHandler, self).__init__(*args, **kwargs)
            self.bot = bot

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(content_length))

            if data['kind'] == 'train_begin':
                bot.send_message(
                    id=data['user_id'],
                    message=message['TRAIN_BEGIN'].format(
                        network_id=data['network_id']
                    )
                )
            elif data['kind'] == 'train_end':
                bot.send_message(
                    id=data['user_id'],
                    message=message['TRAIN_END'].format(
                        network_id=data['network_id']
                    )
                )

            self.send_response(200)
            self.end_headers()

    return ServerHandler


class Server:
    def __init__(self, tbot):
        self.server = HTTPServer(
            (http_host_name, http_port),
            get_server_handler(tbot)
        )
        self.tbot = tbot

    def run(self):
            self.server.serve_forever()
