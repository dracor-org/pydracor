# PlayInCorpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wikidata_id** | **str** |  | [optional] 
**year_written** | **str** |  | [optional] 
**source** | [**SourceInPlayMetadata**](SourceInPlayMetadata.md) |  | [optional] 
**year_premiered** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**networkdata_csv_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title_en** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**date_premiered** | **str** |  | [optional] 
**year_printed** | **str** |  | [optional] 
**year_normalized** | **int** |  | [optional] 
**authors** | [**List[AuthorInPlayInCorpus]**](AuthorInPlayInCorpus.md) |  | [optional] 
**name** | **str** |  | [optional] 
**network_size** | **int** |  | [optional] 
**subtitle_en** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.play_in_corpus import PlayInCorpus

# TODO update the JSON string below
json = "{}"
# create an instance of PlayInCorpus from a JSON string
play_in_corpus_instance = PlayInCorpus.from_json(json)
# print the JSON string representation of the object
print(PlayInCorpus.to_json())

# convert the object into a dict
play_in_corpus_dict = play_in_corpus_instance.to_dict()
# create an instance of PlayInCorpus from a dict
play_in_corpus_from_dict = PlayInCorpus.from_dict(play_in_corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


