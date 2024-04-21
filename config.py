from decouple import config


class Config:
    CELERY_BROKER_URL = config('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')


class DevelopmentConfig(Config):
    DEBUG = True


configuration = {
    'development': DevelopmentConfig,
    'production': Config
}
