import os
import fnmatch
import sys
import subprocess
import threading


def covert(path):
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.aac')
    ]
    print("cover path : " + path + "start")
    cpath = os.path.join(path, "covert")
    if os.path.exists(path=cpath):
        os.makedirs(cpath)

    for filename in filenames:
        source = os.path.join(path, filename)
        print("cover file :" + source);
        dest = os.path.join(cpath, "%s.mp3" % filename[:-4])
        subprocess.call([
            "ffmpeg", "-i",
            source, "-acodec",
            "libmp3lame", dest
        ])


def main(argv):
    print("how to use: python aac2mp3.py aac_dir ...");
    if len(argv) <= 1:
        print("please assign the dir")
    else:
        for i in range(1, len(argv)):
            t = threading.Thread(target=covert, args=(argv[i],))
            t.start()


if __name__ == "__main__":
    main(sys.argv)
