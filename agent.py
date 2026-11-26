import os, json
from openai import OpenAI
from search import search

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1",
                api_key=os.environ["NVIDIA_API_KEY"])
MODEL = "nvidia/nemotron-3.5-lightning-30b-a3b"

tools = [{
    "type": "function",
    "function": {
        "name": "search_jobs",
        "description": "Search job listings by meaning. Use for any job search request.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
}]

def run_agent(user_msg):
    messages = [
        {"role": "system", "content": "You are a career assistant. Use search_jobs to find jobs, then recommend the best matches with a short reason for each."},
        {"role": "user", "content": user_msg},
    ]
    msg = client.chat.completions.create(
        model=MODEL, messages=messages, tools=tools).choices[0].message
    if msg.tool_calls:
        messages.append(msg)
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            result = search(args["query"], k=3)
            messages.append({"role": "tool", "tool_call_id": call.id,
                             "content": json.dumps(result)})
        msg = client.chat.completions.create(
            model=MODEL, messages=messages, tools=tools).choices[0].message
    return msg.content

