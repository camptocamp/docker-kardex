from python:3.7

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
COPY entrypoint.py /entrypoint.py
COPY kardex-proxy.py /kardex_proxy.py
ENTRYPOINT ["python3.7", "/entrypoint.py"]

