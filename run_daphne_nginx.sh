#!/bin/bash

sudo chmod 644 /etc/nginx/ssl/localhost.crt
sudo chmod 600 /etc/nginx/ssl/localhost.key
sudo chown $USER:$USER /etc/nginx/ssl/localhost.*
sudo systemctl start nginx
export RENDER_FILM_REVIEWS=0
daphne -e ssl:8000:privateKey=/etc/nginx/ssl/localhost.key:certKey=/etc/nginx/ssl/localhost.crt film_reviews.asgi:application
