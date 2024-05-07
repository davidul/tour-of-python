FROM python

RUN pip install --upgrade pip
RUN set -eux && pip install --no-cache-dir flake8 && pip install --no-cache-dir mypy
RUN pip install black
