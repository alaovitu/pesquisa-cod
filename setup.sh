#!/bin/bash
# Instala as dependências necessárias para o driver ODBC
apt-get install -y curl gnupg
# Instala o driver ODBC da Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17
ACCEPT_EULA=Y apt-get install -y mssql-tools
# Adiciona as ferramentas ao PATH
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
apt-get install -y unixodbc-dev
