#!/bin/bash

yum update -y

amazon-linux-extras install nginx1 python3.8 -y

cat << 'EOF' >> /tmp/example.com
server {
        listen 80;
        access_log  /var/log/nginx/example.log;
        location / {
                proxy_pass http://127.0.0.1:8000/;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
EOF

mv /tmp/example.com /etc/nginx/conf.d/example.com.conf

# Restart nginx to make it effect
systemctl restart nginx

yum install python3-pip git -y

# Install flask
pip3 install flask gunicorn

# Git clone to fetch the source
su - ec2-user -c "cd /home/ec2-user && git clone https://github.com/d2lee/demo-app.git"

cd /home/ec2-user/demo-app && gunicorn app:app
