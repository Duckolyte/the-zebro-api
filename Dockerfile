FROM python:3

ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

RUN python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run" ]