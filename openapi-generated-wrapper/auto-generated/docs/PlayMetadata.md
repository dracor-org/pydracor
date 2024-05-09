# PlayMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_of_speakers_male** | **int** |  | [optional] 
**diameter** | **int** |  | [optional] 
**wikidata_id** | **str** |  | [optional] 
**num_of_speakers_female** | **int** |  | [optional] 
**average_clustering** | **float** |  | [optional] 
**year_premiered** | **str** |  | [optional] 
**original_source_pub_place** | **str** |  | [optional] 
**num_of_speakers** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**word_count_stage** | **int** |  | [optional] 
**normalized_genre** | **str** |  | [optional] 
**num_of_l** | **int** |  | [optional] 
**word_count_sp** | **int** |  | [optional] 
**num_of_speakers_unknown** | **int** |  | [optional] 
**average_path_length** | **float** |  | [optional] 
**original_source_year** | **int** |  | [optional] 
**max_degree** | **int** |  | [optional] 
**num_edges** | **int** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**first_author** | **str** |  | [optional] 
**original_source_publisher** | **str** |  | [optional] 
**libretto** | **bool** |  | [optional] 
**num_connected_components** | **int** |  | [optional] 
**year_written** | **str** |  | [optional] 
**play_name** | **str** |  | [optional] 
**num_of_p** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**word_count_text** | **int** |  | [optional] 
**date_premiered** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**average_degree** | **float** |  | [optional] 
**year_printed** | **str** |  | [optional] 
**num_of_segments** | **int** |  | [optional] 
**num_of_acts** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**wikipedia_link_count** | **int** |  | [optional] 
**digital_source** | **object** |  | [optional] 
**num_of_person_groups** | **int** |  | [optional] 
**year_normalized** | **int** |  | [optional] 
**num_of_co_authors** | **int** |  | [optional] 
**max_degree_ids** | **str** |  | [optional] 
**original_source_number_of_pages** | **int** |  | [optional] 
**density** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.play_metadata import PlayMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PlayMetadata from a JSON string
play_metadata_instance = PlayMetadata.from_json(json)
# print the JSON string representation of the object
print(PlayMetadata.to_json())

# convert the object into a dict
play_metadata_dict = play_metadata_instance.to_dict()
# create an instance of PlayMetadata from a dict
play_metadata_from_dict = PlayMetadata.from_dict(play_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


