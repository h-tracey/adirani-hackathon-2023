# pylint: disable=no-member, import-error
from dependency_injector import containers, providers
from repos.data_driver import DataRepo
from services.analysis_engine import AnalysisEngine

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_yaml("config.yml", envs_required=True)

    repo_factory = providers.ThreadSafeSingleton(
        DataRepo,
        sql_url=config.sql.conn_str()
    )
    analysis_service = providers.Factory(
        AnalysisEngine,
        repo_factory
    )
