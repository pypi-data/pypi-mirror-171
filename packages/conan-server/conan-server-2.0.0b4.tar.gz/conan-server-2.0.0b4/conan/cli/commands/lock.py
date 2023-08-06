import os

from conan.api.output import ConanOutput
from conan.cli.command import conan_command, COMMAND_GROUPS, OnceArgument, \
    conan_subcommand
from conan.cli.commands import make_abs_path
from conan.cli.commands.install import common_graph_args, graph_compute, _get_conanfile_path
from conan.cli.common import save_lockfile_out, get_lockfile
from conans.errors import ConanException
from conans.model.graph_lock import Lockfile, LOCKFILE
from conans.model.recipe_ref import RecipeReference


@conan_command(group=COMMAND_GROUPS['consumer'])
def lock(conan_api, parser, *args):
    """
    Create or manages lockfiles
    """


@conan_subcommand()
def lock_create(conan_api, parser, subparser, *args):
    """
    Create a lockfile from a conanfile or a reference
    """
    common_graph_args(subparser)
    args = parser.parse_args(*args)

    # parameter validation
    if args.requires and (args.name or args.version or args.user or args.channel):
        raise ConanException("Can't use --name, --version, --user or --channel arguments with "
                             "--requires")

    deps_graph, lockfile = graph_compute(args, conan_api, partial=True)

    if args.lockfile_out is None:
        cwd = os.getcwd()
        path = _get_conanfile_path(args.path, cwd, py=None) if args.path else None
        lock_folder = os.path.dirname(path) if path else cwd
        args.lockfile_out = os.path.join(lock_folder, "conan.lock")

    save_lockfile_out(args, deps_graph, lockfile, os.getcwd())


@conan_subcommand()
def lock_merge(conan_api, parser, subparser, *args):
    """
    Merge 2 or more lockfiles
    """
    subparser.add_argument('--lockfile', action="append", help='Path to lockfile to be merged')
    subparser.add_argument("--lockfile-out", action=OnceArgument, default=LOCKFILE,
                           help="Filename of the created lockfile")

    args = parser.parse_args(*args)

    result = Lockfile()
    for lockfile in args.lockfile:
        lockfile = make_abs_path(lockfile)
        graph_lock = Lockfile.load(lockfile)
        result.merge(graph_lock)

    lockfile_out = make_abs_path(args.lockfile_out)
    result.save(lockfile_out)
    ConanOutput().info("Generated lockfile: %s" % lockfile_out)


@conan_subcommand()
def lock_add(conan_api, parser, subparser, *args):
    """
    Add requires, build-requires or python-requires to existing or new lockfile. Resulting lockfile
    will be ordereded, newer versions/revisions first.
    References can be with our without revisions like "--requires=pkg/version", but they
    must be package references, including at least the version, they cannot contain a version range
    """
    subparser.add_argument('--requires', action="append", help='Add references to lockfile.')
    subparser.add_argument('--build-requires', action="append",
                           help='Add build-requires to lockfile')
    subparser.add_argument('--python-requires', action="append",
                           help='Add python-requires to lockfile')

    subparser.add_argument("--lockfile-out", action=OnceArgument, default=LOCKFILE,
                           help="Filename of the created lockfile")
    subparser.add_argument("--lockfile", action=OnceArgument, help="Filename of the input lockfile")
    args = parser.parse_args(*args)

    lockfile = get_lockfile(args.lockfile, os.getcwd(), None, partial=True)
    if lockfile is None:
        lockfile = Lockfile()  # create a new lockfile
    requires = [RecipeReference.loads(r) for r in args.requires] if args.requires else None
    build_requires = [RecipeReference.loads(r) for r in args.build_requires] \
        if args.build_requires else None
    python_requires = [RecipeReference.loads(r) for r in args.python_requires] \
        if args.python_requires else None

    lockfile.add(requires=requires, build_requires=build_requires, python_requires=python_requires)

    lockfile_out = make_abs_path(args.lockfile_out)
    lockfile.save(lockfile_out)
    ConanOutput().info("Generated lockfile: %s" % lockfile_out)
