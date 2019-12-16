PROJECT = potado
ID = pikesley/${PROJECT}

all: build

build:
	docker build \
		--tag ${ID} .

run:
	docker run \
		--volume $(shell pwd)/potado:/opt/potado \
		--interactive \
		--tty \
		--rm \
		${ID} \
		bash
