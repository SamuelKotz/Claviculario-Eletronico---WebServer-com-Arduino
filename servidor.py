#Esta parte do código pode ser usada caso você não utilize uma extensão para o HTML
#Recomendo usar a extensão Live Server e abrir o HTML diretamente com ele.

import http.server
import socketserver
import os

# Defina o diretório onde o arquivo CSV está localizado
os.chdir('C:/Users/lajeado-lab/OneDrive/Documentos/PySerial testes')  # Mude para o diretório onde está o arquivo CSV


PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servindo na porta {PORT}")
    httpd.serve_forever()
