"""
Django settings for apis_service_center project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

settings.py を settings/base.py にリネームしたもの.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 一段深くしたので
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(0m7o&l@4whs6tq1p03ra#u_dn^@9*v-a&e&_+vh1=dtj-dxvr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'community.apps.CommunityConfig',
    'unit_data.apps.UnitDataConfig',
    'deal.apps.DealConfig',
    'downtime.apps.DowntimeConfig',
    'api.apps.ApiConfig',
    'monitoring.apps.MonitoringConfig',
    'apis_log.apps.ApisLogConfig',
    'scenario.apps.ScenarioConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

####

AUTH_USER_MODEL = 'core.User'
LOGIN_REDIRECT_URL = 'admin:index'
LOGOUT_REDIRECT_URL = 'admin:index'
#LOGIN_URL = 'admin:login'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# メールを送信する代わりにコンソールに表示するダミーのバックエンド
# 運用環境では 'django.core.mail.backends.smtp.EmailBackend' とするべし
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
# EMAIL_HOST_USER = 'someuser'
# EMAIL_HOST_PASSWORD = 'somepassword'
# EMAIL_USE_TLS = False

# Default email address to use for various automated correspondence from the site manager(s). This doesn’t include error messages sent to ADMINS and MANAGERS; for that, see SERVER_EMAIL.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = 'root@localhost'

# A list of all the people who get code error notifications. When DEBUG=False and AdminEmailHandler is configured in LOGGING (done by default), Django emails these people the details of exceptions raised in the request/response cycle.
ADMINS = [
	('dummy', 'nobody@example.com'),
]

# A list in the same format as ADMINS that specifies who should get broken link notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = [
	('dummy', 'nobody@example.com'),
]

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'console': {
			'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		},
		'file': {
			'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		},
	},
	'handlers': {
		'console': {
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
			'formatter': 'console',
		},
		'file': {
			'level': 'WARNING',
			'class': 'logging.FileHandler',
			'formatter': 'file',
			'filename': '/tmp/apis-service_center-warning.log',
		},
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html': True,
		},
	},
	'loggers': {
		'': {
			'level': os.getenv('ROOT_LOG_LEVEL', 'DEBUG'),
			'handlers': ['file', 'console', 'mail_admins'],
		},
		'django': {
			'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
			'handlers': ['file', 'console', 'mail_admins'],
			'propagate': False,
		},
	},
}

#### カスタム設定項目

# MongoDB 用のデータベース設定
MONGODB_DATABASES = {
    'downtime' : {
        'HOST': 'localhost',
        'NAME': 'apis_service_center',
    },
    'unit_data' : {
        'HOST': 'localhost',
        'NAME': 'apis_service_center',
    },
    'deal' : {
        'HOST': 'localhost',
        'NAME': 'apis_service_center',
    },
    'apis_log' : {
        'HOST': 'localhost',
        'NAME': 'apis_service_center',
    },
}

# downtime 集計処理の諸設定
DOWNTIME = {
	'initial_wait_sec': 5,
	'interval_sec': 300,
	'unit_data_fetch_limit': 1000,
	'data_loss_tolerance_sec': 600,	# 実機:120, emulation:600
}

# monitoring 処理の諸設定
MONITORING = {
	'initial_wait_sec': 5,
	'interval_sec': {
		'apis_main_alive': 60,	# 運用:300
		'apis_ccc_alive': 60,
		'grid_master_alive': 60,
		'apis_main_severe': 60,
		'apis_ccc_severe': 60,
		'apis_log_severe': 60,
	},
	'thread_blocking_limit_msec': 300000,
	'notify_from': 'nobody@example.com',
	'default_notify_to': 'nobody@example.com',
}
