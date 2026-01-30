from transformers import pipeline

# Load a lightweight language model
chat_pipeline = pipeline("text-generation", model="gpt2")

def generate_response(user_input: str) -> str:
    response = chat_pipeline(
        user_input,
        max_length=120,
        num_return_sequences=1
    )
    return response[0]["generated_text"]