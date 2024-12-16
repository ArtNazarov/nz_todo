from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from lib_nz_config_attributes import attributes_of_project, attributes_of_task
from lib_nz_model import load_full_model, extract_table_projects_from_model, extract_table_tasks_from_model


class RequestHandler(BaseHTTPRequestHandler):
    def wrap_do_get(self, real_path, load_func):
        # Устанавливаем статус ответа и заголовок Content-Type
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        # Данные для отправки в формате JSON
        data = load_func() # вызов!
        # Преобразуем данные в JSON и отправляем их
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def do_GET(self):

        def load_404_responce():
            return {'error': 'method not allowed'}

        def load_only_projects():
            model = load_full_model()
            return extract_table_projects_from_model(model, attributes_of_project())

        def load_only_tasks():
            print('Called load only tasks!')
            model = load_full_model()
            # Разбираем URL и получаем параметры запроса
            parsed_path = urlparse(self.path)
            query_params = parse_qs(parsed_path.query)
            # Получаем значение параметра 'someParam'
            project_id = query_params.get('project_id', [None])[0]
            print(project_id)
            return extract_table_tasks_from_model(model, project_id, attributes_of_task())

        actions = {
            '/model': load_full_model,
            '/projects': load_only_projects,
            '/tasks': load_only_tasks,
            '/404': load_404_responce
        }

        # Разбираем URL
        parsed_url = urlparse(self.path)
        # Получаем путь без параметров!
        real_path = parsed_url.path
        print(real_path)
        
        if real_path not in actions.keys():
            real_path = '/404'
        
        self.wrap_do_get(real_path, actions.get(real_path, '/404'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address=('', port)
    httpd=server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


def server_mode():
    print("Server mode! Ctrl + C to stop")
    run()
