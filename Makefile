CMD=docker compose

clean:
	@docker image prune -f

up: clean
	@$(CMD) --profile deploy up --build

test: clean
	@$(CMD) --profile test up --build
