# Image-Caption-Generator---Deep-Learning

This is a project based on Deep Learning Techniques (Convolutional Neural Network  &  Recurrent Neural Network), in which caption is generated for image which we will give as an input to our model.

Libraries used :

    1) Numpy
    
    2) OS
    
    3) Tensorflow (Keras)
    
    4) PIL
    
    
Tools used :

    1) Jupyter Notebook
    
    2) Pycharm IDE


Framework used :

    1) Django 



What is **Image-Caption-Generator** :

        Image caption generator is a task that involves computer vision and natural language processing concepts to recognize the context of an image and describe them in a natural language like English.
        

**Project Life Cycle :**

**1) Data Collection (About Data...) :-** 
 
        a) Data is collected from kaggle.
        
        b) Dataset Link : https://www.kaggle.com/ming666/flicker8k-dataset
        
        c) In dataset, there are two folders - 
        
                (i) Flicker8k_dataset , this folder contain 8K+ images with their unique id(name)
                
                (ii) Flicker8k_text, this folder contains txt file. Flickr8k.token.txt file contains captions for these 8K+ images and five captions given for one image . Flickr_8k.trainImages.txt file contains ids of 6000 images for training model. 
                

**2) Data Preprocessing :-**

    a) First of all read the file "Flickr8k.token.txt" and create a dictonary in which key is the image name and value is a list that contains 5 captions for that image.
    
    b) After that, read that dictionary and cleaned the data(captions). For cleaning, removed all numbers, commas, special symbols.....
    
    c) Then using "Xception model" , extracted the features from images and store them in a dictonary, in which key is the image name and value is feature for that image. Remove the last classification layer and get the 2048 feature vector.
    
    d)After that, read Flickr_8k.trainImages.txt file and find all captions and features for these 6000 images.
    
    e) Then create Tokenizer using Keras library and generate tokens  of captions of trainImages and save these in tokenizer.p file for future reference using pickle library.
    
    f) Then Create Data generator because we have to train our model on 6000 images and each image will contain 2048 length feature vector and caption is also represented as numbers. This amount of data for 6000 images is not possible to hold into memory so we will be using a generator method that will yield batches. The generator will yield the input and output sequence. ( For example: the input to our model is [x1, x2] and the output will be y, where x1 is the 2048 feature vector of that image, x2 is the input text sequence and y is the output text sequence that the model has to predict.)
    
    g) Now we have to build model, beacuse we have completed preprocessing to our data.
    
    
    
**3) Model Creation(Train our model):-**

        a) Used CNN & RNN model for model creation, because CNN is required for images data and RNN is required for text data.
        
        b) First of all define the the layers(input layer, dropout layer, dense layer) for CNN model and then define layers(input layer, embedding layer, dropout layer, LSTM layer) for RNN model.  then define some dense layers and output layer.
        
        c) Then merge both layers using keras library.
        
        d) Then create model using Model function with input layers and output layers.
        
        f) Then define loss and optimizer for our model.
        
        g) Now train the model using fit function and saved model file( .h5 files).
        
    
 **4) Prediction :-**
    
        a) first of all read the image for testing and create 2048 feature using Xception model and generate token for that.
        
        b) then predict the caption using our model.
        
        
 **At last, using Django framework build the front end and integrate our model in frontend.  (Frontend + Backend)**
 
 **Now our project is completely ready.**
 
 -----------------------------------------------------------------------------------------------------
 
 **Some Glimpses of our project :-** 
 
![a1](https://user-images.githubusercontent.com/61588604/118388609-2d0fb400-b643-11eb-885a-4ad603d5ce59.png)

![a2](https://user-images.githubusercontent.com/61588604/118388613-313bd180-b643-11eb-9275-1c6e095d40d3.png)

![a3](https://user-images.githubusercontent.com/61588604/118388614-313bd180-b643-11eb-87eb-4b509efe615a.png)

-------------------------------------------------------------------------------------------------------
**Some glimpses of our predictor :-**

![output](https://user-images.githubusercontent.com/61588604/118403007-0f197200-b68a-11eb-98fa-46a047ec824c.png)

![out1](https://user-images.githubusercontent.com/61588604/118388673-81b32f00-b643-11eb-84f2-df5bffd28bbd.png)

![out3](https://user-images.githubusercontent.com/61588604/118388674-837cf280-b643-11eb-8579-6a8ebabd64da.png)



**<======================================= END ==========================================>**







