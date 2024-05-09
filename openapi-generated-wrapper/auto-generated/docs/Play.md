# Play


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wikidata_id** | **str** |  | [optional] 
**segments** | [**List[SegmentItemInPlayMetadata]**](SegmentItemInPlayMetadata.md) |  | [optional] 
**corpus** | **str** |  | [optional] 
**year_premiered** | **str** |  | [optional] 
**all_in_index** | **float** |  | [optional] 
**title_en** | **str** |  | [optional] 
**authors** | [**List[AuthorInPlayMetadata]**](AuthorInPlayMetadata.md) |  | [optional] 
**name** | **str** |  | [optional] 
**normalized_genre** | **str** |  | [optional] 
**subtitle_en** | **str** |  | [optional] 
**characters** | [**List[CharacterInPlayMetadata]**](CharacterInPlayMetadata.md) |  | [optional] 
**source** | [**SourceInPlayMetadata**](SourceInPlayMetadata.md) |  | [optional] 
**subtitle** | **str** |  | [optional] 
**libretto** | **bool** |  | [optional] 
**all_in_segment** | **int** |  | [optional] 
**year_written** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**date_premiered** | **str** |  | [optional] 
**year_printed** | **str** |  | [optional] 
**relations** | [**List[RelationItemInPlayMetadata]**](RelationItemInPlayMetadata.md) |  | [optional] 
**title** | **str** |  | [optional] 
**year_normalized** | **int** |  | [optional] 
**original_source** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.play import Play

# TODO update the JSON string below
json = "{}"
# create an instance of Play from a JSON string
play_instance = Play.from_json(json)
# print the JSON string representation of the object
print(Play.to_json())

# convert the object into a dict
play_dict = play_instance.to_dict()
# create an instance of Play from a dict
play_from_dict = Play.from_dict(play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


