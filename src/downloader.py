from file_utils import check_format
import os
import requests
from pytube import YouTube

"""
Validates the URL to ensure it starts with either HTTP or HTTPS and is not too long.

Returns:
    bool: True if the URL is valid, False otherwise.
"""
def validate_url(url):
    allowed_schemes = ['http', 'https']
    if not any(url.startswith(f"{scheme}://") for scheme in allowed_schemes):
        print("Invalid URL scheme. Only HTTP and HTTPS are allowed.")
        return False
    if len(url) > 2048:
        print("URL is too long.")
        return False
    return True

    
def download(url):
    """
    Downloads a file or media content from the given URL and saves it to a specific directory 
    based on the file format.

    Args:
        url (str): The URL of the file or media to be downloaded.

    Returns:
        None

    Behavior:
        - Validates the URL using the `validate_url` function.
        - Determines the format of the file using the `check_format` function.
        - Maps the file format to a specific directory path.
        - Creates the target directory if it does not exist.
        - Handles special cases for YouTube videos using the `pytube` library.
        - Downloads the file in chunks for non-YouTube URLs using the `requests` library.
        - Prints the download status and file path upon successful completion.
        - Prints an error message if the format is unsupported or if the download fails.

    Notes:
        - Supported formats and their corresponding directories are defined in the `paths` dictionary.
        - For YouTube videos, the highest resolution stream is downloaded.
        - Requires the `pytube` and `requests` libraries to be installed.
        - Handles exceptions for invalid URLs, unsupported formats, and download errors.
    """
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
