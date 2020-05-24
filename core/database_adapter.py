import config
from peewee import PostgresqlDatabase, Model, AutoField, IntegerField, TextField, ForeignKeyField, TimestampField
from playhouse.postgres_ext import ArrayField, BlobField

_connection = PostgresqlDatabase(config.DATABASE_NAME,
                                 host=config.DATABASE_HOST,
                                 port=config.DATABASE_PORT,
                                 user=config.DATABASE_USER,
                                 password=config.DATABASE_PASSWORD)


class _BaseModel(Model):
    id = AutoField()

    class Meta:
        database = _connection


class _NamedModel(_BaseModel):
    name = TextField()


class Category(_NamedModel):
    pass


class Brand(_NamedModel):
    pass


class UserRole(_NamedModel):
    pass


class MediaResource(_BaseModel):
    content = BlobField()
    telegram_upload_id = TextField()


class User(_BaseModel):
    user_role = ForeignKeyField(UserRole, column_name="user_role_id")
    telegram_user_id = TextField()
    telegram_username = TextField()
    first_name = TextField()


class Item(_BaseModel):
    title = TextField()
    description = TextField()
    category = ForeignKeyField(Category, column_name="category_id")
    brand = ForeignKeyField(Brand, column_name="brand_id")
    price = IntegerField()
    in_stock = IntegerField()
    media_resources = ArrayField(IntegerField, column_name='media_resource_ids')
    # edited_by = IntegerField()
    # created_at = TimestampField()
    # updated_at = TimestampField()
    # flags_ids is unused
