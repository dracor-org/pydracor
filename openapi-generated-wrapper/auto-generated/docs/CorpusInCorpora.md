# CorpusInCorpora


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acronym** | **str** |  | [optional] 
**metrics** | [**CorpusMetrics**](CorpusMetrics.md) |  | [optional] 
**title** | **str** |  | [optional] 
**licence** | **str** |  | [optional] 
**licence_url** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.corpus_in_corpora import CorpusInCorpora

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusInCorpora from a JSON string
corpus_in_corpora_instance = CorpusInCorpora.from_json(json)
# print the JSON string representation of the object
print(CorpusInCorpora.to_json())

# convert the object into a dict
corpus_in_corpora_dict = corpus_in_corpora_instance.to_dict()
# create an instance of CorpusInCorpora from a dict
corpus_in_corpora_from_dict = CorpusInCorpora.from_dict(corpus_in_corpora_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


