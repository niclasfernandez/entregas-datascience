#Sería mejor un nombre más descriptivo del tipo de gráfico
# Libs import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
from seaborn import boxplot, violinplot
from pandas_profiling import ProfileReport

def graph_histplot_boxplot(df, column):
    with plt.rc_context({'axes.edgecolor':'orange', 'xtick.color':'red', 'ytick.color':'green', 'figure.facecolor':'white'}):
        fig,axes = plt.subplots(nrows=1,ncols=2,dpi=120,figsize = (12,4))

        plot0=sns.histplot(data= df, x=column, kde=True,ax=axes[0],color='green')
        axes[0].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
        axes[0].set_title('Distribution',fontdict={'fontsize':8})
        axes[0].set_xlabel(column,fontdict={'fontsize':7})
        axes[0].set_ylabel('Count/Dist.',fontdict={'fontsize':7})
        plt.tight_layout()

        plot1=sns.boxplot(data=df[column],ax=axes[1], orient="v")
        #axes[1].set_title('Distribution of popularity',fontdict={'fontsize':8})
        #Acá sería mejor no harcodear el string:
        axes[1].set_title(f'Distribution of {column}',fontdict={'fontsize':8})
        axes[1].set_xlabel(column,fontdict={'fontsize':7})
        return plt.tight_layout()
        
def get_frec_acum(df, column):
    # count y convert de popularity
    frec = df[column].value_counts().sort_index()
    frec_df = pd.DataFrame(frec)
    #Asignamos el nombre Frec_abs a la columna
    frec_df.rename(columns={column:'Frec_abs'},inplace=True)
    #Obtenemos los valores de las Frecuencias Absolutas
    Frec_abs_val = frec_df["Frec_abs"].values
    #Creamos una lista vacia en donde vamos a guardar las frecuencias absolutas acumuladas
    acum = []
    #Iniciamos una variable en la que guardaremos los valores anteriores
    valor_acum = 0
    #Recorremos la lista  de las frecuencias absolutas para irlas sumando
    for i in Frec_abs_val:
        valor_acum = valor_acum + i
        acum.append(valor_acum)   
    frec_df["frec_abs_acum"] = acum
    #Calculamos la Frecuencia Relativa en %
    
    #Lo mismo acá
    #frec_df["frec_rel_%"] = round(100 * frec_df["Frec_abs"]/len(df.popularity),4)
    frec_df["frec_rel_%"] = round(100 * frec_df["Frec_abs"]/len(df[column]),4)
    
    #Obtenemos los valores de las Frecuencias Relativas
    Frec_rel_val = frec_df["frec_rel_%"].values
    #Creamos una lista vacia en donde vamos a guardar las frecuencias relativas acumuladas
    acum = []
    #Iniciamos una variable  en la que guardaremos los valores anteriores
    valor_acum = 0
    #Recorremos la lista  de las frecuencias relativas para irlas sumando
    for i in Frec_rel_val:
        valor_acum = valor_acum + i
        acum.append(valor_acum)  
    frec_df["frec_rel_%_acum"] = acum
    return frec_df