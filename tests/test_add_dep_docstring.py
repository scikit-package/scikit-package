import argparse

import pytest

from scikit_package.cli.add import print_deprecation_docstring


@pytest.mark.parametrize(
    "input,expected_print",
    [
        (
            [
                "new_func",
                "4.0.0",
            ],
            "This function has been deprecated and will be "
            "removed in version 4.0.0.\n"
            "Please use new_func instead.",
        ),
        (
            ["new_func", "4.0.0", "-n", "diffpy.foo"],
            "This function has been deprecated and will be "
            "removed in version 4.0.0.\n"
            "Please use diffpy.foo.new_func instead.",
        ),
    ],
)
def test_print_deprecation_docstring(capsys, input, expected_print):
    # Test the deprecation docstring prints given args
    parser = argparse.ArgumentParser()
    parser.add_argument("new_name")
    parser.add_argument("removal_version")
    parser.add_argument("-n", "--new-base", default=None)
    args = parser.parse_args(input)
    print_deprecation_docstring(args)
    captured = capsys.readouterr()
    actual_print = captured.out.rstrip()
    assert actual_print == expected_print.rstrip()
