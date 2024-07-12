# Dell Poweredge (R720XD) Nvidia Fancontrol

This repository contains a Python script designed to monitor Nvidia GPU temperatures and dynamically adjust the fan speeds. Tested and used on a Dell PowerEdge R720xd server, 
the fans are controlled using the IPMI protocol.

## Enable IPMI on your Dell Server

You have first to enable the IPMI feature on your Dell server this is done in the IDRAC settings. This is needed to be able to communicate with the fans using the IPMI protocol.
In the IPMI protcol to be able to communicate you havet to set a digit key, the default is all zeros **(YOU SHOULD CHANGE THIS)**

## Run the Script 

The steps below show you how to run the script

1. Open a terminal window and navigate to the repo folder
2. install the required dependencies as follows ```pip install -r requirements.txt```
3. modify the parameters in **/lib/ipmi_command.py** which are the following below
  - **IPMIHOST**: this is the IP address for the IDRAC
  - **IPMIUSER**: this is the username for the IDRAC login
  - **IPMIPASSWORD**: this is the password for the IDRAC login
  - **IPMIKEY**: this is the IPMI Key
4. run the script as follows ```python main.py```

## how to make the script automatically run by itself

There are various ways to achieve this, I have set up a service that will automatically run when the server starts using **systemctl**, the steps are the following 

1. create the following the service file with name **nvidia-fan-control.service** in **/etc/systemd/system** you can do this as follows, **GIVEN: the current directory is /home/USER** where **USER** is your username for the Linux account
  ```
      sudo touch /etc/systemd/system/Nvidia-fan-control.service
  ```
2. now edit the created service file and add the following data, this will set up the **systemctl** service
```
[Unit]
Description="Fan control based on Nvidia GPUs temperature"
After=multi-user.target

[Service]
Restart=always
ExecStart=PYTHON_EXECUTABLE PATH_TO_REPO_FOLDER/main.py
Type=simple
WorkingDirectory=PATH_TO_REPO_FOLDER
StandardOutput=syslog
StandardError=syslog

[Install]
WantedBy=multi-user.target
```
You have to set the **PYTHON_EXECUTABLE** and **PATH_TO_REPO_FOLDER**

3. update the systemctl daemon using ```sudo systemctl daemon-reload```
4. enable the service using ```sudo systemctl enable Nvidia-fan-control.service```
5. start the service using ```sudo systemctl start nvidia_fan_control```
6. now the service should be up and running which you can check using ```sudo systemctl service nvidia-fan-control.service```

#### logging

The script will automatically log data in **PATH_TO_REPO_FOLDER/logs/fan_control_logs.log** the retention policy is 10 days meaning log data older than 10 days old will be removed by the new log data 

