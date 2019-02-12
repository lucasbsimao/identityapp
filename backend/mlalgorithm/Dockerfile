FROM tensorflow/tensorflow:1.12.0-gpu-py3

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install Flask

EXPOSE 5000

CMD ["python3", "server.py"]