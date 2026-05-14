#!/usr/bin/env python3
"""
Translate German content in Jupyter notebooks to English.
- Translates all markdown cells entirely
- Translates comment lines (starting with #) in code cells
- Does NOT touch variable names, column names, data strings, etc.
"""

import json
import os
import re

BASE = '/Users/felixklein/Documents/Claude/Projects/Personal Enginnering System/01_REPO_INBOX/Python-Course'

NOTEBOOKS = [
    'lec02/03_logical_functions.ipynb',
    'lec02/05_logical_functions_exercise.ipynb',
    'lec02/07_logical_functions_exercise_solution.ipynb',
    'lec03/01_numpy_empty.ipynb',
    'lec03/02_numpy_filled.ipynb',
    'lec03/04_numpy_exercise.ipynb',
    'lec03/06_numpy_exercise_solution.ipynb',
    'lec04/01_pandas_empty.ipynb',
    'lec04/02_pandas_filled.ipynb',
    'lec04/05_pandas_exercise.ipynb',
    'lec04/07_pandas_exercise_solution.ipynb',
    'lec04/09_matplotlib.ipynb',
    'lec04/10_matplotlib_exercise.ipynb',
    'lec04/11_matplotlib_exercise_solution.ipynb',
    'lec05/01_seaborn_distribution_plots.ipynb',
    'lec05/02_seaborn_categorical_plots.ipynb',
    'lec05/03_seaborn_matrix_plots.ipynb',
    'lec05/04_seaborn_grids.ipynb',
    'lec05/05_seaborn_regression_plots.ipynb',
    'lec05/06_seaborn_style_and_color.ipynb',
    'lec05/07_plotly.ipynb',
]

# -------------------------------------------------------------------
# Translation tables
# Each entry: (exact_source_string, translated_string)
# Order matters: more specific / longer strings first.
# -------------------------------------------------------------------

MARKDOWN_TRANSLATIONS = {
    # lec03/04_numpy_exercise.ipynb and lec03/06_numpy_exercise_solution.ipynb
    '# Übung numpy - Lösung': '# NumPy Exercise',

    # lec04/01_pandas_empty.ipynb and lec04/02_pandas_filled.ipynb – markdown cells
    '## Einführung Pandas\n\nPandas kann man sich als eine sehr mächtige Version von Excel vorstellen, welche viel mehr Werkzeuge liefert. Hier behandeln:\n    - Series\n    - Dataframes\n    - Missing Data \n    - GroupBy\n    - Merging, Joining und Concatenating\n    - Operationen\n    - Dateneingabe und -ausgabe':
        '## Introduction to Pandas\n\nPandas can be thought of as a very powerful version of Excel that provides many more tools. Topics covered here:\n    - Series\n    - DataFrames\n    - Missing Data\n    - GroupBy\n    - Merging, Joining, and Concatenating\n    - Operations\n    - Data Input and Output',

    '** Auch hier müssen wir Pandas erstmal installieren! ** via poetry: `poetry add pandas`':
        '** Here too we need to install Pandas first! ** via poetry: `poetry add pandas`',

    '** Auch hier müssen wir Pandas erstmal installieren! **\nvia poetry: `poetry add pandas`':
        '** Here too we need to install Pandas first! **\nvia poetry: `poetry add pandas`',

    '### Series\nEine Folge in Pandas ist fast genau wie ein Numpy Array und fast genau wie eine Liste mit einem individuellen Index. Allerdings erlaubt eine Pandas Serie im Gegensatz zu einem Numpy Array, dass die Achsen beschriftet bzw gelabelt sein können. Es kann zudem jedes beliebige Python Objekt beinhalten.':
        '### Series\nA Pandas Series is almost exactly like a NumPy array and almost exactly like a list with an individual index. However, unlike a NumPy array, a Pandas Series allows the axes to be labeled. It can also contain any arbitrary Python object.',

    '#### Index\nDie Möglichkeit Indexs zu verwenden macht Pandas Serien sehr nützlich.\nBeispiel:':
        '#### Index\nThe ability to use indexes makes Pandas Series very useful.\nExample:',

    'Gibt uns die Spalte mit dem Index X zurück, welche nichts anderes als eine Pandas Serie ist!':
        'Returns the column with index X, which is nothing other than a Pandas Series!',

    '#### Spalten löschen': '#### Deleting Columns',

    '#### Zeilen löschen\n\nFunktioniert genauso, nur muss der axis-Parameter auf 0 gesetzt werden':
        '#### Deleting Rows\n\nWorks the same way, but the axis parameter must be set to 0',

    '#### Reihen auswählen': '#### Selecting Rows',

    '#### Teilmengen von Zeilen und Spalten auswählen': '#### Selecting Subsets of Rows and Columns',

    '#### Weitere Möglichkeiten': '#### Further Options',

    '#### Concatenation (Verkettung)\nVerkettet DataFrames. Die Länge der Achse, auf die verkettet wird, muss übereinstimmen. Zum Verketten kann man pd.concat verwenden.':
        '#### Concatenation\nConcatenates DataFrames. The length of the axis being concatenated must match. You can use pd.concat for concatenation.',

    'Es gibt vesrschiedene wichtige Operationen, die nützlich für uns sein können. Ein paar möchten wir hier kennenlernen. Aber wie immer gilt im programmieren. Dokumentationen der Bibliotheken bzw das Internet zu durchforschen, falls man ein Problem lösen möchte':
        'There are various important operations that can be useful for us. We want to get to know a few of them here. But as always in programming: search the library documentation or the internet when you want to solve a problem.',

    '#### Eine Spalte für immer Löschen': '#### Permanently Deleting a Column',

    '#### Spalten- und Indexnamen zurückgeben': '#### Returning Column and Index Names',

    "Das Laden von Datensätzen erfolgt über eine der folgenden Funktionen:\n\n    - pd.read_csv\n    - pd.read_excel\n    - pd.read_html\n\nFür einen Überblick siehe https://pandas.pydata.org/pandas-docs/stable/io.html\n\nBsp:\n\n    pd.read_csv('myfile.csv')":
        "Loading datasets is done using one of the following functions:\n\n    - pd.read_csv\n    - pd.read_excel\n    - pd.read_html\n\nFor an overview see https://pandas.pydata.org/pandas-docs/stable/io.html\n\nExample:\n\n    pd.read_csv('myfile.csv')",

    'Pandas kann Excel-Dateien lesen und schreiben. **Aber Pandas kann nur Daten importiert.** Keine Formeln, Bilder, Makros! Kann zum Absturz führen!':
        'Pandas can read and write Excel files. **But Pandas can only import data.** No formulas, images, or macros! This can cause crashes!',

    '#### Excel Ausgabe\n\nDazu wird das paket ***openpyxl*** benötigt.':
        '#### Excel Output\n\nThis requires the ***openpyxl*** package.',

    'Je nachdem was man einlesen möchte gibt es hier weiterführende Bibliotheken, die man zuvor installieren muss.\n\nIn der Anaconda Command Prompt:\n    - conda install lxml\n    - conda install html5lib\n    - conda install BeautifulSoup4\n    \nJupyter neustarten und dann kann es losgehen!':
        'Depending on what you want to read, there are additional libraries that need to be installed first.\n\nIn the Anaconda Command Prompt:\n    - conda install lxml\n    - conda install html5lib\n    - conda install BeautifulSoup4\n    \nRestart Jupyter and then you are good to go!',

    # lec04/05_pandas_exercise.ipynb and lec04/07_pandas_exercise_solution.ipynb
    '# Pandas Übung': '# Pandas Exercise',

    'Lade aus der Datei `04_pandas-excelbsp.xlsx` das Sheet `BL_7-Tage-Inzidenz` als `pd.DataFrame` ein. Verwende das Argument `index_col=0`, um die Bundesländer als Index zu setzen für die Zeilen.':
        'Load the sheet `BL_7-Tage-Inzidenz` from the file `04_pandas-excelbsp.xlsx` as a `pd.DataFrame`. Use the argument `index_col=0` to set the federal states as the row index.',

    'Glückwunsch, du hast es geschafft!': 'Congratulations, you made it!',

    # lec04/09_matplotlib.ipynb
    '## Einführung\nMatplotlib ist die erste Bibliothek zur Datenvisualisierung mit Python, auf der viele andere Biliotheken beruhen. Es wurde von John Hunter erstellt. Dabei versuchte er die Plotfunktionen von MatLab (einer weiteren Programmiersprache) in Python zu replizieren. Wer mit matlab vertraut ist, wird sich sofort wie zu Hause fühlen.':
        '## Introduction\nMatplotlib is the first Python data visualization library, on which many other libraries are built. It was created by John Hunter, who tried to replicate the plotting functions of MatLab (another programming language) in Python. Anyone familiar with Matlab will immediately feel at home.',

    'Außerdem muss folgende Zeile ebenfalls immer ausgeführt werden:':
        'In addition, the following line must always be executed:',

    'Notiz: Das gilt nur fuer das Jupyter Notebook. Für andere Editoren gilt es `plt.show()` am Ende des ganzen Programmcodes anzufügen, damit die Grafik sich in einem neuen Fenster öffnet!':
        'Note: This only applies to the Jupyter Notebook. For other editors, you need to add `plt.show()` at the end of the entire program code so the plot opens in a new window!',

    '### Einfuehrung in die objektorientierte Methode\nDiese Art und Weise ist uebersichtlicher, wenn mehrere Grafiken in einer Ausgabe ausgegeben werden sollen.\n\nZu Beginn erstellen wir eine Instanz `figure`. Dann können wir diesem Objekt Achsen hinzufuegen:':
        '### Introduction to the Object-Oriented Method\nThis approach is cleaner when multiple plots need to be displayed in a single output.\n\nWe start by creating a `figure` instance. We can then add axes to this object:',

    'Code ist etwas komplizierter, aber der Vorteil ist, dass wir jetzt die volle Kontrolle darüber haben, wo die einzelnen Achsen der Plots platziert sind. Wir koennen dadurch einfach weitere Plots hinzufuegen:':
        'The code is a bit more complex, but the advantage is that we now have full control over where the individual axes of the plots are placed. This makes it easy to add further plots:',

    '### Abbildungsgröße (figure size), Seitenverhältnis (aspect ratio) und DPI\nMatplotlib ermoeglicht die Angabe von Seitenverhaeltnis, DPI und Abbildungsgroeße beim Erstellen des Figure-Objekts. \n\n   - `figsize` ist ein Tupel aus der Breite und Hoehe der Figur in Zoll.\n   -  `dpi` ist die Punktzahl pro Zoll in der Figur.':
        '### Figure Size, Aspect Ratio, and DPI\nMatplotlib allows you to specify the aspect ratio, DPI, and figure size when creating the Figure object.\n\n   - `figsize` is a tuple of the width and height of the figure in inches.\n   - `dpi` is the number of dots per inch in the figure.',

    '# Spezielle Plottypen\n\nEs gibt viele spezialisierte Diagramme, die wir erstellen können, wie z.B. Barplots, Histogramme, Scatter-Plots und vieles mehr. \n\nDie meisten dieser Arten von Plots werden wir aber mit seaborn erstellen, einer statistischen Plotbibliothek für Python. \n\nHier allerdings ein paar kurze Beispiele, lediglich um zu zeigen, was möglich ist!':
        '# Special Plot Types\n\nThere are many specialized charts we can create, such as bar plots, histograms, scatter plots, and much more.\n\nHowever, most of these plot types will be created with Seaborn, a statistical plotting library for Python.\n\nHere are just a few brief examples, simply to show what is possible!',

    '# Weiterführende Quellen': '# Further Resources',

    # lec04/10_matplotlib_exercise.ipynb and lec04/11_matplotlib_exercise_solution.ipynb
    '# Matplotlib Uebungen \n\nNehmt euch hierfuer nun Zeit, Matplotlib kann anfangs schwierig zu verstehen sein. Dies sind relativ einfache Diagramme, aber es trotzdem nicht einfach, wenn man das erste Mal mit matplotlib arbeitet.\n\nAußerdem keine Sorge, falls ihr die Syntax von Matplotlib frustrierend findet, viele Leute bevorzugen tatsächlich eine andere Bibliothek namens Seaborn, die wir uns im Anschluss genauer anschauen.':
        '# Matplotlib Exercises\n\nTake your time here — Matplotlib can be difficult to understand at first. These are relatively simple charts, but it is still not easy when working with Matplotlib for the first time.\n\nAlso, do not worry if you find the Matplotlib syntax frustrating; many people actually prefer a different library called Seaborn, which we will look at in more detail next.',

    '## Aufgabe 1\n** Führe diese Schritte aus:**\n\n    - Erstelle ein Figure-Objekt namens fig mit plt.figure().\n    - Verwende add_axes, um eine Achse zur Figuren-Leinwand bei [0,0,1,1] hinzuzufuegen. Nenne diese neue Achse ax.\n    - Plotte (x,y) auf den Achsen und waehle Beschriftung und Titel so, dass sie korrekt sind.':
        '## Exercise 1\n** Follow these steps:**\n\n    - Create a Figure object named fig using plt.figure().\n    - Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Name this new axis ax.\n    - Plot (x,y) on the axes and choose labels and title appropriately.',

    '** Plotte nun (x,y) und (x,z) auf den Achsen. Spiele mit der Linienbreite und dem Stil herum. Außerdem sorge dafuer, dass es keine Ueberlappung gibt.**':
        '** Now plot (x,y) and (x,z) on the axes. Experiment with line width and style. Also make sure there is no overlap.**',

    # lec05/01_seaborn_distribution_plots.ipynb
    '## Daten\nSeaborn stellt Beispieldatensätze zur Verfügung, welche wir hier verwenden werden.':
        '## Data\nSeaborn provides example datasets, which we will use here.',

    '## jointplot\n\njointplot() ermoeglicht es, zwei distplots für bivariate Daten zu vergleichen. Hierbei setzt man den **kind** Parameter, um anzugeben, welche Art von Plot man verwenden moechte: \n\n* "scatter" \n* "reg" \n* "resid" \n* "kde" \n* "hex"':
        '## jointplot\n\njointplot() allows you to compare two distribution plots for bivariate data. You set the **kind** parameter to specify which type of plot to use:\n\n* "scatter"\n* "reg"\n* "resid"\n* "kde"\n* "hex"',

    '## pairplot\n\npairplot zeichnet paarweise Beziehungen über ein gesamtes Dataframe (nur für die numerischen Spalten) und unterstützt ein Argument für den Farbton (für kategorische Spalten). ':
        '## pairplot\n\npairplot plots pairwise relationships across an entire DataFrame (only for numerical columns) and supports a hue argument (for categorical columns).',

    '## rugplot\n\nRugplots sind eigentlich ein sehr einfaches Konzept. Sie zeichnen lediglich eine Strichmarkierung für jeden Punkt einer univariaten Verteilung. Sie sind der Baustein eines KDE-Plots:':
        '## rugplot\n\nRug plots are actually a very simple concept. They simply draw a tick mark for each point in a univariate distribution. They are the building block of a KDE plot:',

    '## kdeplot\n\nkdeplots sind [Kernel Density Estimation plots (Kerndichteschaetzer)*](https://de.wikipedia.org/wiki/Kerndichteschätzer). Diese KDE-Diagramme ersetzen jede einzelne Beobachtung durch eine Gaußsche (Normal-)Verteilung, die sich um diesen Wert dreht. Zum Beispiel:':
        '## kdeplot\n\nKDE plots are [Kernel Density Estimation plots](https://en.wikipedia.org/wiki/Kernel_density_estimation). These KDE plots replace each individual observation with a Gaussian (normal) distribution centered around that value. For example:',

    # lec05/02_seaborn_categorical_plots.ipynb
    '# Diagramme fuer kategorische Daten\n\nHier schauen wir uns nun die Verwendung von Seaborn zur Darstellung kategorischer Daten an! Es gibt dafür einige wesentliche Plottypen:\n\n\n* factorplot\n* boxplot\n* violinplot\n* stripplot\n* swarmplot\n* barplot\n* countplot\n\nIm Folgenden gibt es Beispiele fuer jeden Plottypen!':
        '# Charts for Categorical Data\n\nHere we look at how to use Seaborn to visualize categorical data! There are several key plot types:\n\n\n* factorplot\n* boxplot\n* violinplot\n* stripplot\n* swarmplot\n* barplot\n* countplot\n\nBelow are examples for each plot type!',

    '## barplot and countplot\n\n**Barplot** ist eine allgemeine Darstellung, die es ermöglicht, die kategorischen Daten basierend auf einer Funktion zu aggregieren, standardmäßig den Mittelwert:':
        '## barplot and countplot\n\n**Barplot** is a general representation that allows you to aggregate categorical data based on a function, by default the mean:',

    '### countplot\n\nDies ist im Wesentlichen dasselbe wie bei Barplot, außer dass der Schätzer explizit die Anzahl der Vorkommnisse zählt. Deshalb übergeben wir nur den x-Wert:':
        '### countplot\n\nThis is essentially the same as barplot, except that the estimator explicitly counts the number of occurrences. That is why we only pass the x value:',

    '## boxplot und violinplot\n\nBoxplots und Violinplots werden verwendet, um die Verteilung der kategorischen Daten darzustellen. Ein Box-Plot (oder Box-and Whisker-Plot) zeigt die Verteilung quantitativer Daten so, dass Vergleiche zwischen Variablen oder über Ebenen einer kategorischen Variablen hinweg erleichtert werden:':
        '## boxplot and violinplot\n\nBoxplots and violin plots are used to show the distribution of categorical data. A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable:',

    '### violinplot\n\nEine Violinplot spielt eine ähnliche Rolle wie eine Box- und Whiskerplot. Es zeigt die Verteilung quantitativer Daten über mehrere Ebenen einer (oder mehrerer) kategorialer Variablen, so dass diese Verteilungen verglichen werden können. Im Gegensatz zu einem Boxplot, bei dem alle Plots seine Komponenten zusammenfasst, hat Violinplots alle Datenpunkte vorhanden und erlaubt so einen besseren visuellen Eindruck der zugrundeliegenden Verteilung:':
        '### violinplot\n\nA violin plot plays a similar role to a box-and-whisker plot. It shows the distribution of quantitative data across multiple levels of one (or more) categorical variables so that these distributions can be compared. Unlike a boxplot which summarizes all components, a violin plot shows all data points and thus gives a better visual impression of the underlying distribution:',

    '## stripplot und swarmplot\n\nDer Stripplot zeichnet ein Scatterplot, bei dem eine Variable kategorisch ist. Ein Streifenplot kann für sich allein gezeichnet werden, ist aber auch eine gute Ergänzung zu einem Box- oder Geigenplot, wenn alle Beobachtungen zusammen mit einer Darstellung der zugrunde liegenden Verteilung gezeigt werden sollen:':
        '## stripplot and swarmplot\n\nThe strip plot draws a scatter plot where one variable is categorical. A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot when you want to show all observations alongside a representation of the underlying distribution:',

    '## factorplot\n\nAndere Möglichkeit: Faktorplot ist die allgemeine Form eines kategorischen Plots. Es kann ein **kind** Parameter übergeben werden, um den Plottyp anzupassen:':
        '## factorplot\n\nAnother option: Factorplot is the general form of a categorical plot. A **kind** parameter can be passed to customize the plot type:',

    # lec05/03_seaborn_matrix_plots.ipynb
    '# Matrix Plots\n\nMatrixdiagramme ermöglichen es, Daten als farbcodierte Matrizen darzustellen und können auch verwendet werden, um Cluster innerhalb der Daten anzuzeigen.\n\nBeginnen wir mit der Erkundung der Heatmap und Clustermap von Seaborn:':
        '# Matrix Plots\n\nMatrix plots allow you to display data as color-coded matrices and can also be used to show clusters within the data.\n\nLet us start by exploring the Heatmap and Clustermap from Seaborn:',

    '## Heatmap\n\nDamit eine Heatmap richtig funktioniert, sollten die Daten bereits in Matrixform vorliegen, die Funktion sns.heatmap färbt sie im Grunde nur ein. Zum Beispiel:':
        '## Heatmap\n\nFor a heatmap to work correctly, the data should already be in matrix form — the sns.heatmap function essentially just colors it. For example:',

    'Beachte hier, dass die Jahre und Monate nicht mehr geordnet sind, sondern nach Wertgleichheit gruppiert (Passagierzahl). Das bedeutet, dass wir anfangen können, aus dieser Handlung auf Dinge zu schließen, wie z.B. August und Juli sind sich ähnlich (ergibt Sinn, da beide Sommerreisemonate sind).':
        'Note here that the years and months are no longer ordered, but grouped by similarity in value (passenger count). This means we can start to infer things from this plot, such as: August and July are similar (which makes sense, as both are summer travel months).',

    # lec05/04_seaborn_grids.ipynb
    '# Grids (Gitter)\n\nGitter sind allgemeine Arten von Diagrammen, die es ermöglichen, Diagrammtypen auf Zeilen und Spalten eines Gitters abzubilden, was hilft, ähnliche Diagramme zu erstellen, die durch Merkmale (Features) getrennt sind.':
        '# Grids\n\nGrids are general types of plots that allow you to map plot types onto rows and columns of a grid, which helps to create similar charts separated by features.',

    '## JointGrid\n\nJointGrid ist eine weitere Möglichkeit Plots vom Typ jointplot() zu erstellen. Kurzes Beispiel:':
        '## JointGrid\n\nJointGrid is another way to create jointplot()-type plots. A brief example:',

    # lec05/05_seaborn_regression_plots.ipynb
    '# Regressionsplots\n\nSeaborn hat viele eingebaute Fähigkeiten für Regressionsplots. Hier werden wir uns lediglich die Funktion **lmplot()** anschauen und das Thema Regression im Allgemeinen nicht näher behandeln.\n\n**lmplot** ermöglicht es, lineare Modelle anzuzeigen, aber es ermöglicht auch, diese Diagramme auf Gittermuster aufzuteilen, wobei es sich als leistungsstarkes Werkzeug erweist.':
        '# Regression Plots\n\nSeaborn has many built-in capabilities for regression plots. Here we will only look at the **lmplot()** function and will not go into regression in general.\n\n**lmplot** allows you to display linear models, but it also allows you to split these plots onto grid patterns, making it a powerful tool.',

    '### Marker\n\nlmplot kwargs werden an regplot übergeben, was eine umfassendere Form von lmplot() ist. regplot hat einen scatter_kws-Parameter, der an plt.scatter übergeben wird. Man setzt also den Parameter s in diesem Dictionary, der der quadratischen Markergröße entspricht. Mit anderen Worten, man übergibt s=100 für 10x10-Marker.':
        '### Marker\n\nlmplot kwargs are passed to regplot, which is a more comprehensive form of lmplot(). regplot has a scatter_kws parameter that is passed to plt.scatter. So you set the parameter s in this dictionary, which corresponds to the squared marker size. In other words, pass s=100 for 10x10 markers.',

    '## Benutzung eines Gitters\n\nWir können eine variable Trennung durch Spalten und Zeilen eines Gitters hinzufügen. Dazu gibt man einfach die Argumente col oder row an.':
        '## Using a Grid\n\nWe can add a variable separation via columns and rows of a grid. Simply pass the col or row arguments.',

    '## Aspekt und Größe\n\nSeaborn-Figuren können ihre Größe und ihr Seitenverhältnis mit den Parametern **size** und **aspect** einstellen:':
        '## Aspect and Size\n\nSeaborn figures can set their size and aspect ratio using the **size** and **aspect** parameters:',

    # lec05/06_seaborn_style_and_color.ipynb
    '# Stil und Farbe\n\nHier nochmal eine genaue Erklärung wie man den Stil und die Farben in Seaborn verändern kann.':
        '# Style and Color\n\nHere is a detailed explanation of how to change the style and colors in Seaborn.',

    "Man kann matplotlib's **plt.figure(figsize=(width,height) ** verwenden, um die Größe der meisten Seaborn-Plots zu ändern.\n\nUnd man kann die Größe und das Seitenverhältnis der meisten Seaborn-Gitterplots steuern, indem Sie Parameter übergeben: size und aspect. Zum Beispiel:":
        "You can use matplotlib's **plt.figure(figsize=(width,height))** to change the size of most Seaborn plots.\n\nAnd you can control the size and aspect ratio of most Seaborn grid plots by passing the parameters: size and aspect. For example:",

    '## Skala und Kontext\n\nDie Funktion set_context() ermöglicht es, Standardparameter zu überschreiben:':
        '## Scale and Context\n\nThe set_context() function allows you to override default parameters:',

    # lec05/07_plotly.ipynb
    '# Einführung in Plotly': '# Introduction to Plotly',

    ' [Plotly](https://plotly.com) ist eine interaktive Python Plottingbibliothek mit der über 40 verschiedene Charttypen, die eine Breite Anwendung inder Statistik, BWL, Geographie und anderen Use-Cases haben.\n\n Aufbauen auf der Plotly JavaScript Bibliothek, ermöglicht  `plotly` Pythonnutzern sehr einfach interaktive Plots zu erstellen.':
        ' [Plotly](https://plotly.com) is an interactive Python plotting library with over 40 different chart types that have broad applications in statistics, business, geography, and other use cases.\n\n Built on top of the Plotly JavaScript library, `plotly` makes it very easy for Python users to create interactive plots.',

    '## Plotly Express\n\nDas `plotly.express` Modul enthält zahlreiche Funktionen, mit denen sehr schnell Plots erstellt werden können. Es wird empfohlen, stets mit diesen Modul zu beginnen, um schnell Plots zu prototypen. Jede Plotly Express Funktion nutzt intern `graph objects` und gibt ein `plotly.graph_objects.Figure` zurück.':
        '## Plotly Express\n\nThe `plotly.express` module contains numerous functions that allow you to create plots very quickly. It is recommended to always start with this module to rapidly prototype plots. Each Plotly Express function uses `graph objects` internally and returns a `plotly.graph_objects.Figure`.',

    '### Scatterplot\n\nPlotly enthält auch standardmäßig Datensätze, einen solchen werden wir verwenden.':
        '### Scatter Plot\n\nPlotly also includes built-in datasets, one of which we will use here.',

    'Der Plot kann auch super einfach mit weiteren Features ausgestattet werden wie hier im Beispiel OLS-Schätzer und Violinenplots, eine Modifikation von Boxplots. Für den Plot wird das Modul  `statsmodels` benötigt, dass ihr mit `poetry add statsmodels` installieren könnt.':
        'The plot can also be very easily extended with additional features, such as OLS estimators and violin plots (a modification of boxplots) as shown in this example. The plot requires the `statsmodels` module, which you can install with `poetry add statsmodels`.',

    "...das war's auch schon, was wir Euch aus dem bunten Blumenstrauß, den Plotly bietet, zeigen wollten. Es gibt wesentlich mehr, dazu könnt ihr einfach euch die Plotly Dokumentation anschauen. Kurz sei im Folgenden noch erwähnt, wie Graph Objects auch manuell gebaut werden können.":
        "...and that is all we wanted to show you from the wide range of what Plotly has to offer. There is much more available — simply check the Plotly documentation. Below is a brief look at how Graph Objects can also be built manually.",

    'Wenn wir nicht das High-Level-Interface nutzen moechten, können wir Graph Objects auch explizit als Objekt definieren und zusammenbauen. Dazu importieren wir das Graph Objects Modul.':
        'If we do not want to use the high-level interface, we can also define and assemble Graph Objects explicitly as objects. To do this, we import the Graph Objects module.',

    'Alternativ kann man auch ein Graph Object als Dictionary übergeben.':
        'Alternatively, you can also pass a Graph Object as a dictionary.',
}

# Code comment translations: map exact comment strings (without the leading #)
# We match lines that start with optional whitespace + #
CODE_COMMENT_TRANSLATIONS = {
    # lec03/02_numpy_filled.ipynb
    'Mit Daten befüllen': 'Fill with data',

    # lec03/04_numpy_exercise.ipynb and lec03/06_numpy_exercise_solution.ipynb
    ' Erstelle eine Einheitsmatrix (1 auf der Diagonale, sonst überall0 0) der Dimension (6,6)':
        ' Create an identity matrix (1 on the diagonal, 0 everywhere else) of dimension (6,6)',
    ' Lasse dir die Einheitsmatrix ausgeben':
        ' Display the identity matrix',
    ' Erstelle nun eine Matrix mit 1,2,...,6 auf der Diagonalen und sonst überall 0 indem du die Matrix Einheitsmatrix mit dem Vektor Noten multiplizierst.':
        ' Now create a matrix with 1,2,...,6 on the diagonal and 0 everywhere else by multiplying the identity matrix by the vector of grades.',
    ' ...': ' ...',
    ' Lasse dir alle Einträge von Normalmatrix ausgeben, die über dem empirischen Mittelwert aller Beobachtungen sind':
        ' Display all entries of normalmatrix that are above the empirical mean of all observations',
    ' Berechne nun den Mittelwert und den Median der davor ausgewählten Elemente':
        ' Now calculate the mean and median of the previously selected elements',

    # lec04/01_pandas_empty.ipynb and lec04/02_pandas_filled.ipynb code comments
    ' hier nochmal: parameter-namen müssen nicht angegeben werden, wenn man die reihenfolge der parameter einhält!':
        ' reminder: parameter names do not need to be specified if you follow the order of parameters!',
    ' man kann auch gleich mehrere Spalten ausgeben lassen, indem man eine Liste mit den Indexen übergibt':
        ' you can also display multiple columns at once by passing a list of indexes',
    ' es wird nur aus der Ansicht gelöscht, aber nicht aus dem eigentlichen DataFrame (das muss explizit spezifiziert werden)!':
        ' it is only deleted from the view, but not from the actual DataFrame (this must be specified explicitly)!',
    " um die Spalte 'komplett' zu löschen muss der inplace-Parameter auf True gesetzt werden":
        " to delete the column 'permanently', the inplace parameter must be set to True",
    ' Index zurücksetzen auf 0,1,...,n Index': ' Reset index to 0,1,...,n index',
    ' wieder nicht inplace, da Parameter nicht gesetzt': ' not inplace again, since parameter is not set',
    ' Laender als Index auswählen': ' Select countries as index',
    " andere Möglichkeit für df.loc['G1'] - cross-section": " another option for df.loc['G1'] - cross-section",
    ' Lösche die Zeilen, die fehlende Daten haben': ' Delete the rows that have missing data',
    ' Lösche die Spaalten die fehlende Daten haben': ' Delete the columns that have missing data',
    ' meistens überlegt man sich eine Strategie, wie man mit fehlenden Werten umgeht. Bei Zahlen könnte man sich überlegen':
        ' usually you think of a strategy for handling missing values. For numbers, you might consider',
    ' den Mittelwert zu nehmen': ' taking the mean',
    ' Daten für das DataFrame': ' Data for the DataFrame',
    ' Geht natürlich auch direkt': ' Can of course also be done directly',
    '\xa0data\xa0für\xa0df1': ' data for df1',
    ' data für df2': ' data for df2',
    'Hier Frage!': 'Question here!',
    'Anzahl eindeutiger Werte rausfinden': 'Find number of unique values',
    'Möglichkeit1': 'Option 1',
    'Selektieren von einem DataFrame basierend auf Kritieren für mehrere Spalten':
        'Select from a DataFrame based on criteria for multiple columns',
    ' Zeilen mit Nullwerten löschen': ' Delete rows with null values',

    # lec04/05_pandas_exercise.ipynb and lec04/07_pandas_exercise_solution.ipynb
    ' Lasse dir alle Indizenzen für den 13. Oktober (2020-10-13) ausgeben':
        ' Display all incidences for October 13 (2020-10-13)',
    ' Lasse dir das Bundesland ausgeben, in dem die höchste Inzidenz geherrscht hat am 13. Oktober':
        ' Display the federal state with the highest incidence on October 13',
    ' Tipp: idxmax()': ' Hint: idxmax()',
    ' Lasse dir für Baden-Württemberg die Zahlen von 01. Oktober bis einschließlich 15. Oktober ausgeben':
        ' Display the figures for Baden-Württemberg from October 1 through October 15 inclusive',
    ' Tipp: df.loc[...][...:...]': ' Hint: df.loc[...][...:...]',
    ' Gruppiere nach Wochentagen (Mo-Fr), und bilde den jeweiligen Mittelwert über alle Observationen an dem Wochentag für jedes Bundesland':
        ' Group by weekday (Mon-Fri), and calculate the mean across all observations for that weekday for each federal state',
    ' Tipp: df.columns.weekday, axis=1, mean': ' Hint: df.columns.weekday, axis=1, mean',
    ' Verwende das Ergebnis des letzten Schritts und berechne den Mittelwert über alle Bundesländer für die jeweiligen Wochentage':
        ' Use the result from the previous step and calculate the mean across all federal states for each weekday',
    ' Tipp: groupby, mean': ' Hint: groupby, mean',
    ' Berechne nun die Differenz der logarithmierten Werte von einem auf den nächsten Tag':
        ' Now calculate the difference of the log values from one day to the next',
    ' Tipp: diff, axis=1': ' Hint: diff, axis=1',
    ' Berechne nun den Mittelwert für jedes Bundesland über alle Beobachtungen':
        ' Now calculate the mean for each federal state across all observations',
    ' Tipp: mean, axis=1, skipna=True': ' Hint: mean, axis=1, skipna=True',
    ' Berechne nun den Median für jedes Bundesland über alle Beobachtungen':
        ' Now calculate the median for each federal state across all observations',
    ' Tipp: median, axis=1, skipna=True': ' Hint: median, axis=1, skipna=True',

    # lec04/09_matplotlib.ipynb code comments
    " Wir benutzen ein Numpy array fuer die Daten die wir 'plotten' moechten! Deswegen wird hier numpy importiert.":
        " We use a NumPy array for the data we want to plot! That is why numpy is imported here.",
    ' Beispieldaten:': ' Example data:',
    'Reminder: liefert uns gleichmaeßig verteilte Zahlen über ein bestimmtes Intervall. 11 Werte in (0,5)':
        'Reminder: returns evenly spaced numbers over a specified interval. 11 values in (0,5)',
    'Reminder: quadriert jeden Wert': 'Reminder: squares each value',
    "'tuple unpacking' ermoeglicht es, einem Tupel von Variablennamen (hier: fig, axes), ":
        "'tuple unpacking' allows assigning a tuple of variable names (here: fig, axes), ",
    " Werte von einem Tupel, rechts neben der Zuweisung, zuzuweisen.":
        " values from a tuple on the right side of the assignment.",
    ' Jetzt koennen wir die ax-Methoden nutzen': ' Now we can use the ax methods',
    ' Durch dieses Array koenen wir iterieren und dadurch Plot, Titel, Label hinzuefuegen':
        ' We can iterate over this array to add plots, titles, and labels',
    " Gebe das fig Objekt zurück    ": ' Return the fig object    ',
    ' Hier ein paar Moeglichkeiten': ' Here are a few options',
    ' hier verschiedene Linientypen': ' here different line types',

    # lec05/03_seaborn_matrix_plots.ipynb code comments
    ' Wenn man die Daten zusätzlich noch normalisiert, bekommt man die Informationen ein bisschen deutlicher dargestellt.':
        ' If you also normalize the data, the information is displayed a bit more clearly.',
}


def translate_markdown(source_lines):
    """Translate a markdown cell (list of strings) to English."""
    text = ''.join(source_lines)
    if text in MARKDOWN_TRANSLATIONS:
        translated = MARKDOWN_TRANSLATIONS[text]
        # Preserve original line structure (newlines)
        if source_lines and source_lines[-1].endswith('\n'):
            lines = translated.split('\n')
            result = [l + '\n' for l in lines[:-1]] + [lines[-1]]
        else:
            lines = translated.split('\n')
            result = [l + '\n' for l in lines[:-1]] + [lines[-1]]
        return result, True
    return source_lines, False


def translate_code_comments(source_lines):
    """Translate comment lines in a code cell. Returns (new_lines, changed_bool)."""
    changed = False
    new_lines = []
    for line in source_lines:
        # Match lines that are purely a comment (optional whitespace + #)
        stripped = line.rstrip('\n')
        comment_match = re.match(r'^(\s*)(#)(.*?)(\n?)$', line)
        if comment_match:
            indent = comment_match.group(1)
            hash_char = comment_match.group(2)
            comment_body = comment_match.group(3)
            newline = comment_match.group(4)
            if comment_body in CODE_COMMENT_TRANSLATIONS:
                new_body = CODE_COMMENT_TRANSLATIONS[comment_body]
                new_lines.append(f"{indent}{hash_char}{new_body}{newline}")
                changed = True
                continue
        new_lines.append(line)
    return new_lines, changed


def process_notebook(nb_path):
    full_path = os.path.join(BASE, nb_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells_changed = 0
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            new_source, changed = translate_markdown(cell['source'])
            if changed:
                cell['source'] = new_source
                cells_changed += 1
        elif cell['cell_type'] == 'code':
            new_source, changed = translate_code_comments(cell['source'])
            if changed:
                cell['source'] = new_source
                cells_changed += 1

    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return cells_changed


def main():
    total_notebooks_modified = 0
    total_cells_changed = 0

    for nb_path in NOTEBOOKS:
        cells = process_notebook(nb_path)
        if cells > 0:
            total_notebooks_modified += 1
            print(f"  {nb_path}: {cells} cells changed")
        else:
            print(f"  {nb_path}: no changes")
        total_cells_changed += cells

    print(f"\nSummary: {total_notebooks_modified} notebooks modified, {total_cells_changed} cells changed")

    # Verification: check for remaining German umlauts in markdown cells
    print("\nVerification — checking for remaining German umlauts in markdown cells:")
    remaining = []
    for nb_path in NOTEBOOKS:
        full_path = os.path.join(BASE, nb_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'markdown':
                src = ''.join(cell['source'])
                found = [c for c in src if c in 'äöüÄÖÜß']
                if found:
                    remaining.append((nb_path, i, found, src[:120]))

    if remaining:
        print(f"  WARNING: {len(remaining)} markdown cell(s) still contain German umlauts:")
        for nb_path, cell_idx, chars, snippet in remaining:
            print(f"    {nb_path} cell {cell_idx}: chars={chars}, snippet={repr(snippet)}")
    else:
        print("  OK: No German umlauts remain in markdown cells.")

    # Also check for remaining umlauts in code comments
    print("\nVerification — checking for remaining German umlauts in code comment lines:")
    remaining_code = []
    for nb_path in NOTEBOOKS:
        full_path = os.path.join(BASE, nb_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                for line in cell['source']:
                    if re.match(r'^\s*#', line):
                        if any(c in line for c in 'äöüÄÖÜß'):
                            remaining_code.append((nb_path, i, repr(line.rstrip())))
    if remaining_code:
        print(f"  WARNING: {len(remaining_code)} code comment line(s) still contain German umlauts:")
        for nb_path, cell_idx, line in remaining_code:
            print(f"    {nb_path} cell {cell_idx}: {line}")
    else:
        print("  OK: No German umlauts remain in code comment lines.")


if __name__ == '__main__':
    main()
