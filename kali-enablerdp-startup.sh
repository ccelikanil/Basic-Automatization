#!/bin/bash

command sudo apt-get update
command sudo apt install kali-desktop-xfce
command sudo apt install xrdp
command sudo service xrdp start
command sudo systemctl enable xrdp
command sudo ufw allow 3389

echo "DONE!"
