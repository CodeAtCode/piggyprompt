import sqlite3


def init_db():
    conn = sqlite3.connect('prompts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY,
            provider TEXT,
            model TEXT,
            prompt TEXT,
            label TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_prompt(provider, model, prompt, label):
    conn = sqlite3.connect('prompts.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO prompts (provider, model, prompt, label)
        VALUES (?, ?, ?, ?)
    ''', (provider, model, prompt, label))
    conn.commit()
    conn.close()

def load_prompts():
    conn = sqlite3.connect('prompts.db')
    c = conn.cursor()
    c.execute('SELECT provider, model, prompt, label FROM prompts')
    prompts = c.fetchall()
    conn.close()

    organized_prompts = {}
    for provider, model, prompt, label in prompts:
        if provider not in organized_prompts:
            organized_prompts[provider] = {}
        if model not in organized_prompts[provider]:
            organized_prompts[provider][model] = []
        organized_prompts[provider][model].append((prompt, label))  # Store prompt and label as a tuple

    return organized_prompts

def delete_prompt(provider, model, label):
    conn = sqlite3.connect('prompts.db')
    c = conn.cursor()
    c.execute('''
        DELETE FROM prompts
        WHERE provider = ? AND model = ? AND label = ?
    ''', (provider, model, label))
    conn.commit()
    conn.close()
