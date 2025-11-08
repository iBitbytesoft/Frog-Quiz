# Uvicorn configuration for Railway deployment
# Forces HTTP/1.1 to avoid connection issues

config = {
    'host': '0.0.0.0',
    'port': None,  # Will be set from environment
    'reload': False,
    'log_level': 'info',
    # Force HTTP/1.1
    'http': 'h11',
    # Disable HTTP/2
    'interface': 'asgi3',
    # Connection settings
    'timeout_keep_alive': 5,
    'timeout_graceful_shutdown': 10,
}
