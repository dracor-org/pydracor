# CharacterInPlayMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wikidata_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_group** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.character_in_play_metadata import CharacterInPlayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterInPlayMetadata from a JSON string
character_in_play_metadata_instance = CharacterInPlayMetadata.from_json(json)
# print the JSON string representation of the object
print(CharacterInPlayMetadata.to_json())

# convert the object into a dict
character_in_play_metadata_dict = character_in_play_metadata_instance.to_dict()
# create an instance of CharacterInPlayMetadata from a dict
character_in_play_metadata_from_dict = CharacterInPlayMetadata.from_dict(character_in_play_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


