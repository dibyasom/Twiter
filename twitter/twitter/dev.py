'''
Loads configurations from environment vairables for running django-app in dev mode.
'''

import environ
import os


# Create django-environ config.
env = environ.Env(
    DEBUG=(bool, False)
)

# Set the project base directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(base_dir, 'twitter/.env'))

'''
Load local db config. (postgres container)
'''
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("DATABASE_NAME"),
#         "USER": env("DATABASE_USER"),
#         "PASSWORD": env("DATABASE_PASSWORD"),
#         "HOST": env("DATABASE_HOST"),
#         "PORT": env("DATABASE_PORT"),
#     }
# }

secret_key = env("SECRET_KEY")