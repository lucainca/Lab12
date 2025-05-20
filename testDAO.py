from database.DAO import DAO

mydao= DAO()

print(mydao.getCountries())
print(mydao.getYears())
print(mydao.getNodes("Italy"))
