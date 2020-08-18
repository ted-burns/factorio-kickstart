#!/bin/bash

# Centos: Install required programs
yum install sudo -y
yum install wget -y
sudo dnf update -y
sudo dnf install git -y

# Install Factorio init
git clone https://github.com/Bisa/factorio-init.git
cp /opt/factorio-init/factorio.service.example /etc/systemd/system/factorio.service
ln -s /opt/factorio-init/factorio /etc/init.d/factorio
systemctl enable factorio 
chmod +x /opt/factorio-init/factorio 
mv factorio-init/config.example factorio-init/config
useradd factorio

# Install Factorio
factorio-init/factorio install
rm /opt/factorio/data/server-settings.json
mv server-settings.json  /opt/factorio/data/server-settings.json
chown -R factorio:factorio /opt/factorio 
