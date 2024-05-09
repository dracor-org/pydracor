# PlayWithWikidataCharacter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**authors** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.play_with_wikidata_character import PlayWithWikidataCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of PlayWithWikidataCharacter from a JSON string
play_with_wikidata_character_instance = PlayWithWikidataCharacter.from_json(json)
# print the JSON string representation of the object
print(PlayWithWikidataCharacter.to_json())

# convert the object into a dict
play_with_wikidata_character_dict = play_with_wikidata_character_instance.to_dict()
# create an instance of PlayWithWikidataCharacter from a dict
play_with_wikidata_character_from_dict = PlayWithWikidataCharacter.from_dict(play_with_wikidata_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


