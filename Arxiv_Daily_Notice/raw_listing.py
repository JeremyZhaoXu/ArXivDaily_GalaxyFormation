# encoding: utf-8
"""Save the full, unfiltered arXiv 'new submissions' for selected categories.

Only the "New submissions" section is kept (cross-lists and replacements are
dropped). Output: raw/YYYY-MM-DD-<CAT>.json, one file per category.
"""
from __future__ import print_function, unicode_literals

import datetime
import io
import json
import os
import time
import urllib.request

from bs4 import BeautifulSoup as bs

RAW_CATEGORIES = ["astro-ph.GA", "astro-ph.CO"]
RAW_DIR = "./raw"
UA = "ArXivDaily_GalaxyFormation (github.com/JeremyZhaoXu)"


def _text(tag, prefix=""):
    if tag is None:
        return ""
    t = " ".join(tag.get_text(" ").split()).replace(" ,", ",")
    if prefix and t.startswith(prefix):
        t = t[len(prefix):].strip()
    return t


def parse_new_submissions(html):
    soup = bs(html, "html.parser")
    content = soup.body.find("div", {"id": "content"})

    header = ""
    for h3 in content.find_all("h3"):
        if "showing new listings for" in h3.get_text().lower():
            header = " ".join(h3.get_text().split())
            break

    # Walk h3/dt/dd in document order; keep only entries under "New submissions".
    section, papers, pending_id = None, [], None
    for el in content.find_all(["h3", "dt", "dd"]):
        if el.name == "h3":
            h = el.get_text().strip().lower()
            if h.startswith("new submissions"):
                section = "new"
            elif h.startswith("cross") or h.startswith("replacement"):
                section = "other"
            continue
        if section != "new":
            continue
        if el.name == "dt":
            dt_txt = el.get_text(" ").lower()
            if "cross-list" in dt_txt or "replaced" in dt_txt:
                pending_id = None
                continue
            a = el.find("a", {"title": "Abstract"})
            aid = (a.get_text() if a else el.get_text()).split("arXiv:")[-1].strip()[:10]
            pending_id = aid
        elif el.name == "dd" and pending_id:
            papers.append({
                "id": pending_id,
                "title": _text(el.find("div", {"class": "list-title"}), "Title:"),
                "authors": _text(el.find("div", {"class": "list-authors"}), "Authors:"),
                "subjects": _text(el.find("div", {"class": "list-subjects"}), "Subjects:"),
                "abstract": _text(el.find("p", {"class": "mathjax"})),
            })
            pending_id = None
    return header, papers


def save_raw_listings(date_str=None):
    date_str = date_str or datetime.datetime.utcnow().strftime("%Y-%m-%d")
    if not os.path.isdir(RAW_DIR):
        os.makedirs(RAW_DIR)
    for i, cat in enumerate(RAW_CATEGORIES):
        if i:
            time.sleep(5)  # be polite to arXiv
        url = "https://arxiv.org/list/%s/new" % cat
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            html = urllib.request.urlopen(req, timeout=60).read()
            header, papers = parse_new_submissions(html)
        except Exception as e:  # never break the main daily report
            print("raw listing failed for %s: %r" % (cat, e))
            continue
        out = {
            "category": cat,
            "fetched_utc": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "listing_header": header,
            "n_new": len(papers),
            "papers": papers,
        }
        fn = os.path.join(RAW_DIR, "%s-%s.json" % (date_str, cat.split(".")[-1]))
        with io.open(fn, "w", encoding="utf-8") as f:
            f.write(json.dumps(out, ensure_ascii=False, indent=1))
        print("saved %s (%d new) | %s" % (fn, len(papers), header))
