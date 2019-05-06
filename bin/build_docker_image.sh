#!/bin/bash
#
#  Builds Docker image of the
#  `aquapion` program.
#
VERSION=$1
docker build --tag  aquapion:$VERSION .