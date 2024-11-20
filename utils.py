# Copyright (C) 2024  Alexei Kartashov <zebra@alt-gnome.ru>


from enum import StrEnum, auto
import requests


class Branch(StrEnum):
    sisyphus = auto()
    p10 = auto()


class Arch(StrEnum):
    x86_64 = auto()
    ppc64le = auto()
    i586 = auto()
    aarch64 = auto()
    noarch = auto()


class Pckgs(dict[str, str]):
    ...


def get_pckgs(branch: Branch, arch: StrEnum, /) -> Pckgs:
    responce = requests.get(f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch.name}",
                            params={"arch": arch.name}
                            )
    return {i['name']: f"{i['version']}-{i['release']}" for i in responce.json()['packages']}
