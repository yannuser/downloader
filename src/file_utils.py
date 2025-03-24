from urllib.parse import urlparse

import requests

def check_format(url):
    """
    Determines the format of the file based on the URL.
    
    Args:
        url (str): The URL of the file to check.
    
    Returns:
        str: The format type if recognized, otherwise None.
    """
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return None
    
    safe_url = url.lower()
    formats = {
        'youtube': ['youtube.com', 'youtu.be'],
        'mp4': ['.mp4'],
        'm3u8': ['.m3u8'],
        'audio': ['.mp3', '.wav'],
        'image': ['.jpg', '.jpeg', '.png', '.gif'],
        'document': ['.pdf', '.txt', '.docx'],
        'archive': ['.zip', '.rar'],
        'torrent': ['.torrent']
    }
    
    for format_type, keywords in formats.items():
        for keyword in keywords:
            if keyword in safe_url:
                return format_type
            
    x = requests.head(safe_url)
    return str(x.headers.get('content-type')) if 'content-type' in x.headers else None
