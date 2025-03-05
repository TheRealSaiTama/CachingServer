import argparse
import http.server
import socketserver
import requests
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

responsecache = {}

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, upstream=None, **kwargs):
        self.upstream = upstream
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parseurl = urlparse(self.path)
        cachekey = parseurl.path

        if cachekey in responsecache:
            logging.info(f'Cache hit for {cachekey}')
            self.send_response(200)
            self.send_header('X-Cache', 'HIT')
            self.end_headers()
            self.wfile.write(responsecache[cachekey])
        else:
            upstreamurl = f"{self.upstream}{self.path}"
            logging.info(f'Cache miss for {cachekey}, fetching from {upstreamurl}')
            response = requests.get(upstreamurl)
            responsecache[cachekey] = response.content

            self.send_response(response.status_code)
            self.send_header('X-Cache', 'MISS')
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(response.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start a caching proxy server.')
    parser.add_argument('--port', type=int, required=True, help='Port on which the caching proxy server will run.')
    parser.add_argument('--origin', type=str, required=True, help='URL of the server to which the requests will be forwarded.')
    parser.add_argument('--clear-cache', action='store_true', help='Clear the cache.')
    args = parser.parse_args()

    if args.clear_cache:
        responsecache.clear()
        print('Cache cleared.')
    else:
        handler = lambda *handler_args, **handler_kwargs: ProxyHandler(*handler_args, upstream=args.origin, **handler_kwargs)
        with socketserver.TCPServer(('', args.port), handler) as httpd:
            logging.info(f'Starting caching proxy server on port {args.port}, forwarding to {args.origin}')
            httpd.serve_forever()