**Usage**

**#Build Docker file**

sudo docker build -t exercise .

**#run docker image**

sudo docker run -v $(pwd)/output:/output exercise


**cd output**

You will find cves.csv file
