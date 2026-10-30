"""Create human-review tables and contact sheets for dataset duplicates."""
from __future__ import annotations
import argparse, csv, sys, math
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
PROJECT_ROOT=Path(__file__).resolve().parents[1]

def font(size=18):
    try: return ImageFont.truetype('arial.ttf', size)
    except OSError: return ImageFont.load_default()

def load_rows(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def make_sheets(items, root, out, prefix, per_page=12):
    out.mkdir(parents=True, exist_ok=True); pages=[]
    for page_start in range(0,len(items),per_page):
        batch=items[page_start:page_start+per_page]; cols=3; cell_w,cell_h=420,330
        sheet=Image.new('RGB',(cols*cell_w, math.ceil(len(batch)/cols)*cell_h),'white'); d=ImageDraw.Draw(sheet)
        for j,entry in enumerate(batch):
            r,c=divmod(j,cols); x,y=c*cell_w,r*cell_h; path=root/entry['relative_path']
            try:
                with Image.open(path) as im:
                    im=im.convert('RGB'); im.thumbnail((cell_w-20,235)); px=x+(cell_w-im.width)//2; py=y+5; sheet.paste(im,(px,py))
                text=entry['caption']
            except Exception as exc: text=f"{entry['caption']}\nREAD ERROR: {type(exc).__name__}: {exc}"
            d.multiline_text((x+8,y+245),text,fill='black',font=font(15),spacing=3)
        p=out/f'{prefix}_{page_start//per_page+1:03d}.jpg'; sheet.save(p,quality=92); pages.append(p)
    return pages

def main():
    ap=argparse.ArgumentParser(description='Build duplicate review CSV and contact sheets.')
    ap.add_argument('--dataset-root',type=Path,default=PROJECT_ROOT/'Dataset'); ap.add_argument('--audit-csv',type=Path,default=PROJECT_ROOT/'outputs/metrics/dataset_audit/dataset_audit_files.csv'); ap.add_argument('--output-dir',type=Path,default=PROJECT_ROOT/'outputs/metrics/dataset_audit/review'); args=ap.parse_args()
    rows=load_rows(args.audit_csv); by_hash=defaultdict(list)
    for r in rows:
        if r['readable'].lower()=='true' and r['sha256']: by_hash[r['sha256']].append(r)
    groups=[g for g in by_hash.values() if len(g)>1]; groups.sort(key=lambda g:g[0]['relative_path'])
    review=[]; exact_items=[]
    for i,g in enumerate(groups,1):
        gid=f'EXACT-{i:03d}'; splits={r['split'] for r in g}; labels={r['label'] for r in g}; typ='exact_same_split_same_label'
        if len(splits)>1 and len(labels)>1: typ='exact_cross_split_different_label'
        elif len(splits)>1: typ='exact_cross_split_same_label'
        elif len(labels)>1: typ='exact_same_split_different_label'
        priority='HIGH' if len(splits)>1 or len(labels)>1 else 'MEDIUM'
        paths=[]
        for r in g: paths.append(r['relative_path']); exact_items.append({**r,'caption':f'{gid}\n{Path(r["relative_path"]).name}\n{r["split"]} | {r["label"]}'})
        for r in g: review.append({'group_id':gid,'file_path_1':r['relative_path'],'file_path_2':'','split_1':r['split'],'split_2':'','class_1':r['label'],'class_2':'','duplicate_type':typ,'sha256':r['sha256'],'hamming_distance':'','priority':priority,'review_status':'not_reviewed','decision':'','review_notes':''})
    near_path=Path(args.audit_csv).parent/'dataset_audit_near_duplicates.csv'; near=[]
    if near_path.exists():
        with near_path.open(encoding='utf-8-sig',newline='') as f: near=list(csv.DictReader(f))
    for i,p in enumerate(near,1):
        review.append({'group_id':f'NEAR-{i:03d}' ,'file_path_1':p['path_a'],'file_path_2':p['path_b'],'split_1':p.get('split_a',''),'split_2':p.get('split_b',''),'class_1':p.get('label_a',''),'class_2':p.get('label_b',''),'duplicate_type':'near_duplicate','sha256':'','hamming_distance':p.get('distance',''),'priority':'HIGH' if p.get('split_a')!=p.get('split_b') or p.get('label_a')!=p.get('label_b') else 'MEDIUM','review_status':'not_reviewed','decision':'','review_notes':''})
    args.output_dir.mkdir(parents=True,exist_ok=True)
    fields=['group_id','file_path_1','file_path_2','split_1','split_2','class_1','class_2','duplicate_type','sha256','hamming_distance','priority','review_status','decision','review_notes']
    with (args.output_dir/'duplicate_review.csv').open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(review)
    near_items=[]
    for i, pair in enumerate(near, 1):
        for side in ("a", "b"):
            path_key = "path_" + side
            split_key = "split_" + side
            label_key = "label_" + side
            caption = "NEAR-{0:03d} | distance={1}\n{2}\n{3} | {4}".format(i, pair.get("distance", ""), Path(pair[path_key]).name, pair.get(split_key, ""), pair.get(label_key, ""))
            near_items.append({"relative_path": pair[path_key], "caption": caption})
    exact_pages = make_sheets(exact_items, args.dataset_root, args.output_dir / "contact_sheets", "exact_duplicates")
    near_pages = make_sheets(near_items, args.dataset_root, args.output_dir / "contact_sheets", "near_duplicates")
    print(f"Exact groups: {len(groups)}; review rows: {len(review)}; exact sheets: {len(exact_pages)}; near pairs: {len(near)}; near sheets: {len(near_pages)}")
if __name__=='__main__': main()




