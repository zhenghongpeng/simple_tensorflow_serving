# ------------------------------------------------- #
#                                                   #
#    MAKEFILE                                       #
#    --------                                       #
#                                                   #
#    Makefile commands for aquapion:               #
#                                                   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                   #
#        test:  run tests via nosetest.             #
#                                                   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                   #
#        build:  builds all Docker images for       #
#        aquapion.                                 #
#                                                   #
#        build-app-image:  build Crytonic's         #
#        API Docker image.                          #
#                                                   #
#        build-cache-image:  build Crytonic's       #
#        cache Docker image.                        #
#                                                   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                   #
#        deploy:  deploy combination of Docker      #
#        containers locally.                        #
#                                                   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                                                   #
#        package:  packages all components into     #
#        a few Docker images ready for deployment.  #
#                                                   #
#        package-ui:  packages the aquapion UI.    #
#                                                   #
# ------------------------------------------------- #

appName = aquapion

all: test package

test:
	bash bin/test.sh;

#
#  Build Docker images.
#
.PHONY: build
build: build-app-image

build-app-image:
	bash bin/build_docker_image.sh "latest";


#usage make publish rev=latest

rev ?= $(shell python -c "import build; print(build.version.replace('+','-'))")

all:
	# Nothing to do
image:
	docker -D build --tag $(appName):$(rev) .
	docker image prune --force
publish-image:
	aws ecr describe-repositories --registry-id=181748805414 --region=us-east-1 --repository-names $(appName) >/dev/null 2>&1 || \
	  aws ecr create-repository --region=us-east-1 --repository-name $(appName)
	`aws ecr get-login --registry-id 181748805414 --region us-east-1 --no-include-email`
	docker tag $(appName):$(rev) 181748805414.dkr.ecr.us-east-1.amazonaws.com/$(appName):$(rev)
	docker push 181748805414.dkr.ecr.us-east-1.amazonaws.com/$(appName):$(rev)
	docker rmi 181748805414.dkr.ecr.us-east-1.amazonaws.com/$(appName):$(rev)

deploy: 
	docker-compose up -d;