# AuthorInPlayInCorpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refs** | [**List[ExternalReferenceResourceId]**](ExternalReferenceResourceId.md) |  | [optional] 
**also_known_as** | **List[str]** |  | [optional] 
**fullname_en** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**shortname_en** | **str** |  | [optional] 
**name_en** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**shortname** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.author_in_play_in_corpus import AuthorInPlayInCorpus

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorInPlayInCorpus from a JSON string
author_in_play_in_corpus_instance = AuthorInPlayInCorpus.from_json(json)
# print the JSON string representation of the object
print(AuthorInPlayInCorpus.to_json())

# convert the object into a dict
author_in_play_in_corpus_dict = author_in_play_in_corpus_instance.to_dict()
# create an instance of AuthorInPlayInCorpus from a dict
author_in_play_in_corpus_from_dict = AuthorInPlayInCorpus.from_dict(author_in_play_in_corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


