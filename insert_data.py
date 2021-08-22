from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='news', ignore=400)

data = {'title': '华夏古都迎传奇夜宴，高端白酒说世纪传奇',
        'url': 'http://view.inews.qq.com/a/AJB2021070500487700'}
result = es.create(index='news', id=2, body=data)
print(result)
