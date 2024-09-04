import http.server
import socketserver

with socketserver.TCPServer(('127.0.0.1', 8000),
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()


# スクリプトからブラウザを立ち上げる

# import webbrowser
# webbrowser.open('http://127.0.0.1:8000')

# f = webbrowser.get('firefox')
# f.open('http://127.0.0.1:8000')
