FROM python:3.10-alpine AS compile-image
RUN apk update && apk add python3-dev gcc libc-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN mkdir /buildtmp
COPY . /buildtmp
RUN pip install /buildtmp

FROM python:3.10-alpine AS build-image
COPY --from=compile-image /opt/venv /opt/venv
COPY cross_monitor_bot/ /app
RUN mkdir -p /opt/cross_monitor_bot

WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH"
CMD ["python", "-m", "cross_monitor_bot.run", "-c", "/opt/cross_monitor_bot/config.py"]

#docker build -t cross_monitor_bot:latest .
#docker run -d --mount type=bind,source=/opt/cross_monitor_bot,target=/opt/cross_monitor_bot cross_monitor_bot
