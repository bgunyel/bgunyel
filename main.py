from markdown_it.token import Token
from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import ImageItem, Markdown, Heading
from markdown_it.token import Token

console = Console(record=True, width=100)

## PANEL 1

about = """I'm a Data Scientist / Machine Learning Engineer with 2x M.Sc. degrees. I worked primarily on Computer Vision problems in the past. Currently, I'm more interested in Natural Language Processing and Time-Series applications. 

You can find me on [bold link=https://twitter.com/bertan_gunyel]Twitter[/] and [bold link=https://www.linkedin.com/in/bertan-gunyel/]Linkedin"""

panel1 = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hello everyone", width=90
)

## PANEL 2

tree = Tree("[link=https://www.linkedin.com/in/bertan-gunyel/]Bertan Günyel", guide_style="bold")
projects_tree = tree.add(":open_file_folder: Projects", guide_style="bold")
tech_stack_tree = tree.add(":computer: Tech Stack", guide_style="bold")

projects_time_series_tree = projects_tree.add(':chart_with_upwards_trend: Time-series')
projects_nlp_tree = projects_tree.add(':memo: NLP')

projects_time_series_tree.add("⭐ [link=https://github.com/bgunyel/electricity-load-forecasting]Electricity Load Forecasting")
# projects_time_series_tree.add("⭐ [link=https://github.com/bgunyel/strava-runners]Strava Runners")

projects_nlp_tree.add("⭐ Coming Soon")

tech_stack_nlp_tree = tech_stack_tree.add(':memo: NLP')
tech_stack_ml_tree = tech_stack_tree.add(':rocket: Machine Learning')
tech_stack_ds_tree = tech_stack_tree.add(':dart: Data Science')
tech_stack_vis_tree = tech_stack_tree.add(':art: Visualization')
tech_stack_mlops_tree = tech_stack_tree.add(':hourglass: ML Ops')
tech_stack_cloud_tree = tech_stack_tree.add(':crystal_ball: Cloud Computing')

tech_stack_nlp_tree.add('⭐ Hugging Face')
tech_stack_nlp_tree.add('⭐ NLTK')

tech_stack_ml_tree.add('⭐ PyTorch')
tech_stack_ml_tree.add('⭐ Scikit-learn')

tech_stack_ds_tree.add('⭐ Pandas')
tech_stack_ds_tree.add('⭐ Numpy')
tech_stack_ds_tree.add('⭐ Stats-models')

tech_stack_vis_tree.add('⭐ Matplotlib')
tech_stack_vis_tree.add('⭐ Seaborn')
tech_stack_vis_tree.add('⭐ Plotly')

tech_stack_mlops_tree.add('⭐ Domino Data Lab')
tech_stack_mlops_tree.add('⭐ Weights & Biases')

tech_stack_cloud_tree.add('⭐ AWS')
tech_stack_cloud_tree.add('⭐ GCP')
tech_stack_cloud_tree.add('⭐ Azure')

panel2 = Panel.fit(tree, box=box.DOUBLE, border_style="blue", title="[b]Technical Breakdown", width=80)

## PANEL 3



# panel3 = Panel.fit(img, box=box.DOUBLE, border_style="blue", title="[b]Github Stats", width=80)

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item

This is an image
![encoder-decoder](https://miro.medium.com/max/700/1*62xsdc5F5DNdLXluQojeBg.png)
"""

md = Markdown(MARKDOWN)




# console.print(md)
console.print(Columns([panel1, panel2, md]))



CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
