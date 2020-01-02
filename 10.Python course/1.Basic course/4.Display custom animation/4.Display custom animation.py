from microbit import *
while True:
    face1 = Image("00000:09090:00000:90009:09990")
    face2 = Image("00000:09090:00000:99999:00000")
    face3 = Image("00000:09090:00000:09990:90009")
    face4 = Image("90009:99099:00000:09990:90009")
    face5 = Image("00000:00000:00000:00000:00000")
    all_faces = [face1, face2, face3, face4, face5, ]
    display.show(all_faces, delay=200)
