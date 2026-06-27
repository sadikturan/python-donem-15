import pyodbc
from fastapi import APIRouter, Depends, HTTPException, status

from database import fetchall_dict, fetchone_dict, get_db
from schemas import Product, ProductCreate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])

SELECT_COLUMNS = """
    ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit,
    UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
"""


@router.get("", response_model=list[Product])
def list_products(db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(f"SELECT {SELECT_COLUMNS} FROM Products ORDER BY ProductID")
    return fetchall_dict(cursor)


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        f"SELECT {SELECT_COLUMNS} FROM Products WHERE ProductID = ?",
        product_id,
    )
    product = fetchone_dict(cursor)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO Products (
            ProductName, SupplierID, CategoryID, QuantityPerUnit,
            UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
        )
        OUTPUT
            INSERTED.ProductID, INSERTED.ProductName, INSERTED.SupplierID,
            INSERTED.CategoryID, INSERTED.QuantityPerUnit, INSERTED.UnitPrice,
            INSERTED.UnitsInStock, INSERTED.UnitsOnOrder, INSERTED.ReorderLevel,
            INSERTED.Discontinued
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        payload.ProductName,
        payload.SupplierID,
        payload.CategoryID,
        payload.QuantityPerUnit,
        payload.UnitPrice,
        payload.UnitsInStock,
        payload.UnitsOnOrder,
        payload.ReorderLevel,
        payload.Discontinued,
    )
    product = fetchone_dict(cursor)
    db.commit()
    return product


@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: pyodbc.Connection = Depends(get_db),
):
    get_product(product_id, db)

    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        return get_product(product_id, db)

    set_clause = ", ".join(f"{field} = ?" for field in updates)
    values = list(updates.values()) + [product_id]

    cursor = db.cursor()
    cursor.execute(f"UPDATE Products SET {set_clause} WHERE ProductID = ?", values)
    db.commit()
    return get_product(product_id, db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: pyodbc.Connection = Depends(get_db)):
    get_product(product_id, db)

    cursor = db.cursor()
    cursor.execute("DELETE FROM Products WHERE ProductID = ?", product_id)
    db.commit()
