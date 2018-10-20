import logging

from elasticsearch import Elasticsearch, helpers

logging.basicConfig(level=logging.INFO)

class Index:

    def __init__(self, connection, index_name):
        self._connection = connection
        self._index_name = index_name
        self._doc_type = index_name

    def bulk_insert(self, records):
        def to_dict():
            for record in records:
                res = record
                yield res

        helpers.bulk(self._connection, to_dict(), doc_type=self._doc_type, index=self._index_name)


def connect(host, port):
    connection = Elasticsearch([{'host': host, 'port': port}])
    if connection.ping():
        print("Connection to elasticsearch at " + host + ":" + port)
    else:
        print("Could not connect to elasticsearch at " + host + ":" + port)
    return connection

