# -*- coding: utf-8 -*-
"""Final_Project_Kelompok_11_Visualisasi_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JiRvKHeJQc-rBUKrEkomsI0QtUhbt9G_

# Import Libraries
"""

import pandas as pd
import numpy as np
import datetime

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, DatetimeTickFormatter, HoverTool
from bokeh.models import HoverTool, value, LabelSet, Legend, ColumnDataSource,LinearColorMapper,BasicTicker, PrintfTickFormatter, ColorBar
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel, Select


"""# Load Dataset"""

# Memasukkan dataset saham
df_saham = pd.read_csv('saham.csv',parse_dates=[0])

# Menampilkan dataset saham
df_saham.head()

"""Keterangan Nama Kolom :

1. Date : Tanggal jalannya perdagangan
2. Previous : Harga penutupan hari bursa sebelumnya
3. openPrice : Harga pembukaan pada hari tersebut
4. firstTrade : - 
5. high : Harga tertinggi pada hari tersebut
6. low : Harga terendah pada hari tersebut
7. close : Harga penutupan pada hari tersebut
8. change : Perubahan harga pada hari tersbeut
9. volume : Volume perdagangan (dalam satuan lembar)
10. value : Total nilai perdagangan pada hari tersebut
11. frequency : Frekuensi perdagangan pada hari tersebut
12. indexInvidual : -    
13. offer : Nilai penawaran harga jual pada hari tersebut
14. offerVolume : Volume penawaran harga jual pada hari tersebut
15. bid : Nilai penawaran harga beli pada hari tersebut
16. listedShares : Jumlah saham yang beredar di masyarakat
17. tradebleShares : Jumlah saham yang dapat diperjualbelikan oleh masyarakat
18. weightForIndex : -   
19. foreignSell : Total penjualan oleh asing (dalam satuan lembar)
20. foreignBuy : Total pembelian oleh asing (dalam satuan lembar)
21. foreignBuy : Total pembelian oleh asing (dalam satuan lenbar)
22. delistingDate : Tanggal penghapusan pencatatan saham di BEI
23. nonRegularVolume : Volume pada pasar non-regular
24. nonRegularValue : Total nilai perdagangan pada pasar non-reguler
25. nonRegularFrequency : Total frekuensi transaksi pada pasar non-requler
26. name : Nama perusahaan

# Menampilkan Pergerakan Value, Volume, serta Change Saham dari Perusahaan BNI, BRI, BCA

### Value
"""

# Mengambil data nama perusahaan yang ada dalam dataset yaitu : BNI, BRI, dan BCA
bri = df_saham[df_saham['name'] == 'BRI']
bni = df_saham[df_saham['name'] == 'BNI']
bca = df_saham[df_saham['name'] == 'BCA']


bri_cds = ColumnDataSource(bri)
bni_cds = ColumnDataSource(bni)
bca_cds = ColumnDataSource(bca)

tooltip= [('name', '@name'), ('value', '$y{0.2f}')]
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom,tap"

fig = figure(x_axis_type='datetime', plot_height=500, plot_width=1000, title='',
             x_axis_label='Date', y_axis_label='Value', tooltips = tooltip, tools = TOOLS)

fig.line('date', 'value', color="blue", legend_label='VALUE BRI', source=bri_cds)
fig.line('date', 'value', color="red", legend_label='VALUE BNI', source=bni_cds)
fig.line('date', 'value', color="green" ,legend_label='VALUE BCA', source=bca_cds)

fig.legend.click_policy="hide"
fig.legend.location = 'center_right'

"""### Volume"""

tooltip= [('name', '@name'), ('volume', '$y{0.2f}')]
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom,tap"

fig2 = figure(x_axis_type='datetime', plot_height=500, plot_width=1000, title='Volume',
             x_axis_label='Date', y_axis_label='Volume', tooltips = tooltip, tools = TOOLS)

fig2.line('date', 'volume', color="blue", legend_label='VOLUME BRI', source=bri_cds)
fig2.line('date', 'volume', color="red", legend_label='VOLUME BNI', source=bni_cds)
fig2.line('date', 'volume', color="green" ,legend_label='VOLUME BCA', source=bca_cds)

fig2.legend.click_policy="hide"
fig2.legend.location = 'center_right'

"""### Change"""

tooltip= [('name', '@name'),('change', '$y{0.2f}')]
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom,tap"

fig3 = figure(x_axis_type='datetime', plot_height=500, plot_width=1000, title='Change',
             x_axis_label='Date', y_axis_label='Change', tooltips = tooltip, tools = TOOLS)

fig3.line('date', 'change', color="blue", legend_label='PERUBAHAN HARGA BRI', source=bri_cds)
fig3.line('date', 'change', color="red", legend_label='PERUBAHAN HARGA BNI', source=bni_cds)
fig3.line('date', 'change', color="green" ,legend_label='PERUBAHAN HARGA BCA', source=bca_cds)

fig3.legend.click_policy="hide"
fig3.legend.location = 'center_right'

"""### Convert Data dalam Bentuk Bokeh Widgets Interactive : Tabs """

# import library untuk widgets bokeh tabs
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure

# fungsi untuk menampilkan produk yang akan tersambung dengan show()
output_notebook()
output_file('interactive_tabs.html', title='PERGERAKAN SAHAM BNI, BRI, BCA')

# mengonversikan data figure value, volume, dan change ke dalam variabel tab
tab1 = Panel(child=fig, title="Value")
tab2 = Panel(child=fig2, title="Volume")
tab3 = Panel(child=fig3, title="Change")

# memasukkan data tabs ke dalam variabel figs
figs = Tabs(tabs=[ tab1, tab2,tab3 ])

# menampilkan tabs untuk data value, volume, dan change
show(figs)

"""Menampilkan data dalam bentuk bokeh interactive (Select) Dropdown"""

from bokeh.models import CustomJS, Select
from bokeh.io import show

output_notebook()

output_file('interactive_select.html', title='PERGERAKAN SAHAM BNI, BRI, BCA')

select = Select(title="Pergerakan Saham", value="BASE", options=['Value', 'Volume', 'Change'])
select.js_on_change('value', CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))

# Show the tabbed layout
show(select)
