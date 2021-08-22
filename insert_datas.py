from elasticsearch import Elasticsearch

es = Elasticsearch()

datas = [
    {
        'title': '华夏古都迎传奇夜宴，高端白酒说世纪传奇',
        'url': 'http://view.inews.qq.com/a/AJB2021070500487700',
    },
    {
        'title': '八大古都，一省就占四个，你肯定知道是哪个省',
        'url': 'https://k.sina.com.cn/article_7522021850_1c058f1da00100z16a.html',
    },
    {
        'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
        'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    },
    {
        'title': '他，活出了我们理想的样子',
        'url': 'https://new.qq.com/omn/20210821/20210821A020ID00.html',
    }
]

for data in datas:
    es.index(index='news', body=data)
