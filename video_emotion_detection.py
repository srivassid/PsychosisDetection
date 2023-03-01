from fer import Video
from fer import FER

video_filename = "psy.mp4"
video = Video(video_filename)

# Analyze video, displaying the output
detector = FER(mtcnn=True)
raw_data = video.analyze(detector, display=True,)
df = video.to_pandas(raw_data)
print(df)
df.to_csv('video_emotion_detection.csv', header=True, index=False)