#!/bin/bash

# Configuramos la zona horaria
cp /usr/share/zoneinfo/Europe/Madrid /etc/localtime

# Añadimos localhost a los known_hosts para que hadoop pueda hacer ssh sin problemas
ssh-keyscan -t rsa localhost > /root/.ssh/known_hosts

exit 0;