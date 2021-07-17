# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '158^+4g%rah-@zo+m49dk(atmfw7l-rdo84x$4k3+&aij$hx0k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'socialdb',
        'USER': 'social_event',
        'PASSWORD': 'Social_event',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
