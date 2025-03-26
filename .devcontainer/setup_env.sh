#!/bin/bash

cp $BIN_FOLDER/ubuntu_bashrc $HOME/.bashrc

OMNI_PATH="/usr/local/lib/python3.10/dist-packages/omni/"
CACHE_PATH="//home/dev/.cache"
if [ -e "${OMNI_PATH}" ]; then
  echo "Taking ownership of isaac sim folder"
  sudo chown $USER:$USER ${OMNI_PATH}
  sudo chown $USER:$USER ${CACHE_PATH}
fi
mkdir -p $HOME/ws_ai
source /opt/ros/humble/setup.bash
