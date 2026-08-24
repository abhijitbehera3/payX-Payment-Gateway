from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    UniqueConstraint
)

from datetime import datetime

from .database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    transaction_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    amount = Column(
        Float,
        nullable=False
    )

    currency = Column(
        String,
        nullable=False
    )

    payment_method = Column(
        String,
        nullable=False
    )

    reference_id = Column(
        String,
        nullable=False
    )

    customer_email = Column(
        String,
        nullable=False
    )

    customer_phone = Column(
        String,
        nullable=False
    )

    api_key = Column(
        String,
        nullable=False
    )

    idempotency_key = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="processing"
    )

    compliance_flagged = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        UniqueConstraint(
            "api_key",
            "idempotency_key",
            name="unique_idempotency"
        ),
    )
    