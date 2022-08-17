import tabula

a = tabula.read_pdf("Demo.pdf", pages="all", encoding="cp1252")

tabula.convert_into("Demo.pdf", "Demo.csv", pages="all", output_format="csv")

print(a)