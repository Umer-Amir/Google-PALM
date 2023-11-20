import pprint
import google.generativeai as palm

palm.configure(api_key='YOUR_API_KEY')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print("MODEL:" +model + "\n\n")

prompt = """
Write in great detail about the philosphy of consciousness. 
Use multiple perspectives to describe the nature of consciousness. 
Defend each perspective with examples and counterexamples. 
I need atleast 500 words. 
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)