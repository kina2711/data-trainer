# -*- coding: utf-8 -*-
"""DS3 · AppEvents — log hanh vi nguoi dung, du lieu ban cau truc.
Dung cho buoi 42-43 (funnel/sankey), 51-57 (CDC/Kafka/Airflow), 62-67 (Spark/BigQuery).
Mac dinh sinh 2 trieu event (~250MB). Dung --rows de sinh toi 50 trieu cho buoi Spark/BigQuery.
  python3 generate_ds3.py --rows 50000000 --out /duong/dan/khac
"""
import argparse, csv, json, os, random, datetime as dt
ap=argparse.ArgumentParser()
ap.add_argument("--rows",type=int,default=2_000_000)
ap.add_argument("--out",default=None)
ap.add_argument("--seed",type=int,default=2718)
a=ap.parse_args()
random.seed(a.seed)
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT=a.out or os.path.join(ROOT, "_data","ds3-appevents","sample")
os.makedirs(OUT,exist_ok=True)

# Phieu: mo app -> xem SP -> chi tiet -> them gio -> ma giam -> thanh toan -> nhan hang -> danh gia
FUNNEL=["app_open","view_list","view_detail","add_to_cart","apply_coupon","checkout","payment_ok","review"]
# ti le di tiep tung buoc — co y de buoc thanh toan rot manh tren android
KEEP   =[1.0, .82, .61, .34, .19, .27, .88, .21]
PLAT=[("android",.52),("ios",.33),("web",.15)]
VER=["4.1.9","4.2.0","4.2.1","4.3.0"]
SRC=["organic","facebook","google","tiktok","email","direct"]
def pick(ws):
    r=random.random();c=0
    for v,w in ws:
        c+=w
        if r<=c: return v
    return ws[-1][0]

path=os.path.join(OUT,"events.csv")
d0=dt.datetime(2024,10,1); span=92*24*3600
n=0; sess=0
with open(path,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["event_id","session_id","user_id","event_name","step","ts",
                "platform","app_version","utm_source","props_json"])
    while n < a.rows:
        sess+=1
        sid=f"S{sess:09d}"; uid=f"U{random.randint(1,900000):07d}"
        plat=pick(PLAT); ver=random.choice(VER); src=random.choice(SRC)
        t0=d0+dt.timedelta(seconds=random.randint(0,span))
        for i,ev in enumerate(FUNNEL):
            keep=KEEP[i]
            # LOI CAI SAN: app 4.2.1 tren android rot manh o buoc checkout
            if ev=="checkout" and plat=="android" and ver=="4.2.1" and t0>=dt.datetime(2024,10,3):
                keep*=0.34
            if i>0 and random.random()>keep: break
            t0+=dt.timedelta(seconds=random.randint(2,240))
            props={"screen":ev}
            if ev=="add_to_cart": props["sku"]=f"P{random.randint(1,2000):05d}"
            if ev=="payment_ok":  props["amount"]=random.randint(49,4900)*1000
            if ev=="apply_coupon":props["code"]=random.choice(["SALE10","FREESHIP","NEW50",""])
            w.writerow([f"E{n:010d}",sid,uid,ev,i+1,t0.strftime("%Y-%m-%d %H:%M:%S"),
                        plat,ver,src,json.dumps(props,ensure_ascii=False)])
            n+=1
            if n>=a.rows: break
print(f"  events.csv  {n:,} event · {sess:,} phiên · {os.path.getsize(path)/1048576:.0f} MB")
print(f"  Lỗi cài sẵn: app 4.2.1 trên Android rớt mạnh ở bước checkout từ 03/10 —")
print(f"  đây chính là tình huống case study của Buổi 1 và bài phân tích phễu Buổi 42.")
