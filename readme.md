# Pupper classifier

The project consists of 3 parts:

### 1. Google collab notebook - https://colab.research.google.com/drive/17Z7-E5G1sa_gZBzxF1JNZOsA05XIwelq

It's where the end-to-end multi-class image classifier is built. It uses TensorFlow 2.0 and TensorFlow Hub and Keras sequential API. The model was trained on a set of 10 000+ images from Kaggle's dog breed identification competition.

[https://www.kaggle.com/c/dog-breed-identification/data](https://www.kaggle.com/c/dog-breed-identification/data)

It exports the pre-trained model as h5 file.

### 2. FE - [https://github.com/anna-morawska/pupper-classifier-FE](https://github.com/anna-morawska/pupper-classifier-FE)

created with typescript based on create-react-app boilerplate. It's connected with backend API and allows users to upload a picture and as a response display the result of model prediction as a top 5 indexes of highest probabilities and corresponding dog breed names

to start the project run:

1. `npm install`
2. `npm start`

### 3. BE - [https://github.com/anna-morawska/pupper-classifier-BE](https://github.com/anna-morawska/pupper-classifier-BE)

Backend app is a REST API developed with Python Flask-RESTPlus framework, which provides a description of an API compatible with OpenAPI Specification.

The main job of the backend app is to process incoming POST requests with the image as a payload, pass an image to pre-trained model and

then responds with 10 top probabilities in JSON format.

In the end, the image is saved in Google Firebase Storage.

To run the containerized version of the backend app, first, you need to create `.env` file in the project's root directory. Base it off of `.env-example` file and fill it with your authentication credentials to your application, Then run:

`docker-compose up`

and navigate to [http://0.0.0.0:5000/](http://0.0.0.0:5000/)
