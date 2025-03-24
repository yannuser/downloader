from file_utils import check_format
import os
import requests
from pytube import YouTube

def validate_url(url):
    allowed_schemes = ['http', 'https']
    if not any(url.startswith(f"{scheme}://") for scheme in allowed_schemes):
        raise ValueError("Invalid URL scheme. Only HTTP and HTTPS are allowed.")
    if len(url) > 2048:
        raise ValueError("URL is too long.")
    return True

    
def download(url):
    if not validate_url(url):
        return
    format = check_format(url)
    paths = {
        'mp4': '../downloads/videos/',
        'm3u8': '../downloads/videos/',
        'audio': '../downloads/audios/',
        'image': '../downloads/images/',
        'document': '../downloads/files/',
        'archive': '../downloads/files/',
        'torrent': '../downloads/files/',
        'txt': '../downloads/files/',
        'youtube': '../downloads/videos/'
    }

    if format not in paths:
        print(f'Unsupported format: {format}')
        return

    path = paths[format]
    os.makedirs(path, exist_ok=True)

    if format == 'youtube':
        print('Downloading YouTube video...')
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            file_name = os.path.join(path, stream.default_filename)
            stream.download(output_path=path)
            print(f'URL: {url}\nPath: {file_name}\nDownload complete')
        except Exception as e:
            print(f'Failed to download YouTube video: {e}')
        return

    print(f'Downloading {format}...')
    file_name = os.path.join(path, url.split('/')[-1])

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'URL: {url}\nPath: {file_name}\nDownload complete')
    except requests.RequestException as e:
        print(f'Failed to download: {e}')
