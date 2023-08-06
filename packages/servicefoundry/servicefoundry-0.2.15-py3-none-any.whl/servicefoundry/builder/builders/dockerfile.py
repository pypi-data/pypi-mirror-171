from typing import Optional

from servicefoundry.auto_gen.models import DockerFileBuild
from servicefoundry.builder.utils import build_docker_image

__all__ = ["build"]


def build(
    tag: str,
    build_configuration: DockerFileBuild,
    cache_from: Optional[str] = None,
):
    build_docker_image(
        tag=tag,
        path=build_configuration.build_context_path,
        file=build_configuration.dockerfile_path,
        cache_from=cache_from,
    )
