CREATE TABLE han_ji (
  id SERIAL,
  han_ji VARCHAR(6),
  chu_im VARCHAR(15),
  freq REAL,
  siann VARCHAR(3),
  un VARCHAR(5),
  tiau INTEGER,
  old_chu_im VARCHAR(15),
  sni_siann VARCHAR(3),
  sni_un VARCHAR(5),
  PRIMARY KEY (id)
)