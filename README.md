# NW AI Gen

This is an experimental playground for testing Python + LangChain to utilize generative AI (specifically OpenAI ChatGPT).

Future improvements would be:
- Optimize the proompting.
- Use embeddings and possible vector DB integration.
- Sanity check community-based generative AI against editorial expert content for correctness (new chain step?).
- RAG-ify: utilize querying expert content during generation.

### Running Locally
Setup the dockerized environment.
* MySQL database.

This is intended to store simplified community and expert data in a database.
```sh
docker compose up
```

Setup your environment variables in a local `.env` file.
```
OPENAI_API_KEY="YOUR_KEY"
```

Install dependencies.
```sh
pip install -r requirements.txt
```

Run the command line application.
```sh
python src/main.py
```