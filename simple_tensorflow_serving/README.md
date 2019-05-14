# Server

## Introduction

Start the server with installed binary.

```
simple_tensorflow_serving --port=8500 --model_base_path="./models/tensorflow_template_application_model"
``

Or start with Python script.

```
simple_tensorflow_serving --port=8500 --model_base_path="./models/tensorflow_template_application_model"
``

Or start with [gunicorn](http://gunicorn.org/).

```
gunicorn --bind 0.0.0.0:8500 wsgi
```

Or run with `uwsgi`.

```
uwsgi --http 0.0.0.0:8500 -w wsgi

uwsgi --http 0.0.0.0:8501 -w wsgi --pyargv "--model_name hello"

```
AWS stack deployment

```
aws cloudformation create-stack --profile datavedik --stack-name ml-serv --template-body file://$PWD/stack.yml

exporet DOCKER_HOST=tcp://{{ec2publicipaddress}}:2375
make image dev=latest
docker run -ti --rm -p 80:8500 aquapion:latest
aws cloudformation delete-stack --profile datavedik --stack-name ml-serv




```
Google deployment


```
 curl https://sdk.cloud.google.com | bash
 gcloud components install kubectrl
 gcloud auth configure-docker                                                            
 docker tag aquapion:latest gcr.io/$PROJECT_ID/aquapion:latest                           
 docker push  gcr.io/$PROJECT_ID/aquapion:latest   
 gcloud container clusters create kubecluster --zone us-central1-a
 kubectl run kubecluster --image=gcr.io/kubernetes-app-240915/aquapion:latest --port=80
 kubectl expose deployment kubecluster --type="LoadBalancer"
 kubectl get services kubecluster


```

Azure deployment


```

 gcloud auth configure-docker                                                            
 docker tag aquapion:latest gcr.io/$PROJECT_ID/aquapion:latest                           
 docker push  gcr.io/$PROJECT_ID/aquapion:latest   
 gcloud container clusters create kubecluster --zone us-central1-a
 kubectl run kubecluster --image=gcr.io/kubernetes-app-240915/aquapion:latest --port=80
 kubectl expose deployment kubecluster --type="LoadBalancer"
 kubectl get services kubecluster


```
