from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class CustomerBase(BaseModel):
    CompanyName: str = Field(..., max_length=40)
    ContactName: str | None = Field(None, max_length=30)
    ContactTitle: str | None = Field(None, max_length=30)
    Address: str | None = Field(None, max_length=60)
    City: str | None = Field(None, max_length=15)
    Region: str | None = Field(None, max_length=15)
    PostalCode: str | None = Field(None, max_length=10)
    Country: str | None = Field(None, max_length=15)
    Phone: str | None = Field(None, max_length=24)
    Fax: str | None = Field(None, max_length=24)


class CustomerCreate(CustomerBase):
    CustomerID: str = Field(..., min_length=1, max_length=5)


class CustomerUpdate(BaseModel):
    CompanyName: str | None = Field(None, max_length=40)
    ContactName: str | None = Field(None, max_length=30)
    ContactTitle: str | None = Field(None, max_length=30)
    Address: str | None = Field(None, max_length=60)
    City: str | None = Field(None, max_length=15)
    Region: str | None = Field(None, max_length=15)
    PostalCode: str | None = Field(None, max_length=10)
    Country: str | None = Field(None, max_length=15)
    Phone: str | None = Field(None, max_length=24)
    Fax: str | None = Field(None, max_length=24)


class Customer(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    CustomerID: str


class CategoryBase(BaseModel):
    CategoryName: str = Field(..., max_length=15)
    Description: str | None = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    CategoryName: str | None = Field(None, max_length=15)
    Description: str | None = None


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    CategoryID: int


class ProductBase(BaseModel):
    ProductName: str = Field(..., max_length=40)
    SupplierID: int | None = None
    CategoryID: int | None = None
    QuantityPerUnit: str | None = Field(None, max_length=20)
    UnitPrice: Decimal | None = None
    UnitsInStock: int | None = None
    UnitsOnOrder: int | None = None
    ReorderLevel: int | None = None
    Discontinued: bool = False


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    ProductName: str | None = Field(None, max_length=40)
    SupplierID: int | None = None
    CategoryID: int | None = None
    QuantityPerUnit: str | None = Field(None, max_length=20)
    UnitPrice: Decimal | None = None
    UnitsInStock: int | None = None
    UnitsOnOrder: int | None = None
    ReorderLevel: int | None = None
    Discontinued: bool | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    ProductID: int
