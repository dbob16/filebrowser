FROM python:3.12.3
RUN pip install --no-cache-dir --upgrade "fastapi[standard]"
WORKDIR /code
COPY ./app.py /code/app.py
COPY ./templates /code/templates
EXPOSE 80
CMD ["fastapi", "run", "app.py", "--proxy-headers", "--port", "80"]