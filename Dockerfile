FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install python3-dev build-essential make gcc
RUN apt-get -y install gfortran
RUN apt-get -y install musl-dev
RUN ln -s /lib/aarch64-linux-musl/libc.so /lib/libc.musl-aarch64.so.1
RUN /usr/local/bin/python -m pip install flask uWSGI
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "app/app.ini"]