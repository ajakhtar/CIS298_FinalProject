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
| Abdullah | App logic, session state, interactions |
| Vanessa | Data structure, story JSON, assets |
| Mohamed | Story writing, UI/CSS design |

---

## Time Log

| Commit | Date | Member   | Hours | What was done                                                                                                                              |
|--------|------|----------|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | 2026-04-18 | Abdullah | 2.5 | Set up Streamlit app skeleton, created folder structure and README                                                                         |
| 2      | 2026-04-19 | Mohamed Alhmood | 3.0 | Designed StoryNode data structure, implemented JSON-to-object loader, and integrated dynamic story traversal with Streamlit session state  |
| 3      | 2026-04-21 | Vanessa Clark | 2.5 | Beginning draft of story, added destinations and video audio content                                                                       |
| 4      | 2026-04-21 | Abdullah | 4.0 | Added title screen with started flag, guarded media files with os.path.exists, improved ending messages, Play Again resets to title screen |
| 5      | 2026-04-22 | Vanessa | 3.0 | Implemented world map feature and corrected image rendering                                                                                |
| 6      | 2026-04-22 | Mohamed Alhmood | 3.0 | Expanded nodes.json with additional story branches, deeper paths, and multiple endings                                                     
| 7      | 2026-04-22 | Abdullah | 2.5 | Added journey history sidebar, st.toast() on choices, stop counter on ending screen, history reset on Take Another Trip                    |
| 8      | 2026-04-25 | Vanessa | 6 | Added Istanbul/Mexico videos and preserved playback during navigation                                                                      |
 | 9      | 2026-04-25 | Abdullah | 3.0 | Tweaked allergy system. ⚠️ warning on risky choice buttons, Anthony comments appear on relevant nodes                                      |
| 10     | 2026-04-25 | Mohamed Alhmood   | 3.5   | Enhanced UI with custom CSS, removed Streamlit header, added card-style layout, & improved button styling |
