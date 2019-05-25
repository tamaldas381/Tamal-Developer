import SimpleHTTPServer
import socketserver

port = 8000

Handeler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("",port),  Handeler)

print "serving at port", port
httpd.serve_forever()