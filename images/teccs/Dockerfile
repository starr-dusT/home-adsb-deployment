FROM python:3

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ./tdcore-1.2.1+5.g2c41d4c-py3-none-any.whl
RUN pip install ./tdtrack-1.9.3-py3-none-any.whl

ENTRYPOINT ["python"]
