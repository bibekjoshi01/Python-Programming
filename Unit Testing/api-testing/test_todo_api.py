import requests

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200


def test_can_create_task():
    payload = {
        "content": "This is test content",
        "user_id": "1",
        "is_done": False
    }

    response1 = requests.put(f"{ENDPOINT}/create-task", json=payload)
    assert response1.status_code == 200
    data1 = response1.json()

    task_id = data1['task']['task_id']
    response2 = requests.get(f"{ENDPOINT}/get-task/{task_id}")
    assert response2.status_code == 200
    data2 = response2.json()

    assert data1["task"]['content'] == data2['content']
    assert data1["task"]['user_id'] == data2['user_id']
