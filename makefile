build: 
	apt-get update && apt-get install -y --no-install-recommends libxmlsec1-dev
	pip install --upgrade pip && pip install -r requirements.txt
train: 
	rm -rf ./models/*
	rasa train
interactive:
	make train
	rasa interactive
shell:
	make train
	rasa shell
formatter:
	black --verbose --config pyproject.toml actions tests