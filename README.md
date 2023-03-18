<h1 align = "center">First ML Deploy</h1>
<p align = "center">An image classifier that uses the VGG19 model to return the probability of an image input by the user.</p>

# About this work

It is my first MLOps project, so the purpose of this repository is educational only. So I used this [tutorial](https://medium.com/towards-data-science/machine-learning-in-production-keras-flask-docker-and-heroku-933b5f885459) to do this Project with some modifications that I believed would be relevant for good practices within this Project.

# Tech :gear:
 The technologies used in this project: 
 * Flask
 * TensorFlow
 * Keras
 * Docker
 * Heroku

# How to run :rocket:
This project used Docker to contenizer the application, and the comands to made is:

**1.** The first thing to do, obviously, is to [download and install Docker](https://www.docker.com/products/docker-desktop)

**2.** Create the [requirements.txt](./requirements.txt) in your main directory

**3.** Create a [Dockerfile](./Dockerfile) (without extension) which contains the instructions for building your Docker image

**4.** In a terminal, run the following command to build the Docker image:
  ```bash
 docker build -f Dockerfile -t recog_container:api .
  ```

**5.** Run container in background and print container ID using:
```bash
docker run -p 5000:5000 -d recog_container:api
```
Once this is running, you should be able to view your app running in your browser at
```
http://localhost:5000/upload
```

