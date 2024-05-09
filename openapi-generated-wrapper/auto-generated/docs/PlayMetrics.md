# PlayMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_path_length** | **float** |  | [optional] 
**diameter** | **int** |  | [optional] 
**nodes** | [**List[NodeInPlayMetrics]**](NodeInPlayMetrics.md) |  | [optional] 
**corpus** | **str** |  | [optional] 
**average_clustering** | **float** |  | [optional] 
**max_degree** | **int** |  | [optional] 
**wikipedia_link_count** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**num_edges** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**average_degree** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**max_degree_ids** | **List[str]** |  | [optional] 
**num_connected_components** | **int** |  | [optional] 
**density** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.play_metrics import PlayMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PlayMetrics from a JSON string
play_metrics_instance = PlayMetrics.from_json(json)
# print the JSON string representation of the object
print(PlayMetrics.to_json())

# convert the object into a dict
play_metrics_dict = play_metrics_instance.to_dict()
# create an instance of PlayMetrics from a dict
play_metrics_from_dict = PlayMetrics.from_dict(play_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


