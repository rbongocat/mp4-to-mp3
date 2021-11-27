import os
import sys
import time
from moviepy.video.io.VideoFileClip import VideoFileClip

mypath = "B:\Desktop\MP4 to MP3"
mp4 = []
for file in os.listdir(mypath):
    if file.endswith(".mp4"):
        mp4.append(file)

if len(mp4) == 0:
    print("No MP4 files found. Program exit.")
    time.sleep(3)
    sys.exit()

selector = ''
for i in range(len(mp4)):
    selector += f"{i + 1}: {file}\n"

print(selector)
select_file = int(input("Which MP4 to convert to MP3? (Input number): "))
selected_file = mp4[select_file - 1]
mp4_file_path = f"{mypath}\{selected_file}"
mp3_name = input("Input name of MP3 file (input nothing for same name): ")
if mp3_name == "":
    mp3_name = selected_file
mp3_file_path = f"{mypath}\{mp3_name.split('.')[0]}.mp3"

video = VideoFileClip(mp4_file_path)
video.audio.write_audiofile(filename=mp3_file_path)
video.audio.close()
video.close()

os.remove(mp4_file_path)