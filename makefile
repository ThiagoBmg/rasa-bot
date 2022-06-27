build: 
# apt-get update && apt-get install -y --no-install-recommends libxmlsec1-dev
	pip install --upgrade pip && pip install -r requirements.txt
	pip install pip install black
	python -m spacy download pt_core_news_lg
api:
	make train
	rasa run --endpoints ./endpoints/local.yml -p 8000 --cors "*" --auth-token 0d0a3081bfff925160bbbe9755ad8c196ab51414
train: 
	rm -rf ./models/*
	rasa train --config ./config/config-whiteSpace.yml --endpoint /endpoints/local.yml
interactive:
	make train
	rasa interactive --config ./config/config-whiteSpace.yml
shell:
	make train 
	rasa shell --config ./config/config-whiteSpace.yml
# test: 
# 	rasa test core --stories ./tests/test_faq.yml --out results
formatter:
	black --verbose --config pyproject.toml actions tests
# delete: 
# 	docker kill $(docker ps -a -q)
# 	docker rm $(docker ps -a -q)
# 	docker rmi $(docker images -q)
