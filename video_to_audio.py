import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip("psy.mp4")

# Insert Local Audio File Path
clip.audio.write_audiofile("psy.wav")