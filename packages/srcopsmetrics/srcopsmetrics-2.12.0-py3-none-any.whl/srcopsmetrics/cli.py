#!/usr/bin/env python3
# SrcOpsMetrics
# Copyright(C) 2019, 2020 Francesco Murdaca, Dominik Tuchyna
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""This is the CLI for SrcOpsMetrics to create, visualize, use bot knowledge."""

import logging
import os
from datetime import date, timedelta
from typing import List, Optional

import click
from tqdm.contrib.logging import logging_redirect_tqdm

from srcopsmetrics.bot_knowledge import analyse_projects
from srcopsmetrics.enums import EntityTypeEnum, StoragePath
from srcopsmetrics.github_knowledge import GitHubKnowledge
from srcopsmetrics.kebechet_metrics import KebechetMetrics
from srcopsmetrics.kebechet_sli_slo_metrics import KebechetSliSloMetrics

_LOGGER = logging.getLogger("aicoe-src-ops-metrics")
logging.basicConfig(level=logging.INFO)


def _parse_entities(entities_raw: Optional[str]) -> List[str]:
    """Get passed entities as list."""
    if entities_raw and entities_raw != "":
        return [e.strip() for e in entities_raw.split(",")]

    return []


def _parse_repos(repository: Optional[str], organization: Optional[str]):
    repos = []

    if repository:
        for rep in repository.split(","):
            repos.extend(GitHubKnowledge().get_repositories(repository=rep.strip()))
    if organization:
        repos.extend(GitHubKnowledge().get_repositories(organization=organization))

    return repos


def _check_env_vars(is_local: bool):
    if not is_local:
        ceph_needed_vars = ["CEPH_KEY_ID", "CEPH_SECRET_KEY", "CEPH_BUCKET_PREFIX", "S3_ENDPOINT_URL", "CEPH_BUCKET"]
        missing = []
        for env in ceph_needed_vars:
            if os.getenv(env) is None:
                missing.append(env)

        if len(missing) > 0:
            _LOGGER.warning("--is_local option is not set but Ceph environment variables are missing.")
            _LOGGER.warning("Missing: " + ",".join(env))

    if os.getenv("GITHUB_ACCESS_TOKEN") is None:
        _LOGGER.warning(
            "Missing GITHUB_ACCESS_TOKEN environment variable; The rate limit of GitHub API request will be limited"
        )


def _set_env_vars(is_local: bool, knowledge_path: Optional[str], merge_path: Optional[str]):
    os.environ["IS_LOCAL"] = "True" if is_local else "False"
    os.environ[StoragePath.LOCATION_VAR.value] = knowledge_path
    os.environ[StoragePath.MERGE_LOCATION_ENVVAR_NAME.value] = merge_path


@click.command()
@click.option(
    "--repository",
    "-r",
    type=str,
    required=False,
    help="""Repository to be analysed (e.g thoth-station/performance)
            Multiple repositories are supported - just separate repos
            by comma (e.g. -r x/foo,y/bar,z/qua)""",
)
@click.option(
    "--organization",
    "-o",
    type=str,
    required=False,
    help="All repositories of an Organization to be analysed",
)
@click.option(
    "--create-knowledge",
    "-c",
    is_flag=True,
    help=f"""Create knowledge from a project repository.
            Storage location is {StoragePath.KNOWLEDGE.value}
            Removes all previously processed storage""",
)
@click.option(
    "--is-local",
    "-l",
    is_flag=True,
    help="Use local for knowledge loading and storing.",
)
@click.option(
    "--entities",
    "-e",
    type=str,
    required=False,
    help="""Entities to be analysed for a repository.
            For multiple entities please use format
            -e Foo,Bar,...
            If nothing specified, all entities will be analysed.
            Current entities available are:
            """
    + "\n".join([entity.value for entity in EntityTypeEnum]),
)
@click.option(
    "--knowledge-path",
    "-k",
    default=StoragePath.DEFAULT.value,
    required=False,
    help=f"""Environment variable named {StoragePath.LOCATION_VAR}
            with path where all the analysed and processed knowledge
            are stored. Default knowledge path is {StoragePath.DEFAULT.value}
            """,
)
@click.option(
    "--thoth",
    "-t",
    is_flag=True,
    required=False,
    help="""Launch performance analysis of Thoth Kebechet managers for specified repository for yesterday.""",
)
@click.option(
    "--metrics",
    "-x",
    is_flag=True,
    required=False,
    help="""Launch Metrics Calculation for specified repository.""",
)
@click.option(
    "--merge",
    "-m",
    is_flag=True,
    required=False,
    help="""Merge all of the aggregated data under given KNOWLEDGE_PATH.""",
)
@click.option(
    "--merge-path",
    "-M",
    required=False,
    default=StoragePath.MERGE_PATH.value,
    help="""Data/statistics are stored under this path.""",
)
@click.option(
    "--sli-slo",
    is_flag=True,
    required=False,
    help="""Launch sli-slo metrics calculation given repositories. Must be used in conjunction with -t""",
)
def cli(
    repository: Optional[str],
    organization: Optional[str],
    create_knowledge: bool,
    is_local: bool,
    entities: Optional[str],
    knowledge_path: str,
    thoth: bool,
    metrics: bool,
    merge: bool,
    merge_path: str,
    sli_slo: bool,
):
    """Command Line Interface for SrcOpsMetrics."""
    _check_env_vars(is_local=is_local)
    _set_env_vars(is_local=is_local, knowledge_path=knowledge_path, merge_path=merge_path)

    repos = _parse_repos(repository=repository, organization=organization)
    entities_args = _parse_entities(entities)

    if create_knowledge:
        analyse_projects(repositories=repos, is_local=is_local, entities=entities_args)

    # for project in repos:
    #     os.environ["PROJECT"] = project

    today = date.today()
    yesterday = today - timedelta(days=1)

    if thoth:
        _LOGGER.info("#### Launching thoth data analysis ####")

        if repos and not merge and not sli_slo:
            for repo in repos:
                _LOGGER.info("Creating metrics for repository %s" % repo)
                kebechet_metrics = KebechetMetrics(repository=repo, day=yesterday, is_local=is_local)
                kebechet_metrics.evaluate_and_store_kebechet_metrics()

        if sli_slo:
            _LOGGER.info("#### Inspecting kebechet repositories and creating SLI/SLO metrics ####")
            keb_sli_slo = KebechetSliSloMetrics(repositories=repos, is_local=is_local)
            keb_sli_slo.evaluate_and_store_sli_slo_kebechet_metrics()
            # keb_sli_slo.evaluate_and_store_usage_timestamp_sli_slo_kebechet_metrics()

    if merge:
        if thoth:
            _LOGGER.info("Merging kebechet metrics for %s" % yesterday)

            ## TODO: merge action omitted ?
            KebechetMetrics.merge_kebechet_metrics_per_day(day=yesterday, is_local=is_local)
        else:
            raise NotImplementedError


if __name__ == "__main__":
    with logging_redirect_tqdm():
        cli(auto_envvar_prefix="MI")
