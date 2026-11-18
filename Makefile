.PHONY: help lint test build run tf-fmt

IMAGE ?= platform-api
TAG   ?= dev

help:
	@grep -E '^[a-zA-Z_-]+:.*' Makefile | cut -d: -f1

lint:
	cd apps/api && ruff check .

test:
	cd apps/api && pytest -q

build:
	docker build -t $(IMAGE):$(TAG) apps/api

run:
	docker run --rm -p 8000:8000 $(IMAGE):$(TAG)

tf-fmt:
	terraform fmt -recursive infra
