#!/usr/bin/env python3
import docker as dockerlib

docker = dockerlib.from_env()


class DockerContainer:
    def __init__(self, image_name):
        self._image_name = image_name

    def __enter__(self):
        self._container = docker.containers.run(image=self._image_name, detach=True)
        return self._container

    def __exit__(self, *args):
        self._container.kill()
        self._container.remove()


if __name__ == '__main__':
    with DockerContainer("zebro") as zebro:
        try:
            for line in zebro.logs(stream=True):
                print(">> %s" % line)
        except InterruptedError as e:
            pass
