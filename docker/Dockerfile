FROM cgr.dev/chainguard/python:latest-dev AS builder

ENV PYTHONUNBUFFERED=True
WORKDIR /app
USER nonroot


COPY --chown=nonroot:nonroot pyproject.toml requirements.lock README.md ./
RUN sed -i '/^-e file:/d' requirements.lock
# RUN pip install . --constraint requirements.lock
RUN pip install -r requirements.lock --user

ADD --chown=nonroot:nonroot postmodern ./postmodern/


# FROM cgr.dev/chainguard/python:latest

# WORKDIR /app

# # Make sure you update Python version in path
# COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages

# COPY --from=builder /app/postmodern/memory_example.py /app/postmodern/memory_example.py

ENTRYPOINT [ "python", "/app/postmodern/memory_example.py" ]
