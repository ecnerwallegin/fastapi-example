docker build --tag fastapi-example --file Dockerfile.dev . &&
docker run \
  --name fastapi-example \
  --rm -it \
  --env-file .env \
  -p 5603:80 \
  -v ${PWD}/app:/app/app:Z \
  fastapi-example
