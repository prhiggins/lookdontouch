FROM python:3.9-slim as builder
WORKDIR /app

RUN apt-get update
RUN apt-get install -y --no-install-recommends git

# Set up virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

FROM python:3.9-slim as app
COPY ./app .

# copy and config virtualenv
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
ENTRYPOINT [ "flask" ]
CMD [ "run" ]