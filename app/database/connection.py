import pymysql


def create_mysql_connection():
    connection = pymysql.connect(
        host="localhost",
        user="debian-sys-maint",
        password="gKOfOvk2iVPfI6FT",
        # database="cineverse"
    )
    return connection
