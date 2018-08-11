library(corrplot)

library(neuralnet)
prices <- read.csv('A:\\Vasu\\Big Data Masters\\MRP\\Input_with_Yuan.csv')

prices$Date <- NULL
prices$Gold.Price <- as.numeric(gsub(",","", as.character(prices$Gold.Price), fixed = TRUE))
prices$DJIA <- as.numeric(gsub(",","", as.character(prices$DJIA), fixed = TRUE))

matrix <- cor(prices)
corrplot(matrix, method = "circle")

maxes <- apply(prices, 2, max, na.rm=TRUE )
mini <- apply(prices,2, min, na.rm=TRUE)
# creates a scaled dataframe with values between 0 and 1
scaled <- as.data.frame(scale(prices, center = mini, scale = maxes - mini))

NeualNet <- neuralnet(Gold.Price ~ Silver.Price + US.Dollar.Index + Copper.Price + 
                        DJIA + VIX + USD.CNH, hidden = c(6,2), data = scaled)

plot(NeualNet)

test_prices <- read.csv('A:\\Vasu\\Big Data Masters\\MRP\\Output.csv')

test_prices$Date <- NULL

test_prices$DJIA <- as.numeric(gsub(",","", as.character(test_prices$DJIA), fixed = TRUE))

maxes_test <- apply(test_prices, 2, max, na.rm=TRUE)
mini_test <- apply(test_prices,2, min, na.rm=TRUE)

scaled_test <- as.data.frame(scale(test_prices, center = mini_test, scale = maxes_test - mini_test))

predict <- compute(NeualNet, scaled_test)
# converts the scaled price of Gold to the real price
Gold_price_pred <- predict$net.result*(max(prices$Gold.Price, na.rm = TRUE) - min(prices$Gold.Price, na.rm = TRUE)) + min(prices$Gold.Price, na.rm = TRUE)
