import sqlite3
conn = sqlite3.connect('quotes.db')
cursor = conn.cursor()

cursor.execute("""
create table srtfiles(
id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
source_name text not null,
source_type text,
source_image text,
srt_file_contents text,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_atDATETIME DEFAULT CURRENT_TIMESTAMP 
);
""")




conn.commit()
conn.close()
print("database created")
