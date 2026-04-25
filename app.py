import streamlit as st
import json
import os
import base64

st.set_page_config(
    page_title="No Reservations: The Afterlife Tour",
    page_icon="🍷",
    layout="centered"
)

class StoryNode:
    def __init__(self, node_id, data):
        self.id = node_id
        self.title = data.get("title", "")
        self.text = data.get("text", "")
        self.choices = data.get("choices", [])
        self.ending = data.get("ending", False)
        self.ending_type = data.get("ending_type", None)
        self.image = data.get("image", None)

def load_story():
    with open("story/nodes.json", "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    nodes = {}
    for node_id, data in raw_data.items():
        nodes[node_id] = StoryNode(node_id, data)
    return nodes

def get_base64_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def show_city_scene():
    city = st.session_state.current_node_id
    scene = st.session_state.city_scene

    scenes = {
        "new_orleans": {
            "main": {
                "text": "Warm night air wraps around you as jazz spills through the streets.",
                "choices": {
                    "Follow the scent of gumbo": "gumbo",
                    "Follow the trumpet into a jazz club": "jazz",
                    "Ask why this city matters so much": "talk"
                }
            },
            "gumbo": {
                "text": "A woman stirs a massive pot with practiced patience. Chef Anthony says, 'Good food takes time. So do people worth knowing.'",
                "choices": {}
            },
            "jazz": {
                "text": "Inside a crowded club, strangers dance like old friends. Chef Anthony laughs, 'Some people wait for permission to feel alive. Never do that.'",
                "choices": {}
            },
            "talk": {
                "text": "'This city knows grief,' he says. 'And it still chose music.'",
                "choices": {}
            }
        },

        "tokyo": {
            "main": {
                "text": "Neon lights reflect off rain-slick streets as Chef Anthony leads you deeper into Tokyo.",
                "choices": {
                    "Follow the smoke to a yakitori stall": "yakitori",
                    "Try monjayaki on a hot griddle": "monjayaki"
                }
            },
            "yakitori": {
                "text": "Smoke curls above tiny stools. Chef Anthony says, 'Respect the small places. They often hold the biggest truths.'",
                "choices": {}
            },
            "monjayaki": {
                "text": "You scrape crispy edges from the grill. Chef Anthony grins, 'Not every masterpiece looks pretty at first.'",
                "choices": {}
            }
        },

        "istanbul": {
            "main": {
                "text": "Lanterns glow near the Bosphorus as Chef Anthony leads you through the city’s ancient streets.",
                "choices": {
                    "Visit the spice market": "spice",
                    "Eat by the water": "water"
                }
            },
            "spice": {
                "text": "The air blooms with saffron, sumac, and tea. 'A city is a recipe,' Chef Anthony says. 'Everything that passed through leaves flavor behind.'",
                "choices": {}
            },
            "water": {
                "text": "You eat grilled fish as ferries cross the dark water. 'Some places live between worlds,' he says. 'So do people.'",
                "choices": {}
            }
        },

        "mexico_city": {
            "main": {
                "text": "The city hums around you as grills crackle and tortillas warm by hand.",
                "choices": {
                    "Try tacos from a crowded stand": "tacos",
                    "Visit the market for mole": "mole"
                }
            },
            "tacos": {
                "text": "You eat standing on the sidewalk. Chef Anthony says, 'Never confuse simple with ordinary.'",
                "choices": {}
            },
            "mole": {
                "text": "The mole is deep, smoky, sweet, and bitter. 'Some flavors take generations to explain,' he says.",
                "choices": {}
            }
        }
    }

    current_scene = scenes[city][scene]
    st.write(current_scene["text"])

    for button_text, next_scene in current_scene["choices"].items():
        if st.button(button_text):
            st.session_state.city_scene = next_scene
            st.rerun()

    if scene != "main":
        if st.button("Back to choices"):
            st.session_state.city_scene = "main"
            st.rerun()

    if st.button("Return to destinations"):
        st.session_state.current_node_id = "start"
        st.session_state.started = False
        st.session_state.selected_destination = None
        st.session_state.city_scene = "main"
        st.rerun()

story_data = load_story()

if "started" not in st.session_state:
    st.session_state.started = False

if "current_node_id" not in st.session_state:
    st.session_state.current_node_id = "start"

if "selected_destination" not in st.session_state:
    st.session_state.selected_destination = None

if "allergy" not in st.session_state:
    st.session_state.allergy = None

if "history" not in st.session_state:
    st.session_state.history = []

if "city_scene" not in st.session_state:
    st.session_state.city_scene = "main"

if st.session_state.started and st.session_state.history:
    with st.sidebar:
        st.markdown("### 🗺️ Your Journey")
        for i, stop in enumerate(st.session_state.history):
            st.markdown(f"{i + 1}. {stop}")

# TITLE SCREEN
if not st.session_state.started:
    if os.path.exists("tonyy.png"):
        st.image("tonyy.png", use_container_width=True)

    st.title("🍷 No Reservations: The Afterlife Tour")
    st.write("The city sleeps. Somewhere, one final table is waiting...")

    start_node = story_data["start"]
    st.subheader(start_node.title)
    st.write(start_node.text)

    st.divider()
    st.write("### Before we begin...")
    st.write("Any allergies the chef should be aware of?")

    allergy_options = [
        "No allergies",
        "Seafood allergy",
        "Nut allergy",
        "Dairy allergy",
        "Gluten allergy"
    ]

    selected_allergy = st.radio("Select one option:", allergy_options, index=0)
    st.session_state.allergy = selected_allergy

    if st.session_state.allergy != "No allergies":
        st.info(f"Noted: {st.session_state.allergy}")

    st.divider()

    plane_positions = {
        "istanbul": ("61%", "36%"),
        "tokyo": ("84%", "41%"),
        "new_orleans": ("23%", "42%"),
        "mexico_city": ("17%", "50%")
    }

    plane_left = "50%"
    plane_top = "50%"

    if st.session_state.selected_destination in plane_positions:
        plane_left, plane_top = plane_positions[st.session_state.selected_destination]

    if os.path.exists("worldmap.png"):
        map_base64 = get_base64_file("worldmap.png")
        st.markdown(
            f"""
            <div style="position: relative; width: 100%; max-width: 1000px; margin: auto;">
                <img src="data:image/png;base64,{map_base64}" style="width: 100%; border-radius: 14px;">
                <div style="
                    position: absolute;
                    left: {plane_left};
                    top: {plane_top};
                    transform: translate(-50%, -50%);
                    font-size: 34px;
                    transition: all 0.8s ease;
                ">
                    ✈️
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("### Choose your first destination")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Istanbul, Turkey"):
            st.session_state.selected_destination = "istanbul"
            st.session_state.current_node_id = "istanbul"
            st.session_state.city_scene = "main"
            st.rerun()

        if st.button("Tokyo, Japan"):
            st.session_state.selected_destination = "tokyo"
            st.session_state.current_node_id = "tokyo"
            st.session_state.city_scene = "main"
            st.rerun()

    with col2:
        if st.button("New Orleans, USA"):
            st.session_state.selected_destination = "new_orleans"
            st.session_state.current_node_id = "new_orleans"
            st.session_state.city_scene = "main"
            st.rerun()

        if st.button("Mexico City, Mexico"):
            st.session_state.selected_destination = "mexico_city"
            st.session_state.current_node_id = "mexico_city"
            st.session_state.city_scene = "main"
            st.rerun()

    if st.session_state.selected_destination:
        st.success(
            f"Destination selected: {st.session_state.selected_destination.replace('_', ' ').title()}"
        )

    if st.button("Begin the Tour"):
        if st.session_state.selected_destination is None:
            st.warning("Choose a destination first.")
        else:
            st.session_state.started = True
            st.rerun()

# GAME SCREEN
else:
    current_node = story_data[st.session_state.current_node_id]

    if not st.session_state.history or st.session_state.history[-1] != current_node.title:
        st.session_state.history.append(current_node.title)

    st.title("🍷 No Reservations: The Afterlife Tour")
    st.subheader(current_node.title)

    if st.session_state.allergy and st.session_state.allergy != "No allergies":
        st.caption(f"Chef note: {st.session_state.allergy}")

    if current_node.image:
        image_path = os.path.join("assets/images", current_node.image)
        if os.path.exists(image_path):
            st.image(image_path)

    if st.session_state.current_node_id == "tokyo" and os.path.exists("tokyovideo.mp4"):
        st.video("tokyovideo.mp4")

    if st.session_state.current_node_id == "mexico_city" and os.path.exists("mexico.mp4"):
        st.video("mexico.mp4")

    if st.session_state.current_node_id == "istanbul" and os.path.exists("istanbul.mp4"):
        st.video("istanbul.mp4")

    if st.session_state.current_node_id == "new_orleans" and os.path.exists("jazz.m4a"):
        st.audio("jazz.m4a")

    st.divider()

    if st.session_state.current_node_id in ["tokyo", "istanbul", "new_orleans", "mexico_city"]:
        show_city_scene()

    elif current_node.ending:
        if current_node.ending_type == "good":
            st.success("🍽️ Another unforgettable meal. The End.")
            st.balloons()
        elif current_node.ending_type == "bad":
            st.error("💀 Some tables you shouldn't have sat at. The End.")
            st.snow()
        else:
            st.info("The End.")

        stops = len(st.session_state.history)
        st.markdown(f"**You made {stops} stop{'s' if stops != 1 else ''} on this journey.**")

        if st.button("Take Another Trip"):
            st.session_state.current_node_id = "start"
            st.session_state.started = False
            st.session_state.selected_destination = None
            st.session_state.allergy = None
            st.session_state.history = []
            st.session_state.city_scene = "main"
            st.rerun()

    else:
        st.write(current_node.text)

        for choice in current_node.choices:
            if st.button(choice["text"]):
                st.session_state.current_node_id = choice["next"]
                st.session_state.city_scene = "main"
                st.rerun()