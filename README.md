# pydracor

pydracor is a Python package which provides access to the [DraCor API](https://dracor.org/doc/api).

## Acknowledgment:

The development of this package was supported by Computational Literary Studies Infrastructure (CLS INFRA). CLS INFRA has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 101004984.

## Classes
  - *DraCor* 
    > Base class used to represent Drama Corpus entity.
    > DraCor consists of Corpora.
  - *Corpus*
    > A class used to represent a Corpus of DraCor.
    > Corpus (*als*/*bash*/*cal*/*fre*/*ger*/*gersh*/*greek*/*hun*/*ita*/*rom*/*rus*/*shake*/*span*/*swe*/*tat*) consists of plays.
  - *Play*
    > A class used to represent a Play of a Corpus.
    > Play consists of Characters.
  - *Character*
    > A class used to represent a Character of a Play.

## Code examples

### Import all classes

```python
>>> from pydracor import *
```

### Dracor
  - Initialize a *DraCor* instance
    ```python
    >>> dracor = DraCor()
    ```
  - Summary in a dictionary
    ```python
    >>> dracor.summary()
    ```
  - Summary in a string
    ```python
    >>> str(dracor)
    ```
  - DraCor info in a dictionary
    ```python
    >>> dracor.dracor_info()
    ```
  - List available corpora in DraCor
    ```python
    >>> dracor.corpora()
    >>> dracor.corpora(include='metrics')
    ```
  - List available corpora names in DraCor
    ```python
    >>> dracor.corpora_names()
    ```
  - List available corpora titles in DraCor
    ```python
    >>> dracor.corpora_titles()
    ```
  - Map X to Y
    ```python
    >>> dracor.corpus_name_to_repository()
    >>> dracor.corpus_name_to_title()
    >>> dracor.corpus_name_to_uri()
    >>> dracor.play_title_to_corpus_name()
    >>> dracor.play_title_to_play_id()
    >>> dracor.play_name_to_corpus_name()
    >>> dracor.play_name_to_play_id()
    >>> dracor.play_id_to_play_title()
    >>> dracor.play_id_to_play_name()
    ```
  - Submit SPARQL queries with query parameter
    ```python
    >>> dracor.sparql("PREFIX urn: <http://fliqz.com/> SELECT *  FROM <urn:x-arq:UnionGraph> WHERE {?sub ?pred ?obj .} LIMIT 1")
    ```
### Corpus
  - Initialize a *Corpus* instance
    ```python
    >>> corpus = Corpus('rus')
    >>> corpus = Corpus('cal')
    ...
    ```
  - Summary in a dictionary
    ```python
    >>> corpus.summary()
    ```
  - Summary in a string
    ```python
    >>> str(corpus)
    ```
  - Authors' summary for a corpus
    ```python
    >>> corpus.authors_summary()
    >>> corpus.authors_summary(num_of_authors=5)
    ```
  - String representation of authors_summary method
    ```python
    >>> corpus.authors_summary_str()
    >>> corpus.authors_summary_str(num_of_authors=5)
    ```
  - Corpus info in a dictionary
    ```python
    >>> corpus.corpus_info()
    ```
  - Get all corpus' play Xs
    ```python
    >>> corpus.play_ids()
    >>> corpus.play_names()
    >>> corpus.play_titles()
    ```
  - Map play id to the X year
    ```python
    >>> corpus.written_years()
    >>> corpus.premiere_years()
    >>> corpus.premiere_years()
    ```
  - List of metadata for all plays in a corpus
    ```python
    >>> corpus.metadata()
    ```
  - Filter Plays of a Corpus
  
    Filters are equivalent to the django filters
  
    Possible relations: *eq* / *ne* / *gt* / *ge* / *lt* / *le* / *contains* / *icontains* / *exact* / *iexact* / *in*
  
    Possible fields: all the attributes that the *Corpus* instance contains
    ```python
    >>> corpus.filter(written_year__eq=1913, network_size__lt=20)
    >>> corpus.filter(print_year__lt=1850, source__icontains='lib.ru', premiere_year__gt=1845)
    >>> corpus.filter(
        id__in=frozenset(f"rus000{num:03d}" for num in range(0, 250, 2)),
        subtitle__icontains='комедия',
        author__name__contains='Крылов'
    )
    >>> corpus.filter(name__contains='mysl')
    >>> corpus.filter(title__exact='Мысль')
    >>> corpus.filter(
        year_normalized__in=frozenset(['1935', '1936'])
        source_url__contains='lib'
    )
    >>> corpus.filter(wikidata_id__iexact='Q1989636')
    >>> corpus.filter(networkdata_csv_url__icontains='/andreyev-ne-ubiy/')
    >>> corpus.filter(authors__name__icontains='Бабель')
    ```
### Play
  - Initialize a *Play* instance

    If *play_id* is not None, *play_name* and *play_title* are not considered

    If *play_id* is None *AND* *play_name* is not None, *play_title* is not considered

    If *play_id* is None *AND* *play_name* is None, *play_title* should not be None, otherwise *ValueError* is raised

    If *play_id* is None, automatic corpus detection is applied
    ```python
    >>> play = Play('rus000160')
    >>> play = Play(play_id='rus000160')
    >>> play = Play(play_name='ostrovsky-dohodnoe-mesto')
    >>> play = Play(play_title='Доходное место')
    ```
  - Summary in a dictionary
    ```python
    >>> play.summary()
    ```
  - Summary in a string
    ```python
    >>> str(play)
    ```
  - Play info in a dictionary
    ```python
    >>> play.play_info()
    ```
  - Get network metrics for a single play
    ```python
    >>> play.metrics()
    ```
  - Get a list of characters of a play
    ```python
    >>> play.get_cast()
    ```
  - Get X of a play
    ```python
    >>> play.num_of_male_characters
    >>> play.num_of_female_characters
    >>> play.num_of_unknown_characters
    >>> play.tei
    >>> play.rdf
    >>> play.csv
    >>> play.gexf
    ```
  - Get spoken text of a play (excluding stage directions)
    ```python
    >>> play.spoken_text()
    >>> play.spoken_text(gender='MALE')
    >>> play.spoken_text(gender='FEMALE')
    >>> play.spoken_text(gender='UNKNOWN')
    ```
  - Get spoken text for each character of a play
    ```python
    >>> play.spoken_text_by_character()
    ```
  - Get all stage directions of a play
    ```python
    >>> play.stage_directions()
    ```
  - Get all stage directions of a play including speakers
    ```python
    >>> play.stage_directions_with_speakers()
    ```
### Character
  - Initialize a *Character* instance
    ```python
    >>> character = Character('yakov', 'rus000138')
    >>> character = Character('kraft', 'rus000137')
    ...
    ```
  - Summary in a dictionary
    ```python
    >>> character.summary()
    ```
  - Summary in a string
    ```python
    >>> str(character)
    ```

## Installation
```sh
$ pip install pydracor
```
## Todos
 - write more methods
 - write more tests

## License
MIT
