#!/bin/sh

# Upgrade the pre-installed packages
apt -y update

# Install the nginx
apt -y install nginx

# Remove the default page
rm /etc/nginx/sites-enabled/default

# Create the configuration file for flask site

cat << 'EOF' >> /tmp/example.com
server {
        listen 80;

        location / {
                proxy_pass http://127.0.0.1:8000/;
        }
}
EOF

mv /tmp/example.com /etc/nginx/sites-available/example.com

# Link from sites-available to sites-enabled folder
ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com

# Restart nginx to make it effect
service nginx restart

# Install pip3
apt -y install python3-pip

# Install gunicorn
pip3 install gunicorn

# change to home direct
cd /home/ubuntu

# git clone to fetch the source
git clone https://github.com/d2lee/demo-app.git

