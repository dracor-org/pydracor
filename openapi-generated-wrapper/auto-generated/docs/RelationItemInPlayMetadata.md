# RelationItemInPlayMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directed** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.relation_item_in_play_metadata import RelationItemInPlayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RelationItemInPlayMetadata from a JSON string
relation_item_in_play_metadata_instance = RelationItemInPlayMetadata.from_json(json)
# print the JSON string representation of the object
print(RelationItemInPlayMetadata.to_json())

# convert the object into a dict
relation_item_in_play_metadata_dict = relation_item_in_play_metadata_instance.to_dict()
# create an instance of RelationItemInPlayMetadata from a dict
relation_item_in_play_metadata_from_dict = RelationItemInPlayMetadata.from_dict(relation_item_in_play_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


