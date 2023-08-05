import moviepy.editor

video = moviepy.editor.VideoFileClip("Video-1.mp4")

audio = video.audio

audio.write_audiofile("Video-1.mp3")