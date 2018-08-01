from elasticsearch import Elasticsearch

es = Elasticsearch()
result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
