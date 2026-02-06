from argparse import Namespace

import pytest

from scikit_package.cli.add import print_deprecation_docstring


@pytest.mark.parametrize(
    "input,expected_print",
    [
        (
            [  # UC: user prints docstring without new base
                # expect: deprecation docstring prints without new base
                "new_func",
                "4.0.0",
            ],
            "This function has been deprecated and will be "
            "removed in version 4.0.0.\n"
            "Please use new_func instead.",
        ),
        (  # UC: user prints docstring with new base
            # expect: deprecation docstring prints with new base
            ["new_func", "4.0.0", "-n", "diffpy.foo"],
            "This function has been deprecated and will be "
            "removed in version 4.0.0.\n"
            "Please use diffpy.foo.new_func instead.",
        ),
    ],
)
def test_print_deprecation_docstring(capsys, input, expected_print):
    args = Namespace(
        new_name=input[0],
        removal_version=input[1],
        new_base=input[3] if len(input) > 3 else None,
    )
    print_deprecation_docstring(args)
    captured = capsys.readouterr()
    actual_print = captured.out.rstrip()
    assert actual_print == expected_print.rstrip()
