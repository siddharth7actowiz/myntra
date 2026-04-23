# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class MyntraPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="actowiz",
            database="myntra"
        )
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories_urls (
                id INT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(255),
                subcategory VARCHAR(255),
                link VARCHAR(500) UNIQUE,
                status VARCHAR(50)          
            )
         """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_links4 (
                id INT AUTO_INCREMENT PRIMARY KEY,
                                             
                product_name VARCHAR(255),
                product_id INT,
                category_hierarchy JSON,            
                product_link VARCHAR(500) ,
                status VARCHAR(50)          
            )
         """)



    def process_item(self, item, spider):
        
        adap=ItemAdapter(item)
        if spider.name=="cate":
            category=adap.get("category")
            subcategory = adap.get("subcategory")
            link = adap.get("link")
            status = adap.get("status")
            self.cursor.execute("""
                INSERT IGNORE INTO  categories_urls (category, subcategory, link,status)
                VALUES (%s, %s, %s, %s)
            """, (category, subcategory, link, status ))

            self.con.commit()
            return item
        elif spider.name=="prodlinks":
          
            product_name=adap.get("product_name")
            product_id=adap.get("product_id")
            category_hierarchy=adap.get("category_hierarchy")
            product_link=adap.get("product_link")
            status=adap.get("status")

            self.cursor.execute("""
                INSERT  INTO  product_links4 (product_name, product_id, category_hierarchy,product_link,status)
                VALUES (%s, %s, %s, %s,%s)
            """, (product_name, product_id,category_hierarchy, product_link, status ))
            self.con.commit()
            return item
     
        return item
    
    def fetch_from_db(self):
        self.cursor.execute("""
                            SELECT category,subcategory,link 
                            FROM  categories_urls 
                            WHERE status='pending'
                            ;""")
        
        return self.cursor.fetchall()
    
    def update_status(self,link):
        self.cursor.execute("""
                            UPDATE categories_urls 
                            SET status='done' 
                            WHERE link=%s
                            ;""",(link,))
        self.con.commit()
    