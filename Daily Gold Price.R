library(neuralnet)
library(corrplot)
# reading input from python merge file
prices <- read.csv('A:\\Vasu\\Big Data Masters\\MRP\\Input.csv')


# converting factor to numeric values
# removing comma in Gold and Dow Jones, so it can be converted
prices$Gold.Price <- as.numeric(gsub(",","", as.character(prices$Gold.Price), fixed = TRUE))
prices$DJIA <- as.numeric(gsub(",","", as.character(prices$DJIA), fixed = TRUE))

# removes Date from the dataframe
prices$Date <- NULL

matrix <- cor(prices)
corrplot(matrix, method = "circle")
# calculating max and min for each column of prices
maxes <- apply(prices, 2, max, na.rm=TRUE )
mini <- apply(prices,2, min, na.rm=TRUE)
# creates a scaled dataframe with values between 0 and 1
scaled <- as.data.frame(scale(prices, center = mini, scale = maxes - mini))

NeualNet <- neuralnet(Gold.Price ~ Silver.Price + US.Dollar.Index + Copper.Price + 
                  DJIA + VIX, hidden = c(6,2), data = scaled)

plot(NeualNet)

test_prices <- read.csv('A:\\Vasu\\Big Data Masters\\MRP\\Test Prices Daily.csv')

test_prices$Date <- NULL

test_prices$DJIA <- as.numeric(gsub(",","", as.character(test_prices$DJIA), fixed = TRUE))

maxes_test <- apply(test_prices, 2, max, na.rm=TRUE)
mini_test <- apply(test_prices,2, min, na.rm=TRUE)

scaled_test <- as.data.frame(scale(test_prices, center = mini_test, scale = maxes_test - mini_test))

predict <- compute(NeualNet, scaled_test)
# converts the scaled price of Gold to the real price
Gold_price_pred <- predict$net.result*(max(prices$Gold.Price, na.rm = TRUE) - min(prices$Gold.Price, na.rm = TRUE)) + min(prices$Gold.Price, na.rm = TRUE)

#---------------------------------------- without vix -------------------------------------
# calculates the same thing but without vix
NN <- neuralnet(Gold.Price ~ Silver.Price + US.Dollar.Index + Copper.Price + 
                        DJIA, hidden = c(6,2), data = scaled)
plot(NN)
test_prices$CBOE.Volatility <- NULL

maxes_test <- apply(test_prices, 2, max, na.rm=TRUE)
mini_test <- apply(test_prices,2, min, na.rm=TRUE)

scaled_test <- as.data.frame(scale(test_prices, center = mini_test, scale = maxes_test - mini_test))

predict <- compute(NN, scaled_test)

Gold_price_pred <- predict$net.result*(max(prices$Gold.Price, na.rm = TRUE) - min(prices$Gold.Price, na.rm = TRUE)) + min(prices$Gold.Price, na.rm = TRUE)
