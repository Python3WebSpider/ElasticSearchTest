from elasticsearch import Elasticsearch

es = Elasticsearch()
result = es.delete(index='news', doc_type='politics', id=1)
print(result)
