import moviepy.editor
from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)

audio = video.audio
audio.write_audiofile("demp.mp3")
print("___End___")