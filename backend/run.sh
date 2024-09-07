#!/bin/bash

case $1 in
    up)
        echo "raising all the services ..."
        docker-compose up
        ;;
    do**)
        echo "deregister the server ..."
        docker-compose down
        echo "-> service is down ..."
        ;;
    she**)
        # ! script from  https://gist.github.com/prozz/8bdda7bcc12db7b877f9014ffae2eab9
        echo "Executing shell in web container ..."

        name="${2:-web}" # * it take a value by defaul called "web"
        containerId=$(docker ps | grep $name | grep -o '^\w\+')

        if [ $(echo $containerId | wc -w) -gt 1 ];
        then
            echo "Multiple docker containers found for: $name"
            exit 0
        fi

        if [[ -n "$containerId" ]]; then
            docker exec -it $containerId /bin/bash -c "python manage.py shell"
        else
            echo "No docker container with name: $name is running"
        fi
        ;;
    ba**)
        # ! script from  https://gist.github.com/prozz/8bdda7bcc12db7b877f9014ffae2eab9
        echo "Executing shell in web container ..."

        name="${2:-web}" # * it take a value by defaul called "web"
        containerId=$(docker ps | grep $name | grep -o '^\w\+')

        if [ $(echo $containerId | wc -w) -gt 1 ];
        then
            echo "Multiple docker containers found for: $name"
            exit 0
        fi

        if [[ -n "$containerId" ]]; then
            docker exec -it $containerId /bin/bash
        else
            echo "No docker container with name: $name is running"
        fi
        ;;
    *)
        echo "Raising the web server ..."
        docker-compose up -d db
        docker-compose run --rm --service-ports web python manage.py runserver 0:8000
        ;;
esac