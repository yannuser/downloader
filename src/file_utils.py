from urllib.parse import urlparse

def check_format(url):
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
    return None
