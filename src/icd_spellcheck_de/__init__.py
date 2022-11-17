import csv
import pathlib

import typer

from . import utils

app = typer.Typer()


@app.command()
def generate(
    icd_csv: typer.FileText = typer.Argument(...),  # noqa: B008
    output: typer.FileTextWrite = typer.Argument("dist/icd-10-de.txt"),  # noqa: B008
) -> None:
    wordlist: set[str] = set()

    with typer.progressbar(
        list(csv.reader(icd_csv, delimiter="|")), label="Generating word list"
    ) as rows:
        for row in rows:
            wordlist.update(
                word
                for word in utils.split_terms(row[-1])
                if (
                    len(word) > 2
                    and word[0].isalnum()
                    and utils.contains_letters(word)
                    and not utils.is_acronym(word)
                )
            )
    pathlib.Path(output.name).parent.mkdir(parents=True, exist_ok=True)
    output.write(
        "# Die Erstellung erfolgt unter Verwendung "
        "der maschinenlesbaren Fassung "
        "des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM).\n"
    )
    output.writelines((f"{w}\n" for w in sorted(wordlist)))
