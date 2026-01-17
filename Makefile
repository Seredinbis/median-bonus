up:
	@docker image prune -f
	@docker compose up --build