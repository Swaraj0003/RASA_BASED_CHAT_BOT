🤖 Rasa Conversational AI Project

This repository contains the full setup for a Rasa-based conversational assistant, including training data, NLU configuration, custom actions, and deployment settings. The project is designed to be modular, scalable, and easy to extend as your chatbot grows in functionality.





├── data/               # Training data: NLU examples, stories, rules

├── models/             # Trained models (auto-generated after training)

├── actions/            # Custom action server code (Python)

├── config.yml          # NLU pipeline, policies, and ML model configuration

├── domain.yml          # Intents, entities, slots, responses, and actions

├── credentials.yml     # Credentials for connecting to messaging platforms

├── endpoints.yml       # Action server & tracker store configuration

├── tests/              # Test stories for automated conversation tests

└── README.md           # Project overview and setup instructions


This project implements a conversational AI assistant using Rasa Open Source. It includes training data for NLU and dialogue management, along with custom actions and configuration files required to run and test the bot.

 Features

Natural Language Understanding (intent classification & entity extraction)

Dialogue management through stories and rules

Custom Python actions for dynamic responses

Support for multiple messaging channels

Easy-to-train and extend architecture

Automated tests for conversation flows


git clone <your-repo-url>
cd <project-folder>

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt




