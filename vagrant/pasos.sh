#!/bin/bash

sudo apt update -y &> /dev/null
sudo apt install -y mariadb-server &> /dev/null
sudo apt install -y software-properties-common &> /dev/null
sudo add-apt-repository ppa:deadsnakes/ppa -y &> /dev/null
sudo apt install -y python3.9 &> /dev/null
sudo apt update && sudo apt install python3-pip -y &> /dev/null
pip3 install requests &> /dev/null
pip3 install mysql.connector &> /dev/null
sudo mysql -e "alter user 'root'@'localhost' identified by 'root';"
python3 /home/vagrant/shared_folder/actualizar_precios.py
