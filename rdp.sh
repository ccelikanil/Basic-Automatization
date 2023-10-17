# enables rdp access on kali (rdp user shouldn't be root)

#!/bin/bash

command sudo apt-get update
command sudo apt install kali-desktop-xfce -y
command sudo apt install xrdp -y
command sudo service xrdp start
command sudo systemctl enable xrdp
command sudo apt install ufw -y && ufw allow 3389

echo "DONE!"
