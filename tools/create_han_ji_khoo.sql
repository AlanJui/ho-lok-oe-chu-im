DROP TABLE han_ji;

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
);

COPY han_ji(han_ji, chu_im, freq, siann, un, tiau, old_chu_im, sni_siann, sni_un)
FROM '/Users/alanjui/workspace/rime/ho-lok-oe-chu-im/tools/nga_siok_thong_sip_ngoo_im.csv'
DELIMITER ','
CSV HEADER;
