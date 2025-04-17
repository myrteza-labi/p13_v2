import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # permet à Sentry de continuer à capter
    'formatters': {
        'simple': {
            'format': '[{levelname}] {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'level': 'WARNING',  # le niveau global par défaut
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'lettings': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'profiles': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
