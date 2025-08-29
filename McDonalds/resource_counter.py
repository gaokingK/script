from collections import defaultdict
import os, sys
sys.path.insert(0, os.getcwd())
# 读取文件并统计资源
resource_count = defaultdict(int)
file_path = os.path.join(os.path.dirname(__file__), 'temp.md')
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            # 按制表符分割，如果没有制表符则按最后一个空格分割
            if '\t' in line:
                parts = line.rsplit('\t')
            else:
                parts = line.split(' ')  
            parts = [part for part in parts if part]        
            if len(parts) == 2:
                resource_name = parts[0].strip()
                try:
                    count = int(parts[1].strip())
                    resource_count[resource_name] += count
                except ValueError:
                    continue
            else:
                resource_name = " ".join(parts[:-1])
                count = int(parts[-1].strip())
                resource_count[resource_name] += count

# 输出结果到文件
file_path = os.path.join(os.path.dirname(__file__), 'resource_summary.txt')
print(f"结果文件路径: {file_path}")
with open(file_path, 'w', encoding='utf-8') as output:
    output.write("资源统计结果：\n")
    output.write("-" * 40 + "\n")
    for resource, total in sorted(resource_count.items()):
        output.write(f"{resource}\t{total}\n")
    output.write(f"\n总共 {len(resource_count)} 种资源\n")

print("统计完成，结果已保存到 resource_summary.txt")
