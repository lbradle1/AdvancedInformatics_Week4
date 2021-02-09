rule database:
    input: "Week4.R", "Week4.py"
    output: "mtcars.sqlite3"
    shell: "Rscript Week4.R"
