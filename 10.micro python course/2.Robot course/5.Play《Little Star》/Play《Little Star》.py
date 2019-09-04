from microbit import *
import music
display.show(Image.MUSIC_QUAVER)
# Display a music pattern on the micro:bit dot matrix

tune = ["C4:4", "C", "G", "G", "A", "A", "G:8", "F:4",
        "F", "E", "E", "D:4", "D", "C:8", "G:4", "G",
        "F", "F", "E", "E", "D:8", "G:4", "G", "F",
        "F", "E", "E", "D:8", "C4:4", "C", "G", "G",
        "A", "A", "G:8", "F:4", "F", "E", "E", "D:4",
        "D", "C:8"]   # Song little star
music.play(tune)