# Enter the number of videos you want to download
# the location you want to download to
# and  paste all the video urls


from pytube import YouTube


def download_video(save_path, n):
    # A list to store all the links
    links = []
    print("Please enter the urls of the videos.")

    for i in range(0, n):
        url = input()
        links.append(url)

    for i in range(0, n):
        link = links[i]
        try:
            # create an object of the link
            yt = YouTube(link)

            # Get the highest resolution stream with the mp4 format
            video_stream = yt.streams.filter(file_extension='mp4').first()

            file_name = yt.title

            # download the video
            video_stream.download(output_path=save_path, filename=file_name)

            print("Video Downloaded.")

        except Exception as e:
            print("Cannot download the video.")
            print(f"Error: {e}")


n = int(input("Enter the number of youtube videos to download: "))

save_path = input("Which location do you want to save the video in: ")

download_video(save_path, n)
