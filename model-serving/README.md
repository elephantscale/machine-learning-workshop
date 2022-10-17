# Model Serving

## Step-1: Build and Save a Model

Run [build-model.ipynb](build-model.ipynb) to build and save a model

## WebService

We will host the service using [Flask web server](https://flask.palletsprojects.com/en/1.1.x/)

## Step-2: Install 

Install prerequisites

To run the webservices, install the prerequisites

```bash

# for conda environments
$  conda  install flask
# or
# for pip install
$  pip install flask
```

## Step-3: web_service.py

Inspect file [web_service.py](web_service.py)


## Step-4: Run the webservice

```bash
$   cd  model-serving
$   python web_service.py
```

## Step-5: Make a Web service request

In the browswer go to : http://localhost:5000  (or adjust the port number accordingly)

We can also use `curl` to make a webservice request

```bash
$  curl 'http://localhost:5000/'
```

We will see 

```text
Hello world!
```

Great, web service is working

## Step-6 : Call `prediction` webservice

Run the following request.  You can modify the parameters to test it out

Go to this url in your browser

```text
http://localhost:5000/predict?Bedrooms=4&Bathrooms=2.5&SqFtTotLiving=2000&SqFtLot=8000&LandVal=500000
```

or using curl

```bash
$   curl 'http://localhost:5000/predict?Bedrooms=4&Bathrooms=2.5&SqFtTotLiving=2000&SqFtLot=8000&LandVal=500000'
```

## Production ready web services

Here we used [Flask web server](https://flask.palletsprojects.com/en/1.1.x/) for a small web service.  While Flask is really great for quick deployments, it is not really production strength.

Look at frameworks like [gunicorn](https://gunicorn.org/) for implementing production ready systems.

[Tornado](https://www.tornadoweb.org/en/stable/)

[Fast API](https://realpython.com/fastapi-python-web-apis/)

## Other References

[ColabCode: Deploying Machine Learning Models From Google Colab](https://towardsdatascience.com/colabcode-deploying-machine-learning-models-from-google-colab-54e0d37a7b09)

[Deploy Machine Learning Web Applications with Streamlit](https://ngugijoan.medium.com/deploy-machine-learning-web-applications-with-streamlit-238b0380679d)

[Deploy Machine Learning Model using Flask to Heroku — Beginners(Part 1)](https://medium.com/analytics-vidhya/deploy-machine-learning-model-using-flask-to-heroku-beginners-part-1-451b117a4c7e)


## Load Testing Tools

- [Jmeter](https://jmeter.apache.org/)
- [Apache bench](https://httpd.apache.org/docs/2.4/programs/ab.html)