# import os
# from flask import Flask, render_template, request, jsonify
# from detect_emotions import detect_emotion
#
# app = Flask(__name__)
# app.config["IMAGE_UPLOADS"] = ""
# port = int(os.environ.get("PORT", 5300))
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/emotion_recognizer', methods = ['GET', 'POST'])
# def recocnize_faces():
#    if request.method == 'POST':
#        image = request.files['image']
#        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
#        response_emotion = detect_emotion(image.filename)
#        return jsonify(
#            resp_emotion=response_emotion)
#
# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0',port=port)

from flask import Flask, render_template, Response
# from camera import VideoCamera
from real_time_video import start

app = Flask(__name__)
video_path = 'МИЛАНЕ НАДОЕЛИ СЪЁМКИ! SUPER HOUSE ТИК ТОК.mp4'

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(start(video_path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)
