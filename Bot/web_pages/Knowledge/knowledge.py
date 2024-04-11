import pandas as pd
from taipy.gui import Markdown

import taipy.gui.builder as tgb


css_styles = """.sidebar {
    background-color: black; /* Set sidebar background color to black */
    color: white; /* Set text color to white */
    padding: 20px;
}

.mainpage {
    background-color: grey; /* Set main page background color to grey */
    padding: 20px;
    text-align: center; /* Center-align content within the main page */
}

.button {
    background-color: white; /* Set button background color to white */
    color: black; /* Set button text color to black */
    padding: 10px 20px; /* Adjust padding as needed */
    border: none; /* Remove border */
    cursor: pointer;
}

.container-bg {
  background-color: rgb(80, 127, 172);
}
"""

path = ""
def analyze_file(state):
    with open(state.path,"r", encoding="utf-8") as f:
        data = f.read()
        # split lines and eliminates duplicates
        file_list = list(dict.fromkeys(data.replace("\n", " ").split(".")[:-1]))
    state.path = None

with tgb.Page() as knowledge_ui:
    tgb.file_selector("{path}", extensions=".txt", label="Upload .txt file",
                    on_action=analyze_file)


knowledge_ui = Markdown("web_pages/knowledge/knowledge.md",style=css_styles)
