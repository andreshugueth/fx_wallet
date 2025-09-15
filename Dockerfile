FROM python:3.12.4

WORKDIR /urc/src/app


COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000

