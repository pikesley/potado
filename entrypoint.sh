#!/bin/bash

function __show_help() {
    echo "Container entrypoint commands:"
    echo "  schedule - apply the schedule found in 'conf/schedule.yaml'"
    echo "  init - set up default schedules given your existing zones"
    echo "  help - show this help"
    echo ""
    echo "Any other command will be executed within the container."
}

case ${1} in
  help )
    __show_help
    ;;

  schedule )
    shift
    cd /opt/potado
    make schedule
    ;;

  init )
    shift
    cd /opt/potado
    make init
    ;;

  * )
    exec "$@"
    ;;
esac
