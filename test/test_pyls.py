import pytest
import json
from pyls.ls import PyLS
import argparse
from typing import Optional
from pyls.parser import PyLSParser

test_json_file = "test/test_json.json"


def simulate_options(
    path: str = ".",
    l: bool = False,
    A: bool = False,
    r: bool = False,
    t: bool = False,
    h: bool = False,
    help: bool = False,
    filter: Optional[str] = None,
) -> argparse.Namespace:
    # Mock the argparse Namespace with default options
    return argparse.Namespace(
        path=path, l=l, A=A, r=r, t=t, h=h, help=help, filter=filter
    )


def start_test(test_options: argparse.Namespace) -> str:
    with open(test_json_file) as f:
        sample_json_structure = json.load(f)

    parser = PyLSParser()
    parser.set_args(test_options)

    parser.check_args()

    if parser.args.help:
        parser.help_string_output()
    else:
        args = parser.args
        pyls = PyLS(json_structure=sample_json_structure, options=args)
        pyls.generate_output()

        return pyls.get_output()


def test_help_output(capfd):
    test_options = simulate_options(help=True, path="")
    with pytest.raises(SystemExit):
        start_test(test_options)
        captured = capfd.readouterr()
        assert "usage" in captured.out


def test_output():
    test_options = simulate_options()
    assert "file1" in start_test(test_options)


def test_all_files_output():
    test_options = simulate_options(A=True)
    assert "file1" in start_test(test_options)


def test_list_all_info_output():
    test_options = simulate_options(A=True, l=True)
    assert "file1" in start_test(test_options)


def test_reverse_order_output():
    test_options = simulate_options(r=True)
    assert "file1" in start_test(test_options)


def test_human_readable_output():
    test_options = simulate_options(h=True, l=True)
    assert "M" in start_test(test_options)


def test_only_files_output():
    test_options = simulate_options(filter="file")
    assert "file1" in start_test(test_options)


def test_only_dirs_output():
    test_options = simulate_options(filter="dir")
    assert "dir1" in start_test(test_options)


def test_time_ordered_output():
    test_options = simulate_options(t=True)
    assert "file1" in start_test(test_options)


def test_nested_output():
    test_options = simulate_options(path="root/dir1")
    assert "file2" in start_test(test_options)


def test_alias_output():
    test_options = simulate_options(path="root")
    assert "file1" in start_test(test_options)


def test_not_correct_filter(capfd):
    test_options = simulate_options(filter="files")
    with pytest.raises(SystemExit):
        start_test(test_options)
        captured = capfd.readouterr()
        assert "error" in captured.out


def test_not_exists_path(capfd):
    test_options = simulate_options(path="dir4")
    with pytest.raises(SystemExit):
        start_test(test_options)
        captured = capfd.readouterr()
        assert "error" in captured.out
