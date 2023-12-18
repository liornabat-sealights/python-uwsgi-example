# python-uwsgi-example

## Install

```bash
pip install uwsgi
pip install Flask
pip install sealights-python-agent
```

## Scan

```bash
sl-python config --appname python-uwsgi-example --tokenfile ./sltoken.txt
sl-python scan
```

## Run

```bash
uwsgi --http 0.0.0.0:9092 --module app:APP --enable-threads  --master --single-interpreter --import python_agent.init
```
