import openai
import os

ENGINE = 'text-davinci-003'
PROMPT_MAX_TOKENS = 2048
MAX_TOKENS = 1000
TEMPERATURE = .5
PROMPT_ENGINEERING = '''
    You will be provided with a sequence of messages. You must answer as the "assistant" with the 
    requested information following these rules:
        - You must answer in the same language as the messages.
        - If the prompt doesn't contain any question or request, just mention that and provide a relevant response.
        - Don't provide an answer for something you weren't asked.
        - Act as if it's a conversation between two people.
        - You must not specify you are giving an 'Answer: '.
'''

openai.api_key = os.getenv('OPENAI_KEY')

def __count_tokens(text: str) -> int:
    token_count = len(text.split()) // 3

    return token_count

def __build_prompt(messages: list) -> str:
    prompt = PROMPT_ENGINEERING + '\n## MESSAGES:\n' + str(messages)

    while __count_tokens(prompt) > PROMPT_MAX_TOKENS:
        prompt = PROMPT_ENGINEERING + '\n## MESSAGES:\n' + str(messages[2:])

    return prompt

def get_completion(messages: list) -> str:
    completion = openai.Completion.create(
        engine=ENGINE,
        prompt=__build_prompt(messages),
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE)
    
    completion = completion.choices[0].text.strip()

    return completion