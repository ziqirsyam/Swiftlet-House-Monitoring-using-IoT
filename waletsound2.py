import vlc

player = vlc.MediaPlayer("/home/pi/Music/10secondswifletsound.mp3")
player.play()

while True: pass