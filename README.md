# Kieren Coetzee's Personal Website
> personal website

## Installation

### Requirements
> these requirements are tested on debain10 using default versions

```
- git
- python>=3.6
- python3-venv
- python3-dev
- libssl-dev
- nginx
- supervisor
```

### Clone the repository
```
cd /srv
sudo mkdir kierencoetzee
cd kierencoetzee
sudo git clone https://github.com/carderbeeuk/kierencoetzee.git .
```

### Add and update permissions
```
sudo groupadd developers
sudo usermod -a -G developers {developer_name}
sudo chown -R kieren:developers /srv/kierencoetzee
```

### Create the virtual environment and install dependencies
```
cd /srv/kierencoetzee

python3 -m venv venv
. venv/bin/activate

pip install wheel
pip install -r requirements.txt
```

### Set up the config
```
cd /srv/kierencoetzee
nano kierencoetzee/settings_private.py
```

add the following keys, these will be used throughout the application

```
# App environment
APPLICATION_ENV = 'production'

# Django common
DJANGO_SECRET_KEY = '***'
DJANGO_DEBUG = 0
DJANGO_ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'kierencoetzee.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kierencoetzee',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Static
# This is where django will store all static stuff like css and js files
STATIC_ROOT = '/srv/kierencoetzee/static/'
MEDIA_ROOT = '/srv/kierencoetzee/media/'
```

generate a secret key like so

```
python -c "import secrets; print(secrets.token_urlsafe())"
```

### Initialize the database
```
sudo -u postgres createdb kierencoetzee
sudo -u postgres createuser kieren
sudo -u postgres psql -c "grant all privileges on database kierencoetzee to kieren"
sudo -u postgres psql -c "alter database kierencoetzee owner to kieren"

# su postgres
# psql
ALTER USER kieren WITH ENCRYPTED PASSWORD '****';
ALTER USER kieren CREATEDB;

# su kieren
cd /srv/kierencoetzee
. venv/bin/activate
python manage.py makemigrations authors blog
python manage.py migrate
python manage.py collectstatic
```

### Create a django superuser
```
cd /srv/kierencoetzee
. venv/bin/activate
python manage.py createsuperuser
```

### Running the application
set up the supervisor config in `/etc/supervisor/conf.d/kierencoetzee.conf`
```
[program:kierencoetzee]
directory=/srv/kierencoetzee
command=/srv/kierencoetzee/venv/bin/gunicorn --workers 2 --timeout 300 --bind 127.0.0.1:8040 kierencoetzee:wsgi
user=kieren
autostart=true
autorestart=true
stdout_logfile=/srv/kierencoetzee/logs/gunicorn.log
stderr_logfile=/srv/kierencoetzee/logs/gunicorn-error.log
```

### Serving the app using nginx
set up for nginx in `/etc/nginx/sites-available/kierencoetzee.com.conf`
```
server {
    listen 80;
    server_name kierencoetzee.com;

    location / {
        proxy_pass http://localhost:8040;
    }

    location /static/ {
        root /srv/kierencoetzee;
    }
}
```
set site enabled
```
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/kierencoetzee.com.conf
```

### Setting up SSL
follow instrunctions here:
https://certbot.eff.org/lets-encrypt/debianbuster-nginx