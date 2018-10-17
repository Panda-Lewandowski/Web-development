from http.server import BaseHTTPRequestHandler, HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<h1 align='center'>Welcome to sevice #2!</h1>")
            self.wfile.write(b"<p align='center'>Maybe you need this?</p>")
            self.wfile.write(b"<p align='center'><a href='./tmp'>Mimimi</a></p>")
        elif self.path == '/tmp':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<img src='https://sun1-8.userapi.com/c635107/v635107389/24ce/0zLgBHTVQf4.jpg' />")
        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'404 :(')

serv = HTTPServer(("127.0.0.1", 8004), HttpProcessor)
print("Server is running...")
serv.serve_forever()