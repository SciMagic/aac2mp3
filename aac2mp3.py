import os
import fnmatch
import sys
import subprocess


def covert(path):
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.aac')
    ]

    cpath = os.path.join(path, "covert")
    print("the c path is" + cpath)
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
    print("how to use:");
    print("python aac2mp3.py aac_dir")
    if argv[1] == None:
        print("Please specify the AAC files dir")
    else:
        covert(argv[1])


if __name__ == "__main__":
    main(sys.argv)
