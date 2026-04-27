# from itemadapter import ItemAdapter
# from mysql.connector import pooling
# import mysql.connector
#
#
#
# class MyntraPipeline:
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#         # Buffers for batch insert
#         self.category_buffer = []
#         self.product_buffer = []
#
#         self.batch_size = 500
#
#     # ---------------- CONNECTION ----------------
#     def create_connection(self):
#         self.pool = pooling.MySQLConnectionPool(
#             pool_name="mypool",
#             pool_size=10,  #
#             host="localhost",
#             user="root",
#             password="actowiz",
#             database="myntra"
#         )
#
#         self.con = self.pool.get_connection()
#         self.cursor = self.con.cursor()
#
#     # ---------------- TABLE CREATION ----------------
#     def create_table(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS categories_urls (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 category VARCHAR(255),
#                 subcategory VARCHAR(255),
#                 link VARCHAR(500) UNIQUE,
#                 status VARCHAR(50)
#             )
#         """)
#
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS product_links (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 product_name VARCHAR(255),
#                 product_id INT,
#                 category_hierarchy JSON,
#                 product_link VARCHAR(500) UNIQUE,
#                 status VARCHAR(50)
#             )
#         """)
#
#
#
#     # ---------------- PROCESS ITEM ----------------
#     def process_item(self, item, spider):
#         adap = ItemAdapter(item)
#
#         if spider.name == "cate":
#             data = (
#                 adap.get("category"),
#                 adap.get("subcategory"),
#                 adap.get("link"),
#                 adap.get("status")
#             )
#             self.category_buffer.append(data)
#
#             if len(self.category_buffer) >= self.batch_size:
#                 self.insert_categories()
#
#         elif spider.name == "prodlinks":
#             data = (
#                 adap.get("product_name"),
#                 adap.get("product_id"),
#                 adap.get("category_hierarchy"),  # ensure valid JSON
#                 adap.get("product_link"),
#                 adap.get("status")
#             )
#             self.product_buffer.append(data)
#
#             if len(self.product_buffer) >= self.batch_size:
#                 self.insert_products()
#
#         return item
#
#
#     # ---------------- BULK INSERT ----------------
#     def insert_categories(self):
#         query = """
#             INSERT IGNORE INTO categories_urls (category, subcategory, link, status)
#             VALUES (%s, %s, %s, %s)
#         """
#
#         con = self.pool.get_connection()
#         cursor = con.cursor()
#
#         cursor.executemany(query, self.category_buffer)
#         con.commit()
#
#         cursor.close()
#         con.close()  # returns to pool
#
#         self.category_buffer.clear()
#
#     def insert_products(self):
#         query = """
#             INSERT IGNORE INTO product_links
#             (product_name, product_id, category_hierarchy, product_link, status)
#             VALUES (%s, %s, %s, %s, %s)
#         """
#
#         con = self.pool.get_connection()
#         cursor = con.cursor()
#
#         cursor.executemany(query, self.product_buffer)
#         con.commit()
#
#         cursor.close()
#         con.close()  # returns to pool
#
#         self.product_buffer.clear()
#
#     # ---------------- CLOSE SPIDER ----------------
#     def close_spider(self, spider):
#         # Flush remaining data
#         if self.category_buffer:
#             self.insert_categories()
#
#         if self.product_buffer:
#             self.insert_products()
#
#         self.cursor.close()
#         self.con.close()
#
#     # ---------------- FETCH + UPDATE ----------------
#     def fetch_from_db(self):
#         self.cursor.execute("""
#             SELECT category, subcategory, link
#             FROM categories_urls
#             WHERE status = 'pending'
#            ;
#         """)
#         return self.cursor.fetchall()
#
#     def update_status(self, link):
#         self.cursor.execute("""
#             UPDATE categories_urls
#             SET status = 'done'
#             WHERE link = %s
#         """, (link,))
#         self.con.commit()
#

# from itemadapter import ItemAdapter
# from mysql.connector import pooling
# import mysql.connector
#
#
#
# class MyntraPipeline:
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#         # Buffers for batch insert
#         self.category_buffer = []
#         self.product_buffer = []
#
#         self.batch_size = 500
#
#     # ---------------- CONNECTION ----------------
#     def create_connection(self):
#         self.pool = pooling.MySQLConnectionPool(
#             pool_name="mypool",
#             pool_size=10,  #
#             host="localhost",
#             user="root",
#             password="actowiz",
#             database="myntra"
#         )
#
#         self.con = self.pool.get_connection()
#         self.cursor = self.con.cursor()
#
#     # ---------------- TABLE CREATION ----------------
#     def create_table(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS categories_urls (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 category VARCHAR(255),
#                 subcategory VARCHAR(255),
#                 link VARCHAR(500) UNIQUE,
#                 status VARCHAR(50)
#             )
#         """)
#
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS product_links (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 product_name VARCHAR(255),
#                 product_id INT,
#                 category_hierarchy JSON,
#                 product_link VARCHAR(500) UNIQUE,
#                 status VARCHAR(50)
#             )
#         """)
#
#
#
#     # ---------------- PROCESS ITEM ----------------
#     def process_item(self, item, spider):
#         adap = ItemAdapter(item)
#
#         if spider.name == "cate":
#             data = (
#                 adap.get("category"),
#                 adap.get("subcategory"),
#                 adap.get("link"),
#                 adap.get("status")
#             )
#             self.category_buffer.append(data)
#
#             if len(self.category_buffer) >= self.batch_size:
#                 self.insert_categories()
#
#         elif spider.name == "prodlinks":
#             data = (
#                 adap.get("product_name"),
#                 adap.get("product_id"),
#                 adap.get("category_hierarchy"),  # ensure valid JSON
#                 adap.get("product_link"),
#                 adap.get("status")
#             )
#             self.product_buffer.append(data)
#
#             if len(self.product_buffer) >= self.batch_size:
#                 self.insert_products()
#
#         return item
#
#
#     # ---------------- BULK INSERT ----------------
#     def insert_categories(self):
#         query = """
#             INSERT IGNORE INTO categories_urls (category, subcategory, link, status)
#             VALUES (%s, %s, %s, %s)
#         """
#
#         con = self.pool.get_connection()
#         cursor = con.cursor()
#
#         cursor.executemany(query, self.category_buffer)
#         con.commit()
#
#         cursor.close()
#         con.close()  # returns to pool
#
#         self.category_buffer.clear()
#
#     def insert_products(self):
#         query = """
#             INSERT IGNORE INTO product_links
#             (product_name, product_id, category_hierarchy, product_link, status)
#             VALUES (%s, %s, %s, %s, %s)
#         """
#
#         con = self.pool.get_connection()
#         cursor = con.cursor()
#
#         cursor.executemany(query, self.product_buffer)
#         con.commit()
#
#         cursor.close()
#         con.close()  # returns to pool
#
#         self.product_buffer.clear()
#
#     # ---------------- CLOSE SPIDER ----------------
#     def close_spider(self, spider):
#         # Flush remaining data
#         if self.category_buffer:
#             self.insert_categories()
#
#         if self.product_buffer:
#             self.insert_products()
#
#         self.cursor.close()
#         self.con.close()
#
#     # ---------------- FETCH + UPDATE ----------------
#     def fetch_from_db(self):
#         self.cursor.execute("""
#             SELECT category, subcategory, link
#             FROM categories_urls
#             WHERE status = 'pending'
#            ;
#         """)
#         return self.cursor.fetchall()
#
#     def update_status(self, link):
#         self.cursor.execute("""
#             UPDATE categories_urls
#             SET status = 'done'
#             WHERE link = %s
#         """, (link,))
#         self.con.commit()
#

from itemadapter import ItemAdapter
from mysql.connector import pooling
import mysql.connector


class MyntraPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

        # Buffers for batch insert
        self.category_buffer = []
        self.product_buffer = []

        self.batch_size = 1000

    # ---------------- CONNECTION ----------------
    def create_connection(self):
        self.pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=10,
            host="localhost",
            user="root",
            password="actowiz",
            database="myntra"
        )

    def _get_cursor(self):
        """Always get a fresh connection from the pool — never use a shared cursor."""
        con = self.pool.get_connection()
        return con, con.cursor()

    # ---------------- TABLE CREATION ----------------
    def create_table(self):
        con, cursor = self._get_cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories_urls (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    category VARCHAR(255),
                    subcategory VARCHAR(255),
                    link VARCHAR(500) UNIQUE,
                    status VARCHAR(50)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_links (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    product_name VARCHAR(255),
                    product_id INT,
                    category_hierarchy JSON,
                    product_link VARCHAR(500) UNIQUE,
                    status VARCHAR(50)
                )
            """)
            con.commit()
        finally:
            cursor.close()
            con.close()

    # ---------------- PROCESS ITEM ----------------
    def process_item(self, item, spider):
        adap = ItemAdapter(item)

        if spider.name == "cate":
            data = (
                adap.get("category"),
                adap.get("subcategory"),
                adap.get("link"),
                adap.get("status")
            )
            self.category_buffer.append(data)

            if len(self.category_buffer) >= self.batch_size:
                self.insert_categories()

        elif spider.name == "prodlinks":
            data = (
                adap.get("product_name"),
                adap.get("product_id"),
                adap.get("category_hierarchy"),
                adap.get("product_link"),
                adap.get("status")
            )
            self.product_buffer.append(data)

            if len(self.product_buffer) >= self.batch_size:
                self.insert_products()

        return item

    # ---------------- BULK INSERT ----------------
    def insert_categories(self):
        if not self.category_buffer:
            return

        query = """
            INSERT IGNORE INTO categories_urls (category, subcategory, link, status)
            VALUES (%s, %s, %s, %s)
        """
        con, cursor = self._get_cursor()
        try:
            cursor.executemany(query, self.category_buffer)
            con.commit()
            self.category_buffer.clear()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()

    def insert_products(self):
        if not self.product_buffer:
            return

        query = """
            INSERT IGNORE INTO product_links
            (product_name, product_id, category_hierarchy, product_link, status)
            VALUES (%s, %s, %s, %s, %s)
        """
        con, cursor = self._get_cursor()
        try:
            cursor.executemany(query, self.product_buffer)
            con.commit()
            self.product_buffer.clear()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()

    # ---------------- CLOSE SPIDER ----------------
    def close_spider(self, spider):
        # Flush any remaining buffered data before closing
        if self.category_buffer:
            self.insert_categories()

        if self.product_buffer:
            self.insert_products()

    # ---------------- FETCH + UPDATE ----------------
    def fetch_from_db(self):
        """Each call gets its own connection — safe for concurrent use."""
        con, cursor = self._get_cursor()
        try:
            cursor.execute("""
                SELECT category, subcategory, link
                FROM categories_urls
                WHERE status = 'pending'
                limit 1
                offset 1;
            """)
            return cursor.fetchall()
        finally:
            cursor.close()
            con.close()

    def update_status(self, link):
        """Each call gets its own connection — safe for concurrent use."""
        con, cursor = self._get_cursor()
        try:
            cursor.execute("""
                UPDATE categories_urls
                SET status = 'done'
                WHERE link = %s
            """, (link,))
            con.commit()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()