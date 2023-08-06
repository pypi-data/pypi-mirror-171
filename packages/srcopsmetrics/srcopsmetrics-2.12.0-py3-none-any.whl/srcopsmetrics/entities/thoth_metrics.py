# Copyright (C) 2022 Dominik Tuchyna
#
# This file is part of thoth-station/mi - Meta-information Indicators.
#
# thoth-station/mi - Meta-information Indicators is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# thoth-station/mi - Meta-information Indicators is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with thoth-station/mi - Meta-information Indicators.  If not, see <http://www.gnu.org/licenses/>.

"""Thoth metrics."""

from typing import List

from voluptuous.schema_builder import Schema
from voluptuous.validators import Any

from srcopsmetrics.entities import Entity


class ThothMetrics(Entity):
    """Thoth manager metrics template class for a repository.

    Intended to be used only within polymorphism for loading and storing operations.
    """

    entity_schema = Schema({int: {str: Any(str, int)}})

    def analyse(self) -> List[Any]:
        """Override :func:`~Entity.analyse`."""
        raise NotImplementedError("cannot use with metrics")

    def store(self, github_entity):
        """Override :func:`~Entity.store`."""
        raise NotImplementedError("cannot use with metrics")

    def get_raw_github_data(self):
        """Override :func:`~Entity.get_raw_github_data`."""
        raise NotImplementedError("cannot use with metrics")
