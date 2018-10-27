from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from secret import http_host_name, http_port


def get_server_handler(bot):
    class ServerHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super(ServerHandler, self).__init__(*args, **kwargs)
            self.bot = bot

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            print(post_data)

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
