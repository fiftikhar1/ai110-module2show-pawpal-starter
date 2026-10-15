from datetime import date, datetime, time, timedelta


_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def create_daily_plan(
    tasks: list[dict[str, object]],
    available_start: time,
    available_end: time,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Schedule prioritized tasks in the available window.

    Returns scheduled task copies and task copies that do not fit. Tasks with
    the same priority retain their original order.
    """
    if available_end <= available_start:
        raise ValueError("available_end must be later than available_start")

    ordered_tasks = sorted(
        enumerate(tasks),
        key=lambda indexed_task: (
            _PRIORITY_ORDER.get(
                str(indexed_task[1].get("priority", "")).lower(),
                len(_PRIORITY_ORDER),
            ),
            indexed_task[0],
        ),
    )

    current_time = datetime.combine(date.min, available_start)
    end_of_window = datetime.combine(date.min, available_end)
    scheduled_tasks: list[dict[str, object]] = []
    unscheduled_tasks: list[dict[str, object]] = []

    for _, task in ordered_tasks:
        try:
            duration_minutes = int(task["duration_minutes"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError("Each task needs a valid duration_minutes") from error
        if duration_minutes <= 0:
            raise ValueError("Task durations must be greater than zero")

        task_end = current_time + timedelta(minutes=duration_minutes)
        if task_end > end_of_window:
            unscheduled_tasks.append(dict(task))
            continue

        scheduled_task = dict(task)
        scheduled_task["start_time"] = current_time.strftime("%H:%M")
        scheduled_task["end_time"] = task_end.strftime("%H:%M")
        scheduled_tasks.append(scheduled_task)
        current_time = task_end

    return scheduled_tasks, unscheduled_tasks
