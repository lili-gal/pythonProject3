from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080
page_content = 'index_1.html'


class MyServer(BaseHTTPRequestHandler):
    '''Класс, который отвечает за обработку запросов'''
    def do_GET(self):
        '''Метод для обработки входящих запросов'''
        query_components = parse_qs(urlparse(self.path).query)
        page_address = urlparse(self.path).path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if page_address != '/' or urlparse(self.path).query !='':
            return self.wfile.write(('Contacts').encode())
        else:
            with open(page_content, "rb") as html_file:
                self.wfile.write((bytes(html_file.read())))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

