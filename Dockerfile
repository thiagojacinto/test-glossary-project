# 
FROM python:3.10

# 
WORKDIR /app

# 
COPY ./prod-requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./testglossary /app/testglossary

# 
CMD ["uvicorn", "testglossary.main:app", "--host", "0.0.0.0", "--port", "80"]