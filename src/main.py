from downloader import download

def main():
    """
    Main function to initiate the download process for a specified URL.
    """
    url = input("url >")
    print('')
    download(url)

    # download("https://www.youtube.com/watch?v=v15sS1sL_S4/")


if __name__ == "__main__":
    main()