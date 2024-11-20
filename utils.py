# Copyright (C) 2024  Alexei Kartashov <zebra@alt-gnome.ru>


from enum import StrEnum, auto
import requests

import subprocess as sp


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


def rpmvercmp(ver1: str, ver2: str) -> int:
    # this implementation is used because the rpmvercmp algarithm rewritten in python is slow
    return int(sp.run(f"rpmvercmp {ver1} {ver2}", check=True, text=True, shell=True,
                      stdout=sp.PIPE, stderr=sp.PIPE
                      ).stdout)
