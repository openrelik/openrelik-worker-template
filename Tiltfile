# This is a Tilt configuration file
# Documentation https://docs.tilt.dev/docker_compose.html
#
# It is used to hot reload changed code into your worker container
# and assist in developing faster. No need to rebuild the container
# on every change.
#
# HOWTO
# 1. Install Tilt (single binay!) https://docs.tilt.dev/
# 2. Change the location of the docker_compose() file below.
# 3. Change image name you are working on below.
# 4. Run `tilt up` and open the web interface

# Enforce a minimum Tilt version, so labels are supported
# https://docs.tilt.dev/api.html#api.version_settings
version_settings(constraint=">=0.22.1")

docker_compose("../openrelik/openrelik/docker-compose.yml")

docker_build(
    # Image name - must match the image in the docker-compose file
    "ghcr.io/openrelik/openrelik-worker-template",
    # Docker context
    ".",
    live_update=[
        # Sync local files into the container.
        sync("./src", "/openrelik"),
        # Restart the process to pick up the changed files.
        restart_container(),
    ],
)
