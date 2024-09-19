from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import mimetypes

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            # Get the full file path
            file_path = self.path[1:]  # remove the leading "/"
            
            # Determine the MIME type of the file
            mime_type, _ = mimetypes.guess_type(file_path)
            
            # Open and read the requested file
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-Type', mime_type)
                self.end_headers()
                self.wfile.write(file.read())
        
        except Exception as e:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(server_class=HTTPServer, handler_class=myHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()