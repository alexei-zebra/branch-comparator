# Copyright (C) 2024  Alexei Kartashov <zebra@alt-gnome.ru>


from enum import StrEnum, auto


class Branch(StrEnum):
    sisyphus = auto()
    p10 = auto()


class Arch(StrEnum):
    x86_64 = auto()
    ppc64le = auto()
    i586 = auto()
    aarch64 = auto()
    noarch = auto()


def get_pckgs(branch:Branch, arch:StrEnum, /) -> dict[str, ]:
    pass