library(nnet)

wikitest = read.csv("/Users/michael/Desktop/counttest.csv")
wikitrain = read.csv("/Users/michael/Desktop/counttrain.csv")

model = multinom(language~., wikitrain)

predictions = predict(model, newdata=wikitest)

table(wikitest$language,predictions))


