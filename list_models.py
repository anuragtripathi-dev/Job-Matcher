import os
from openai import OpenAI

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1",
                api_key=os.environ["NVIDIA_API_KEY"])
for m in client.models.list().data:
    if any(k in m.id for k in ["llama", "nemotron", "qwen", "mistral"]):
        print(m.id)