# AuthorInPlayMetadata


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
from openapi_client.models.author_in_play_metadata import AuthorInPlayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorInPlayMetadata from a JSON string
author_in_play_metadata_instance = AuthorInPlayMetadata.from_json(json)
# print the JSON string representation of the object
print(AuthorInPlayMetadata.to_json())

# convert the object into a dict
author_in_play_metadata_dict = author_in_play_metadata_instance.to_dict()
# create an instance of AuthorInPlayMetadata from a dict
author_in_play_metadata_from_dict = AuthorInPlayMetadata.from_dict(author_in_play_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


