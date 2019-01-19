FROM python:3-onbuild
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTONPATH}:./"
CMD ["python", "runserver.py"]
