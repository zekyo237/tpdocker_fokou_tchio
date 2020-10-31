FROM python:3.6
RUN mkdir /src/application/
COPY . /src/application/
WORKDIR /src/application/
EXPOSE 5000
RUN pip install -r requis.txt
CMD["python","application.py"]