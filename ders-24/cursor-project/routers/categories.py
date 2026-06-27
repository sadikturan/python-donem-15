import pyodbc
from fastapi import APIRouter, Depends, HTTPException, status

from database import fetchall_dict, fetchone_dict, get_db
from schemas import Category, CategoryCreate, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Categories"])

SELECT_COLUMNS = "CategoryID, CategoryName, Description"


@router.get("", response_model=list[Category])
def list_categories(db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(f"SELECT {SELECT_COLUMNS} FROM Categories ORDER BY CategoryID")
    return fetchall_dict(cursor)


@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        f"SELECT {SELECT_COLUMNS} FROM Categories WHERE CategoryID = ?",
        category_id,
    )
    category = fetchone_dict(cursor)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.post("", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO Categories (CategoryName, Description)
        OUTPUT INSERTED.CategoryID, INSERTED.CategoryName, INSERTED.Description
        VALUES (?, ?)
        """,
        payload.CategoryName,
        payload.Description,
    )
    category = fetchone_dict(cursor)
    db.commit()
    return category


@router.put("/{category_id}", response_model=Category)
def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: pyodbc.Connection = Depends(get_db),
):
    get_category(category_id, db)

    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        return get_category(category_id, db)

    set_clause = ", ".join(f"{field} = ?" for field in updates)
    values = list(updates.values()) + [category_id]

    cursor = db.cursor()
    cursor.execute(f"UPDATE Categories SET {set_clause} WHERE CategoryID = ?", values)
    db.commit()
    return get_category(category_id, db)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: pyodbc.Connection = Depends(get_db)):
    get_category(category_id, db)

    cursor = db.cursor()
    cursor.execute("DELETE FROM Categories WHERE CategoryID = ?", category_id)
    db.commit()
