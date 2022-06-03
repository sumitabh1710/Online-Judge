FROM python

WORKDIR D:\Code\Django\Onlinejudge

COPY temp.py ./

CMD ["python", "temp.py"]

