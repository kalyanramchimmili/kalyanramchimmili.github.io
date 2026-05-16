---
title: Elucidate
description: A fully local PDF Q&A application — upload a PDF, ask it questions, nothing leaves the machine.
tags: [RAG, Flask, Ollama, ChromaDB, Python]
---

# Elucidate

A fully local PDF Q&A app I built on weekends. Upload a PDF, ask it stuff, it answers — nothing leaves the machine. The [README in the repo](https://github.com/kalyanramchimmili/Elucidate) has the install steps and the config knobs.

## How it started

I was exploring NotebookLM, which felt like a RAG system to me, and I wanted to build something similar. RAG also seemed to be a trending project at many companies.

So the idea was simple: upload a PDF, ask it questions, keep it all local. While I was exploring a few blogs on building RAG, I heard about ChromaDB, Ollama, etc.

Ollama wasn't new. I pulled it once back in 2023, ran a model, said "neat," and then ignored it for two years. This was the excuse to come back. The only real research was figuring out what my 8 GB laptop could run without melting (turns out the smaller `llama3.2`), and on the 24 GB MBP I could go bigger and let `llama3.1:8b` actually reason.

## How I built it

Started with Flask, because that's what my hands type when I open an empty folder. Wired up a few routes — home page, error page, PDF list — and then started thinking about the actual RAG layer.

The structure ended up clean. `app/` is the Flask side, `ingest/` is the RAG side, `pdf/` is where uploads land. Splitting the RAG layer out meant I could test ingestion from the CLI without booting a browser.

The flow once you upload a PDF:

1. The app enters what I dramatically named **"warmup mode"** (it's a loading spinner with extra steps). pypdf rips the text out, the text gets chopped into chunks, each chunk gets embedded with `all-MiniLM-L6-v2`, the vectors land in ChromaDB, and the whole thing — model + embeddings — gets pinned in RAM so queries don't wait on disk.
2. If you've already ingested the PDF before, the embeddings are already on disk and it skips straight to loading them into RAM. Either way the frontend prints `// indexing the document` so you have something to look at.
3. When you ask a question, the same embedding model turns your query into a vector, ChromaDB hands back the top 10 closest chunks, and `ask_ollama()` sends those chunks plus your question plus a short prompt that's basically *"answer using only this, please don't make stuff up."* Ollama streams the answer back word by word.

Chunks are 2000 chars with 250 chars of overlap, so the windows slide along like `0–2000`, `1750–3750`, `3500–5500`, and so on. The overlap exists because the universe is cruel and the answer to your question loves to land exactly on a chunk boundary. Without overlap, it gets sliced in half and neither half retrieves well. I set it to 0 once just to see what happened; the model started inventing things with such confidence that I almost believed it. Put the overlap back.

Two model options are baked into the config — `llama3.1` for when there's enough RAM, `llama3.2` for when there isn't. Switching between them can be done from the UI itself — it lists all the models you have.

The UI was done by Claude. I am not a frontend person. My contributions were mostly "make it darker." The backend was the part I actually had fun building.

## What I picked up

- **Embeddings.** Implementing it was a good exercise to see how it runs.
- **RAG.** The major part of RAG is the retrieval part. A few people argue RAG is dead now that the new models' context window is 1M, but RAG shines on repeated queries — loading a 1000-page PDF every time into an LLM would degrade its quality so badly it would start answering completely unrelated stuff. Happened to me with ChatGPT.
- **ChromaDB.** The sheer algorithm of how RAG works was pretty simple. Heard Postgres too supports vector databases, would like to try that out.
- **Local-first is real.** Once the model and embeddings are in RAM, the only slow part is the first chunk-and-embed pass on a fresh PDF, and that's a one-time cost per document — but hey, everything works.

Along with this, I wanted to learn how to build Docker images. I'd worked with Docker before but never shipped any images, so I learned how to write a Dockerfile and build one. Tbh the performance of Docker on my 8 GB MacBook Air was not great, which was expected, but anyway — could check off the box of shipping my first Docker image.

- For more information on the project refer :- https://github.com/kalyanramchimmili/Elucidate