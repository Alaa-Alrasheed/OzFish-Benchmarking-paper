# OzFish Benchmark Paper

Manuscript and submission materials for **A Leakage-Controlled Benchmark and Taxonomy-Aware Multi-Context Model for Fine-Grained Fish Species Classification on OzFish**, prepared for *Engineering Applications of Artificial Intelligence* (EAAI).

The paper presents a deployment-grouped OzFish benchmark and **Bio-TAC (Biological Taxonomy-Aware Classification)**. Model implementations, training, evaluation, and benchmark splits are maintained in the separate [code repository](https://github.com/Karam-Kreidli/ozfish-finegrained-classification-benchmark).

## Start here

- **[Full paper](main.pdf)** — complete manuscript for the author team.
- **[Anonymized paper](anonymized-manuscript.pdf)** — review copy with author details, acknowledgements, funding, and the identifying code-repository link omitted.
- **[Separate title page](title-page.pdf)** — author names, affiliation, corresponding-author details, acknowledgements, and competing-interest statement.
- **[Submission checklist](docs/SUBMISSION-CHECKLIST.md)** — current status and remaining decisions.

## Feedback needed from the team

- **CRediT contributions:** fill in the [editable contribution draft](CRediT-Author-Contributions-Draft.docx), which includes a role guide and all eight authors. Role assignments await author confirmation.
- **Graphical abstract:** decide whether to include the optional draft: [preview](Graphical_Abstract_v1.png) / [TIFF](Graphical_Abstract_v1.tiff).
- **Contact details:** verify the provisional corresponding-author telephone number on the title page before submission.

The formatting review is complete. Both manuscript PDFs currently have **50 pages**; the separate title page is **one page**. The final submission package and publisher forms still need to be completed.

## Editing and compiling

The editable sources are [main.tex](main.tex), [anonymized-manuscript.tex](anonymized-manuscript.tex), and [title-page.tex](title-page.tex). References are stored in [references.bib](references.bib); [elsarticle.cls](elsarticle.cls) is the Elsevier document class. Figures are supplied as `figure1.pdf` through `figure6.pdf`.

Use **XeLaTeX** and **BibTeX**, or build locally with `latexmk`:

```sh
latexmk -xelatex -interaction=nonstopmode main.tex
latexmk -xelatex -interaction=nonstopmode anonymized-manuscript.tex
latexmk -xelatex -interaction=nonstopmode title-page.tex
```

On Overleaf, import the project, choose XeLaTeX, and select the source file for the version you want to compile.

Keep the complete and anonymized manuscripts synchronized when making changes. Keep identifying details out of the review copy and its PDF metadata. Rebuild the affected PDFs and inspect their layout before sharing changes. Preserve author-approved wording and results unless the author team agrees to revisions.

Compiler intermediates and temporary review images are ignored by Git. Source files, figure assets, and the current PDFs are versioned. Figure 1 can be reproduced with [scripts/make_figure1.py](scripts/make_figure1.py); [figure1.png](figure1.png) is its optional 1000-dpi export.

## Other materials

- [Highlights](Highlights.txt) — five submission highlights.
- [Original Word draft](docs/archive/Research%20Paper%203.docx) — retained for comparison; the LaTeX sources are the current version.
- [Formatting audit history](docs/archive/formatting-audit-history.md) — historical working notes, including superseded findings. Use the current submission checklist for outstanding tasks.
- [Official EAAI Guide for Authors](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence/publish/guide-for-authors) — last checked on 20 October 2026; the live guide and submission portal take precedence.
