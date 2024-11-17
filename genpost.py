#


# Created on Sun Nov 17 2024


# Copyright (c) 2024 Huy Truong


# ------------------------------


# Purpose: create/ update/ delete post as .md file


# ------------------------------


#


from typing import Any, Callable

import numpy as np
from collections import OrderedDict
from datetime import datetime

import argparse
import re


DATETIME_FORMAT: str = "%Y-%m-%d %H:%M"
MSG_LIMIT: int = 70


def create_act(
    uni_act_name: str,
    date: str,
    msg: str,
    hyper_link: str | None = None,
    content_path: str = "github/content",
    pelican_kwargs: OrderedDict[str, Any] = {},
) -> str:
    # add headers

    if "title" not in pelican_kwargs:
        pelican_kwargs["title"] = msg

    if "date" not in pelican_kwargs:
        pelican_kwargs["date"] = date

    if "category" not in pelican_kwargs:
        pelican_kwargs["category"] = "Activity"

    if "author" not in pelican_kwargs:
        pelican_kwargs["author"] = " Huy Truong"

    pub: str = ""

    for k, v in pelican_kwargs.items():
        pub += f"{k}: {v}\n"

    pub += f"{msg}"

    if hyper_link is not None:
        if pub[-1] != ".":
            pub += "."

        samples = ["Discover more here.", "Find out more here.", "Explore further here.", "Read more here.", "See more here."]
        random_index = np.random.randint(len(samples))
        pub += f"[{samples[random_index]}]({hyper_link})"

    pub += "<br>\n"
    year = date[:4]

    bib_name = f"act_truong{year}{uni_act_name}.md"

    md_path = f"{content_path}/{bib_name}"

    with open(file=md_path, mode="w") as f:
        f.write(pub)

    return md_path


def create_pub(
    uni_paper_name: str,
    paper_name: str,
    year: int,
    journal_or_conference: str,
    pdf_link: str,
    authors: list[str] = ["Huy Truong"],
    content_path: str = "github/content",
    pelican_kwargs: OrderedDict[str, Any] = {},
) -> str:
    # add headers

    if "title" not in pelican_kwargs:
        pelican_kwargs["title"] = uni_paper_name

    if "date" not in pelican_kwargs:
        pelican_kwargs["date"] = datetime.now().strftime(DATETIME_FORMAT)

    if "category" not in pelican_kwargs:
        pelican_kwargs["category"] = "Publication"

    if "author" not in pelican_kwargs:
        pelican_kwargs["author"] = " Huy Truong"

    pub: str = ""

    for k, v in pelican_kwargs.items():
        pub += f"{k}: {v}\n"

    pub += f"\n**{paper_name},**<br>\n"

    pub += ",".join(authors)

    pub += ".<br>\n"

    pub += f"{journal_or_conference},{year}<br>\n"

    pub += f"[\[pdf\]]({pdf_link})"  # type:ignore

    first_author = authors[0]

    if " " in first_author:
        family_name = first_author.split(" ")[-1]
    else:
        family_name = first_author

    bib_name = f"pub_{family_name}{year}{uni_paper_name}.md"

    md_path = f"{content_path}/{bib_name}"

    with open(file=md_path, mode="w") as f:
        f.write(pub)

    return md_path


def input_and_validate(prompt: str, expected_type: type, validate_fn: Callable[..., bool], error_hint: str = "Try again") -> Any:
    while True:
        x = input(prompt + " ")

        if validate_fn(x):
            if expected_type is list:
                casted_x = x.split(",")

            elif expected_type is not str:
                casted_x = expected_type(x)
            else:
                casted_x = x

            break
        else:
            print(f"ERROR!{error_hint}")

    return casted_x


def can_cast_to_int(s):
    try:
        int(s)

        return True  # Successfully cast to int

    except ValueError:
        return False  # Failed to cast


def export_publication():
    uni_paper: str = input_and_validate(
        "What is the unique (bib) paper name (e.g., gida, gatres)?", str, validate_fn=lambda x: " " not in x, error_hint="Should not contain space"
    )

    name: str = input_and_validate("What is the full name of your publication?", str, validate_fn=lambda x: True)

    year: int = input_and_validate(
        "What is the publishing year (YYYY)?", int, validate_fn=lambda x: can_cast_to_int(x), error_hint="Should be integer and format is YYYY"
    )

    authors: list[str] = input_and_validate(
        "Insert authors' name (e.g., Huy Truong, A Brother): ",
        expected_type=list,
        validate_fn=lambda x: True,
        error_hint="Ensure comma existing if the paper has multiple authors",
    )

    place: str = input_and_validate("What is the journal/ conference?", expected_type=str, validate_fn=lambda x: True)

    pdf_link: str = input_and_validate(
        "Insert the direct pdf link:", expected_type=str, validate_fn=lambda x: True, error_hint="Try again to insert a website"
    )

    # args = parser.parse_args()

    md_path = create_pub(
        uni_paper_name=uni_paper,
        paper_name=name,
        year=year,
        journal_or_conference=place,
        pdf_link=pdf_link,
        authors=authors,
    )

    print_md_file(md_path)


def print_md_file(md_path: str):
    print(f"Saved the md file at {md_path}!")

    print("#" * 80)

    # Open and read the file

    try:
        with open(md_path, "r", encoding="utf-8") as file:
            content = file.read()

            print(content)  # Print the content to the terminal

    except FileNotFoundError:
        print(f"The file {md_path} does not exist.")

    print("#" * 80)


def can_cast_to_datetime(x: str) -> bool:
    try:
        datetime.fromisoformat(x)
        return True
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False


def export_activity():
    uni_act_name: str = input_and_validate(
        "What is the unique activity name (e.g., travel_to_sw)?", str, validate_fn=lambda x: " " not in x, error_hint="Should not contain space"
    )

    date: str = input_and_validate(
        "What is the date (YYYY-MM-DD)?",
        str,
        validate_fn=lambda x: can_cast_to_datetime(x),
        error_hint="Incorrect data format, should be YYYY-MM-DD",
    )

    msg: str = input_and_validate(
        f"What is the activity (limit: {MSG_LIMIT} chars)?",
        expected_type=str,
        validate_fn=lambda x: len(x) < MSG_LIMIT,
        error_hint=f"Msg is too long. Make sure its length is less than {MSG_LIMIT}",
    )

    do_hyper_link: str = input_and_validate(
        "Do you want add hyperlink (y/n)?", expected_type=str, validate_fn=lambda x: str(x).lower() in ["y", "n"], error_hint="Only y or n"
    )
    print(f"do_hyper_link = {do_hyper_link}")
    if do_hyper_link == "y":
        link: str = input_and_validate("Insert a link:", expected_type=str, validate_fn=lambda x: True, error_hint="Try again to insert a website")

    else:
        link = None

    md_path = create_act(
        uni_act_name=uni_act_name,
        date=date,
        msg=msg,
        hyper_link=link,
    )

    print_md_file(md_path)


if __name__ == "__main__":
    print("Support exporting publication or activity...")
    pub_or_act = input_and_validate(
        "Do you choose publication or activity(p/a)?", expected_type=str, validate_fn=lambda x: x in ["p", "a"], error_hint="Enter p or a"
    )
    if pub_or_act == "p":
        export_publication()
    else:
        export_activity()
