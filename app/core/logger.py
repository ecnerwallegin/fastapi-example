import logging

# Configure logging
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
		"default": {
			"format": "%(asctime)s %(levelname)-8s %(name)s %(message)s",
			"datefmt": "[%Y-%m-%d %H:%M:%S%z]"
		},
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s %(levelname)-8s %(client_addr)s REQUEST: "%(request_line)s" %(status_code)s',
            "datefmt": "[%Y-%m-%d %H:%M:%S%z]",
			"use_colors": False
        },
    },
    "handlers": {
		"default": {
			"formatter": "default",
			"class": "logging.StreamHandler",
			"stream": "ext://sys.stdout",
		}
    },
    "loggers": {
		"": {
			"handlers": ["default"],
			"level": "INFO"
		},
        "uvicorn.access": {
            "handlers": [],
            "level": "INFO",
            "propagate": False
        }
    },
})

logger = logging.getLogger()
