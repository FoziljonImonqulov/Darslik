FROM python:3.11-alpine

WORKDIR apps/
COPY  . .
RUN pip install -r req.txt
CMD python3 main.py

RUN sed -i 's/\r$//g' /apps/entrypoint.sh
RUN chmod +x /apps/entrypoint.sh
ENTRYPOINT ["/apps/entrypoint.sh"]


