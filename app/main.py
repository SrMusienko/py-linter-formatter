def format_linter_error(error: dict) -> dict:

    return {
        "name": [val for key, val in error.items() if key == "code"][0],
        "line": [val for key, val in error.items() if key == "line_number"][0],
        "column":
            [val for key, val in error.items() if key == "column_number"][0],
        "message": [val for key, val in error.items() if key == "text"][0],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(i) for i in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [
        format_single_linter_file(key, linter_report[key])
        if bool(linter_report.get(key))
        else {
            "errors": [],
            "path": key,
            "status": "passed"
        }
        for key in linter_report.keys()
    ]
