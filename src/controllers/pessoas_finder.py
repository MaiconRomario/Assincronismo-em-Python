from src.model.repositories.pessoa_repository import PessoasRepository

class PessoasFinder:
    def __init__(self):
        self.__pessoas_repo = PessoasRepository()

    async def find_people(self) -> dict:
        pessoas = await self.__pessoas_repo.get_all_people()

        formatted_pessoas = []
        for pessoa in pessoas:
            formatted_pessoas.append(
                {"id": pessoa.id, "nome": pessoa.name}
            )

        return {
            "type": "Pessoa",
            "count": len(formatted_pessoas),
            "attributes": formatted_pessoas
        }        