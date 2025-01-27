from fastapi import APIRouter                           # нужно для роутинга
router = APIRouter(prefix='/task', tags=['task'])       # список тегов для всех операций пути маршрутизатора

# методы для взаимодействия с роутером
@router.get('/')
async def all_tasks():
    pass

@router.get('/task_by_id')
async def task_by_id():
    pass

@router.post('/create')
async def create_task():
    pass

@router.put('/update')
async def update_task():
    pass

@router.delete('/delete')
async def delete_task():
    pass
