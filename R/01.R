install.packages("ggplot2")
library(ggplot2)

x <- c("a", "a", "b", "c")
x

qplot(x)
df <- data.frame(sex = c("M", "F", NA, "M", "F"), score = c(5, 4, 3, 4, NA))
df
is.na(df)
