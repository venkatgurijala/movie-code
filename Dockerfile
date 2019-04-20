FROM centos:7
RUN mkdir venkat
COPY ./test.py /venkat/test.py
RUN yum install centos-release-scl -y
RUN yum install rh-python36 -y
RUN scl enable rh-python36 bash
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install requests
ENTRYPOINT ["top", "-b"]
CMD ["-c"]