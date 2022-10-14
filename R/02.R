english <- c(90, 80, 60, 70)
math <- c(50, 60, 100, 20)
df_midterm <- data.frame(english, math)
df_midterm
class <- c(1, 1, 2, 2)
df_midterm <- data.frame(english, math, class)
df_midterm

제품 <- c("사과", "딸기", "수박")
가격 <- c(1800, 1500, 3000)
판매량 <- c(24, 38, 13)

df <- data.frame(제품, 가격, 판매량)
df
mean(df$가격)
mean(df$판매량)