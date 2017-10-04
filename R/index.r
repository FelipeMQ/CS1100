---
title: "HMonitor KPI - Dashboard"
output:
  flexdashboard::flex_dashboard:
    orientation: columns
---

```{r include = FALSE}
library(dplyr)
library(readr)
library(dygraphs)
library(quantmod)
library(viridis)
library(ggplot2)
library(marmap)

getSymbols(c("MSFT", "HPQ", "INTC"), from = "2017-01-01", auto.assign=TRUE)

# Define the list of available metros
lookup <- structure(c(1, 2, 3, 4), .Names = c("Por recarga", "Por consumo", "Por planta", "Por paquete"))

```

# Intro {.sidebar}

```{r}

# Define inputs
selectInput('kpi_name', label = 'Selecciona el tipo de KPI', choices = lookup, selected = 1)

sliderInput('span', label = 'Cantidad de muestras', min = 100, max = 1000, value = 500, step = 100)

# Set up data download


output$downloadCSV <- downloadHandler(
  filename = 'data.csv',
  content = function(file) {
    write_csv(as.data.frame(MSFT[,2:4]), file)
  }
)

downloadLink('downloadCSV', label = 'Descargar CSV del KPI actual (2017)')
```

Los [dataset](https://www.gmc-soft.com) visualizados son para el producto `prepago` durante los ultimos 10min.

# Producto Prepago

## Column 1

### Recarga media por cliente
```{r echo = FALSE}
dygraph(MSFT[,2:4], group = "stocks") %>%
  dySeries(c("MSFT.Low", "MSFT.Close", "MSFT.High"), label = "MSFT") %>%
  dyRangeSelector(height = 20)
```

### Tiempo medio entre recargas
```{r echo = FALSE}
dygraph(HPQ[,2:4], group = "stocks") %>%
  dySeries(c("HPQ.Low", "HPQ.Close", "HPQ.High"), label = "HPQ") %>%
  dyRangeSelector(height = 20)
```

# Producto Postpago

## Column 1

### Viridis colors

```{r fig.cap="Maunga Whao, Auckland, NZ"}
image(volcano, col = viridis(200))
```

### Magma colors

```{r fig.cap="Maunga Whao, Auckland, NZ"}
image(volcano, col = viridis(200, option = "A"))
```

## Column 2

### Inferno colors

```{r fig.cap="Maunga Whao, Auckland, NZ"}
image(volcano, col = viridis(200, option = "B"))
```

### Plasma colors

```{r fig.cap="Maunga Whao, Auckland, NZ"}
image(volcano, col = viridis(200, option = "C"))
```

# Producto Control

## Column 1 {data-width=300}

### Bash support

```{bash}
ls *.Rmd
```

***

This chunk executes bash code.

### Python support

```{python}
x = 'hello, python world!'
print(x.split(' '))
```

***

This chunk executes python code.

## Column 2 {data-width=700}

### Tables with Kable

```{r echo = FALSE, results = 'asis'}
library(knitr)
kable(mtcars[1:5, ], caption = "A knitr kable.")
```

***

It is very easy to make tables with knitr's `kable` function.
