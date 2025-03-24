from downloader import download

def main():
    """
    Main function to initiate the download process for a specified URL.
    """
    # url = input("url >")
    # download(url)

    # download("https://archive.org/details/the-boondocks-4k-season-2-complete-singecku/The+Boondocks+(4K)+S2+E12+-+The+Story+Of+Catcher+Freeman.mp4")
    # download("https://archive.org/download/pictureofdoriang00wildiala/pictureofdoriang00wildiala_archive.torrent")
    # download("https://www.youtube.com/watch?v=v15sS1sL_S4/")
    download("https://www.gutenberg.org/ebooks/75688.txt.utf-8")

if __name__ == "__main__":
    main()