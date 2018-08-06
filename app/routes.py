from queue import Queue

from flask import render_template, redirect
from app import app
from app.forms import VideoForm
import os
import re

myfile_queue = None

@app.route('/')
def index():
    global myfile_queue
    # open queue of files
    if myfile_queue is None:
        myfile_queue = Queue()
        video_names = open('video_index_filtered_all.txt', "r").read().splitlines()
        for video_p in video_names:
            myfile_queue.put(video_p)
            print(video_p)
    # redirect to video with params
    train_part, video_name = get_next_train_part_video()
    if video_name is None:
        return render_template('error.html', title='Error')
    return redirect('/' + train_part + '/' + video_name)


def get_next_train_part_video():
    try:
        next = myfile_queue.get()
        print(next)
        train_part = re.search(r'train-\d+', next)
        train_part = train_part.group(0)
        video_name = re.search(r'\w+-\w+\.mov', next)
        video_name = video_name.group(0)
        return train_part, video_name
    except Exception as e:
        print(str(e))
        return None, None


@app.route('/<train_part>/<video_name>', methods=['GET', 'POST'])
def video(train_part, video_name):
    video_path = os.path.join("/static/", train_part, "videos", video_name)
    form = VideoForm()
    if form.validate_on_submit():
        try:
            print('Label for video {}'.format(
                form.radio.data))
            with open('video_index_all_labels.txt', "w+") as out:
                out.write(train_part + "/videos/" + video_name + ":" + str(form.radio.data))
            train_part, video_name = get_next_train_part_video()
            if video_name is None:
                return render_template('error.html', title='Error')

            return redirect('/'+train_part+'/'+video_name)
        except:
            return redirect('/' + train_part + '/' + video_name)
    return render_template('index.html', title='Home', form=form, video_path=video_path)
