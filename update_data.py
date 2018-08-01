from elasticsearch import Elasticsearch

es = Elasticsearch()
data = {
    'title': '美国留给伊拉克的是个烂摊子吗',
    'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
    'date': '2011-12-16'
}
result = es.update(index='news', doc_type='politics', body=data, id=1)
# result = es.index(index='news', doc_type='politics', body=data, id=1)
print(result)
