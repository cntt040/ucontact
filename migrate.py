from appcore.database import database
from model.schemas import *
# database.create_tables(__members__, True)
database.create_tables([Contact])
