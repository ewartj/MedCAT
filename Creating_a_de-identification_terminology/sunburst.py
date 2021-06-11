import plotly.express as px
import pandas as pd

data = dict(
    concept = ["root concept","name","forename","surname","initials","contact details","address","address line","postcoce","telephone","email","identification num","passport ","driving license","nat insurance","healthcare identifier","nhs num","hosp num","emer dep num","lab num","gmc num","date","date of birth","website"],
    parent = ["","root concept","name","name","name","root concept","contact details","address","address","address","address","root concept","identification num","identification num","identification num","root concept","healthcare identifier","healthcare identifier","healthcare identifier","healthcare identifier","healthcare identifier","root concept","date","root concept"],
    value = ["0","1000","1100","1200","1300","2000","2100","2110","2120","2200","2300","2000","2410","2420","2430","3000","3100","3200","3300","3400","3500","4000","4100","5000"]
)

fig =px.sunburst(
    data,
    names='concept',
    parents='parent',
    values='value',
)
fig.show()