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

# create spot cluster
 aws cloudformation create-stack --profile datavedik --stack-name spotcluster --template-body file://\$PWD/ecs-ec2-spot-fleet.yaml --parameters ParameterKey=keyName,ParameterValue=kp --capabilities CAPABILITY_IAM

aws cloudformation create-stack --profile datavedik --stack-name spotapi --template-body file://\$PWD/apispot.yml --capabilities CAPABILITY_IAM


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

az login
az provider register -n Microsoft.ContainerService
az group create --name kpaks --location eastus
az ad sp create-for-rbac --skip-assignment



Note the appId and password from output
az aks create --resource-group kpaks --name kubelive --node-count 1 --enable-addons monitoring --service-principal "bac8ffd2-3dbb-46f7-a2f0-2aed9b0307fe" --client-secret "8926b76c-e94e-4915-bf32-34fd3ad84e30"
az aks get-credentials --resource-group kpaks --name kubelive
kubectl apply -f azure-vote.yaml
kubectl get service azure-vote-front --watch

kubectl get cs
kubectl cluster-info
kubectl create -f zure_vote.yaml
kubectl get po --watch
kubect; get svc --watch

kubectl run --image=nginx myweb
kubctl get pods
kubectl expose pod myweb-190417145-0sgv4 --prot=80 --target-port=80 --type=LoadBalancer
az acr build --image kpmlserv.azurecr.io/aquapion:v1 --registry kpmlserv --file Dockerfile .

az acr run --registry kpmlserv --file infraazure/quickrun.yaml -ti --rm -p 8500:80 .



```
