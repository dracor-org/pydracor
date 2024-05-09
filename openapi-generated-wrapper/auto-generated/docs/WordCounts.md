# WordCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **int** |  | [optional] 
**stage** | **int** |  | [optional] 
**sp** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.word_counts import WordCounts

# TODO update the JSON string below
json = "{}"
# create an instance of WordCounts from a JSON string
word_counts_instance = WordCounts.from_json(json)
# print the JSON string representation of the object
print(WordCounts.to_json())

# convert the object into a dict
word_counts_dict = word_counts_instance.to_dict()
# create an instance of WordCounts from a dict
word_counts_from_dict = WordCounts.from_dict(word_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


