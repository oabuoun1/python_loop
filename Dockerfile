FROM python:3
RUN pip3 install netifaces
ADD my_script.py /
RUN mkdir /mydata
RUN echo "hello world" > /mydata/greeting
CMD [ "python3", "./my_script.py" ]