# Triathlon HPP Telegram Bot

## Overview

As athletes, our main responsibility is to show up at competitions and give it our all. One of the most annoying things I have to do as a triathlete is read through thick documents to derive specific information. Even more annoyingly, sometimes I have to piece together information from many pages apart to get a complete picture of my query. Two years ago, I won a National Championship race in cycling. However, due to document technicalities (such as needing a UCI License, which triathletes typically do not purchase) I didn't read, I was unable to wear the National Champion Jersey.

A week ago, I stumbled across the concept of Retrieval-Augmented Generation (RAG) while exploring algorithms for Question-Answering tasks in Natural Language Processing. The idea behind it is straightforward: you split a document into chunks, embed each chunk into vector embeddings, and store them in vector databases. When you receive input from a user, you embed the input and find the top-k chunks (your context) that are most similar to the embedded input. Then, you engineer a prompt using the context and feed it into a Large Language Model (LLM), which helps collate the necessary information across the document and present it in an organized form.

With this knowledge, I built a Telegram bot based on the Triathlon Association of Singapore's High Performance Programme (HPP) Document, which is provided to us athletes at the start of every year. I was astonished by how powerful the LLMs are in handling my queries on the HPP.

## Features

- **Retrieval-Augmented Generation (RAG)**: Efficiently retrieves relevant document sections and generates coherent responses.
- **Large Language Model (LLM)**: Utilizes the Claude-Instant model by Anthropic for accurate and context-aware answers.
- **Telegram Integration**: Provides a user-friendly interface for athletes to interact with the bot and get instant responses.
- **AWS Ecosystem**: Deployed using AWS Bedrock for generating embeddings and hosted on AWS EC2.

## Tech Stack

- **Backend**: Python
- **Machine Learning**: RAG, Claude-Instant model by Anthropic
- **Data Storage**: Chroma Vector database
- **Deployment**: AWS Bedrock, AWS EC2
- **Messaging Platform**: Telegram

## Installation

1. Launch an instance of Amazon EC2 and clone the repository onto Amazon EC2:
   ```bash
   git clone https://github.com/your-username/triathlon-hpp-telegram-bot.git
   cd triathlon-hpp-telegram-bot

2. Install python, pip and the required packages
   ```bash
   sudo yum install -y python
   sudo yum install -y python-pip
   pip install -r requirements.txt
   
3. Run the bot
   ```bash
   sudo yum install tmux -y
   tmux new -s telegram_bot
   python create_db.py
   python main.py

The bot is now hosted on Amazon EC2!


   
