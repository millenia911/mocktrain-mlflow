#!/bin/bash

# create necessary folders
mkdir new_dataset
mkdir version
mkdir version/1
# download pretrained model
wget \
https://modelrepo-autotraining-poc-ndflx.s3.amazonaws.com/models/modelv1/model-metadata.json \
-O version/1/model-metadata.json

wget https://modelrepo-autotraining-poc-ndflx.s3.amazonaws.com/models/modelv1/output-model.zip
unzip -q output-model.zip -d version/1
rm output-model.zip

# dataset prep
wget https://modelrepo-autotraining-poc-ndflx.s3.amazonaws.com/datasets/vh-det-v01.zip

unzip -q vh-det-v01.zip -d new_dataset
rm vh-det-v01.zip 