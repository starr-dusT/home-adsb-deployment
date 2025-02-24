# ADSB Grab Bag
> All the ADSB things in one convenient bag.

## Setup

Build containers used for [dump1090](https://github.com/flightaware/dump1090.git) and [tar1090](https://github.com/wiedehopf/tar1090):

```
docker build -t dump1090 -f Dockerfile.dump1090 .
docker build -t tar1090 -f Dockerfile.tar1090 .
```

Edit [docker-compose.yml](./docker-compose.yml). Primarily changes needed will be:

- `commands` section of `dump1090` which defines SDR specific configuration
- `environment` section of `tar1090` which defines the timezone, BEASTHOST IP, and home position of SDR

## Usage

Containers to host `dump1090` and `tar1090` can be start/stopeed with docker-compose. Additionally, `rec1090.sh` can be used to record the sbs output to a file. See [rec1090.sh](./rec1090.sh) for usage instructions.
