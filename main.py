from pngmeta import PngMeta
from pathlib import Path
from PIL import Image
import webview
import base64
import shutil
import uuid
import json
import sys
import os

class api:
    def get_uuid(self):
        return str(uuid.uuid4())  
    def get_json(self):
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            file_types=("json文件 (*.json)", "all (*.*)"),
            allow_multiple=False,
        )
        if result:
            f = open(result[0], "r", encoding="UTF-8")
            return f.read()
        return None

    def get_png(self):
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            file_types=("png角色卡 (*.png)", "all (*.*)"),
            allow_multiple=False,
        )
        if result:
            shutil.copy2(result[0],f'{os.path.dirname(sys.executable)}/temp')
            pngdata = base64.b64encode(open(result[0], "rb+").read()).decode("UTF-8")
            try:
                base = PngMeta(result[0])
                # 补世界书和正则
                json_s=json.loads(base64.b64decode(base["chara"]).decode("UTF-8"))
                if json_s.get('data').get('extensions').get('piupiu_regex')==None:
                    json_s['data']['extensions']=json.loads('{"piupiu_regex":{"enabled":true,"ignoreEmptyReplace":false,"scripts":[]},"regex_scripts":[]}')
                if json_s.get('data').get('character_book')==None:
                    json_s['data']['character_book']=json.loads('{"description":"","enabled":false,"entries":[],"global_constant":false,"name":"","scan_depth":101,"token_budget":1536,"token_budget_enabled":false}')
                return [
                    f"data:image/png;base64,{pngdata}",
                    json.dumps(json_s,ensure_ascii=False)
                ]
            except:
                return None
        return None

    def save_file(self,j:str):
        result = window.create_file_dialog(
            webview.SAVE_DIALOG,
            file_types=("png角色卡 (*.png)","all (*.*)"),
            allow_multiple=False,
            save_filename=f"{json.loads(j)['data']['name']}.png"
        )
        if result:
            file=Path(result)
            if(file.suffix != '.png'):
                file=file.with_suffix('.png')
            if(os.path.exists(f'{os.path.dirname(sys.executable)}/temp')):
                print(f'{os.path.dirname(sys.executable)}/temp')
                png=PngMeta(f'{os.path.dirname(sys.executable)}/temp')
            else:
                print(PngMeta(f"{os.path.dirname(os.path.abspath(__file__))}/default.png"))
                png=PngMeta(f"{os.path.dirname(os.path.abspath(__file__))}/default.png")
            png['chara']=base64.b64encode(j.encode('UTF-8')).decode('UTF-8')
            png.save(file.absolute())
            return 2
        return 3
    def set_png(self):
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            file_types=("图片 (*.png;*.jpg)", "all (*.*)"),
            allow_multiple=False,
        )
        if result:
            img = Image.open(result[0])
                
            if img.width >= 1024:
                比例 = 800 / img.width
                img.resize((1024, int(img.height * 比例)))
                img.save(f'{os.path.dirname(sys.executable)}/temp', format="png")
            else:
                img.save(f'{os.path.dirname(sys.executable)}/temp', format="png")
            base=base64.b64encode(open(f'{os.path.dirname(sys.executable)}/temp','rb+').read()).decode('UTF-8')
            return f"data:image/png;base64,{base}"
        return None
                                   
if __name__ =="__main__":
    if(os.path.exists(f'{os.path.dirname(sys.executable)}/temp')):
        os.remove(f'{os.path.dirname(sys.executable)}/temp')
        

html=f"{os.path.dirname(os.path.abspath(__file__))}/ui/dist/index.html"
window = webview.create_window(
    "Piupiu编辑器", html, js_api=api(), frameless=False, easy_drag=False,width=1000,height=800,min_size=(900,750)
    # "Piupiu编辑器", "http://localhost:5173/", js_api=api(), frameless=False, easy_drag=False,width=1000,height=800,min_size=(900,750)
)
webview.start(debug=False)
