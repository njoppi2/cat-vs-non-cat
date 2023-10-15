# 🐱 Cat vs Non-Cat
This repository showcases the Cat vs Non-Cat project, demonstrating various aspects of machine learning, web development, and deployment. Each folder within this repository contributes to different components of the project. For more detailed information, you can enter each folder and read their README's.

<br/>

# Deployment

I demonstrate my ability to create and deploy a machine learning application by using a simple image classification project (cat vs. non-cat). This involves an interactive website deployed using GitHub pages ([frontend](https://github.com/njoppi2/cat-vs-non-cat/tree/front-end) branch), three notebooks with basic ML models ([notebooks-and-models](https://github.com/njoppi2/cat-vs-non-cat/tree/notebooks-and-models) branch), and the current deployment branch, containing files for API creation, Dockerization, and Heroku deployment. Each branch includes a detailed README file.

## 👟 Run and interact with API locally

Before executing the commands of any folder, you must enter their directory: `cd <folder>`.

#### Manually

1. **Run**: `uvicorn app.main:app --reload`
2. **Interact via browser**: Access `http://127.0.0.1:8000/docs`
#### Using docker

1. **Build**: `docker build -t cat-api .`
2. **Run**: `docker run -p 8000:80 cat-api`
3. **Interact via browser**: Access `http://0.0.0.0:8000/docs`
  

## 🚀 Deploying to Heroku

#### Create Heroku server
1. **Create**: `heroku create cat-classifier-app`
2. **Set git remote**: `heroku git:remote cat-classifier-app`
3. **Heroku Docker setup**: `heroku stack:set container`

#### Update Heroku server

1. **Add**: `git add .`
2. **Commit**: `git commit -m "your commit"`
3. **Push**: `git push heroku deployment:main`
   
<br/>

# Notebooks and models

Here we have 3 notebooks, with logistic regression and neural network models. They're quite simple, and were trained on just 209 images and validated on 50 other images, although, data augmentation was used to duplicate the size of the training set. The best performing model was the convolutional neural network, with an accuracy of about 84% on the test set (here we don't have a validation set).

## 📋 Problem Description
The Cat vs Non-Cat problem is a classic machine learning challenge, where we need to build a model that can accurately classify images as either cat or non-cat.

<br/>

# Front-end

Here is a simple react website I made just to interact with the deployed API. To access it, click [here](https://njoppi2.github.io/cat-vs-non-cat/).

## 👟 Running the website locally

1. **Run**: `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
