# extract audio file from an MP4 video file
from moviepy.editor import VideoFileClip    

# Get the path info of each file in the folder
import os
import glob


def list_mp4_files(folder_path):
    # Create a pattern to match all .mp4 files in the directory
    pattern = os.path.join(folder_path, '*.mp4')
    
    # Use glob.glob to find all paths that match the pattern
    mp4_files = glob.glob(pattern)
    
    # Optionally, you can print the paths
    for file_path in mp4_files:
        print(file_path)
    
    # Return the list of paths
    return mp4_files

def process_mp4_files(folder_path):
    mp4_files = list_mp4_files(folder_path)

    #Iterate over the list of mp4 files
    for video_path in mp4_files:
        # Load the video file
        video = VideoFileClip(video_path)

        # Extract the audio from the video
        audio = video.audio

        # Write the audio to a file
        audio_output_path = video_path.replace('.mp4', '.mp3')
        audio.write_audiofile(audio_output_path)

        # Close the video and audio files to free up resources
        audio.close()
        video.close()

# Replace with your actual folder path
folder_path = '/Users/htan/Documents/StreamFab/StreamFab/Output/Youtube Plus'  # Replace with your actual folder path
process_mp4_files(folder_path)




"""
# if mp3 size is more than 25m, cut it so as to use openai api
from pydub import AudioSegment
audio= AudioSegment.from_mp3("/Users/htan/CodeProject/Data/output_audio.mp3")


# PyDub handles time in milliseconds
thirty_minutes = 15 * 60 * 1000

first_30_minutes = audio[:thirty_minutes]

first_30_minutes.export("first_30_mins.mp3", format="mp3")

# Get the everything after the first 30 minutes
rest_of_audio = audio[thirty_minutes:]

rest_of_audio.export("rest_of_audio.mp3", format="mp3")

# Close the video and audio files to free up resources
audio.close()
video.close()
"""