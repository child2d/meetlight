"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

meet_style = {
    "bg": "white",
    "padding": "1em",
    "border_radius": "40px",
    "w": "100%",
    "align_items": "left",
    "font_family": "Silkscreen",
}


class State(pc.State):
    """The app state."""

    prompt = ""
    image_url = ""
    image_processing = False
    image_made = False

    def submit(self):
        pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("MeetLight", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.button(
                pc.icon(tag="arrow_up"),
                _hover={
                    "opacity": 0.85,
                    "color": "rgb(107,99,246)",
                },
                # on_click=home(),
            ),
            pc.button(
                pc.icon(tag="moon"),
                on_click=pc.toggle_color_mode,
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        bg="#ededed",
        padding_top="10%",
    )


def meet():
    return pc.center(
        pc.vstack(
            pc.tabs(
                pc.tab_list(
                    pc.tab(pc.icon(tag="spinner"), id_="chat", panel_id="chat_panel"),
                    pc.tab(pc.icon(tag="star"), id_="square", panel_id="square_panel"),
                ),
                pc.tab_panels(
                    pc.tab_panel(get_chat_data()),
                    pc.tab_panel(get_square_data()),
                ),
                align="center",
                is_fitted=True,
                color="white",
                shadow="lg",
            ),
            font_size="2em",
            style=meet_style,
        ),
        height="100vh",
        align_items="top",
        bg="#ededed",
        overflow="auto",
        padding_top="2.5%",
        padding_right="35%",
        padding_left="35%",
        padding_bottom="2.5%",
    )


def get_square_data():
    return pc.list(
        pc.list_item("Example 1"),
        pc.list_item("Example 2"),
        pc.list_item("Example 3"),
    )


def get_chat_data():
    return pc.vstack(
        pc.image(src="assets/chat_bg.png", width="100px", height="auto"),
        pc.input(placeholder="Enter a prompt..", on_blur=State.set_prompt),
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


# Add state and page to the app.
app = pc.App(
    state=State,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
    ],
)
app.add_page(index)
app.add_page(meet)
app.compile()
