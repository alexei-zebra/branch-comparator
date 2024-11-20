#!/usr/bin/python3

# Utility for comparing altlinux branches
# v0.0.1

# Copyright (C) 2024  Alexei Kartashov <zebra@alt-gnome.ru>


import argparse
from json import dumps

import utils


def main():
    arg_parser = argparse.ArgumentParser(add_help=False,
                                         description='Utility for comparing altlinux branches')
    arg_parser.add_argument('--help', action='help',
                            help='show this help message and exit')
    arg_parser.add_argument("-a", "--arch", type=utils.Arch, default=utils.Arch.x86_64,
                            help=f"({'|'.join(utils.Arch._member_names_)}) set arch default {utils.Arch.x86_64}")
    arg_parser.add_argument("-h", "--human-readable", action='store_true', default=False,
                            help=f"prints in a human-readable format")
    args = arg_parser.parse_args()

    pckgs_p10 = utils.get_pckgs(utils.Branch.p10, args.arch)
    pckgs_sisyphus = utils.get_pckgs(utils.Branch.sisyphus, args.arch)

    outjson: dict[str, utils.Pckgs] = {
        "in_p10_not_in_sisyphus": [i for i in pckgs_p10 if not (i in pckgs_sisyphus.keys())],
        "in_sisyphus_not_in_p10": [i for i in pckgs_sisyphus if not (i in pckgs_p10.keys())],
        "in_p10_not_in_sisyphus": [i for i in pckgs_sisyphus if 0 < (utils.rpmvercmp(pckgs_sisyphus[i], pckgs_p10[i]) if i in pckgs_p10 else 1)]
    }

    print(dumps(outjson, indent=4) if args.human_readable else outjson)


if __name__ == "__main__":
    main()
