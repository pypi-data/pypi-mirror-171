"""
parses haimdall arguments
"""
import argparse


def mk_args():
    parser = argparse.ArgumentParser(description="run: python -m joringels.src.joringels info")
    parser.add_argument("action", metavar="action", nargs=None, help="see joringels_code actions")

    parser.add_argument(
        "-k",
        "--key",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default=None,
        help="key to encrypt/decrypt",
    )

    parser.add_argument(
        "-nk",
        "--newKey",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default=None,
        help="provide a source for new key, i.e. os",
    )
    # currently not used but should be used in upload instead of host
    parser.add_argument(
        "-pr",
        "--projectName",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default=None,
        help="target to be uploaded (i.e. asgard), use 'all' to upload to all targets",
    )

    parser.add_argument(
        "-ip",
        "--host",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default=None,
        help="ip address to get secrets from",
    )

    parser.add_argument(
        "-p",
        "--port",
        required=False,
        nargs="?",
        const=7000,
        type=int,
        default=7000,
        help="port to get secrets from",
    )

    parser.add_argument(
        "-n",
        "--safeName",
        required=False,
        nargs="?",
        const=None,
        type=str,
        default=None,
        help="dataSafe title in kdbx",
    )

    parser.add_argument(
        "-e",
        "--entryName",
        required=False,
        nargs="?",
        const=None,
        type=str,
        default=None,
        help="entry title in kdbx",
    )

    parser.add_argument(
        "-src",
        "--source",
        required=False,
        nargs="?",
        const=None,
        type=str,
        default="kdbx",
        help="source of secrets, i.e. kdbx NOTE: if needed provide full path",
    )

    parser.add_argument(
        "-con",
        "--connector",
        required=False,
        nargs="?",
        const=None,
        type=str,
        default="scp",
        help="upload connector i.e. powershell scp",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        nargs="?",
        const=1,
        type=int,
        default=0,
        help="0:silent, 1:user, 2:debug",
    )

    parser.add_argument(
        "-y",
        "--allYes",
        required=False,
        nargs="?",
        const=1,
        type=bool,
        default=None,
        help="run without confirm, not used",
    )

    parser.add_argument(
        "-rt",
        "--retain",
        required=False,
        nargs="?",
        const=True,
        type=bool,
        default=False,
        help="retain (keep) secrets after reading",
    )

    parser.add_argument(
        "-hard",
        "--hard",
        required=False,
        nargs="?",
        const=True,
        type=bool,
        default=False,
        help="PERMANENT CHANGE",
    )

    return parser.parse_args()
