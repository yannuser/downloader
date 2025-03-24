from file_utils import check_format
import os
import requests
from pytube import YouTube
import subprocess


def validate_url(url):
    """
    Validates the URL to ensure it starts with either HTTP or HTTPS and is not too long.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    allowed_schemes = ['http', 'https']
    if not any(url.startswith(f"{scheme}://") for scheme in allowed_schemes):
        print("Invalid URL scheme. Only HTTP and HTTPS are allowed.")
        return False
    if len(url) > 2048:
        print("URL is too long.")
        return False
    return True

def get_download_path(format):
    """
    Maps the file format to a specific directory path.

    Args:
        format (str): The file format.

    Returns:
        str: The directory path for the given format.
    """
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
    return paths.get(format)

def create_directory(path):
    """
    Creates the target directory if it does not exist.

    Args:
        path (str): The directory path to create.
    """
    os.makedirs(path, exist_ok=True)

def download_youtube_video(url, path):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        url (str): The YouTube video URL.
        path (str): The directory path to save the video.
    """
    print('Downloading YouTube video with yt-dlp...')
    try:
        # Use yt-dlp to download the video
        subprocess.run(
            [
                'yt-dlp',
                '-f', 'best',
                '-o', os.path.join(path, '%(title)s.%(ext)s'),
                url
            ],
            check=True
        )
        print(f'URL: {url}\nDownload complete')
    except subprocess.CalledProcessError as e:
        print(f'Failed to download YouTube video: {e}')

def download_file(url, path):
    """
    Downloads a file from the given URL in chunks.

    Args:
        url (str): The file URL.
        path (str): The directory path to save the file.
    """
    print(f'Downloading file...')
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

def download(url):
    """
    Downloads a file or media content from the given URL and saves it to a specific directory 
    based on the file format.

    Args:
        url (str): The URL of the file or media to be downloaded.
    """
    if not validate_url(url):
        return

    format = check_format(url)
    path = get_download_path(format)

    if not path:
        print(f'Unsupported format: {format}')
        return

    create_directory(path)

    if format == 'youtube':
        download_youtube_video(url, path)
    else:
        download_file(url, path)
