FROM python:3.11-alpine

WORKDIR bot/
COPY  . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requests.txt

RUN sed -i 's/\r$//g' /bot/entrypoint.sh
RUN chmod +x /bot/entrypoint.sh
ENTRYPOINT ["/bot/entrypoint.sh"]


