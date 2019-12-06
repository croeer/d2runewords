FROM python:2.7
RUN pip install Flask jsonpickle
RUN useradd -ms /bin/bash admin
USER admin
COPY finder.py  server.py ./
CMD ["python", "server.py"]

