from moviepy.editor import *

video = VideoFileClip("end.mp4")
video.write_gif("final.gif")