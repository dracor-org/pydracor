# SegmentItemInPlayMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**speakers** | **List[str]** |  | [optional] 
**number** | **int** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.segment_item_in_play_metadata import SegmentItemInPlayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentItemInPlayMetadata from a JSON string
segment_item_in_play_metadata_instance = SegmentItemInPlayMetadata.from_json(json)
# print the JSON string representation of the object
print(SegmentItemInPlayMetadata.to_json())

# convert the object into a dict
segment_item_in_play_metadata_dict = segment_item_in_play_metadata_instance.to_dict()
# create an instance of SegmentItemInPlayMetadata from a dict
segment_item_in_play_metadata_from_dict = SegmentItemInPlayMetadata.from_dict(segment_item_in_play_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


