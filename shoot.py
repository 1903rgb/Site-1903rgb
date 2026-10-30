from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(); errs=[]
    for name,w,h,dpr in [('desktop',1440,900,1),('mobile',390,844,2)]:
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=dpr)
        pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        pg.goto('file:///home/claude/site-1903rgb/index.html',wait_until='networkidle'); pg.wait_for_timeout(600)
        ov=pg.evaluate('document.documentElement.scrollWidth>innerWidth')
        pg.screenshot(path=f'/home/claude/site-1903rgb/_shot-{name}-hero.png')
        pg.screenshot(path=f'/home/claude/site-1903rgb/_shot-{name}-full.png',full_page=True)
        print(name,'overflow',ov)
    print('errors',errs[:5]); b.close()
