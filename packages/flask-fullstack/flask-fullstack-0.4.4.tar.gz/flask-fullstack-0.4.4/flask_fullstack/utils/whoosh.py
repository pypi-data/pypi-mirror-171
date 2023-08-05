from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.event import listen
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import Select
from whooshalchemy import Searcher as SearcherBase, IndexService as IndexServiceBase


class IndexService(IndexServiceBase):
    def __init__(self, config=None, session=None, whoosh_base=None):
        super().__init__(config, session, whoosh_base)

        def wrap_before_commit(session, *_):
            return self.before_commit(session)

        for event in ("before_flush", "after_flush"):
            listen(Session, event, wrap_before_commit)

    def register_as_searchable(self, *searchable: str):
        """
        - Registers database model as searchable with whoosh-sqlalchemy.
        - Adds ``search_stmt`` field (:class:`Searcher`) to the class for searching.

        :param searchable: names of model's fields to create the whoosh schema on
        """

        def register_as_searchable_wrapper(model):
            model.__searchable__ = list(searchable)
            self.register_class(model)

            searcher = model.search_query
            model.search_stmt = Searcher(
                searcher.model_class,
                searcher.primary,
                searcher.index,
            )

            return model

        return register_as_searchable_wrapper


class Searcher(SearcherBase):
    def __call__(self, query, limit=None, stmt: Select = None):
        results = self.index.searcher().search(self.parser.parse(query))
        keys = [x[self.primary] for x in results]
        primary_column = getattr(self.model_class, self.primary)

        if stmt is None:
            stmt = select(self.model_class)
        return stmt.filter(primary_column.in_(keys))
