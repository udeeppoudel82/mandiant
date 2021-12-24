FROM ubuntu
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
COPY . /app
WORKDIR /app
RUN mkdir output
RUN chmod 777 output
RUN chmod 777 start.sh
RUN apt-get install pip
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["./start.sh"]
