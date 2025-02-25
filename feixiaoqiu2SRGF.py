import json
import os

def decode_unicode(name):
    return name.encode('utf-16').decode('utf-16') #非小酋的记录导出是用UTF-16编码的，请注意

def main():
    # 输入JSON文件路径
    json_path = input("请输入JSON文件的路径（建议使用英文路径，留空输入JSON文件的名称。区分大小写，建议把json复制文件名后粘贴在此处，不使用中文字符）：").strip()
    if not json_path:
        json_path = os.path.join(os.getcwd(), '下载.json')

    # 读取原始JSON文件
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"文件未找到：{json_path}")
        return
    except json.JSONDecodeError:
        print(f"文件格式错误：{json_path}")
        return

    # 这里可以去查看UIGF关于SRGF的文档，了解如何填写下面的信息
    uid = input("请输入您的UID（必选，这样可以与其他链接导出工具接续使用）：").strip()
    lang = input("请输入地区（可选，默认为'zh-cn'）：").strip() or "zh-cn"
    region_time_zone = input("请输入时区（默认为8）：").strip() or "8"
    export_app = input("请输入导出APP（可不输入）：").strip()
    export_app_version = input("请输入导出APP版本（可不输入）：").strip()
    output_dir = input("请输入输出文件的路径（建议使用英文路径，留空则输出到当前文件夹）：").strip()
    output_filename = input("请输入输出文件的名称（建议使用英文，必选）：").strip()
    if not output_filename:
        print("输出文件名称不能为空")
        return
    if not output_dir:
        output_dir = os.getcwd()
    output_path = os.path.join(output_dir, output_filename)
    

    # 解析字段并结构化数据
    records = data.get('record', '').split('#')
    structured_data = []

    for record in records:
        if record.strip():
            fields = record.split('_')
            structured_data.append({
                "gacha_id": fields[7],
                "gacha_type": fields[0],
                "item_id": fields[4],
                "count": "1",
                "time": fields[5],
                "name": decode_unicode(fields[2]),
                "item_type": fields[1],
                "rank_type": fields[3],
                "id": fields[6]
            })

    # 创建输出数据表头
    output_data = {
        "info": {
            "uid": uid,
            "lang": lang, #可任意指定，具体请参考SRGF文档
            "region_time_zone": int(region_time_zone),
            "export_timestamp": 1684124992, #可任意指定，具体请参考SRGF文档
            "export_app": export_app,
            "export_app_version": export_app_version,
            "srgf_version": "v1.0" #可在代码中任意指定，具体请参考SRGF文档
        },
        "list": structured_data
    }

    # 将结构化数据写入新的JSON文件
    with open(output_path, 'w', encoding='utf-16') as outfile:
        json.dump(output_data, outfile, ensure_ascii=False, indent=4)
    print(f"结构化数据已写入：{output_path}")

if __name__ == "__main__":
    main()
