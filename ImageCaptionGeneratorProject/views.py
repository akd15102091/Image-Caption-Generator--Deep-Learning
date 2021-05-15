from django.http import HttpResponse
from django.shortcuts import render
import os
from django.db import models
import glob
import numpy as np
from keras.models import load_model
from tensorflow.keras.applications.xception import Xception , preprocess_input
from tensorflow.keras.preprocessing.image import load_img ,img_to_array
from tensorflow.keras.utils import to_categorical
from pickle import dump,load
from tqdm import tqdm
from PIL import Image
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical



from .forms import StudentForm

def index(request) :
    return render(request,"index.html")

def aboutproject(request) :
    return render(request,"aboutproject.html")

def cappredictor(request):
    return render(request,'cappredictor.html')


def test_extract_feature(filename, model):
    try:
        image = Image.open(filename)
    except:
        print('Invalid image')

    image = image.resize((299, 299))
    image = np.array(image)
    if image.shape[2] == 4:
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    feature = model.predict(image)
    return feature

def word_for_id(integer , tokenizer):
    for word , index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def test_generate_desc(model, tokenizer, photo, max_cap_length):
    in_text = 'start'
    for i in range(max_cap_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence],maxlen = max_cap_length )
        pred = model.predict([photo,sequence],verbose=0)
        pred= np.argmax(pred)
        word = word_for_id(pred,tokenizer)
        if word is None:
            break
        in_text += ' '+word
        if word == 'end':
            break
    return in_text


def predictCaption(request) :
    if request.method == 'POST':
        up_files = glob.glob('static/uploads/*')
        for x in up_files:
            os.remove(x)

        ans = ""
        imgurl = ""

        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            f = request.FILES['file']

            with open('static/uploads/' + f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            tokenizer = load(open('tokenizer.p', 'rb'))
            model = load_model('models/model_9.h5')
            xception_model = Xception(include_top=False, pooling='avg')
            img_path = 'static/uploads/'+str(f)
            abc='uploads/'+ str(f)
            imgname= str(f)
            imgurl="static/uploads/"+imgname
            print(imgurl)
            photo = test_extract_feature(img_path, xception_model)
            img = Image.open(img_path)
            max_cap_length = 38
            description = test_generate_desc(model, tokenizer, photo, max_cap_length)
            ans = description[6:len(description)-4]
            ans = "Generated Caption is : "+ans
        return render(request, "cappredictor.html",{"predictedcap":ans,"imgurl":imgurl})
    else:
        student = StudentForm()
        return render(request, "cappredictor.html")