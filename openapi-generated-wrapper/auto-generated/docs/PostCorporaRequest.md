# PostCorporaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | corpus name | 
**title** | **str** | corpus title | 
**repository** | **str** | repository URL | [optional] 
**archive** | **str** | URL of ZIP archive containing TEI files of the corpus The TEI files are expected to be placed in a &#x60;tei&#x60; subdirectory. Other files will be ignored when loading the archive.  | [optional] 

## Example

```python
from openapi_client.models.post_corpora_request import PostCorporaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCorporaRequest from a JSON string
post_corpora_request_instance = PostCorporaRequest.from_json(json)
# print the JSON string representation of the object
print(PostCorporaRequest.to_json())

# convert the object into a dict
post_corpora_request_dict = post_corpora_request_instance.to_dict()
# create an instance of PostCorporaRequest from a dict
post_corpora_request_from_dict = PostCorporaRequest.from_dict(post_corpora_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


