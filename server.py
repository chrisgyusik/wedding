import http.server
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('ngrok-skip-browser-warning', 'true')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # 로그 숨김

os.chdir('/Users/gyusik/wedding')
print("서버 시작: http://localhost:8080")
http.server.HTTPServer(('', 8080), Handler).serve_forever()
