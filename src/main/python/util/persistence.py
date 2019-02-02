import json
import logging

from datastructs import Entity


def load_entities(folder="entities"):
    from glob import glob
    entity_filenames = glob(f"{folder}/*.json")
    entities = [load_entity(filename=fn) for fn in entity_filenames]

    return entities


def save_entity(entity, filename):
    save_dataclass(json.loads(entity.to_json()), filename)


def load_entity(filename):
    d = load_dataclass(filename)
    return Entity.from_json(d)


def delete_entity(filename):
    from os import remove, path
    logging.info(f"deleting {filename}")
    if path.isfile(filename):
        remove(filename)


def save_dataclass(data, filename):
    try:
        logging.info(f"saving dataclass to {filename}")
        with open(filename, "w") as fp:
            json.dump(data, fp)
    except FileNotFoundError:
        logging.info(f"couldn't load dataclass from {filename}, file not "
                     f"found")


def load_dataclass(filename):
    data = {}
    try:
        logging.info(f"loading dataclass from {filename}")
        with open(filename, "r") as fp:
            data = json.load(fp)
    except FileNotFoundError:
        logging.info(f"couldn't load dataclass from {filename}, file not "
                     f"found")
    finally:
        return json.dumps(data)
