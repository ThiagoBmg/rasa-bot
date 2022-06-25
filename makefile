build: 
	apt-get update && apt-get install -y --no-install-recommends libxmlsec1-dev
	pip install --upgrade pip && pip install -r requirements.txt
train: 
	rm -rf ./models/*
	rasa train && rasa interactive