def add_info(conn, raspisanie, id, contest, t_f=0):
    result = raspisanie.select()

    #######################НАДО ЗАХУЯРИТЬ ФУНКЦИЮ

    test1 = raspisanie.insert().values(ID_TG=id, Contest=contest, T_F=t_f)
    conn.execute(test1)

    print(conn.execute(result).fetchall())
