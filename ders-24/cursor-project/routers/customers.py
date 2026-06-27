import pyodbc
from fastapi import APIRouter, Depends, HTTPException, status

from database import fetchall_dict, fetchone_dict, get_db
from schemas import Customer, CustomerCreate, CustomerUpdate

router = APIRouter(prefix="/customers", tags=["Customers"])

SELECT_COLUMNS = """
    CustomerID, CompanyName, ContactName, ContactTitle,
    Address, City, Region, PostalCode, Country, Phone, Fax
"""


@router.get("", response_model=list[Customer])
def list_customers(db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(f"SELECT {SELECT_COLUMNS} FROM Customers ORDER BY CustomerID")
    return fetchall_dict(cursor)


@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: str, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        f"SELECT {SELECT_COLUMNS} FROM Customers WHERE CustomerID = ?",
        customer_id,
    )
    customer = fetchone_dict(cursor)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer


@router.post("", response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerCreate, db: pyodbc.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO Customers (
            CustomerID, CompanyName, ContactName, ContactTitle,
            Address, City, Region, PostalCode, Country, Phone, Fax
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        payload.CustomerID,
        payload.CompanyName,
        payload.ContactName,
        payload.ContactTitle,
        payload.Address,
        payload.City,
        payload.Region,
        payload.PostalCode,
        payload.Country,
        payload.Phone,
        payload.Fax,
    )
    db.commit()
    return get_customer(payload.CustomerID, db)


@router.put("/{customer_id}", response_model=Customer)
def update_customer(
    customer_id: str,
    payload: CustomerUpdate,
    db: pyodbc.Connection = Depends(get_db),
):
    get_customer(customer_id, db)

    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        return get_customer(customer_id, db)

    set_clause = ", ".join(f"{field} = ?" for field in updates)
    values = list(updates.values()) + [customer_id]

    cursor = db.cursor()
    cursor.execute(f"UPDATE Customers SET {set_clause} WHERE CustomerID = ?", values)
    db.commit()
    return get_customer(customer_id, db)


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: str, db: pyodbc.Connection = Depends(get_db)):
    get_customer(customer_id, db)

    cursor = db.cursor()
    cursor.execute("DELETE FROM Customers WHERE CustomerID = ?", customer_id)
    db.commit()
