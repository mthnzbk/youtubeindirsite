from flask import Flask, request, render_template
import pafy

app = Flask(__name__)


@app.route("/getir", methods=["POST"])
def getir():
    if request.method == "POST":
        video_url = request.form["video_url"]
        video = pafy.new(video_url)

        video_title = video.title
        video_id = video.videoid
        video_streams = video.streams

    return render_template("getir.html", video_id=video_id, video_url= video_url, video_title=video_title,
                               video_streams=video_streams)

@app.route("/")
def index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run()


# url_for("index") /
# url_for('static', filename='style.css') /static/style.css
# return render_template('hello.html', name=name) /templates/hello.html name-> get
# request.form['username']
# s.resolution, s.extension, s.get_filesize(), s.url -> streams
# 1280x720 mp4 2421958510 https://r1---sn-aiglln7e.googlevideo.com/videoplayba[...]