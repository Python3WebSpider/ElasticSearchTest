from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='news', ignore=400)

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
}
result = es.create(index='news', id=2, body=data)
print(result)
