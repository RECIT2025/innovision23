import socket
from http.server import HTTPServer,SimpleHTTPRequestHandler

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

server = HTTPServerV6(('::', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
