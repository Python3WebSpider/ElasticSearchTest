from elasticsearch import Elasticsearch

es = Elasticsearch()

data = {
    'title': '华夏古都迎传奇夜宴，高端白酒说世纪传奇',
    'url': 'http://view.inews.qq.com/a/AJB2021070500487700',
    'date': '2021-07-05'
}
result = es.update(index='news', body=data, id=2)
print(result)
