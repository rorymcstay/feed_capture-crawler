FROM selenium/node-chrome:3.141.59-20200326

USER root
RUN apt-get update && \
 apt-get -y install python3-pip

RUN apt-get update && \
 apt-get -y install git
#===================================
# Application files
#===================================
RUN mkdir -p /usr/capture-crawler

WORKDIR /usr/capture-crawler

ADD requirements.txt ./requirements.txt

#RUN python -m pip install pip
RUN which python
RUN python3 -m pip install -r ./requirements.txt


#====================================
# generate a hosts file which blocks
# adds to improve performance
#====================================
RUN git clone https://github.com/StevenBlack/hosts.git hosts_file_gen
RUN cd hosts_file_gen && python3 -m pip install -r ./requirements.txt && python3 updateHostsFile.py --auto --replace && cd /usr/capture-crawler

# Installing packages
# Copying over necessary files
COPY src ./src
COPY capture-crawler.py ./app.py

#====================================
# Scripts to run Selenium Standalone
#====================================
COPY start-selenium-standalone.sh /opt/bin/start-selenium-standalone.sh
RUN chmod +x /opt/bin/start-selenium-standalone.sh


USER seluser
#==============================
# Supervisor configuration file
#==============================
COPY selenium.conf /etc/supervisor/conf.d/



# Entrypoint
CMD ["python3", "/usr/capture-crawler/app.py", "--start-browser"] 

