#!/usr/bin/env python
from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydracor_base.api_client import ApiClient
from pydracor_base.api.public_api import PublicApi
from pydracor_base.api.wikidata_api import WikidataApi
from pydracor_base.api.dts_api import DTSApi
from pydracor_base.models import Corpus as CorpusModel
from pydracor_base.models import Info
from pydracor_base.models import Play as PlayModel
from pydracor_base.models import PlayMetadata
from pydracor_base.models.character import Character
from pydracor_base.models.corpus_in_corpora import CorpusInCorpora
from pydracor_base.models.play_metrics import PlayMetrics
from pydracor_base.models.play_with_wikidata_character import PlayWithWikidataCharacter
from pydracor_base.models.spoken_text_by_character import SpokenTextByCharacter
from pydracor_base.models.dts_entrypoint import DtsEntrypoint
from pydracor_base.exceptions import NotFoundException, BadRequestException
from pydracor_base.configuration import Configuration

class CorpusNotFound(Exception):
    """
    Exception raised when a specified corpus is not found in the DraCor API.
    """
    pass

class PlayNotFound(Exception): 
    """
    Exception raised when a specified play is not found in the DraCor API.
    """
    pass 

class InvalidParameterCombination(Exception):
    """
    Exception raised when an invalid combination of parameters is provided 
    for a an API call.
    """
    pass

class IncludeType(str, Enum):
    """
    Enumeration for specifying additional metadata to include in API responses.

    Attributes:
        metrics: Include metrics data in the response.
    """
    metrics = "metrics"

class DownloadFormat(str, Enum):
    """
    DownloadFormat is an enumeration that represents the available formats 
    for downloading data. Each member of the enumeration corresponds to a 
    specific file format:

    - `csv`: Comma-Separated Values format, commonly used for tabular data.
    - `gexf`: Graph Exchange XML Format, used for representing graph structures.
    - `graphml`: Graph Markup Language, another format for representing graph structures.

    This enumeration can be used to specify the desired format when interacting 
    with APIs or other systems that support multiple download formats.
    """
    csv = "csv"
    gexf = "gexf"
    graphml = "graphml"

class DraCorAPI:
    """
    A wrapper class for interacting with the DraCor API.
    This class provides methods to retrieve information about corpora, plays, and characters
    from the DraCor API. It is used to created Corpus and Play instances. 
    Attributes:
    """

    def __init__(self, api_client=None, host=None) -> None:
        """
        Initializes the DraCorAPI instance with an optional API client or host URL.
        Args:
            api_client: An optional API client instance to use for requests.
            host (str): An optional host URL to configure the API client, can e.g. be set to localhost or staging.
        """
        if host:
            configuration = Configuration(host=host)
            api_client = ApiClient(configuration=configuration)
        self._api = PublicApi(api_client)

    def get_info(self) -> Info:
        """
        Retrieves general information about the DraCor API.
        Returns:
            Info: Information about the API.
        """
        return self._api.api_info()

    def get_corpora(self, include: Optional[IncludeType]=None) -> List[CorpusInCorpora]:
        """
        Retrieves a list of available corpora. Optionally includes additional metadata.
        Returns:
            List[CorpusInCorpora]: Metadata for the corpora in DraCor.
        """
        return self._api.list_corpora(include)

    def get_corpus(self, name: str) -> Corpus:
        """
        Creates an instance of Corpus by its name.
        Args:
            name (str): corpus name, must be available in DraCor. 
        Returns:
            Corpus: Instance of the Corpus class.
        Raises:
            CorpusNotFound: If the specified corpus name is not valid.
        """
        try:
            corpus = self._api.list_corpus_content(name)
        except NotFoundException as e:
            raise CorpusNotFound(f"The name {name} is not a valid corpus name") from e
        return Corpus(self._api, corpus)

    def get_play(self, corpus_name: str, play_name: str) -> Play:
        """
        Creates an instance of Play by the corpus name and the play name.
        Args:
            corpus_name (str): name of the corpus, must be available in DraCor. 
            play_name (str): name of the play, must be available in the DraCor corpus of corpus_name.
        Returns:
            Play: Instance of the Play class.
        Raises:
            PlayNotFound: If the specified play name is not valid within the given corpus.
        """
        try:
            play = self._api.play_info(corpus_name, play_name)
        except NotFoundException as e:
            raise PlayNotFound(f"The play name {play_name} is not a valid play name in corpus {corpus_name}") from e
        return Play(self._api, play)

    def get_resolve_play_id(self, dracor_play_id: str) -> None:
        """
        Resolves a DraCor play ID and redirects to the play URL.
        Args:
            dracor_play_id (str): ID of a play in DraCor. 
        Returns:
            None 
        """
        return self._api.resolve_id(dracor_play_id)

    def get_plays_with_character_by_id(
        self, wikidata_id: str
    ) -> List[PlayWithWikidataCharacter]:
        """
        Retrieves a list of plays that include a character with the specified Wikidata ID.
        Args:
            wikidata_id: Wikidata ID of a character. 
        Returns:
            List[PlayWithWikidataCharacter]: List of information about the plays including the character.    
        """
        return self._api.plays_with_character(wikidata_id)


class Corpus(CorpusModel):
    """
    Represents a DraCor corpus, extending the CorpusModel class and wrapping functionality
    for interacting the corpus' data through the PublicApi.

    Attributes:
        _api (PublicApi): An instance of the PublicApi class used to interact with the API.
    """
    _api: PublicApi

    def __init__(self, api: PublicApi, corpus_model: CorpusModel) -> None:
        """
        Initializes the Corpus instance with the given API and corpus model.
        Args:
            api (PublicApi): The API instance used to fetch corpus data.
            corpus_model (PlayModel): The base corpus model containing initial data.
        """
        super().__init__(**corpus_model.model_dump())
        self._api = api

    def get_metadata(self) -> List[PlayMetadata]:
        """
        Retrieves metadata for all plays in the corpus.
        Returns:
            List[PlayMetadata]: Metadata for the plays in the corpus.
        """
        return self._api.corpus_metadata(self.name)

    def get_metadata_csv(self) -> str:
        """
        Retrieves metadata for all plays in the corpus in CSV format.
        Returns:
            str: Metadata for the plays in the corpus in CSV format.
        """
        return self._api.corpus_metadata_csv_endpoint(self.name)

    def get_play(self, play_name: str) -> Optional[Play]:
        """
        Creates a play instance whith the corpus name and the play name. 
            Raises a PlayNotFound exception if the play name is not valid.
        Returns
            Play: An instance of the class Play. 
        """
        if play_name not in [play.name for play in self.plays]:
            raise PlayNotFound(f"The play name {play_name} is not a valid play name in corpus {self.name}.")
        play = self._api.play_info(self.name, play_name)
        return Play(self._api, play)


class Play(PlayModel):
    """
    A class representing a play, extending the PlayModel class and wrapping methods
    to interact with the play's data through the PublicApi.
    Attributes:
        _api (PublicApi): An instance of the PublicApi used to fetch data related to the play.
    """
    _api: PublicApi

    def __init__(self, api: PublicApi, play_model: PlayModel) -> None:
        """
        Initialize a Play instance.
        Args:
            api (PublicApi): The API instance used to fetch play data.
            play_model (PlayModel): The base play model containing initial data.
        """
        super().__init__(**play_model.model_dump())
        self._api = api

    def get_metrics(self) -> PlayMetrics:
        """
        Retrieve metrics for the play.
        Returns:
            PlayMetrics: Metrics data for the play.
        """
        return self._api.play_metrics(self.corpus, self.name)

    def get_tei(self) -> str:
        """
        Retrieve the TEI-XML representation of the play.
        Returns:
            str: The TEI-XML representation of the play.
        """
        return self._api.play_tei(self.corpus, self.name)
    
    def get_txt(self) -> str:
        """
        Retrieve the plain text representation of the play.
        Returns:
            str: The plain text representation of the play.
        """
        return self._api.play_txt(self.corpus, self.name)
    
    def get_characters(self) -> List[Character]:
        """
        Retrieve the list of characters in the play.
        Returns:
            List[Character]: A list of characters in the play.
        """
        return self._api.get_characters(self.corpus, self.name)

    def get_characters_csv(self) -> str:
        """
        Retrieve the list of characters in the play as a CSV string.
        Returns:
            str: A CSV string containing the characters in the play.
        """
        return self._api.get_characters_csv(self.corpus, self.name)

    def get_networkdata(self, download_format: DownloadFormat) -> str:
        """
        Retrieve network data for the play in the specified format.
        Args:
            download_format (DownloadFormat): The format in which to download the network data.
        Returns:
            str: The network data in the specified format.
        Raises:
            ValueError: If the specified download format is invalid.
        """
        if download_format == DownloadFormat.csv:
            return self._api.network_csv(self.corpus, self.name)
        elif download_format == DownloadFormat.gexf:
            return self._api.network_gexf(self.corpus, self.name)
        elif download_format == DownloadFormat.graphml:
            return self._api.network_graphml(self.corpus, self.name)
        else:
            raise ValueError(f"The download_format {download_format} is invalid. It must be one of: {', '.join([df.value for df in DownloadFormat])}")

    def get_relations(self, download_format: DownloadFormat) -> str:
        """
        Retrieve relations data for the play in the specified format.
        Args:
            download_format (DownloadFormat): The format in which to download the relations data.
        Returns:
            str: The relations data in the specified format.
        Raises:
            ValueError: If the specified download format is invalid.
        """
        if download_format == DownloadFormat.csv:
            return self._api.relations_csv(self.corpus, self.name)
        elif download_format == DownloadFormat.gexf:
            return self._api.relations_gexf(self.corpus, self.name)
        elif download_format == DownloadFormat.graphml:
            return self._api.relations_graphml(self.corpus, self.name)
        else:
            raise ValueError(f"The download_format {download_format} is invalid. It must must be one of: {', '.join([df.value for df in DownloadFormat])}")

    def get_spoken_text(
        self,
        sex: Optional[str] = None,
        role: Optional[str] = None,
        relation: Optional[str] = None,
        relation_active: Optional[str] = None,
        relation_passive: Optional[str] = None
    ) -> str:
        """
        Retrieve the spoken text in the play, optionally filtered by various parameters.
        Args:
            sex (Optional[str]): Filter by the sex of the speaker (MALE or FEMALE).
            role (Optional[str]): Filter by the role of the speaker.
            relation (Optional[str]): Filter by the relation of the speaker.
            relation_active (Optional[str]): Filter by the active relation of the speaker.
            relation_passive (Optional[str]): Filter by the passive relation of the speaker.
        Returns:
            str: The spoken text in the play, filtered by the specified parameters.
        """
        if sex:
            sex = sex.upper()
        return self._api.play_spoken_text(
            self.corpus, self.name, sex, role, relation, relation_active, relation_passive 
        )

    def get_spoken_text_by_character(self) -> List[SpokenTextByCharacter]:
        """
        Retrieve the spoken text in the play grouped by character.
        Returns:
            List[SpokenTextByCharacter]: A list of spoken text grouped by character.
        """
        return self._api.play_spoken_text_by_character(self.corpus, self.name)

    def get_stage_directions(self) -> str:
        """
        Retrieve the stage directions in the play.
        Returns:
            str: The stage directions in the play.
        """
        return self._api.play_stage_directions(self.corpus, self.name)

    def get_stage_directions_with_speakers(self) -> str:
        """
        Retrieve the stage directions and the spoken text of the play.
        Returns:
            str: The stage directions and spoken text of the play.
        """
        return self._api.play_stage_directions_with_speakers(self.corpus, self.name)
    

class Wikidata:
    """
    A wrapper class for interacting with DraCor Wikidata endpoints.

    This class provides methods to retrieve information about authors and
    access Mix'n'Match data from Wikidata.

    Attributes:
        _api (WikidataApi): An instance of the `WikidataApi` class used to
            interact with the Wikidata API.
    """

    def __init__(self, api_client=None) -> None:
        """
        Initializes the Wikidata wrapper with an optional API client.
        Args:
            api_client: An optional API client instance to use for requests.
        """
        self._api = WikidataApi(api_client)

    def get_author_info(self, wikidata_id: str) -> dict:
        """
        Retrieves information about an author from Wikidata using their Wikidata ID.
        Returns:
            dict: Author information provided by Wikidata.
        """
        return self._api.wikidata_author_info(wikidata_id)

    def get_mixnmatch(self) -> str:
        """
        Retrieves Mix'n'Match data from Wikidata, matching the DraCor plays to 
        Wikidata IDs.
        Returns:
            str: Matches of the DraCor plays to Wikidata IDs.
        """
        return self._api.wikidata_mixnmatch()

class DTS:
    """
    A wrapper class for interacting with DraCor DTS (Document Type Services) endpoints.

    This class provides methods to retrieve DTS entry points, collections, navigation, 
    and document data from the API.

    Attributes:
        _api (DTSApi): An instance of the `DTSApi` class used to interact with the DTS API.
    """

    def __init__(self, api_client=None, host=None) -> None:
        """
        Initializes the DTS wrapper with an optional API client or host.

        Args:
            api_client: An optional API client instance to use for requests.
            host: An optional host URL to configure the API client.
        """
        if host:
            configuration = Configuration(host=host)
            api_client = ApiClient(configuration=configuration)
        self._api = DTSApi(api_client)
    
    def get_dts(self) -> DtsEntrypoint:
        """
        Retrieves the DTS entry point from the API.

        Returns:
            DtsEntrypoint: The entry point data for the DTS API.
        """
        return self._api.dts_entrypoint()
    
    def get_collection(self,
                       collection_id: str,
                       nav: Optional[str] = None
                       ) -> dict:
        """
        Retrieves a specific DTS collection by its ID.

        Args:
            collection_id (str): The ID of the collection to retrieve.
            nav (Optional[str]): An optional navigation parameter.

        Returns:
            dict: The collection data.
        """
        return self._api.get_dts_collection(collection_id, nav)

    def get_navigation(self,
                       resource: str,
                       reference: Optional[str] = None,
                       start: Optional[str] = None,
                       end: Optional[str] = None
                       ) -> dict:
        """
        Retrieves navigation data for a specific resource. Either the reference can be 
        provided OR the start and end parameter.

        Args:
            resource (str): The resource ID to retrieve navigation data for.
            reference (Optional[str]): An optional reference parameter.
            start (Optional[str]): An optional start parameter for range-based navigation.
            end (Optional[str]): An optional end parameter for range-based navigation.

        Returns:
            dict: The navigation data.

        Raises:
            InvalidParameterCombination: If both 'reference' and 'start'/'end' are used together.
        """
        try:
            result = self._api.get_dts_navigation(resource, reference, start, end)
        except BadRequestException as e:
            raise InvalidParameterCombination(
                "Either use the parameter 'reference' or the parameters 'start' and 'end'. "
                "The use of both is not allowed."
            )
        return result

    def get_document(self,
                     resource: str,
                     reference: Optional[str] = None,
                     start: Optional[str] = None,
                     end: Optional[str] = None
                    ) -> str:
        """
        Retrieves document data for a specific resource. Either the reference can be 
        provided OR the start and end parameter.

        Args:
            resource (str): The resource ID to retrieve document data for.
            reference (Optional[str]): An optional reference parameter.
            start (Optional[str]): An optional start parameter for range-based retrieval.
            end (Optional[str]): An optional end parameter for range-based retrieval.

        Returns:
            str: The document data.

        Raises:
            InvalidParameterCombination: If both 'reference' and 'start'/'end' are used together.
        """
        try:
            result = self._api.get_dts_document(resource, reference, start, end)
        except BadRequestException as e:
            raise InvalidParameterCombination(
                "Either use the parameter 'reference' or the parameters 'start' and 'end'. "
                "The use of both is not allowed."
            )
        return result



