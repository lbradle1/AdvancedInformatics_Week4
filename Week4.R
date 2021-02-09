
data(mtcars)

library(dbplyr)
con <- DBI::dbConnect(RSQLite::SQLite(), "mtcars.sqlite3")
DBI::dbWriteTable(con, "mtcars", mtcars)
list.files(pattern="*.sqlite3")
