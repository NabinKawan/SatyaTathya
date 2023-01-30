from dependency_injector import containers, providers

from app.services.db_service import DbService


# WIP dependency injection
class AppContainer(containers.DeclarativeContainer):
    """
    container to store providers
    """

    wiring_config = containers.WiringConfiguration(
        packages=["app.services"]
    )
    db_service = providers.Dependency(instance_of=DbService)
