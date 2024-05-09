# CorpusMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characters** | **int** |  | [optional] 
**stage** | **int** |  | [optional] 
**updated** | **str** |  | [optional] 
**sp** | **int** |  | [optional] 
**text** | **int** |  | [optional] 
**plays** | **int** |  | [optional] 
**wordcount** | [**WordCounts**](WordCounts.md) |  | [optional] 
**male** | **int** |  | [optional] 
**female** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.corpus_metrics import CorpusMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusMetrics from a JSON string
corpus_metrics_instance = CorpusMetrics.from_json(json)
# print the JSON string representation of the object
print(CorpusMetrics.to_json())

# convert the object into a dict
corpus_metrics_dict = corpus_metrics_instance.to_dict()
# create an instance of CorpusMetrics from a dict
corpus_metrics_from_dict = CorpusMetrics.from_dict(corpus_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


