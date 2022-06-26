build: 
	apt-get update && apt-get install -y --no-install-recommends libxmlsec1-dev
	pip install --upgrade pip && pip install -r requirements.txt
	python -m spacy download pt_core_news_lg
api:
	make train
	rasa run --endpoints endpoints.yml -p 8000 --cors "*"
train: 
	rm -rf ./models/*
	rasa train --config ./config/config-spacyNPL.yml
interactive:
	make train
	rasa interactive
shell:
	make train 
	rasa shell
formatter:
	black --verbose --config pyproject.toml actions tests
# api test:
# 	curl -X POST -H "Content-Type: application/json" -d '{"sender": "test_user","message": "qual é seu nome?"}' http://localhost:8000/webhooks/rest/webhook
# python -m spacy download pt_core_news_sm