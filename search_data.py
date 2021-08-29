from elasticsearch import Elasticsearch
import json

dsl = {
    'query': {
        'match': {
            'title': '高考 圆梦'
        }
    }
}

es = Elasticsearch()
result = es.search(index='news', body=dsl)
# print(json.dumps(result, indent=2, ensure_ascii=False))
print(result)

result = es.search(index='news')
# print(result)
# print(json.dumps(result, indent=2, ensure_ascii=False))
