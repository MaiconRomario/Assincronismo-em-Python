from databases import Database


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///./schema.db"
        self.__database = Database(self.__connection_string)

    async def connect_to_db(self):
        await self.__database.connect()  # Abre a conexão com o banco de dados

    async def disconnect_to_db(self):
        await self.__database.disconnect()  # Fecha a conexão com o banco de dados

    def get_db_conn(self):
        return self.__database  # Retorna o objeto de conexão com o banco de dados



db_connection_handler = DBConnectionHandler()
