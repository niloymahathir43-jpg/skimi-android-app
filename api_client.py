"""Placeholder client for future secure backend integration."""
from api_config import API_BASE_URL

def backend_is_configured():
    return bool(API_BASE_URL.strip())
