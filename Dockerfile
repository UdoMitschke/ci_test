# Base image
FROM python:latest

RUN sleep 15

RUN pip install pandas

RUN sleep 20

# copy lambda settings
RUN mkdir all_folder
COPY all_folder all_folder
RUN chmod 755 -R all_folder

CMD ["python3", "--version"]