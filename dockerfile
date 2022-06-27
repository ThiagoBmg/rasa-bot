# NB! when updating make sure the version is in sync with:
# * rasa version in requirements.txt
# * RASA_VERSION and RASA_X_VERSION  in .github/workflows/continuous-deployment.yml
# Pull SDK image as base image
FROM rasa/rasa:3.2.1

# Use subdirectory as working directory
WORKDIR /app

# Copy actions requirements
COPY requirements.txt ./

# Change to root user to install dependencies
USER root

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  python3 \
  python3-venv \
  python3-pip \
  python3-dev \
  # required by psycopg2 at build and runtime
  libpq-dev \
  libxmlsec1-dev \
  # required for health check
  curl \
  && apt-get autoremove -y

# Make sure that all security updates are installed
RUN apt-get update && apt-get dist-upgrade -y --no-install-recommends

# Install extra requirements for actions code
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy actions code to working directory
COPY . /app
# COPY ./../config /app/config

# Install modules from setup.py
COPY readme.md /app

# Download spacy language data
# RUN python -m spacy download pt_core_news_lg

# Don't use root user to run code
USER 1001
# rasa run --endpoints endpoints.yml -p 8000 --cors "*" --auth-token 0d0a3081bfff925160bbbe9755ad8c196ab51414
# Start the action server
CMD ["run", "--endpoints","endpoints.yml","-p", "5000", "--cors", "*", "--auth-token","0d0a3081bfff925160bbbe9755ad8c196ab51414"]
