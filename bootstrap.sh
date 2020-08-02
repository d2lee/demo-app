# Install the nginx
apt -y install nginx

# Remove the default page
rm /etc/nginx/sites-enabled/default

# Create the configuration file for flask site

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

mv /tmp/example.com /etc/nginx/sites-available/example.com

# Link from sites-available to sites-enabled folder
ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com

# Restart nginx to make it effect
service nginx restart

# Install pip3 and gunicorn
apt -y install python3-pip gunicorn3

# Install flask
pip3 install flask

# Git clone to fetch the source
su - ubuntu -c "cd /home/ubuntu && git clone https://github.com/d2lee/demo-app.git"

# run the gunicorn
cd /home/ubuntu/demo-app && gunicorn3 app:app
