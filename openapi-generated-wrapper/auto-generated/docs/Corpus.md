# Corpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acronym** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**licence** | **str** |  | [optional] 
**licence_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**plays** | [**List[PlayInCorpus]**](PlayInCorpus.md) |  | [optional] 
**repository** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.corpus import Corpus

# TODO update the JSON string below
json = "{}"
# create an instance of Corpus from a JSON string
corpus_instance = Corpus.from_json(json)
# print the JSON string representation of the object
print(Corpus.to_json())

# convert the object into a dict
corpus_dict = corpus_instance.to_dict()
# create an instance of Corpus from a dict
corpus_from_dict = Corpus.from_dict(corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


