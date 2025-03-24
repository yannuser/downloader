from downloader import download

def main():
    """
    Main function to initiate the download process for a specified URL.
    """
    url = input("url >")
    print('\n\n')
    download(url)


if __name__ == "__main__":
    main()