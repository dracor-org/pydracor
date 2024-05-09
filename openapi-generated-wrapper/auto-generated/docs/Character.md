# Character


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closeness** | **float** |  | [optional] 
**wikidata_id** | **str** |  | [optional] 
**betweenness** | **float** |  | [optional] 
**degree** | **int** |  | [optional] 
**weighted_degree** | **int** |  | [optional] 
**num_of_speech_acts** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**eigenvector** | **float** |  | [optional] 
**num_of_scenes** | **int** |  | [optional] 
**num_of_words** | **int** |  | [optional] 
**is_group** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.character import Character

# TODO update the JSON string below
json = "{}"
# create an instance of Character from a JSON string
character_instance = Character.from_json(json)
# print the JSON string representation of the object
print(Character.to_json())

# convert the object into a dict
character_dict = character_instance.to_dict()
# create an instance of Character from a dict
character_from_dict = Character.from_dict(character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


