def build_prompt(query,context):

    return f'''
You are a Pharmaceutical Knowledge Reconstruction Engine.

Rules:

- Do not summarize.

- Do not invent information.

- User should not need original PDF.

Context:

{context}

Question:

{query}
'''
