build: 
	apt-get update && apt-get install -y --no-install-recommends libxmlsec1-dev
	pip install --upgrade pip && pip install -r requirements.txt
	python -m spacy download pt_core_news_lg
api:
	make train
	rasa run --endpoints endpoints.yml -p 8000 --cors "*" --auth-token 0d0a3081bfff925160bbbe9755ad8c196ab51414
train: 
	rm -rf ./models/*
	rasa train --config ./config/config-whiteSpace.yml
interactive:
	make train
	rasa interactive --config ./config/config-whiteSpace.yml
shell:
	make train 
	rasa shell --config ./config/config-whiteSpace.yml
test: 
	rasa test core --stories ./tests/test_faq.yml --out results
formatter:
	black --verbose --config pyproject.toml actions tests
# api test:
# 	curl -X POST -H "Content-Type: application/json" -d '{"sender": "test_user","message": "qual é seu nome?"}' http://localhost:8000/webhooks/rest/webhook
# python -m spacy download pt_core_news_sm

# rasa train --config ./config/config-whiteSpace.yml
