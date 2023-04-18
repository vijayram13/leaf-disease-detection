# to suggest the treatment using CHATGPT

import openai
openai.api_key = "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"  # Replace with your API key
engine = "text-davinci-003"

#engine = "davinci"


def treatment(text):
    completions = openai.Completion.create(
        engine=engine,  # Replace with the name of the OpenAI engine you want to use
        prompt= f"Treatment for :\n{text}\n",
        temperature= 0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    message = completions.choices[0].text.strip()
    #print(message)
    return message


def translator(text, language):
    completions = openai.Completion.create(
        engine=engine,  # Replace with the name of the OpenAI engine you want to use
        prompt= f"Translate the following text into {language}:\n{text}\nOutput:",
        temperature= 0.9,
        max_tokens=1025,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    message = completions.choices[0].text.strip()
    #print(message)
    return message


def ask_question(text):
    completions = openai.Completion.create(
        engine=engine,  # Replace with the name of the OpenAI engine you want to use
        prompt=text,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    message = completions.choices[0].text.strip()
    #print(message)
    return message
if (__name__ =="__main__"):
    import sys
    print(sys.version)
    prompt = "potato early blight"
    text = (ask_question(prompt))
    language = "hindi"
    #print(text)
    #print(translator(text, language))

    treatment_txt = treatment(prompt)
    print(treatment_txt)
    print(translator(treatment_txt, language))


