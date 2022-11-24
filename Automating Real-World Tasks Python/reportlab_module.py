#!/usr/bin/env python3

from string import hexdigits
from turtle import width
from reportlab.platypus import SimpleDocTemplate
#flowables for different parts of report
from reportlab.platypus import Paragraph, Spacer, Table, Image
# style sheet and colors table formatting etc
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
# adding graphs and charts
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

# report object generate PDF using filename given to it
report = SimpleDocTemplate('./report.pdf')

# sytle object similar to HTML sytle objects for fomatting
styles = getSampleStyleSheet()

# report title using paragraph object
report_title = Paragraph("A complete Inventory of My Fruit", styles["h1"])

# convert fruit dictionary into list of list or 2-dim array
table_data = []
for key, value in fruit.items():
    table_data.append([key, value])

# report table object
# report_table = Table(data=table_data)

# formatting table using report lab stylesheet and colors module
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')

# creating pie object
report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

# drawing object to add our pie object for drawing
report_chart = Drawing()
report_chart.add(report_pie)

# building report with title, table and pie chart
report.build([report_title, report_table, report_chart])
