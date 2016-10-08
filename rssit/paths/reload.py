# -*- coding: utf-8 -*-


import rssit.config


def process(server, path, normpath, options):
    rssit.config.load()

    server.send_response(200, "OK")
    server.end_headers()

    server.wfile.write(bytes("Configuration reloaded", "UTF-8"))


infos = [{
    "path": "reload",
    "process": process
}]
