# extract audio file from an MP4 video file
from moviepy.editor import VideoFileClip    
from pydub import AudioSegment

# Specify the path to your video file
video_path = '/Users/htan/Documents/StreamFab/StreamFab/Output/Youtube Plus/Keynote 3  Our AI Future – Mobile World Live.mp4'
# Specify the output audio file name
audio_output_path = '/Users/htan/Documents/StreamFab/StreamFab/Output/Youtube Plus/output_audio.mp3'

# Load the video file
video = VideoFileClip(video_path)

# Extract the audio from the video
audio = video.audio

# Write the audio to a file
audio.write_audiofile(audio_output_path)


# if mp3 size is more than 25m, cut it so as to use openai api
audio= AudioSegment.from_mp3("/Users/htan/Documents/StreamFab/StreamFab/Output/Youtube Plus/output_audio.mp3")

# PyDub handles time in milliseconds
thirty_minutes = 30 * 60 * 1000

first_30_minutes = audio[:thirty_minutes]

first_30_minutes.export("first_30_mins.mp3", format="mp3")

# Get the everything after the first 30 minutes
rest_of_audio = audio[thirty_minutes:]

rest_of_audio.export("rest_of_audio.mp3", format="mp3")

# Close the video and audio files to free up resources
audio.close()
video.close()
