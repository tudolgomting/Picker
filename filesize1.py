import os

try:
    #n = os.path.getsize("Django Reinhardt - Minor Swing.mp3")
    n = os.path.getsize("down/kasumi-arimura-000001.jpg")
    print("%d Bytes" % n)
    print("%d KB" % (n / 1024))
    print("%.2f MB" % (n / (1024.0 * 1024.0)))
except os.error:
    print("No file or Error.")
