# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base
from models.creditcard import CreditCard
from models.user import User
