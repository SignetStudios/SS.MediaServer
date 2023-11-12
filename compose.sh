if ! [[ -x ./scripts/bridge_connect.sh ]]
then
    chmod +x ./scripts/bridge_connect.sh
fi

git pull

docker compose up -d --remove-orphans && ./scripts/bridge_connect.sh