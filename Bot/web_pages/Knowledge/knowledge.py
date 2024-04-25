import pandas as pd
from taipy.gui import Markdown
import taipy.gui.builder as tgb



import taipy.gui.builder as tgb

navigation = [("/Setting", "Setting"), ("/Knowledge", "Knowledge"),("/Security", "Security"),("/Function", "Function"),("/Flow", "Flow")]



path = "File.pdf"
File_description= {
    "File Name": ["File.pdf","File.pdf"],
    "File Description":["File.pdf","File.pdf"]
}

tgb.table("{File_description}", show_all=True)

def analyze_file(state):
    with open(state.path,"r", encoding="utf-8") as f:
        data = f.read()
        # split lines and eliminates duplicates
        file_list = list(dict.fromkeys(data.replace("\n", " ").split(".")[:-1]))
    state.path = None

with tgb.Page() as knowledge_ui:
    tgb.file_selector("{path}", extensions=".txt", label="Upload .txt file",
                    on_action=analyze_file)


knowledge_ui = Markdown("web_pages/knowledge/knowledge.md")
