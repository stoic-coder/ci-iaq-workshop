def test_docker_is_installed(host):
    # testen, ob das Paket "docker-ce" installiert ist
    docker = host.package("docker")
    assert docker.is_installed()


def test_docker_service_is_running(host):
    # testen, ob der Service "docker" läuft und verfügbar ist
    service = host.service("docker")
    assert service.is_installed

def test_heroapp_container_is_running(host):
    # testen, ob der container mit dem Namen "my-hero-app" läuft
    docker = host.package("docker")
    container = docker.get_container("my-hero-app")
    assert container.is_running()

def test_heroapp_is_available_on_port_80(host):
    # testen, ob auf tcp://0.0.0.0:80 gehorcht wird
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening()
