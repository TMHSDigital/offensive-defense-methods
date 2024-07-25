#!/bin/bash

# Install prerequisites
sudo apt-get update
sudo apt-get install -y git python3-virtualenv libssl-dev libffi-dev build-essential

# Clone the Cowrie repository
git clone http://github.com/cowrie/cowrie

# Set up the virtual environment
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate

# Install Cowrie dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Start Cowrie
bin/cowrie start
