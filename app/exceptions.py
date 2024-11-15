from fastapi import HTTPException, status

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись с таким id не найден"
)

TodoNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не создана. Проблема в заполнение.",
)

TodoNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не обновлена. Вы передали неправильные данные.",
)
