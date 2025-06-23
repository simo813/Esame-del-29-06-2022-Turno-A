from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getNodes(duration):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select a.AlbumId , a.Title , sum(t.Milliseconds)/(1000*60) as duration
                        from itunes.album a , itunes.track t 
                        where a.AlbumId = t.AlbumId 
                        group by a.AlbumId , a.Title
                        having sum(t.Milliseconds)/(1000*60) > %s
                        """
            cursor.execute(query, (duration, ))

            for row in cursor:
                result.append(Album(row["AlbumId"], row["Title"], row["duration"]))
            cursor.close()
            cnx.close()
        return result

