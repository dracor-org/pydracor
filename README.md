# pydracor

pydracor is a Python package which provides access to the [DraCor API](https://dracor.org/doc/api/). It is based on [`pydracor-base`](https://pypi.org/project/pydracor-base/) which was automatically generated using [OpenAPITools](https://github.com/OpenAPITools/openapi-generator).

## Acknowledgment:

The development of this package was supported by Computational Literary Studies Infrastructure (CLS INFRA). CLS INFRA has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 101004984.

## Installation
```sh
pip install pydracor
```

## Classes
  - *DraCorAPI*
    > Base class used to represent the Drama Corpus entity with which *Corpus* and *Play* are created. 
  - *Corpus*
    > A class with which the `corpora/{corpusname}` endpoints can be requested
  - *Play*
    > A class with which the `corpora/{corpusname}/plays/{playname}` endpoint can be requested
  - *DTS*
    > A class with which the `dts` endpoints can be requested
  - *Wikidata*
    > A class with which the `wikidata` endpoints can be requested 

## Code examples

### Import all classes

```python
from pydracor import DraCorAPI, Corpus, Play, Wikidata, DTS
```

### Dracor
  - Initialize a *DraCor* instance
    ```python
    dracor = DraCorAPI()
    ```

  - Initialize a local *DraCor* instance by setting the host
    ```python
    dracor = DraCor(host="http://localhost:8088/api/v1")
    ```

  - Get summary as an Info object (`/info`)
    ```python
    dracor.get_info()
    ```

  - Get the list of available corpora in DraCor (`/info/copora`) and get names
    ```python
    corpora = dracor.get_corpora()
    corpora_metrics = dracor.get_corpora(include='metrics')
    corpora_names = [corpus.name for corpus in corpora]
    ```

  - Get the resolved id for a play (`/id/{id}`)
    ```python 
    dracor.get_resolve_play_id("als000001")
    ```

  - Get the plays with characters by wikidata id
    ```python 
    dracor.get_plays_with_character_by_id("Q131412")
    ```

### Corpus
  - Initialize a *Corpus* instance with the DraCor class (`/corpora/{corpusname}`)
    ```python
    corpus = dracor.get_corpus('rus')
    ```

  - Corpus info as dictionary
    ```python
    corpus.to_dict()
    ```

  - Access corpus attributes, plays as a list of PlayInCorpus objects
    ```python
    corpus.name
    corpus.plays
    ```

  - Extract all play ids from the corpus
    ```python
    play_ids = [play.id for play in corpus.plays]
    ```

  - Filter plays: normalized year after 1800
    ```python
    plays_after_1800 = [play for play in corpus.plays if play.year_normalized > 1800]
    ```

  - Get list of metadata for all plays in a corpus (`/corpora/{corpusname}/metadata`)
    ```python
    metadata = corpus.metadata()
    ```

  - Filter plays: Number of Acts more than five
    ```python
    plays_more_than_five_acts = [play for play in metadata if play.num_of_acts > 5]
    ```

  - Convert metadata to DataFrame
    ```python
    import pandas as pd
    play_metadata_df = pd.DataFrame([play_metadata.to_dict() for play_metadata in metadata])
    ```

  - Get metadata as csv (`/corpora/{corpus}/metadata/csv`) 
    ```python 
    metadata_csv = corpus.get_metadata_csv()
    ```
  - Create Play in corpus (`corpora/{corpusname}/plays/{playname}`)
    ```python
    play = corpus.get_play("gogol-revizor")
    ```


### Play
  - Initialize a *Play* instance by corpus name and play name (`corpora/{corpusname}/plays/{playname}`)
    ```python
    play = dracor.get_play("ger","gengenbach-der-nollhart")
    ```

  - Extract summary in a dictionary
    ```python
    play.to_dict()

    ```
  - Access Play attributes
    ```python 
    play.normalized_genre
    play.characters
    ```

  - Get and access network metrics for a single play (`corpora/{corpusname}/plays/{playname}/metrics`)
    ```python
    metrics = play.get_metrics()
    metrics.average_degree
    ```

  - Get a list of characters of a play (`corpora/{corpusname}/plays/{playname}/characters`)
    ```python
    characters = play.get_characters()
    ```

  - Convert character list to DataFrame
    ```python
    import pandas as pd
    df = pd.DataFrame([character.to_dict() for character in characters])
    ```

  - Get a list of characters of a play as csv (`corpora/{corpusname}/plays/{playname}/characters/csv`)
    ```python
    play.get_characters_csv()
    ```

  - Get networkdata of a play in different formats (`corpora/{corpusname}/plays/{playname}/networkdata/{graphml, gexf, csv}`)
    ```python
    play.get_networkdata("graphml")
    play.get_networkdata("gexf")
    play.get_networkdata("csv")
    ```

  - Get relations of a play in different formats (`corpora/{corpusname}/plays/{playname}/relations/{graphml, gexf, csv}`)
    ```python
    play.get_relations("graphml")
    play.get_relations("gexf")
    play.get_relations("csv")
    ```

  - Get spoken text of a play (excluding stage directions) (`corpora/{corpusname}/plays/{playname}/spoken-text`)
    ```python
    play.get_spoken_text()
    play.get_spoken_text(sex='MALE')
    play.get_spoken_text(relation='siblings')
    ```

  - Get spoken text for each character of a play (`corpora/{corpusname}/plays/{playname}/spoken-text-by-character`)
    ```python
    play.get_spoken_text_by_character()
    ```

  - Get stage directions of a play (`corpora/{corpusname}/plays/{playname}/stage-directions`)
    ```python
    play.get_stage_directions()
    ```

  - Get stage directions and speaker text of a play (`corpora/{corpusname}/plays/{playname}/stage-directions-with-speakers`)
    ```python
    play.get_stage_directions_with_speakers()
    ```

### DTS (Distributed Text Services) 
  - Initialize a *DTS* instance
    ```python
    dts = DTS()
    ```

  - Get Entrypoint of the DraCor DTS implementation (`/dts`) 
    ```python 
    dts.get_dts()
    ```

  - Get the list of the available collections of a corpus (`/dts/collection`)
    ```python
    dts.get_collection("rus")
    ```

  - Use navigation endpoint of DTS (`/dts/navigation`)
    ```python
    dts.get_navigation("rus000160", "body/div[1]")
    dts.get_navigation("rus000160", start="body/div[2]/div[1]", end="body/div[2]/div[2]")
    ```

  - Use document endpoint of DTS (`/dts/document`)
    ```python
    dts.get_document("rus000160", "body/div[1]")
    dts.get_document("rus000160", start="body/div[2]/div[1]", end="body/div[2]/div[2]")
    ```

### Wikidata
  - Initialize a *Wikidata* instance
    ```python
    wikidata = Wikidata()
    ```

  - Get author information by WikidataID
    ```python
    author_info = wikidata.get_author_info("Q34628")
    ```

  - Get Wikidata Mix'n'match information as CSV
    ```python
    wikidata_mixnmatch = wikidata.get_mixnmatch()
    ```


## License
MIT
