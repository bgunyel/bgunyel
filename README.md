# Bertan Günyel

### Anyone can build a demo. I build AI systems that can be proven to work.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bertan-gunyel/)
[![X](https://img.shields.io/badge/-black?logo=x&style=for-the-badge)](https://x.com/bertan_gunyel)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bertan.gunyel@gmail.com)

---

## About

AI/ML engineer. Twenty years building systems that ship — natural language processing, computer vision, time-series forecasting, and most recently LLM applications and agent systems.

What I care about is whether they work, and whether anyone can prove it. Most AI projects can't answer that. The demo goes well, the tests pass, and nobody can tell you what the system gets wrong until a customer finds out.

So I build the evidence alongside the system: evaluation sets that get checked rather than assumed, measurements that survive a hard question, and failures published next to results.

---

## Clause & Effect

**An evaluation-first RAG system over the GDPR — built in public, on stream, mistakes included.**

The compliance assistant isn't the point. The evidence layer under it is: a test set that gets checked rather than assumed, and every failure published next to every result.

**Status, as of 2026-08-06:**

| | |
|---|---|
| Test cases | 433 |
| Passing every quality check | 299 |
| Quality gate | **FAILING** |
| Published performance numbers | **none** |

The gate fails because 134 supporting quotes don't match the article they claim to come from. I'm not publishing system numbers off a test set that doesn't pass its own checks, and I'm not relaxing the gate to make it green. They go up when they're real — including everything the system gets wrong.

Six sessions in, the instrument has turned out to be broken before the system four times running: a parser that silently destroyed 76 of 99 articles, a test suite that stayed green over it, a grounding rule that flagged correct data as wrong, and a document converter that severed paragraphs from the negations governing them — so that a *perfect* retriever would have returned text meaning the opposite of the law.

[Repository](https://github.com/bgunyel/clause-and-effect) · [Build sessions](https://youtube.com/@bertangunyel/streams) · [Why evaluation comes first](https://www.linkedin.com/posts/bertan-gunyel_most-rag-demos-die-the-same-death-they-look-share-7484875320953851904-SKav)

---

## Other Projects

**LLM and agent systems**

- [ai-common](https://github.com/bgunyel/ai-common) — shared infrastructure: one interface across LLM providers, reusable graph components. The library the rest are built on.
- [RAGNAR](https://github.com/bgunyel/ragnar) — business intelligence agent with a database-first architecture. LangGraph, Supabase, FastAPI, LangSmith.
- [business-researcher](https://github.com/bgunyel/business-researcher) — company and professional research with structured output validation. LangChain, Pydantic, Tavily.
- [deep-sage](https://github.com/bgunyel/deep-sage) — long-form research reports via a plan-distribute-collect-combine workflow.
- [summary-writer](https://github.com/bgunyel/summary-writer) — topic summaries through an iterative generate-evaluate loop.
- [auto-company](https://github.com/bgunyel/auto-company) — company analysis over SEC EDGAR filings. In development.

**Earlier work**

- [electricity-load-forecasting](https://github.com/bgunyel/electricity-load-forecasting) — electricity demand forecasting, classical and deep learning approaches.
- [nlp-fun](https://github.com/bgunyel/nlp-fun) · [cv-fun](https://github.com/bgunyel/cv-fun) — exploration repositories from NLP and computer vision work.

---

## Let's Connect

If you're building something where being wrong is expensive — or you think I'm measuring this wrong — I'd like to hear from you.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bertan-gunyel/)
[![X](https://img.shields.io/badge/-black?style=for-the-badge&logo=x)](https://x.com/bertan_gunyel)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bertan.gunyel@gmail.com)

---

**Runs is not works.**
