FROM tiangolo/uwsgi-nginx-flask

# Create app directory
WORKDIR /usr/src/app


COPY app2.py .

EXPOSE 5000
CMD [ "python", "app2.py" ]
