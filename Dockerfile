FROM python

ENV DIR_HOME /home/xiaocao/boce_ip_test

COPY . $DIR_HOME

WORKDIR $DIR_HOME

RUN pip3 install -r $DIR_HOME/requirements.txt  \
    && apt update -y  \
    && apt-get install libnss3 -y  \
    && apt-get install chromium -y  \
    && python ./run.py