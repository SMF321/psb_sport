def add_info(conn, raspisanie, date_text, name, url, latitude, longitude, points):


    result = raspisanie.select()


#######################НАДО ЗАХУЯРИТЬ ФУНКЦИЮ

    test1 = raspisanie.insert().values(Date=date_text,Name=name,URL=url,Latitude=latitude,Longtitude=longitude,PRICE=points)
    conn.execute(test1)

    print(conn.execute(result).fetchall())
