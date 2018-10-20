from helpers.Index import Index, connect
from helpers.XMLRepository import XMLRepository

connection = connect("localhost", "9200")

index = Index(connection, "meu-index")

dados = XMLRepository("./datasets/bitcoin/")

index.bulk_insert(dados.data())

