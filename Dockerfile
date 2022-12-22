FROM node:12 as build
WORKDIR /app
COPY webui /app
RUN npm ci
RUN npm run build

FROM node:18 as build-mobile
WORKDIR /app
COPY prismarine-mobile /app
ENV PUBLIC_URL /mobile
RUN npm ci
RUN npm run build

FROM python:3.8-alpine
RUN apk add ffmpeg nginx
RUN mkdir /app
WORKDIR /app
COPY --from=build /app/dist /app/static
COPY --from=build-mobile /app/build /app/static/mobile
COPY main.py ./
COPY prismarine prismarine
COPY requirements.txt .
COPY application.yml .
COPY deploy/docker/nginx.conf /etc/nginx/nginx.conf
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENV PYTHONPATH /app


RUN addgroup -S prismarine
RUN adduser \
    --disabled-password \
    --ingroup prismarine \
    prismarine
RUN chown -R prismarine:prismarine /var/lib/nginx
RUN chown -R prismarine:prismarine /var/log/nginx
RUN chown -R prismarine:prismarine /run/nginx
USER prismarine:prismarine

EXPOSE 5000
CMD ["/bin/sh", "-c", "nginx & gunicorn --bind=unix:/tmp/gunicorn.sock --workers=1 --threads=4 main:app --timeout 400"]
#CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=1", "--threads=4","--timeout=400", "main:app"]