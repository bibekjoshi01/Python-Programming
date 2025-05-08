import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200


def test_can_create_task():
    payload = new_task_payload()

    response1 = create_task(payload)
    assert response1.status_code == 200
    data1 = response1.json()

    task_id = data1["task"]["task_id"]
    response2 = get_task(task_id)
    assert response2.status_code == 200
    data2 = response2.json()

    assert data1["task"]["content"] == data2["content"]
    assert data1["task"]["user_id"] == data2["user_id"]


def test_can_update_task():
    payload = new_task_payload()
    response1 = create_task(payload)
    task_id = response1.json()["task"]["task_id"]

    new_payload = {
        "content": "This is updated content",
        "user_id": payload["user_id"],
        "is_done": True,
        "task_id": task_id,
    }
    ressponse2 = update_task(new_payload)
    assert ressponse2.status_code == 200

    # Get and validate the content
    get_response = get_task(task_id)
    assert get_response.status_code == 200

    assert get_response.json()["content"] == new_payload["content"]
    assert get_response.json()["is_done"] == new_payload["is_done"]


def test_can_list_tasks():
    N = 3
    payload = new_task_payload()
    for _ in range(N):
        create_task_resp = create_task(payload)
        assert create_task_resp.status_code == 200

    list_task_resp = list_tasks(payload["user_id"])
    assert list_task_resp.status_code == 200
    data = list_task_resp.json()
    assert len(data["tasks"]) == 3


def test_can_delete_task():
    payload = new_task_payload()
    create_tast_resp = create_task(payload)
    assert create_tast_resp.status_code == 200

    task_id = create_tast_resp.json()["task"]["task_id"]
    delete_task_resp = delete_task(task_id)

    assert delete_task_resp.status_code == 200

    get_task_resp = get_task(task_id)
    assert get_task_resp.status_code == 404


# helpers 

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)


def get_task(task_id):
    return requests.get(f"{ENDPOINT}/get-task/{task_id}")


def delete_task(task_id):
    return requests.delete(f"{ENDPOINT}/delete-task/{task_id}")


def list_tasks(user_id):
    return requests.get(f"{ENDPOINT}/list-tasks/{user_id}")


def new_task_payload():
    return {
        "content": "This is test content",
        "user_id": uuid.uuid4().hex,
        "is_done": False,
    }
