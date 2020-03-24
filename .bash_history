ls
sudo apt-get update && apt-get upgrade -y
sudo -i
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx git
sudo su - postgres
git clone https://github.com/abhishekraj272/scrapshut.git
ls
cd scrapshut
cd ..
ls
cd scrapshut
ls
pip3 --version
sudo apt install python3-pip
pip3 freeze
python3 --version

sudo python3 manage.py runserver 0.0.0.0:80
clear
django-admin --version
pip3 freeze
clear
pip3 freeze
pip3 install -r requirements.txt
pip3 freeze
pip3 freeze > check.log
nano check.log
clear
ls
python3 manage.py runserver
sudo python3 manage.py runserver 0.0.0.0:80
sudo python3 manage.py runserver 0.0.0.0:8000
clear
pip3 install psycopg2
cd ss
nano settings.py
fg
nano settings.py
cd ..
cd ...
cd ..
pip3 install gunicorn
cd scrapshut
python3 manage.py makemigrations
python3 manage.py migrate
cd ss
nano settings.py
cd ..
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
python3 manage.py runserver 0.0.0.0:8000
python3 manage.py collectstatic
git push origin master
git add .
git commit -m "added postgre"
git push origin master
clear
gunicorn --bind 0.0.0.0:8000 sample_project.wsgi
pip3 install gunicorn
gunicorn --bind 0.0.0.0:8000 sample_project.wsgi
sudo apt install gunicorn
gunicorn --bind 0.0.0.0:8000 sample_project.wsgi
gunicorn3 --bind 0.0.0.0:8000 sample_project.wsgi
gunicorn --bind 0.0.0.0:8000 sample_project.wsgi
clear
gunicorn --version
clearclear
clear
gunicorn --bind 0.0.0.0:8000 sample_project.wsgi
gunicorn --bind 0.0.0.0:8000 ss.wsgi
sudo apt-get install python-virtualenv
clear
virtualenv ss-env
source ss-env/bin/activate
git clone https://github.com/abhishekraj272/scrapshut.git
pip3 install -r requirements.txt
pip3 install psycopg2
pip3 freeze > req.log
nano re.log
nano req.log
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py runserver 0.0.0.0:8000
clear
pip3 install gunicorn
cd ss
gunicorn --bind 0.0.0.0:8000 ss.wsgi
cd ..
gunicorn --bind 0.0.0.0:8000 ss.wsgi
cd ~/scrapshut
cd ~/
cd ~/scrapshut
gunicorn --bind 0.0.0.0:8000 ss.wsgi
sudo apt-get remove gunicorn
deactivate
source ss-env/bin/activate
gunicorn --bind 0.0.0.0:8000 ss.wsgi
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 ss.wsgi
pip install django
gunicorn --bind 0.0.0.0:8000 ss.wsgi
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 ss.wsgi
pip3 install gunicorn
gunicorn --bind 0.0.0.0:8000 ss.wsgi
pip3 freeze
pip freeze
sudo apt-get install gunicorn3
gunicorn3 --bind 0.0.0.0:8000 ss.wsgi
python3 manage.py collectstatic
gunicorn3 --bind 0.0.0.0:8000 ss.wsgi
ls
cd scrapshut
ls
cd ..
source ss-env/bin/activate
cd scrapshut
ls
mv ss-env ~/
ls
cd ..
ls
clear
source ss-env/bin/activate
ls
deactivate
cd scrapshut
ls
cd ss
nano settings.py
ls
cd scrapshut
cd bin
ls
cd ..
cd ss-env
ls
cd bin
ls
cd ..
sudo nano /etc/systemd/system/gunicorn.service
cd /etc/nginx
ls
cd sites-available
ls
sudo nano scrapshut
sudo ln -s /etc/nginx/sites-available/scrapshut /etc/nginx/sites-enabled
cd ..
cd ~/
sudo nginx -t
sudo service nginx restart
sudo nano /etc/nginx/sites-available/scrapshut
sudo service nginx restart
sudo nginx -t
sudo ln -s /etc/nginx/sites-available/scrapshut /etc/nginx/sites-enabled
sudo nano /etc/nginx/sites-enabled/scrapshut
sudo nginx -t
sudo nano /etc/nginx/sites-enabled/scrapshut
sudo nginx -t
sudo ln -s /etc/nginx/sites-available/scrapshut /etc/nginx/sites-enabled
sudo service nginx restart
cd /etc/nginx
ls
semanage port -a -t PORT_TYPE -p tcp 80
sudo nginx -t
sudo nano /etc/nginx/sites-enabled/scrapshut
clear
cd ~/
ls
mv ss-env scrapshut/
ls
cd scrapshut
ls
cd scrapshut
ls
cd ..
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn3.socket
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
clear
sudo systemctl start gunicorn3.socket
sudo systemctl start gunicorn.socket
sudo nano /etc/systemd/system/gunicorn.socket
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
sudo systemctl status gunicorn3
sudo systemctl status gunicorn
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo journalctl -u gunicorn3
sudo systemctl enable gunicorn.socket
sudo journalctl -u gunicorn3
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn3
sudo nano /etc/systemd/system/gunicorn.socket
sudo mv /etc/systemd/system/gunicorn.socket /etc/systemd/system/gunicorn3.socket
sudo nano /etc/systemd/system/gunicorn3.socket
sudo nano /etc/systemd/system/gunicorn.service
sudo nano /etc/systemd/system/gunicorn3.service
sudo systemctl start gunicorn3.socket
sudo systemctl enable gunicorn3.socket
sudo systemctl status gunicorn3.socket
file /run/gunicorn3.sock
sudo journalctl -u gunicorn3.socket
sudo systemctl status gunicorn3
curl --unix-socket /run/gunicorn3.sock localhost
sudo systemctl status gunicorn3
sudo journalctl -u gunicorn3
ls
cd scrapshut
pip3 freeze
pip3 Channels --version
pip3 channels --version
python3 manage.py runserver 0.0.0.0:8000
python3 manage.py runserver 0.0.0.0:443
sudo python3 manage.py runserver 0.0.0.0:443
clear
cd ..
cd scrapshut
ls
source ss-env/bin/active
source ss-env/bin/activate
pip3 freeze > file.log
nano file.log
pip install -r requirements.txt
cd scrapshut
ls
cd ..
rm scrapshut
ls

sudo python3 manage.py runserver 0.0.0.0:443
sudo apt-get purge nginx nginx-common
sudo apt-get autoremove
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
deactivate
clear
sudo nano /etc/apache2/sites-available/000-default.confsudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
lear
clear
sudo nano /etc/apache2/sites-available/000-default.conf
cd ..
cd /home/ubuntu
cd /home/ubuntu/scrapshut
sudo systemctl restart apache2
sudo apache2ctl configtest
cdmod 777
chown 777
chown 777 ss
sudo apache2ctl configtest
cd ..
sudo chown 777 scrapshut
sudo apache2ctl configtest
cd scrapshut
sudo systemctl stop apache2
sudo python3 manage.py runserver 0.0.0.0:80
screen
ls
cd scrapshut
gunicorn3 --bind 0.0.0.0:8000 ss.wsgi
clear
sudo nano /etc/systemd/system/gunicorn.service
ls
screen -r
