#!/bin/bash

echo "Cloning cloudrail knowledge repository";
git clone git@github.com:indeni/cloudrail-knowledge.git knowledge

cd knowledge
git checkout feature/code-examples
cd ../

python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
