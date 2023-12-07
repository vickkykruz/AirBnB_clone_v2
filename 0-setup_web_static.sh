#!/usr/bin/env bash
# This is a script that sets up your web servers for the deployment of web_static.

# Install nginx if it is not install
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# Create the important folder
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create the fake HTML File
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t<h1>Holberton School</h1>\n\t</body>\n\t</html>" | sudo tee /data/web_static/releases/test/index.html

# Remove the existing symbolic link if it exist
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi

# Create the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the User and Group
sudo chown -R ubuntu:ubuntu /data/

# Update the nginx configuration
sudo sed -i "s/^\s*location \/ {/\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tindex index.html index.htm;\n\t}\n\n&/" /etc/nginx/sites-enabled/default

# Restart the nginx
sudo service nginx restart

exit 0
