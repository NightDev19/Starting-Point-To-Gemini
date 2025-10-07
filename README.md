# Gemini CLI Project

This project is a simple **command-line interface (CLI)** for interacting with the Google Gemini API using Python.
It includes a basic chatbot interface, automated tests with `pytest`, and a GitHub Actions CI workflow.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [GitHub Actions CI](#github-actions-ci)
- [Secrets Management](#secrets-management)
- [Requirements](#requirements)

---

## Features
- Interactive command-line chatbot using Gemini API
- Secure API key management with `.env` or GitHub Secrets
- Automated testing with `pytest`
- Continuous Integration with GitHub Actions

---

## Prerequisites
- Python 3.13
- Git
- Google Gemini API Key
- GitHub account (for CI integration)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NightDev19/Starting-Point-To-Gemini.git
cd Starting-Point-To-Gemini
```
2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Create .env file for local development:
```
touch .env
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

# Usage
Run the interactive CLI:
```
python main.py
```
Example session:
```
💬 Gemini CLI — type 'exit' to quit
You: Explain AI in simple words
Gemini: AI is the science of making machines learn and perform tasks that usually require human intelligence.
You: exit
Exiting Gemini CLI.
```
## Testing
Run automated tests with:
```
pytest
```
