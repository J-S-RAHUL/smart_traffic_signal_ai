import os
from openai import OpenAI


def call_llm(task_id):
    client = OpenAI(
        base_url=os.environ["API_BASE_URL"],
        api_key=os.environ["API_KEY"]
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Select best traffic signal action for {task_id}. Return only 0,1,2,3"
            }
        ]
    )

    return response.choices[0].message.content.strip()


def run_task(task_id):
    print(f"[START] task={task_id}")

    output = call_llm(task_id)

    print(output)
    return output


if __name__ == "__main__":
    tasks = ["task_1", "task_2", "task_3"]

    for task in tasks:
        run_task(task)
