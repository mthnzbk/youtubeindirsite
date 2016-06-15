from flask import Flask, request, url_for, render_template, abort, redirect, make_response
import pafy
import requests


app = Flask(__name__)


def sizeToMb(size):
    if size > 1024**2:
        return str(size/1024**2)+"Mb"
    else:
        return str(size/1024)+"Kb"



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        video = pafy.new(video_url)

        video_title = video.title
        video_id = video.videoid
        video_streams = video.streams
        audio_streams = video.audiostreams

        return render_template("index.html", video_id=video_id, video_url= video_url, video_title=video_title,
                               video_streams=video_streams, audio_streams=audio_streams)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()


# url_for("index") /
# url_for('static', filename='style.css') /static/style.css
# return render_template('hello.html', name=name) /templates/hello.html name-> get
# request.form['username']
# s.resolution, s.extension, s.get_filesize(), s.url -> streams
# 1280x720 mp4 2421958510 https://r1---sn-aiglln7e.googlevideo.com/videoplayba[...]
"""print(a.bitrate, a.extension, a.get_filesize())
...
256k m4a 331379079
192k ogg 172524223
128k m4a 166863001
128k ogg 108981120
48k m4a 62700449"""