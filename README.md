<p align="center">
  <img width="200" src="https://github.com/CodeAtCode/piggyprompt/blob/main/static/logo.png">
</p>

# PiggyPrompt - The Trusty Vault for Your AI Prompts

## Install and run

```
pip install -r requirements.txt
streamlit run piggyprompt.py
```

## Set an application password

- Generate a bcrypt hashed password, you can use the following method:
  - Visit https://www.bcrypt-generator.com/ or https://bcrypt-generator.com/
  - Enter your desired password and click "Generate".
- Rename the .env.example file as .env
- Uncomment the HASHED_PASSWORD variable by removing the ```#``` symbol at the start of the line
- Copy the generated hash and place it in the variable
- Restart the app
