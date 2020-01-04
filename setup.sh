#!/bin/bash
SCRIPT=$(readlink -f "$0")
BASEDIR=$(dirname "$SCRIPT")

if [[ $(whoami) -ne 'root' ]]; then
  echo "Must run as root!"
  exit -1
fi

echo "Creating virtual environment"
python3 -m venv venv
. venv/bin/activate

echo "Installing python libraries..."
pip install --upgrade -r requirements.txt

echo "Installation complete."
