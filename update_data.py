from elasticsearch import Elasticsearch

es = Elasticsearch()

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    'date': '2021-07-05'
}
result = es.update(index='news', body=data, id=2)
print(result)
