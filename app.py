from transformers import pipeline

# Simple AI Text Generator
generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial Intelligence will change the future because of "
result = generator(prompt, max_length=50, num_return_sequences=1)

print("Generated Text:\n", result[0]['generated_text'])
