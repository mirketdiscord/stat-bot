import sqlite3 as s3
import locale
import os


class manager():

    def __init__(self, guildId):
        self.guildId = str(guildId)
        self.__connectDatabase()
        locale.setlocale(locale.LC_ALL, '')

    def __firstConnect(self, filepath: str, query: str):
        # __connectDatabase() için özel yazdım.
        self.connect = s3.connect(filepath)
        self.cursor = self.connect.cursor()
        self.cursor.execute(query)
        self.connect.commit()

    def __otherConnect(self, filepath:str):
        # __connectDatabase() için özel yazdım.
        self.connect = s3.connect(filepath)
        self.cursor = self.connect.cursor()
        self.connect.commit()        

    def __connectDatabase(self):
        # Ana komutlar
        filepath = os.getcwd() + "/db/guild/" + self.guildId + "mirket.db"

        if os.path.isfile(filepath) == False:

            f = open(filepath, "x")

            self.__firstConnect(
                filepath, "CREATE TABLE IF NOT EXISTS GUILDSTATUS (guild_status TEXT, member_count TEXT, member TEXT, m_id TEXT, m_desktop_status TEXT, m_mobile_status TEXT, m_raw_status TEXT, time TEXT)")
            self.__firstConnect(
                filepath, "CREATE TABLE IF NOT EXISTS MEMBER (member TEXT, m_id TEXT, discriminator TEXT, m_display_name TEXT, m_name TEXT, m_nick TEXT, m_avatar_url TEXT, m_created_at TEXT)")
            self.__firstConnect(
                filepath, "CREATE TABLE IF NOT EXISTS MESSAGE (channel TEXT, raw_mentions TEXT, raw_channel_mentions TEXT, raw_role_mentions TEXT, clean_content TEXT, created_at TEXT, jump_url TEXT, member TEXT, m_id TEXT, m_desktop_status TEXT, m_mobile_status TEXT, m_raw_status TEXT, time TEXT)")
            self.__firstConnect(
                filepath, "CREATE TABLE IF NOT EXISTS STATUS (status TEXT, status_status TEXT, member TEXT, m_id TEXT, m_desktop_status TEXT, m_mobile_status TEXT, m_raw_status TEXT, time TEXT)")
            self.__firstConnect(
                filepath, "CREATE TABLE IF NOT EXISTS VOICE (channel TEXT, channel_status TEXT, member TEXT, m_id TEXT, m_desktop_status TEXT, m_mobile_status TEXT, m_raw_status TEXT, time TEXT)")

        self.__otherConnect(filepath)

    def getGuildStatus(self):
        """Kullanıcıların sunucuya ne zaman girip çıktılarının bilgisini döndürür.

        Returns:
            List or -1: Veri olmadığında `-1`
        """
        self.cursor.execute(f"SELECT * FROM GUILDSTATUS")
        guild = self.cursor.fetchall()
        self.connect.commit()
        if guild==[]:
            return -1
        return guild

    def getMember(self):
        """Tüm kullanıcıların bilgilerini döndürür.

        Returns:
            List or -1: Veri olmadığında `-1`
        """
        self.cursor.execute(f"SELECT * FROM MEMBER")
        guild = self.cursor.fetchall()
        self.connect.commit()
        if guild==[]:
            return -1
        return guild
