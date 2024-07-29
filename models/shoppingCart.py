from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

class ShoppingCart(Base):
    __tablename__ = "ShoppoingCart"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("Customer.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("Products.id"))
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)

    customer: Mapped["Customer"] = relationship("Customer", back_populates="shopping_cart")
    product: Mapped["Products"] = relationship("Products")

from models.customer import Customer

Customer.shopping_cart = relationship("ShoppingCart", order_by=ShoppingCart.id, back_populates="customer")

