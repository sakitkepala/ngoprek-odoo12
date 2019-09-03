sudo apt-get update
sudo apt-get upgrade -y

# Install Python 3 -> 3.6
sudo apt-get install -y python3-dev python3-pip

# Install wkhtmltopdf -> 0.12.5-1
sudo apt-get install -y wkhtmltopdf
sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo apt install -f

sudo rm -rf wkhtmltox_0.12.5-1.bionic_amd64.deb

sudo cp /usr/local/bin/wkhtmltopdf /usr/bin
sudo cp /usr/local/bin/wkhtmltoimage /usr/bin

# Install node, npm & LESS
sudo apt-get install -y npm #-> latest
sudo npm install -g less less-plugin-clean-css #-> latest

# Install PostgreSQL & bikin user dengan nama vagrant -> latest
sudo apt-get install -y postgresql
sudo su - postgres -c "createuser -s $USER"

# Install tool untuk development & dependensi sistem yang diperlukan
sudo apt-get install -y libxml2-dev libxslt1-dev libevent-dev \
                      libpq-dev libjpeg-dev poppler-utils
sudo apt-get install -y libldap2-dev libsasl2-dev

# Install dependensi Python untuk jalankan Odoo
sudo pip3 install -r /12/requirements.txt
