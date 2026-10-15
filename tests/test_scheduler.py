from datetime import time

import pytest

from scheduler import create_daily_plan


def test_schedules_by_priority_within_available_window():
    tasks = [
        {"title": "Play", "duration_minutes": 20, "priority": "low"},
        {"title": "Walk", "duration_minutes": 30, "priority": "high"},
        {"title": "Feed", "duration_minutes": 15, "priority": "medium"},
    ]

    scheduled, unscheduled = create_daily_plan(tasks, time(8, 0), time(8, 50))

    assert [task["title"] for task in scheduled] == ["Walk", "Feed"]
    assert [(task["start_time"], task["end_time"]) for task in scheduled] == [
        ("08:00", "08:30"),
        ("08:30", "08:45"),
    ]
    assert [task["title"] for task in unscheduled] == ["Play"]
    assert "start_time" not in tasks[1]


def test_task_that_does_not_fit_does_not_block_shorter_tasks():
    tasks = [
        {"title": "Long walk", "duration_minutes": 70, "priority": "high"},
        {"title": "Feed", "duration_minutes": 30, "priority": "medium"},
    ]

    scheduled, unscheduled = create_daily_plan(tasks, time(8, 0), time(9, 0))

    assert [task["title"] for task in scheduled] == ["Feed"]
    assert scheduled[0]["start_time"] == "08:00"
    assert [task["title"] for task in unscheduled] == ["Long walk"]


def test_rejects_invalid_availability_window():
    with pytest.raises(ValueError, match="available_end must be later"):
        create_daily_plan([], time(17, 0), time(8, 0))


def test_rejects_non_positive_task_duration():
    tasks = [{"title": "Walk", "duration_minutes": 0, "priority": "high"}]

    with pytest.raises(ValueError, match="greater than zero"):
        create_daily_plan(tasks, time(8, 0), time(9, 0))
