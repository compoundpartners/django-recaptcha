DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite',
    }
}

INSTALLED_APPS = [
    'recaptcha',
]

RECAPTCHA_PRIVATE_KEY = 'privkey'
RECAPTCHA_PUBLIC_KEY = 'pubkey'
