if ! [[ -x ./scripts/bridge_connect.sh ]]
then
    chmod +x ./scripts/bridge_connect.sh
fi
docker compose up -d && ./scripts/bridge_connect.sh