def change(id, t_f=0):
    from sqlalchemy import create_engine, Table, MetaData

    engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
    meta = MetaData(engine)

    raspisanie = Table('PSB_SPORT', meta, autoload=True)

    conn = engine.connect()
    result = raspisanie.select()
    update_info = raspisanie.update().where(raspisanie.c.ID_TG == id).values(T_F=t_f)

    conn.execute(update_info)

    print(conn.execute(result).fetchall())

def change1(id,contest, t_f=0):
    from sqlalchemy import create_engine, Table, MetaData

    engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
    meta = MetaData(engine)

    raspisanie = Table('PSB_SPORT', meta, autoload=True)

    conn = engine.connect()
    result = raspisanie.select()
    update_info = raspisanie.update().where(raspisanie.c.ID_TG == id).values(T_F=t_f)

    conn.execute(update_info)

    print(conn.execute(result).fetchall())
