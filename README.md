# Youtubedl python client for linux
## Author: Gustavo Wydler Azuaga
## Release date: April 2023

### This client is a youtube video/audio downloader, which uses the yt-dlp linux binary package to download video, and/or audio tracks from youtube.

--------------------------------------------------------------------------------------------------------------------------------------------------

### Main Features:

  - List available formats - Opens a gnome terminal showing the different audio/video codecs for the specified track
  - Download Youtube Video
  - Download Youtube Audio
  - Download customized - Allows the codec selection to download either video, audio, or both
  - View Downloaded Content - Opens the folder where the content was downloaded
  - View Playlist Content
  - Download Entire playlist (Video and Audio)
  - Download playlist (Audio MP3)
  - Re-set url - Allows the user to change the provided youtube url, to work with different content
  - Live operations log. The console shows the operations run by the user with datetime timestamps.

--------------------------------------------------------------------------------------------------------------------------------------------------

### Installation requirements - running the pogram:

  - NOTE: a gnome terminal is required to be installed (if not already), as the python script uses it to launch the instances.
  - Clone the repo 
  - Open a gnome terminal and run: pip3 install -r REQUIREMENTS.TXT (Install the easygui librariy)
  - Copy all the .png files where the python file will be executed - Recommended to copy all content to /home/$USER/
  - Download the binary from here: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
    - INFO: Source URL for yt-dlp binary: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#readme
    - Copy the yt-dlp binary file to /usr/local/bin/
    - Test the binary by issuing: yt-dlp --version - If the version is displayed, the binary is ready to be used.
  - Run the python script from your /home/$USER/ folder: python3.x python_ytdl_client.py. Tested with version 3.8
  - The python client should open up the easygui program and you should be set to start using it.

--------------------------------------------------------------------------------------------------------------------------------------------------

### How to use it:

-  On client startup, you must provide a valid youtube url to work with.
-  Upon providing a valid youtube url, the client should list it in the main operations console, and you can start using the application.
-  Click on the desired button to operate the program.

### How it works: 

- It first creates a folder called "ytdl_downloads".
- Then it creates a video, and an audio folder in this parent directory.
- It requests the user to provide a valid youtube url to operate the program.
- The program works simply by using the yt-dlp binary to run different operations, and download youtube content.
  
