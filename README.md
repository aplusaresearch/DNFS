# Docker: Nginx + Flask + SSL

This is a simple example of how to use Nginx as a reverse proxy with SSL for a Flask app.

## Usage

### Create a self-signed certificate

On a linux machine, you can create a self-signed certificate using the following command:

```bash
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout server.key -out server.crt
```
 Then, create a pem file:
```bash 
    openssl dhparam -out server.pem 4096
```

Place them in the `ssl` folder.

### Update the conf files with your domain

There is an example for HTTP and HTTPS configurations in the `nginx` folder.

Replace `localhost` with your domain in the following files:
- `nginx/nginx-https.conf`
- `nginx/nginx-http.conf`

Also, update the conf files in the `snippets` folder and the `docker-compose.yml`
file,  according to your created ssl files.

### Start the project

```bash
docker compose up -d
```

### Access the app

Open your browser and go to [https://localhost](https://localhost).  
Tot test the HTTP version, go to  [http://localhost](http://localhost).  
It should be redirecting to the HTTPS version. If not, clear your browser cache.

### Stop the project

```bash
docker compose down
```