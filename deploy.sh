#!/bin/bash

cd /var/www/My_Project/
git pull
systemctl restart my-application
