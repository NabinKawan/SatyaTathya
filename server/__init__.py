from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

from app.models.enums.data_format_enum import DataFormatEnum
from app.services.impl.khwopa_service import KhwopaService
from app.settings import configs
from app.services import db_service
import json

blockchain_settings = configs.blockchain_settings
khwopa_service = KhwopaService()


class KhwopaBlockchainServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # checking for path params
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if self.path == '/status':
            response_data = {'message': f'{blockchain_settings.name} connected successfully!'}
            json_data = json.dumps(response_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())


        elif self.path == '/blocks':
            datas = db_service.get_all_datas(DataFormatEnum.JSON)
            response_data = {'blockchain_datas': datas}
            json_data = json.dumps(response_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif path.startswith('/blocks/'):
            block_hash = path.split('/')[2]
            data = db_service.get_data_by_identifier(block_hash, DataFormatEnum.JSON)
            if (data):
                response_data = data
                json_data = json.dumps(response_data)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode())
            else:
                self.send_error(404, 'Not Found')

        else:
            self.send_error(404, 'Not Found')

    def do_POST(self):
        if self.path == '/add_block':
            if self.headers['Content-Type'] != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid Content-Type, only application/json is supported')
                return

            # Get the length of the incoming data
            content_length = int(self.headers['Content-Length'])
            # Read the incoming data
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            block_hash = khwopa_service.add_block(json_data['tx'])
            response_data = {'tx_hash': block_hash}
            json_data = json.dumps(response_data)
            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == '/add_contract':
            if self.headers['Content-Type'] != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid Content-Type, only application/json is supported')
                return

            # Get the length of the incoming data
            content_length = int(self.headers['Content-Length'])
            # Read the incoming data
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            block_hash = khwopa_service.add_contract(json_data['tx']['byte_code'], json_data['tx']['contract_data'])
            new_response_data = {'contract_address': block_hash}
            new_json_data = json.dumps(new_response_data)
            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(new_json_data.encode())

        elif self.path == '/update_contract':
            if self.headers['Content-Type'] != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid Content-Type, only application/json is supported')
                return

            # Get the length of the incoming data
            content_length = int(self.headers['Content-Length'])
            # Read the incoming data
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            khwopa_service.update_contract(json_data['contract_address'], json_data['contract_data'])
            tx = {'inputs': json_data['inputs'], 'address': json_data['contract_address']}
            # adding contract tx to block
            block_hash = khwopa_service.add_block(tx)
            new_response_data = {'tx_hash': block_hash,
                                 'message': f'Successfully updated contract {json_data["contract_address"]}'}
            new_json_data = json.dumps(new_response_data)
            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(new_json_data.encode())


def run_server():
    server_address = (blockchain_settings.host, blockchain_settings.port)
    httpd = HTTPServer(server_address, KhwopaBlockchainServer)
    print(f"Listening on port {server_address[1]}")
    httpd.serve_forever()
