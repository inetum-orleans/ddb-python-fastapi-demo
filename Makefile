init: dc-build dc-up install

dc-build:
	docker compose build

dc-up:
	docker compose up -d

install: 
	poetry install

watch:
	uvicorn main:app --host 0.0.0.0 --reload