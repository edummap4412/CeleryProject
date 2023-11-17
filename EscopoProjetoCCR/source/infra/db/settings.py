from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "postgresql+psycopg2",
            "user",
            "password",
            "localhost",
            "32769",
            "user"
        )

        self.__engine = self.create_db_engine()

    def create_db_engine(self):
        return create_engine(self.__connection_string)

    def get_db_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        