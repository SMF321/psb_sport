def prosmotr_raspisaniya5(id):
    from sqlalchemy import create_engine, Table, MetaData, select

    engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
    conn = engine.connect()
    meta = MetaData(engine)
    raspisanie = Table('PROFILS', meta, autoload=True)
    s = select([raspisanie]).where(raspisanie.c.ID_TG == id)
    print(s)
    result1 = conn.execute(s).fetchone()
    print('#####################################################')
    print(result1)
    return result1