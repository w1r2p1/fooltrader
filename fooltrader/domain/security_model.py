# -*- coding: utf-8 -*-
from elasticsearch_dsl import Keyword, Date

from fooltrader.domain import BaseDocType


class CryptocurrencyMeta(BaseDocType):
    id = Keyword()
    type = Keyword()
    exchange = Keyword()
    code = Keyword()
    name = Keyword()
    listDate = Date()
    timestamp = Date()

    class Meta:
        index = 'crypto_currency_meta'
        doc_type = 'doc'
