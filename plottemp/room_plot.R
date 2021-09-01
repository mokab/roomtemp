library(ggplot2)
library(scales)
library(RSQLite)
con = dbConnect(SQLite(), "~/Desktop/roomtemp.db", synchronous="off")
res <- dbGetQuery(con, "select * from temp")
plot(res$temp, type = 'l' )
res$datetime <- as.POSIXct(res$datetime)

p <- ggplot(res, aes(x = datetime, y = temp))
p <- p + geom_line()
p <- p + scale_x_datetime(date_breaks = "60 mins", 
                          labels = date_format(format = "%d/ %H:%M", 
                                               tz = "Asia/Tokyo"))
plot(p)

p <- ggplot(res, aes(x = datetime, y = temp))
p <- p + geom_line()
p <- p + scale_x_datetime(date_breaks = "1 day",
                          labels = date_format(format = "%d",
                                               tz = "Asia/Tokyo"))
plot(p)

plot(decompose(ts(res$temp, frequency = 24)))


p <- ggplot(res[res$datetime > "2021-08-23",], aes(x = datetime, y = temp))
p <- p + geom_line()
p <- p + scale_x_datetime(date_breaks = "1 day",
                          labels = date_format(format = "%d",
                                               tz = "Asia/Tokyo"))
p
