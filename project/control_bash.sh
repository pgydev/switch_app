#!/bin/bash


IMAGE_NAME="image_name"
DOCKERFILE_PATH="dockerfile_name"
CONTAINER_NAME="container_name"


function build_docker_image() {
    docker build -t "$IMAGE_NAME" "$DOCKERFILE_PATH"
}

function start_docker_container() {
    docker run -d --name "$CONTAINER_NAME" $PORT_OPTIONS $VOLUME_OPTIONS $ENV_OPTIONS "$IMAGE_NAME"
}

function stop_docker_container() {
    docker stop "$CONTAINER_NAME" && docker rm "$CONTAINER_NAME"
}

case "$1" in
    build)
        build_docker_image
        ;;
    start)
        start_docker_container
        ;;
    stop)
        stop_docker_container
        ;;
    *)
        exit 1
esac
