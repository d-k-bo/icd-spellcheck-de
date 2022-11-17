# icd-spellcheck-de

A word list for spell checking medical terms based on the german translation of ICD-10.

The latest pre-generated word list is available here: [dist/icd-10-de.txt](dist/icd-10-de.txt).

## Generate it yourself

1. Download the alphabetic index from the [website of _Bundesinstitut für Arzneimittel und Medizinprodukte_ (BfArM)](https://www.bfarm.de/SharedDocs/Downloads/DE/Kodiersysteme/klassifikationen/icd-10-gm/version2023/icd10gm2023alpha-txt_zip.html) and extract the CSV file.
2. Using [`pipx`](https://pypa.github.io/pipx/) you can download this project and its dependencies and execute the script:

```
pipx run --spec=git+https://github.com/d-k-bo/icd-spellcheck-de.git icd-spellcheck-de $PATH_TO_ICD_TXT $OUTPUT_PATH
```

## License

This project is licensed under the MIT No Attribution License. See [LICENSE](LICENSE) for more information.

The generated word list is distributed according to BfArM's [Downloadbedingungen für die ICD-10-GM](Downloadbedingungen für die ICD-10-GM).
