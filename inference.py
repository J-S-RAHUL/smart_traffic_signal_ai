def run_task(task_id):
    print(f"[START] task={task_id}")

    # sample output logic
    if task_id == "task_1":
        output = 0
    elif task_id == "task_2":
        output = 1
    elif task_id == "task_3":
        output = 2
    else:
        output = 0

    print(output)
    return output


if __name__ == "__main__":
    tasks = ["task_1", "task_2", "task_3"]

    for task in tasks:
        run_task(task)
