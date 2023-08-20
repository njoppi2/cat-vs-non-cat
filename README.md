# 🐱 Cat vs Non-Cat
I demonstrate my ability to create and deploy a machine learning application by using a simple image classification project (cat vs. non-cat). This involves an interactive website deployed using GitHub pages ([frontend](https://github.com/njoppi2/cat-vs-non-cat/tree/front-end) branch), three notebooks with basic ML models ([notebooks-and-models](https://github.com/njoppi2/cat-vs-non-cat/tree/notebooks-and-models) branch), and the current deployment branch, containing files for API creation, Dockerization, and Heroku deployment. Each branch includes a detailed README file.

## 👟 Run and interact with API locally

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

## 📂 Repository Structure
**app/**: This directory contains files to run the server's API, as well as a saved machine learning model as a pickle file, to be run when the API receives a request.

**Dockerfile**: This file contains instructions for Docker to set up a separate and self-contained environment for an application.

**requirements.txt**: This file lists the external libraries and dependencies needed for a Python project to run successfully within a Docker container.

**heroku.yml**: This file provides configuration instructions for deploying and running applications on the Heroku platform.

