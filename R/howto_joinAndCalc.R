### setup
setwd("C:\\Users\\stevenconnorg\\Documents\\knight-federal-solutions\\CIP_DataReview")

source("R/init.R")


      
rmarkdown::render(input = paste0(getwd(),"/R/howto_joinAndCalc.Rmd"),
        output_format = "pdf_document",
        output_file = "How_to_Use_Join_and_Calculate_Tool.pdf",
        output_dir = paste0(getwd(),"/tutorials"))
      

