FROM python:3.10

COPY main.py utils.py transform.py exctract_air_pollution.py requirement.txt ./

COPY data ./data

COPY doc ./doc

RUN pip install -r requirement.txt

RUN pip install psycopg2

CMD ["python", "./main.py"]
