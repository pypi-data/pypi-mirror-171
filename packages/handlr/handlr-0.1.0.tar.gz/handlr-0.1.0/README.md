# Handlr | Without the 'e' #

##### Created by [Joe Tilsed](http://JoeTilsed.com) | Created 11/10/2022 | Last Updated: 11/10/2022 | Current Version: 0.1.0

Handlr is a Python handler to logging services, i.e. Logstash as part of the ELK stack.

## How to install
Simply run: `pip install handlr`.

## How to use
An example would be to use this package for a logstash as part of the ELK stack.

```python
import logging

from handlr import Handler

LOGGER_ENDPOINT = 'localhost'
LOGGER_PORT = 5040
LOG_LEVEL = 'DEBUG'
LOG_LABEL = 'VM_123ABC'
LOG_TAGS = ['virtual-machine', 'workers', 'EMEA']

log = logging.getLogger(__name__)
handler = Handler(LOGGER_ENDPOINT, LOGGER_PORT, LOG_LABEL, LOG_TAGS)
log.addHandler(handler)

# If you don't want the logs being shown to the console (aka only shown on ELK stack) then remove the below line.
log.addHandler(logging.StreamHandler())

log.setLevel(LOG_LEVEL)
log.info(f"Setup log, log level {LOG_LEVEL}. Sending logs to {LOGGER_ENDPOINT}:{LOGGER_PORT}.")
```

Enjoy!

<br />

###### # That's all folks...
