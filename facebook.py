import youtube_dl


class FacebookVideoDownloader:
    def __init__(self, url):
        self.url = url
        self.use_credentials = False

    def download_video(self):
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
        }


        if self.use_credentials:
            username = input("Enter your Facebook username: ")
            password = input("Enter your Facebook password: ")
            ydl_opts['username'] = username
            ydl_opts['password'] = password


        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])


if __name__ == '__main__':

    video_url = input("Enter the Facebook video URL: ")
    use_credentials = input("Do you want to enter your credentials for private videos? (y/n): ").lower() == 'y'

    downloader = FacebookVideoDownloader(video_url)
    downloader.use_credentials = use_credentials
    downloader.download_video()
