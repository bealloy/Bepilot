import pandas as pd
from taipy.gui import Markdown

flow_ui = Markdown("web_pages/Flow/flow.md")

navigation = [("/Setting", "Setting"), ("/Knowledge", "Knowledge"),("/Security", "Security"),("/Function", "Function"),("/Flow", "Flow")]