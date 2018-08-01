from elasticsearch import Elasticsearch

es = Elasticsearch()
result = es.indices.create(index='news', ignore=400)
print(result)
