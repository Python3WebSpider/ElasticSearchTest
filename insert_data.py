from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='news', ignore=400)

data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
# result = es.index(index='news', doc_type='politics', body=data)
result = es.create(index='news', doc_type='politics', id=1, body=data)
print(result)
