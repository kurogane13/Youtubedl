import easygui as eg
import subprocess
import os
import sys
import requests

# Create the 'ytdl_downloads' folder if it doesn't exist
download_folder = 'ytdl_downloads'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
# Create 'video' and 'audio' subfolders if they don't exist
video_folder = os.path.join(download_folder, 'video')
audio_folder = os.path.join(download_folder, 'audio')

if not os.path.exists(video_folder):
    os.makedirs(video_folder)

if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

def main_screen():
    # Display the main welcome message and image
    choices = [
        "OK",
        "Exit"
    ]
    button_choice = eg.buttonbox("                    Youtube Python Video/Audio Download Client", title="YOUTUBE DL - PYTHON 3 CLIENT APPLICATION" ,choices=choices, image="/home/gus/ytdl.png")

    if button_choice == "OK":
        def check_url():

            def url_error():
                error_image = "/home/gus/ytdl/redcross.png"
                eg.msgbox("Provided url: " + set_url + " is not a valid url.\n\nPlease click OK, to proceed to the prompt, to provide a working url", title="ERROR", image=error_image)
                check_url()

            def connection_error():
                error_image = "/home/gus/ytdl/redcross.png"
                eg.msgbox("There has been a connection error.\n\nUnable to validate the url " + set_url + " at this time.\n\nPlease click OK, to proceed to the prompt", title="Response validation error", image=error_image)
                check_url()

            global set_url
            set_url = eg.enterbox("Enter the Youtube URL:", title="Youtube video url")
            if not set_url:
                # If URL is not provided, go back to the main screen
                warning="/home/gus/ytdl/warning.png"
                choices = ["Retry","Exit Program"]
                choice = eg.buttonbox("No input detected.\n\nProvide a valid youtube url please", title="NO INPUT DETECTED", image=warning, choices=choices)
                if choice == "Retry":
                    check_url()
                if choice == "Exit Program":
                    sys.exit(0)
            else:
                # Proceed to the next screen with options
                youtube_format_url="youtube.com/"
                https_string="https://"
                www="www"
                def error_base_url():
                    error_image = "/home/gus/ytdl/redcross.png"
                    eg.msgbox(msg="This is not a valid video or playlist address\n\nPlease provide a valid video, or playlist url\n\nClick OK to go back to the url prompt", title="ERROR", image="error_image")
                    check_url()
                if https_string not in set_url:
                    url_error()
                if youtube_format_url not in set_url:
                    url_error()
                else:

                    if youtube_format_url in set_url and https_string in set_url and www in set_url:
                        if set_url == https_string+youtube_format_url:
                            error_base_url()
                        if set_url == https_string+www+youtube_format_url:
                            error_base_url()
                        if set_url == None:
                            main_screen()
                        else:
                            options_screen(set_url)
                    elif youtube_format_url in set_url and https_string in set_url:
                        if set_url == https_string+youtube_format_url:
                            error_base_url()
                        if set_url == None:
                            main_screen()
                        else:
                            options_screen(set_url)

        check_url()
    if button_choice == "Exit":
        sys.exit(0)

def options_screen(set_url):
    choices = [
        "List available formats",
        "Download Youtube Video",
        "Download Youtube Audio",
        "Download Customized",
        "View Downloaded Content",
        "View Playlist Content",
        "Download Entire Playlist (Video and Audio)",
        "Download Playlist (Audio MP3)",
        "<-- Re-set url",
        "Exit"
    ]

    choice = eg.buttonbox("                  Click on a button to excecute an operation\n\n            Set video url is: \n\n"+"               "+set_url+"\n\n\n          NOTE:  To view the downloaded content use the View Downloaded Content button.\n\n", choices=choices, title="Youtube dl client operations screen", image="/home/gus/Pictures/audio_video.png")

    if choice == "List available formats":
        list_formats(set_url)
    elif choice == "Download Youtube Video":
        def start_download():
            choices = ["Yes, Download Now", "No, back to options screen"]
            choice = eg.buttonbox("Confirm if you want to start downloading now: \n\n"+set_url, choices=choices, title="Confirm download", image="/home/gus/ytdl/ytdl_video.png")
            if choice == "Yes, Download Now":
                download_video(set_url)
            if choice == "No, back to options screen":
                options_screen(set_url)
            else:
                start_download()
        start_download()

    elif choice == "Download Youtube Audio":
        def start_download():
            choices = ["Yes, Download Now", "No, back to options screen"]
            choice = eg.buttonbox("Confirm if you want to start downloading audio track now: \n\n"+set_url, choices=choices, title="Confirm download", image="/home/gus/ytdl/ytdl_audio.png")
            if choice == "Yes, Download Now":
                download_audio(set_url)
            if choice == "No, back to options screen":
                options_screen(set_url)
            else:
                start_download()
        start_download()
    elif choice == "Download Customized":
        codes = "/home/gus/ytdl/ytdl_codes.png"
        enter_code = eg.enterbox("Enter the custom format code like this:\n\nFor one code, enter only a code in the box.\n\n To combine specific video and audio codes, provide video code+audio code all together(leave blank for default)\n\nTo check the list of available codes, go back to the main menu\nand Click on List available formats.\n\nNOTE: THE IMAGE BELOW SHOWS A SAMPLE SCREENSHOT OF THE CODES. TO VIEW THE CODES FOR THIS VIDEO, GO BACK TO THE MENU AND CLICK LIST AVAILABLE FORMATS\n\n\nPlease provide a code or combination of codes to download the video: ", title="Enter Format Code", image=codes)
        if enter_code:
            download_customized(set_url, enter_code)
        if not enter_code:
            enter_code = "best"
            choices = ["Download now", "<-- Back to main menu"]
            warning="/home/gus/warning.png"
            loop = 1
            while loop == 1:
                noinput = eg.buttonbox(msg="No code, nor combination of code was provided\n\nTo download the video with the best quality format now, proceed with the buttons\n\n", title="No code input", choices=choices, image=codes)
                if noinput == "Download now":
                    download_customized(set_url, enter_code)
                if noinput == "<-- Back to main menu":
                    options_screen(set_url)
                if noinput == None:
                    loop = 1
        if enter_code == None:
            main_screen()
    elif choice == "View Playlist Content":
        view_playlist_content(set_url)
    elif choice == "Download Entire Playlist (Video and Audio)":
        def start_download():
            choices = ["Yes, Download Now", "No, back to options screen"]
            choice = eg.buttonbox("Confirm if you want to start downloading the entire playlist now: \n\n"+set_url, choices=choices, title="Confirm download", image="/home/gus/ytdl/ytdl_playlist_video.png")
            if choice == "Yes, Download Now":
                download_entire_playlist(set_url)
            if choice == "No, back to options screen":
                options_screen(set_url)
            else:
                start_download()
        start_download()
    elif choice == "Download Playlist (Audio MP3)":
        def start_download():
            choices = ["Yes, Download Now", "No, back to options screen"]
            choice = eg.buttonbox("Confirm if you want to start downloading the entire playlist audio tracks now: \n\n"+set_url, choices=choices, title="Confirm download", image="/home/gus/ytdl/ytdl_playlist_audio.png")
            if choice == "Yes, Download Now":
                download_playlist_audio(set_url)
            if choice == "No, back to options screen":
                options_screen(set_url)
            else:
                start_download()
        start_download()
    elif choice == "View Downloaded Content":
        view_downloaded_content()
    elif choice == "<-- Re-set url":
        main_screen()
    elif choice == "Exit":
        sys.exit(0)


def open_terminal(command):
    # Open GNOME Terminal and run the provided command
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
    options_screen(set_url)

def list_formats(set_url):
    # List available formats using yt-dlp in an external terminal
    command = f"yt-dlp --list-formats {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def download_video(set_url):
    # Download Youtube video using yt-dlp to the specified folder in an external terminal
    command = f"yt-dlp --output '{video_folder}/%(title)s.%(ext)s' {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def download_audio(set_url):
    # Download Youtube audio using yt-dlp to the specified folder in an external terminal
    command = f"yt-dlp --extract-audio --audio-format mp3 --output '{audio_folder}/%(title)s.%(ext)s' {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def download_customized(set_url, enter_code):
    # Download a customized video using yt-dlp to the specified folder in an external terminal
    command = f"yt-dlp -f {enter_code} --output '{download_folder}/%(title)s.%(ext)s' {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def download_entire_playlist(set_url):
    # Download entire playlist (video and audio) using yt-dlp to the specified folder in an external terminal
    #command = f"yt-dlp --output '{video_folder}/%(playlist)s/%(title)s.%(ext)s' --yes-playlist {set_url}; read -p 'Press Enter to close this session...'"
    command = f"yt-dlp bestvideo[ext = mp4]+bestaudio[ext = m4a] / mp4 --output '{video_folder}/%(playlist)s/%(title)s.%(ext)s' --yes-playlist {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def download_playlist_audio(set_url):
    # Download playlist in audio MP3 format using yt-dlp to the specified folder in an external terminal
    command = f"yt-dlp --extract-audio --audio-format mp3 --output '{audio_folder}/%(playlist)s/%(title)s.%(ext)s' --yes-playlist {set_url}; read -p 'Press Enter to close this session...'"
    open_terminal(command)

def view_playlist_content(set_url):
    command = f"yt-dlp -i -o '%(playlist_index)s-%(title)s-%(uploader)s-%(id)s' --get-filename {set_url}; read -p 'Press Enter to close this session once all the tracks are shown... '"
    open_terminal(command)

def view_downloaded_content():
    command = f" nautilus '{download_folder}'"
    open_terminal(command)

# Start the application by displaying the main screen
main_screen()
