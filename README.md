# 🚀 CacheProxy

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
  ![License](https://img.shields.io/badge/License-MIT-green.svg)
  [![GitHub](https://img.shields.io/github/followers/TheRealSaiTama?label=Follow&style=social)](https://github.com/TheRealSaiTama)
  
  <p>A lightning-fast HTTP caching proxy server with minimal configuration.</p>
</div>

## 📋 Overview

CacheProxy is a lightweight caching proxy server that intercepts and caches HTTP requests. It improves performance by storing responses locally and serving them directly for repeated requests, reducing latency and server load.

## ✨ Features

- 🔄 **Transparent Proxy**: Seamlessly forwards requests to the origin server
- ⚡ **Intelligent Caching**: Stores responses for quick retrieval
- 🔍 **Cache Hit/Miss Headers**: Clearly indicates whether responses come from cache
- 🧹 **Cache Management**: Simple commands to clear the cache when needed
- 📊 **Detailed Logging**: Provides insights into cache performance

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/TheRealSaiTama/CacheProxy.git

# Navigate to the project directory
cd CacheProxy

# Install dependencies
pip install requests
```

## 🚀 Usage

### Starting the proxy server

```bash
python cacheproxy.py --port <PORT_NUMBER> --origin <ORIGIN_URL>
```

Example:

```bash
python cacheproxy.py --port 3000 --origin http://dummyjson.com
```

This starts the proxy server on port 3000 and forwards requests to http://dummyjson.com.

### Making requests

Once the server is running, you can make requests to your proxy:

```
http://localhost:<PORT_NUMBER>/your-path
```

Example:

```
http://localhost:3000/products
```

This will forward the request to `http://dummyjson.com/products` and cache the response.

### Clearing the cache

```bash
python cacheproxy.py --clear-cache
```

## 🔍 How It Works

1. Client makes a request to the proxy server
2. The proxy checks if the request is in the cache:
   - If found (cache hit): Returns the cached response with `X-Cache: HIT` header
   - If not found (cache miss): Forwards request to the origin, caches the response, and returns it with `X-Cache: MISS` header
3. Subsequent identical requests are served from cache

## 📋 Technical Details

The implementation uses Python's built-in `http.server` and `socketserver` modules to create the proxy server. The `requests` library handles outgoing requests to the origin server, and responses are cached in memory.

## 📝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  
  Created with ❤️ by [TheRealSaiTama](https://github.com/TheRealSaiTama)
  
</div>
