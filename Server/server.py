"""
    Script creating HTTPS server
"""

import http.server
import socketserver

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

def launch_server():
    """
    Function launching the HTTPS server
    """
    print("Server started at localhost:" + str(PORT))
    with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
        httpd.serve_forever()

launch_server()
