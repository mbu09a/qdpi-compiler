# QDPI Compiler

**A quad-directional symbolic compiler for recursive meaning-making.**

QDPI (Quad-Directional Parsing Interface) is the foundational AI engine behind *Gibsey* and *DreamRIA*. It is not a chatbot. It is a recursive ritual system—an architecture for symbolic transformation, poetic synthesis, and post-scarcity interaction design.

Built in modular Python, QDPI compiles gifted user input through four recursive stages:

> **Input → Parse → Index → Transform → Emit**

Each module performs a symbolic function. Each response is not predicted—but composed, remembered, and refracted. QDPI is designed to replace token prediction with contextual recursion, memory, and ritual.

## ✨ Core Features

- Symbolic processing engine with modular architecture
- Configurable memory system (`memory_store.json`)
- Stylized transformation layer (placeholder logic with poetic templates)
- Plug-and-play ready for Firebase, Render, or local CLI use
- Corpus-driven architecture with full extensibility

## 📂 Project Structure

```
qdpi-compiler/
├── engine.py          # Main compiler loop
├── reader.py          # Accepts input
├── parser.py          # Parses structure
├── indexer.py         # Pulls fragments
├── transformer.py     # Transforms content
├── emitter.py         # Emits output
├── memory.py          # Optional memory handling
├── manifest.yaml      # Compiler config
├── run.py             # CLI launcher
└── data/
    ├── corpus.json
    ├── fragments.json
    ├── memory_store.json
    ├── symbols.json
    └── templates/
```

## 🛠️ Requirements

```
fastapi
uvicorn[standard]
```

## 🚀 Deployment

To run locally:

```bash
uvicorn main:app --reload
```

To run the standalone compiler from CLI:

```bash
python run.py
```

To deploy on Render:
- Set the **start command** to:  
  `uvicorn main:app --host 0.0.0.0 --port 10000`

## 🌀 License

Open-use for symbolic experimentation and recursive creation.  
Subject to the Gifted License (forthcoming). Attribution always welcomed.

---

*“Not a chatbot. A ritual interface for symbolic recursion.”*

---
