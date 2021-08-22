from elasticsearch import Elasticsearch

es = Elasticsearch()
result = es.delete(index='news', id=1)
print(result)
