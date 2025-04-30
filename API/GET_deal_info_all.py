from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import sqlite3

app = FastAPI()



# Модель Pydantic для валидации данных сделки
class Deal(BaseModel):
    id: int
    user_id: str
    deal_type: str
    status: bool
    creation_time: str
    tg_username: str
    phone_number: Optional[str] = None



app = FastAPI()

# Модель Pydantic для валидации данных


@app.get("/deal-info/all", response_model=List[Deal])
async def get_all_deals(status: Optional[bool] = Query(None)):
    try:
        conn = sqlite3.connect('data_base.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Формируем запрос в зависимости от параметра status
        if status is not None:
            cursor.execute("SELECT * FROM deals WHERE status = ?", (status,))
        else:
            cursor.execute("SELECT * FROM deals")

        deals = cursor.fetchall()
        conn.close()

        return [dict(deal) for deal in deals]

    except sqlite3.Error as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
# @app.get("/deal-info/all", response_model=List[Deal])
# async def get_all_deals():
#     try:
#         # Подключаемся к БД
#         conn = sqlite3.connect('data_base.db')
#         conn.row_factory = sqlite3.Row  # Для доступа к полям по имени
#         cursor = conn.cursor()
#
#         # Выполняем запрос
#         cursor.execute("SELECT * FROM deals")
#         deals = cursor.fetchall()
#
#         # Закрываем соединение
#         conn.close()
#
#         # Конвертируем строки в словари
#         deals_list = [dict(deal) for deal in deals]
#
#         return deals_list
#
#     except sqlite3.Error as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Database error: {str(e)}"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Unexpected error: {str(e)}"
#         )

async def run_fastapi():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()