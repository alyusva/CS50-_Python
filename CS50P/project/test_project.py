import pytest
import project
import os
import json

@pytest.fixture
def setup_tasks():
    tasks = [
        {"description": "Task 1", "due_date": "2024-12-01", "completed": False},
        {"description": "Task 2", "due_date": "2024-12-02", "completed": True},
    ]
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    yield
    os.remove("tasks.json")

def test_add_task(setup_tasks):
    project.add_task("Test task", "2024-12-31")
    tasks = project.load_tasks()
    assert len(tasks) == 3
    assert tasks[2]["description"] == "Test task"
    assert tasks[2]["due_date"] == "2024-12-31"

def test_delete_task(setup_tasks):
    project.delete_task(0)
    tasks = project.load_tasks()
    assert len(tasks) == 1

def test_view_tasks(setup_tasks, capsys):
    project.view_tasks()
    captured = capsys.readouterr()
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out

def test_mark_task_as_completed(setup_tasks):
    project.mark_task_as_completed(0)
    tasks = project.load_tasks()
    assert tasks[0]["completed"] == True

if __name__ == "__main__":
    pytest.main()
