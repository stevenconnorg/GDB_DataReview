library(packrat)
#packrat::init(options = list(ignored.packages = c()))
# packrat::snapshot()
# packify()
# packrat::bundle(project = NULL, file = NULL, include.src = TRUE,
#                  include.lib = FALSE, include.bundles = TRUE,
#                  include.vcs.history = TRUE, overwrite = TRUE, omit.cran.src = TRUE)
# packrat::disable()

Install_And_Load <- function(Required_Packages)
{
  Remaining_Packages <- Required_Packages[!(Required_Packages %in% installed.packages()[,"Package"])];
  
  if(length(Remaining_Packages)) 
  {
    install.packages(Remaining_Packages);
  }
  for(package_name in Required_Packages)
  {
    library(package_name,character.only=TRUE,quietly=TRUE);
  }
}

requiredPackages = c('packrat'
                     ,'rprojroot'
                     ,'ggplot2'
                     ,'dplyr'
                     ,'leaflet'
                     ,'DT'
                     ,'stringr'
                     ,'knitr'
                     ,'markdown'
                     ,'rmarkdown'
                     ,'sf'
                     ,'ggmap'
                     ,'Rcpp'
                     ,'bookdown'
                     ,'purrr'
                     ,'bibtex'
                     ,'anchors'
                     ,'digest'
                     ,'backports'
                     ,'devtools'
)

Install_And_Load(requiredPackages)

devtools::install_github('rstudio/rmarkdown')
install_version("rmarkdown", version = 1.9)
library(rmarkdown)

devtools::install_github('yihui/knitr',force=TRUE)
library(knitr)

devtools::install_github("haozhu233/kableExtra")
library(kableExtra)

install_version("yaml", version = "2.1.14", repos = "http://cran.us.r-project.org")
library(yaml)

devtools::install_github('yihui/tinytex')
library(tinytex)
tinytex::install_tinytex()



