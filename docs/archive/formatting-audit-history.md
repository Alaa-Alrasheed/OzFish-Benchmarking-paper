# EAAI compliance tracking

> Archived working history. Earlier counts, findings, checkboxes, file paths, and permission notes below may be superseded. For the current status, use the [submission checklist](../SUBMISSION-CHECKLIST.md) and [project README](../../README.md). Archived on 21 October 2026; retained for traceability.

Initial inspection: 17 October 2026. This file tracks work; it is not manuscript text.

## Scope and safeguards

- Preserve all existing manuscript wording, results, equations, citations, captions and reference details. Obtain approval for each separate content change.
- Ignore `(model name)` throughout this task.
- Work on one issue at a time. No manuscript edits have been made in this audit.
- Existing uncommitted changes to README.md, main.tex and main.pdf predate this audit and have been preserved. Existing untracked build files were also preserved. No commits made.
- This tracker and the README checklist are synchronized after each completed issue.

## Sources and verification limits

1. [Current EAAI Guide for Authors](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence/publish/guide-for-authors): accessed in the browser on 18 October 2026. It confirms the 250-word abstract maximum, maximum of six keywords, prohibition on undefined acronyms in the title and abstract, single-column format, 50-page maximum, manuscript file size under 100 MB, up to six INSPEC codes, and the highlights and graphical-abstract instructions recorded below.
2. [Elsevier generative AI policy](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals): accessible. Requires disclosure of generative AI manuscript-preparation assistance; lists checking completeness against submission guidelines as an example of use. Basic spelling, grammar and punctuation checks have an exception. Recommends identifying the tool, purpose and author oversight in a separate declaration immediately before references. The page does not specifically classify LaTeX-only conversion, so that use alone is not treated as an independently settled exemption or requirement; the present compliance assistance falls within its explicit examples.
3. [Elsevier LaTeX instructions](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions): accessible. Supports elsarticle, requires the relevant editable sources/assets when requested, and instructs authors to keep submission files at the same folder level for Editorial Manager. Journal-specific bibliography rules defer to the guide.
4. [Elsevier highlights support](https://www.elsevier.support/publishing/answer/how-do-i-include-highlights-with-my-manuscript): accessible, updated 1 June 2026. Highlights are mandatory for some journals and optional for others. If submitted, normally a separate editable source file named Highlights, with 3–5 bullets and at most 85 characters including spaces per bullet. This does not establish EAAI's current mandatory/optional status.
5. [Elsevier declarations support](https://www.elsevier.support/publishing/answer/what-are-conflict-of-interest-statements-funding-source-declarations-author-agreementsdeclarations-and-permission-notes): accessible, updated 3 October 2026. Explains declarations and directs authors to journal-specific instructions and upload requirements; does not establish every statement as a mandatory manuscript section for EAAI.

## Verified baseline

- Source uses `\documentclass[preprint,12pt]{elsarticle}`; local unmodified class version 3.4c, 11 January 2025. Single-column layout confirmed visually.
- Ten individual author commands, ten email commands, one shared institutional affiliation with the verified University of Sharjah postal address, and a corresponding-author marker/email are present.
- Six keywords appear immediately after the abstract, separated by `\sep`, meeting the live guide's maximum of six.
- Abstract has 231 whitespace-separated words, counting hyphenated compounds as one word, and no citation commands. It is within the live guide's 250-word maximum.
- Title has no obvious initialism requiring expansion. The abstract defines DINOv3 as “Self-Distillation with No Labels version 3” and MATANet as “Multi-context Attention and Taxonomy-Aware Network” using author-approved wording.
- Six figure environments/files, eight longtables plus one regular table, fourteen numbered equation environments and 66 records in `references.bib`. All figure paths exist. Citations use Elsevier's author-year style and the generated reference list is alphabetized by first author.
- Static checks: no duplicate labels, missing citation keys or uncited bibliography entries. Table, figure and numbered-section callouts use automatic references; equation, table and figure numbering is consistent.
- The known figure/table placement drafting note is absent. No TODO/TBD match was found. This is not a guarantee that all unfinished content has been found.
- Acknowledgements, an approved AI-use disclosure, an approved competing-interest declaration, an approved funding statement and an approved data-and-code availability statement are present. A separate CRediT section is absent. `Highlights.txt` and graphical-abstract PNG and TIFF drafts are present.
- A fresh two-pass XeLaTeX build of the unchanged source completed with exit code 0 and produced 47 pages in a temporary directory. Existing repository build outputs were not replaced.
- Fresh log: no unresolved citations/references, missing-character messages, overfull-box warnings, hyperref PDF-string warnings or infinite-glue page-splitting warnings. Two visually harmless underfull-box diagnostics remain: one in a justified conclusion paragraph and one around the long repository URL. MiKTeX also reports that updates have not been checked; this is an environment notice.
- Rendered all 47 pages for an overview and inspected pages 1 and 5 at larger scale. No obvious blank pages or gross clipping in the overview. This is preliminary visual review, not full artwork/table/equation sign-off. The front matter spans pages 1–2; Table 1 spans pages 5–6.
- Artwork pixel sizes: figure1 769×576; figure2 1431×565; figure3 1430×617; figure4 1429×564; figure5 1505×620; figure6 1449×784. Embedded DPI is approximately 220; effective print resolution and artwork category must be assessed separately. Do not infer compliance from metadata DPI.

## Prioritized outstanding checklist

Priority reflects submission risk and strength of available evidence; it does not imply every item is mandatory.

1. [x] **AI-use disclosure — completed.** Added the author-approved ChatGPT disclosure immediately before the bibliography. It covers manuscript organization, language and presentation, LaTeX preparation, reference and consistency checks, journal-requirement review, author verification and responsibility.
2. [x] **Competing interests — completed.** Added the author-approved declaration that the authors have no known competing financial interests or personal relationships that could have influenced the reported work.
3. [x] **Data availability and split-release claims — completed.** Added the author-approved statement identifying the original OzFish dataset DOI and the public repository containing the curated splits, model implementations, experiment configurations, training and evaluation code, and reported results.
4. [x] **Funding — completed.** Added the author-approved statement that no specific grant funded the research and that the University of Sharjah provided GPU and AWS cloud infrastructure.
5. [ ] **CRediT — deferred by the authors.** Actual roles for all eight authors remain pending and must not be inferred.
6. [ ] **Title page and postal details — provisional telephone verification pending.** All eight authors and their shared University of Sharjah affiliation are present. Only corresponding author Manar Abu Talib's email is displayed in the manuscript; all co-author emails must be entered separately in Editorial Manager. The separate title page uses provisional telephone +971 52 908 1891; VERIFY with Manar Abu Talib before submission. The separate anonymized review manuscript has been created.
7. [x] **Abstract, keywords, acronyms and INSPEC codes completed.** The revised abstract remains within the verified 250-word maximum, has no citations, defines DINOv3 and MATANet at first mention, and the six keywords meet the verified numerical limit. Four relevant INSPEC codes appear after the keywords: C1230, C5260B, C5290, and C7860.
8. [ ] **Highlights completed; graphical-abstract draft awaiting decision.** Added five author-approved bullets to `Highlights.txt`. Prepared 1800×720 PNG and TIFF graphical-abstract drafts summarizing the dataset, grouped split, multi-context model, headline accuracy and taxonomy-aware analysis. The draft meets the live guide's width and orientation requirements; inclusion and revisions remain for author review.
9. [x] **Compilation diagnostics — completed.** The corresponding-author command is disabled only while hyperref creates plain-text PDF metadata. The longtable output routine now uses stretch-only filler when splitting pages, removing XeLaTeX's infinite-shrink warning without changing the original table breaks or 50-page layout. Removed an unnecessary forced line break before the Macro Accuracy equation. The two remaining underfull-box notices were visually assessed on pages 40 and 42 and are harmless; suppressing them would risk worse spacing or changing the displayed repository URL.
10. [x] **Section numbering — completed.** Converted all manually numbered section, subsection and subsubsection headings to LaTeX-managed numbering, including Acknowledgements. Removed redundant manual bookmark entries and retained labels. Declaration, funding and availability headings remain unnumbered. The visible numbering, wording, pagination and 50-page count are preserved, and the PDF outline now has the correct hierarchy.
11. [x] **Tables — formatting, references and captions completed.** Reviewed all nine tables. Kept all five rows of Table 4 together on page 15, added labels and automatic references to every table, standardized callout capitalization and thousands separators, split Table 7 into two stacked panels at `\footnotesize` for comfortable reading while retaining one table number, and corrected the Table 9 parameter ratio to approximately one-fourteenth. The approved standalone captions for Tables 7–9 are applied to both manuscript versions.
12. [x] **Figures — artwork and placement review completed.** Figure 1 uses its original 2400×1800, 300-dpi source and is displayed at 75% of the text width. Figures 2–6 use their original PDF artwork rather than downsampled PNG copies. All six figures were visually checked at their displayed sizes for legibility, order, subsection placement and clipping. Figures 2–6 are anchored at their source positions so they cannot cross subsection boundaries. Captions were preserved.
13. [x] **Equations — verification completed.** Compared all fourteen numbered equations with the original Word manuscript and visually inspected their PDF rendering. With author approval, corrected the attention grouping in Equation 1, the softmax index mismatch in Equation 4, and the uppercase/lowercase class-index mismatch in Equation 12. Standardized mathematical operators, logits notation, piecewise-condition text, metric typography and spacing; aligned the Equation 12 explanatory subscripts; and added stable labels to all equations. Numbering remains 1–14 with no clipping or overflow.
14. [x] **References — style and metadata completed.** Converted all citations to author-year form with narrative and parenthetical commands, moved all 66 records to `references.bib`, and selected `elsarticle-harv` for an alphabetized reference list. Verified 55 DOI records through Crossref and checked the remaining dataset, arXiv, technical-report, ICLR, ICML, TMLR and NeurIPS records against official repositories or proceedings. All citation keys resolve.
15. [x] **Length and remaining internal notes — completed.** The live guide confirms a 50-page maximum and manuscript-file size under 100 MB; the current 50-page, approximately 2.4 MB PDF is within both limits. All 50 pages were visually reviewed without clipping, overlap, missing pages or misplaced artwork. The model-name placeholders have been replaced with the approved Bio-TAC name.
16. [ ] **Git portability and submission package — pending.** No .gitattributes or .gitignore present at inspection. Consider narrowly scoped LF rules and excluding future generated files, without renormalizing existing files or deleting current outputs automatically. Keep the publisher submission bundle flat. Packaging, licenses/permissions for reused material, and any journal-specific cover-letter/checklist requirements need final confirmation. No commits authorized.

## Issue 1: AI-use disclosure (COMPLETED)

**Issue:** A manuscript-preparation AI declaration was absent. The accessible publisher policy requires disclosure for this kind of assistance, including checking a manuscript against submission guidelines.

**Previous text:** None; the acknowledgements led directly into `thebibliography`.

**Approved section heading:** Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

**Approved paragraph:**

> During the preparation of this work, the authors used ChatGPT to assist with manuscript organization, language and presentation, LaTeX preparation, reference and consistency checks, and review against journal submission requirements. The authors reviewed and verified the resulting assistance, edited the manuscript as needed, and take full responsibility for the content of the publication.

**Reason:** Identifies the tool and approved range of manuscript-preparation purposes without claiming AI performed the research or wrote scientific conclusions.

**Action taken:** The author approved ChatGPT as the tool and authorized insertion on 18 October 2026.

**Location:** Separate unnumbered section immediately before the bibliography.

## Issue 2: competing interests (COMPLETED)

**Issue:** A competing-interest declaration was absent.

**Previous text:** None; this is a new section.

**Approved section heading:** Declaration of competing interest

**Approved paragraph:**

> The authors declare that they have no known competing financial interests or personal relationships that could have influenced the work reported in this paper.

**Reason:** Records the authors' confirmed absence of known financial or personal conflicts relevant to the paper.

**Action taken:** The author approved the exact wording on 18 October 2026.

**Location:** Separate unnumbered section after the AI-use declaration and immediately before the bibliography.

## Issue 3: funding and computational resources (COMPLETED)

**Issue:** A funding statement was absent, although the University of Sharjah provided computational resources used for the research.

**Previous text:** None; this is a new section.

**Approved section heading:** Funding

**Approved paragraph:**

> This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. Computational resources, including GPU and AWS cloud infrastructure, were provided by the University of Sharjah.

**Reason:** Distinguishes the absence of a specific grant from the University's in-kind provision of computing infrastructure.

**Action taken:** The author confirmed that the University paid for the resources and approved the wording on 18 October 2026.

**Location:** Separate unnumbered section after the competing-interest declaration and immediately before the bibliography.

## Issue 4: data and code availability (COMPLETED)

**Issue:** The manuscript described the benchmark split as released but did not provide an access location.

**Previous text:** None; this is a new section.

**Approved section heading:** Data and code availability

**Approved paragraph:**

> The original OzFish dataset used in this study is publicly available from the Australian Institute of Marine Science at https://doi.org/10.25845/5e28f062c5097. The curated benchmark splits, model implementations, experiment configurations, training and evaluation code, and reported results are publicly available at https://github.com/Karam-Kreidli/ozfish-finegrained-classification-benchmark.

**Reason:** Identifies the stable record for the source dataset and the public repository supporting the manuscript's benchmark-release and reproducibility claims.

**Action taken:** The author confirmed the public benchmark repository contents and approved the exact wording on 18 October 2026.

**Location:** Separate unnumbered section after Funding and immediately before the bibliography.

## Change log

- 18 October 2026: Expanded DINOv3 and MATANet at their first mentions in the abstract using the exact author-approved wording. No other manuscript text was changed. The revised abstract has 242 words. A two-pass XeLaTeX rebuild completed successfully and retained the 48-page count. Both abstract pages were visually inspected with clean wrapping and no clipping or overlap. No unresolved citations, references, missing characters or overfull boxes were reported; previously tracked diagnostics remain unchanged.
- 18 October 2026: Prepared the first graphical-abstract draft as separate 1800×720 PNG and TIFF files using a manually constructed schematic and verified manuscript results. The draft meets the live guide's minimum width and horizontal-orientation requirements. It remains optional and awaits author review; the manuscript PDF was unchanged.
- 18 October 2026: Created the separate editable `Highlights.txt` submission file with five author-approved bullets. Verified character counts of 74, 79, 66, 58 and 73, all within the live EAAI guide's 85-character maximum. No manuscript or PDF change was needed.
- 18 October 2026: Accessed the live EAAI Guide for Authors and replaced previously unverified abstract, keyword, page-limit, highlights, graphical-abstract and INSPEC notes with current requirements. Confirmed the 231-word abstract, six-keyword count, 48-page length and file size are within the numerical limits. Kept model-name treatment and INSPEC codes open. Drafted five proposed highlights for author approval; no manuscript text or submission file was changed.
- 18 October 2026: Added the verified University of Sharjah postal address, P.O. Box 27272, to the shared affiliation with author approval. A two-pass XeLaTeX rebuild completed successfully and retained the 48-page count. The full title page was visually inspected: the address wraps cleanly beneath the author list with no clipping, overlap or crowding. No unresolved citations, references, missing characters or overfull boxes were reported; previously tracked diagnostics remain unchanged.
- 18 October 2026: The authors deferred the CRediT contribution statement pending actual contribution roles. The item remains open and no contribution roles were inferred. Synchronized the older README checklist with the completed declarations and current 48-page build.
- 17 October 2026: Created this tracker after read-only source inspection, official-source checks, a temporary two-pass baseline build and preliminary PDF review. No changes to existing manuscript, README, class, figures or repository PDF. Issue 1 awaits approval.
- 18 October 2026: Added the approved ChatGPT disclosure immediately before the bibliography. No other manuscript text was changed. A two-pass XeLaTeX rebuild completed successfully and produced a 47-page PDF. The declaration renders on page 40 immediately before the references without clipping or overlap. No unresolved references, citations, missing characters or overfull boxes were reported. Pre-existing hyperref PDF-string warnings and the longtable glue diagnostic remain tracked separately.
- 18 October 2026: Added the approved competing-interest declaration after the AI-use disclosure and before the bibliography. No other manuscript text was changed. A two-pass XeLaTeX rebuild completed successfully and produced a 47-page PDF. Both declarations render cleanly on page 40 before the references, with no clipping or overlap. No unresolved references, citations, missing characters or overfull boxes were reported. Pre-existing hyperref PDF-string warnings and the longtable glue diagnostic remain tracked separately.
- 18 October 2026: Added the approved funding statement after the competing-interest declaration and before the bibliography. No other manuscript text was changed. A two-pass XeLaTeX rebuild completed successfully and produced a 47-page PDF. The AI-use, competing-interest and funding sections render cleanly on page 40 before the references, with no clipping or overlap. No unresolved references, citations, missing characters or overfull boxes were reported. Pre-existing hyperref PDF-string warnings and the longtable glue diagnostic remain tracked separately.
- 18 October 2026: Added the approved data-and-code availability statement after Funding and before the bibliography, citing the original OzFish dataset DOI and the public benchmark repository. No other manuscript text was changed. A two-pass XeLaTeX rebuild completed successfully and produced a 48-page PDF. The new section and both URLs render cleanly on page 40, and References begins on page 41, with no clipping or overlap. No unresolved references, citations, missing characters or overfull boxes were reported. The long URL introduced one visually harmless underfull-box diagnostic; the pre-existing hyperref PDF-string warnings and longtable glue diagnostic remain tracked separately.
- 18 October 2026: Resolved the four hyperref PDF-string warnings by disabling `\corref` only during PDF metadata generation. The visible corresponding-author marker and footnote remain unchanged. A complete XeLaTeX–BibTeX–XeLaTeX–XeLaTeX rebuild produced a 50-page PDF; its first page renders cleanly, and the embedded author field lists all ten authors without the correspondence command. The longtable/glue and underfull-box diagnostics remain tracked separately.
- 18 October 2026: Resolved XeLaTeX's `Infinite glue shrinkage found in box being split` diagnostic by replacing the two shrinkable `\vss` fillers in `longtable`'s output routine with stretch-only `\vfil` fillers. The original Table 4 continuation across pages 15–16 and all manuscript content remain unchanged. A complete rebuild produced 50 pages, and pages 15–16 were visually verified without clipping, overlap or broken rules. Three underfull-box diagnostics remain for separate review.
- 18 October 2026: Completed compilation-diagnostic review. Removed the unnecessary forced line break immediately before the Macro Accuracy equation, eliminating the badness-10000 underfull box without changing wording or mathematics. Visually inspected the remaining conclusion and repository-URL lines on pages 40 and 42; both render legibly without clipping or excessive gaps, so their low-severity underfull notices were retained rather than forcing inferior spacing. The PDF remains 50 pages.
- 18 October 2026: Converted the nine numbered sections and all numbered subsection levels from starred commands with literal numbers to LaTeX-managed numbering. Removed the redundant manual PDF-outline entries, correcting the hierarchy of `6.3 Comparison with MATANet` from a manually registered section to a true subsection. Acknowledgements remains numbered as section 9; declarations, Funding, and Data and code availability remain unnumbered. Representative section, subsection, subsubsection, conclusion and declaration pages were visually verified, and the rebuilt PDF remains 50 pages.
- 18 October 2026: Completed the approved table corrections while leaving captions 7–9 unchanged for later author discussion. Table 4 now fits completely on page 15 without a continuation page. Added stable labels and automatic references for Tables 1–9, standardized table-callout capitalization and thousands separators, split Table 7 into two stacked `\footnotesize` panels so all seven metrics remain readable under one table number, and corrected the Table 9 prose ratio from one-thirteenth to approximately one-fourteenth. Visually verified pages 15–18, 29–30 and 37; no table is clipped or overfull, and the PDF remains 50 pages.
- 18 October 2026: Replaced the downsampled 769×576 Figure 1 asset with the original 2400×1800, 300-dpi chart from `benchmark_statistics`, reduced its displayed width from the full text width to `0.75\linewidth`, and visually verified the revised page. The chart remains legible, the page is more balanced, and the PDF remains 50 pages.
- 18 October 2026: Replaced the downsampled PNG copies of Figures 2–6 with their matching original PDF artwork from the project files. Kept the multi-panel figures at the full text width, anchored them within their corresponding subsections, and removed the obsolete PNG copies. Visually verified pages 32–36: labels and captions are legible, no figure is clipped, and Figures 2–6 no longer cross subsection boundaries. The PDF remains 50 pages.
- 18 October 2026: Completed the approved equation corrections after comparing all fourteen equations with the original Word manuscript. Corrected the attention grouping in Equation 1, the softmax denominator index in Equation 4, and the class index in Equation 12; standardized operators, logits notation, metric abbreviations and piecewise text; aligned the Equation 12 prose subscripts; and added stable equation labels. Visually verified pages 19–21 and 25–26. All equations remain sequentially numbered, unclipped and legible, and the PDF remains 50 pages.
- 18 October 2026: Completed the 50-page visual and internal-note audit. Replaced manually typed figure and numbered-section callouts with stable LaTeX references and consistent capitalization. At the authors' direction, removed Homaiza Saud and Fatima Dakalbab and their email addresses from the author block and acknowledged their manuscript advice. A full XeLaTeX–BibTeX–XeLaTeX–XeLaTeX rebuild completed successfully; the PDF metadata lists the remaining eight authors, all references resolve, the revised title and acknowledgement pages render cleanly, and the PDF remains 50 pages.
- 18 October 2026: Removed the seven non-corresponding-author email entries from the manuscript title page and retained only Manar Abu Talib's corresponding-author email. Co-author emails remain required in Editorial Manager rather than in the displayed manuscript. The corresponding-author telephone number remains pending for the eventual separate title page.

- 18 October 2026: Applied Bio-TAC (Biological Taxonomy-Aware Classification); created separate title page and anonymized manuscript. Telephone +971 52 908 1891 is provisional and MUST be verified before submission.

- 18 October 2026: Applied the author-approved captions for Tables 7–9 to main.tex and anonymized-manuscript.tex. Table 9 now describes model size and predictive performance rather than computational efficiency.
## Final formatting recheck — 20 October 2026

Re-read the live official EAAI Guide for Authors in the browser: https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence/publish/guide-for-authors

Verified: both manuscript PDFs have 50 pages and are approximately 2.4 MB; the abstract has 242 whitespace-separated words; six keywords and four INSPEC codes are present; five highlight bullets are within 85 characters. The review PDF has no author metadata, and extracted text contains none of the checked team names, institutional details, acknowledgements, funding or identifying repository URL. Current manuscript logs contain no undefined references, missing characters or overfull boxes. Fonts in Figures 2–6 are embedded; Figure 6 photographic panels exceed 300 dpi. Underlining in the results tables identifies second-best numerical results and is scientifically relevant.

Outstanding:
- [x] Added the existing approved acknowledgements to title-page.tex. The live journal guide explicitly requires acknowledgements in the separate title page only; the current review manuscript correctly omits them, but the title page also omits them.
- [x] Included the competing-interest declaration on the title page. The guide additionally requires completing Elsevier's declarations tool and uploading its resulting DOC/DOCX file.
- [ ] Obtain the actual CRediT roles for all eight authors.
- [x] Resolved Figure 1 with vector PDF artwork and a 1000-dpi PNG export. Previous audit finding: the current 2400 x 1800 PNG has effective resolution 593 dpi. The guide lists 1000 dpi for bitmapped line drawings, and recommends editable XLS/XLSX for charts. Prefer original vector PDF artwork or a reproducible export meeting the relevant artwork requirements; do not simply upscale the PNG.
- [ ] Verify the provisional corresponding-author phone number with Manar Abu Talib.
- [ ] Decide whether to include the optional graphical abstract. Highlights and graphical abstracts are encouraged by the live guide.
- [ ] Confirm the final upload bundle and all author/submission declarations before submitting.

Git author and committer both resolve to Alaa Alrasheed <152157837+Alaa-Alrasheed@users.noreply.github.com>. The user conditionally authorized a commit only if the review passes. No commit was made because the outstanding compliance issues above remain. This replaces the earlier unconditional "No commits authorized" note for the current request; manuscript content was not changed during this recheck.

- 20 October 2026: At author direction, recreated Figure 1 as vector PDF with embedded Arial using the Table 6 counts (112, 161, 48); added reproducible scripts/make_figure1.py and an 8000 x 6000, 1000-dpi PNG export. Both manuscripts now include the vector PDF at the same displayed width. Added the existing approved acknowledgements and competing-interest statement to the separate title page. Fixed its hyperref metadata warnings. Visually verified the revised figure and one-page title page; both manuscripts remain 50 pages with no unresolved references, missing characters or overfull boxes. CRediT is explicitly deferred while the author consults the supervisor. Phone verification and publisher submission declarations remain pending. The author authorized commit and push using their configured identity; temporary files and build intermediates are excluded.
