from database.DB_connect import DBConnect
from model.arco import Arco
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getCountries():

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select  distinct gr.Country 
                    from go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])



        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getYears():

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select distinct year (gds.`Date`) 
                    from go_daily_sales gds  """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year (gds.`Date`)"])

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getNodes(country):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from go_retailers gr 
                    where gr.Country = %s  """

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getPeso(u, v, year):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ select count(distinct(gds2.Product_number)) as n
                    from go_daily_sales gds , go_daily_sales gds2 
                    where gds.Product_number = gds2.Product_number
                    and gds.Retailer_code = %s and gds2.Retailer_code =%s
                    and year(gds2.`Date`) = year(gds.`Date`)
                    and year (gds2.`Date`)= %s """

        cursor.execute(query, (u.Retailer_code, v.Retailer_code, year))

        for row in cursor:
            result.append(row["n"])

        cursor.close()
        conn.close()

        return result

