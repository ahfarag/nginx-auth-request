docker:
	docker build -t nginx-auth-request-web web/.
	docker build -t nginx-auth-request-api api/flask/.

run:
	docker-compose up