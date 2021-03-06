import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='df458bfdb22d816f67f56cf375d0a7b0b1b2c172')

url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'

# print(json.dumps(alchemy_language.author(url=url), indent=2))
# print(json.dumps(alchemy_language.concepts(max_items=2, url=url), indent=2))
# print(json.dumps(alchemy_language.dates(url=url, anchor_date='2016-03-22 00:00:00'), indent=2))
# print(json.dumps(alchemy_language.emotion(url=url), indent=2))
f = open('keywords.txt','r')
f2 = open('sentences.txt','r')
keywords_list = f2.read()
print(json.dumps(alchemy_language.entities(text=keywords_list), indent=2))
print(json.dumps(alchemy_language.keywords(text=keywords_list), indent=2))
# print(json.dumps(alchemy_language.category(url=url), indent=2))
# print(json.dumps(alchemy_language.typed_relations(url=url), indent=2))
# print(json.dumps(alchemy_language.relations(url=url), indent=2))
# print(json.dumps(alchemy_language.language(url=url), indent=2))
# print(json.dumps(alchemy_language.text(url=url), indent=2))
# print(json.dumps(alchemy_language.raw_text(url=url), indent=2))
# print(json.dumps(alchemy_language.title(url=url), indent=2))
# print(json.dumps(alchemy_language.feeds(url=url), indent=2))
# print(json.dumps(alchemy_language.microformats(url='http://microformats.org/wiki/hcard-examples'), indent=2))
# print(json.dumps(alchemy_language.publication_date(url=url), indent=2))
# print(json.dumps(alchemy_language.taxonomy(url=url), indent=2))
# combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
# print(json.dumps(alchemy_language.combined(url=url, extract=combined_operations), indent=2))

# Get sentiment and emotion information results for detected entities/keywords:
# print(json.dumps(alchemy_language.entities(url=url, sentiment=True, emotion=True), indent=2))
# print(json.dumps(alchemy_language.keywords(max_items=5, url=url, sentiment=True, emotion=True), indent=2))
