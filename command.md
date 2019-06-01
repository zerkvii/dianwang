# sudo pkill -f uwsgi -9
---
gunicorn sse:app --worker-class gevent --bind 0.0.0.0:5000