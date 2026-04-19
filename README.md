# 📖 Choose Your Own Adventure Game

A choose-your-own-adventure story game built with [Streamlit](https://streamlit.io/). Navigate branching story paths, make choices, and discover multiple endings, using an interactive web app.

## Features
- Branching story represented as a tree data structure (JSON)
- Multiple story paths and endings
- Unique Streamlit effects (balloons, snow) on endings
- Custom UI styling and scene images

## Setup

```bash
pip install streamlit
streamlit run app.py
```

## Project Structure

```
/
├── app.py              # Main Streamlit app
├── story/
│   └── nodes.json      # Story tree data
├── assets/
│   └── images/         # Scene images
└── README.md
```

## Team

| Member | Primary Role |
|--------|-------------|
| A | App logic, session state, interactions |
| B | Data structure, story JSON, assets |
| C | Story writing, UI/CSS design |

---

## Time Log

| Commit | Date | Member   | Hours | What was done                                                      |
|--------|------|----------|-------|--------------------------------------------------------------------|
| 1 | 2026-04-18 | Abdullah | 2.5 | Set up Streamlit app skeleton, created folder structure and README |
| 2 | 2026-04-19 | Mohamed Alhmood | 3.0 | Designed StoryNode data structure, implemented JSON-to-object loader, and integrated dynamic story traversal with Streamlit session state |