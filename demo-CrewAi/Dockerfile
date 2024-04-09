FROM python:3.10.12

WORKDIR /crewai/

COPY ./crewai/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./crewai/ .

CMD ["uvicorn", "main:app", "--root-path", "/crewai/", "--host", "0.0.0.0", "--port", "8005"]