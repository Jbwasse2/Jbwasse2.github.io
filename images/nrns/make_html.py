import glob
import os
import pathlib
from pathlib import Path

import pudb

difficulty = ["easy", "medium", "hard"]
maptype = ["straight", "curved"]
data = ["gibson"]
method = ["gt", "old", "new"]
TC = ["True", "False"]

def make_video_hcat(vid1, vid2):
    s = "ffmpeg -i " + vid1 + " -i " + vid2 + " -filter_complex hstack output.mp4"
    os.system(s)
    cat_path = vid1.replace("True", "Cat")
    s2 = "mv ./output.mp4 " + cat_path
    os.system(s2)

def make_image_hcat(im1, im2):
    s = "convert " + im1 + " " + im2 + " +append ./output.jpg"
    os.system(s)
    cat_path = im1.replace("True", "Cat")
    s2 = "mv ./output.jpg " + cat_path
    os.system(s2)

def make_cat_media():
    files = glob.glob("./True/**/*.mp4", recursive=True)
    for f in files:
        f2 = f.replace("True", "False") 
        cat_path = Path(f.replace("True", "Cat"))
        pathlib.Path(cat_path.parent.absolute()).mkdir(parents=True, exist_ok=True)
        make_video_hcat(f, f2)
        i = f.replace(".mp4", ".jpg")
        i2 = f2.replace(".mp4", ".jpg")
        make_image_hcat(i, i2)

#copy this into NRNS html
#**Easy/Straight**
#
#No Oracle
#<p float="middle">
#  <img src="../images/nrns/noflag/easy/Cantwell_40.jpg" width="320" align="left">
#  <video width="320" height="240" controls align="left">
#    <source src="../images/nrns/noflag/easy/Cantwell_40.mp4" type="video/mp4">
#  </video>
#</p>
def make_html():
    f = open("foo.html", "w")
    word_dict = {
            "old" : "Baseline",
            "new" : "[0,1] Clipping",
            "gt" : "Ground Truth"
                }
    def get_html(im, vid):
        s1 = '<img src="' + str(im) + '" width="640" align="left">\n'
        s15 = '<source src="' + str(vid) + '" type="video/mp4">\n'
        s2 = '<video controls width="640" align="left">\n'
        s3 = '<source src="' + vid + '" type="video/mp4">\n'
        s4 = '</video>\n\n'
        s = s1 + s15 +  s2 + s3 + s4
        return s
    for df in difficulty:
        for mt in maptype:
            for dt in data:
                for m in method:
                    s = "Cat/" + m + "/" + dt + "/" + mt + "/" + df + "/*.mp4"
                    vid = glob.glob(s)[0]
                    vid = "../images/nrns/" + vid
                    im = vid.replace("mp4", "jpg")
                    s1 = "## **" + dt + "/" + df + "/" + mt + "**\n\n"
                    s2 = word_dict[m] + "\n<br>\n"
                    s3 = get_html(im, vid)
                    if m == method[0]:
                        s = s1 + s2 + s3
                    else:
                        s = s2 + s3
                    f.write(s)

difficulty = ["easy", "medium", "hard"]
maptype = ["straight", "curved"]
data = ["gibson"]
method = ["old", "gt", "new"]
TC = ["True", "False"]
#make_cat_media()
make_html()
