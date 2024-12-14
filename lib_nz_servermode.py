from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from lib_nz_model import load_full_model

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/model':
            # Устанавливаем статус ответа и заголовок Content-Type
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            # Данные для отправки в формате JSON
            data = load_full_model()
            # Преобразуем данные в JSON и отправляем их
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


def server_mode():
    print("Server mode! Ctrl + C to stop")
    run()