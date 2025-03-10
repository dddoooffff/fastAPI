from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TasksRepository
import storage

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_task(
    task: Annotated[storage.STaskAdd, Depends()],
) -> storage.STaskId:
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[storage.STask]:
    tasks = await TasksRepository.find_all()
    return tasks