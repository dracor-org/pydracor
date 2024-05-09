#!/usr/bin/env python
from __future__ import annotations

from enum import Enum
from typing import List, Optional

from openapi_client.api.public_api import PublicApi
from openapi_client.api.wikidata_api import WikidataApi
from openapi_client.models import Corpus as CorpusModel
from openapi_client.models import Info
from openapi_client.models import Play as PlayModel
from openapi_client.models import PlayMetadata
from openapi_client.models.character import Character
from openapi_client.models.corpus_in_corpora import CorpusInCorpora
from openapi_client.models.play_metrics import PlayMetrics
from openapi_client.models.play_with_wikidata_character import PlayWithWikidataCharacter
from openapi_client.models.spoken_text_by_character import SpokenTextByCharacter


class DownloadFormat(str, Enum):
    csv = "csv"
    gexf = "gexf"
    graphml = "graphml"


class DraCorAPI:

    def __init__(self, api_client=None) -> None:
        self._api = PublicApi(api_client)

    def get_info(self) -> Info:
        return self._api.api_info()

    def get_corpora(self) -> List[CorpusInCorpora]:
        return self._api.list_corpora()

    # how do we pass the name to the corpus object?
    def get_corpus(self, name: str) -> Corpus:
        corpus = self._api.list_corpus_content(name)
        return Corpus(self._api, corpus)

    def get_play(self, corpus_name: str, play_name: str) -> Play:
        play = self._api.play_info(corpus_name, play_name)
        return Play(self._api, play)

    def get_resolve_play_id(self, dracor_play_id: str) -> None:
        return self._api.resolve_id(dracor_play_id)

    def get_plays_with_character_by_id(
        self, wikidata_id: str
    ) -> List[PlayWithWikidataCharacter]:
        return self._api.plays_with_character(wikidata_id)


class Corpus(CorpusModel):
    _api: PublicApi

    def __init__(self, api: PublicApi, corpus_model: CorpusModel) -> None:
        super().__init__(**corpus_model.dict())
        self._api = api

    # def _populate_corpus(self)

    def get_metadata(self) -> List[PlayMetadata]:
        return self._api.corpus_metadata(self.name)

    def get_metadata_csv(self) -> str:
        return self._api.corpus_metadata_csv_endpoint(self.name)

    def get_play(self, play_name: str) -> Optional[Play]:
        if play_name not in [play.name for play in self.plays]:
            return None
        play = self._api.play_info(self.name, play_name)
        return Play(self._api, play)


class Play(PlayModel):
    _api: PublicApi

    def __init__(self, api: PublicApi, play_model: PlayModel) -> None:
        super().__init__(**play_model.dict())
        self._api = api

    # is name ok? same in auto-generated, but in API is only {play}
    # returns a Play object -> how to handle here?
    def get_info(self) -> PlayModel:
        return self._api.play_info(self.corpus, self.name)

    def get_metrics(self) -> PlayMetrics:
        return self._api.play_metrics(self.name, self.name)

    def get_tei(self) -> str:
        return self._api.play_tei(self.corpus, self.name)

    def get_characters(self) -> List[Character]:
        return self._api.get_characters(self.corpus, self.name)

    def get_characters_csv(self) -> str:
        return self._api.get_characters_csv(self.corpus, self.name)

    def get_networkdata(self, download_format: DownloadFormat) -> str:
        if download_format == DownloadFormat.csv:
            return self._api.network_csv(self.corpus, self.name)
        elif download_format == DownloadFormat.gexf:
            return self._api.network_gexf(self.corpus, self.name)
        elif download_format == DownloadFormat.graphml:
            return self._api.network_graphml(self.corpus, self.name)
        else:
            raise ValueError

    def get_relations_csv(self, download_format: DownloadFormat) -> str:
        if download_format == DownloadFormat.csv:
            return self._api.relations_csv(self.corpus, self.name)
        elif download_format == DownloadFormat.gexf:
            return self._api.relations_gexf(self.corpus, self.name)
        elif download_format == DownloadFormat.graphml:
            return self._api.relations_graphml(self.corpus, self.name)
        else:
            raise ValueError

    # how to handle gender here? need to check – where is it checked?
    # is enum in openai specs, but 'role' is not
    def get_spoken_text(
        self,
        gender: Optional[str] = None,
        relation: Optional[str] = None,
        role: Optional[str] = None,
    ) -> str:
        return self._api.play_spoken_text(
            self.corpus, self.name, gender, relation, role
        )

    def get_spoken_text_by_character(self) -> List[SpokenTextByCharacter]:
        return self._api.play_spoken_text_by_character(self.corpus, self.name)

    def get_stage_directions(self) -> str:
        return self._api.play_stage_directions(self.corpus, self.name)

    def get_stage_directions_with_speaker(self) -> str:
        return self._api.play_stage_directions_with_speakers(self.corpus, self.name)


class Wikidata:

    def __init__(self, api_client=None) -> None:
        self._api = WikidataApi(api_client)

    def get_author_info(self, wikidata_id: str) -> object:
        return self._api.wikidata_author_info(wikidata_id)

    def get_mixnmatch(self) -> str:
        return self._api.wikidata_mixnmatch()
