import os
from openai import OpenAI

def checkKey(key):
    print(f"Checking key: {key}")
    client = OpenAI(
        api_key=key,
    )


    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a coding assistant that talks like a pirate.",
            input="How do I check if a Python object is an instance of a class?",
        )
        print(response.output_text)
        #if no error code 401 , key valid,put in valid keys
        with open('validKeys.txt','a') as f:
            f.write(key + "\n")

    except Exception as e:
        print(f"Error occured: {e}")


with open("keys.txt","r") as f:
    for key in f:
        #check key
        checkKey(key.strip())

