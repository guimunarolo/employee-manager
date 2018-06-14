IMAGE = employee-manager:latest
CONTAINER = employee-manager
MANAGECMD = docker exec -it $(CONTAINER)

build: ## Build the container
	docker build --tag $(IMAGE) .
	docker stop $(CONTAINER) || true && docker rm $(CONTAINER) || true
	docker run -dit --name $(CONTAINER) -v $(shell pwd):/app -p 8000:8000 $(IMAGE) /bin/bash
	$(MANAGECMD) /bin/bash -c "python manage.py loaddata user.json"
test: ## Run tests
	$(MANAGECMD) python manage.py test --settings=app.test

restart: ## Restart the container
	docker restart $(CONTAINER)

cmd: ## Access bash
	$(MANAGECMD) /bin/bash

up: ## Start container
	docker restart $(CONTAINER)
	$(MANAGECMD) /bin/bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

down: ## stop container
	docker stop $(CONTAINER)
