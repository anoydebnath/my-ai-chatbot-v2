# Pharmaceutical Knowledge Reconstruction Engine

FULL_DOC_WORDS=[
'complete','entire','whole','everything',
'guideline','manual','detailed'
]

def detect_intent(query):

    q=query.lower()

    score=sum(word in q for word in FULL_DOC_WORDS)

    return 'document' if score>=2 else 'question'
