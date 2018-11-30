FROM kennethreitz/pipenv

WORKDIR /app
COPY . /app
RUN pipenv install

CMD [ "pipenv", "run", "python", "/app/mypluging/plugin/main.py" ]