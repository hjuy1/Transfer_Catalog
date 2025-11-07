# PDF书签转移工具

这个工具可以将一个PDF文件中的书签（目录）转移到另一个PDF文件中，同时保持书签结构不变。

## 功能特点

- 保留原始书签的完整结构，包括嵌套的子书签
- 支持将书签从一个PDF文件复制到另一个PDF文件
- 保持书签与页面的正确对应关系
- 使用Python编写，跨平台支持

## 使用场景

- 当你有一个带书签的PDF文件，但需要替换为另一个版本（如高清版）的PDF时
- 当你需要将一个PDF的书签应用到另一个没有书签的PDF文件时
- 处理扫描版PDF时，可以将目录书签添加到优化后的版本中

## 安装依赖

```bash
pip install PyPDF2
```

## 使用方法

1. 准备两个PDF文件：
   - 源PDF文件：包含需要转移的书签
   - 目标PDF文件：需要添加书签的PDF文件

2. 修改脚本中的文件路径：
   ```python
   source = Path(r"源PDF文件路径")
   target = Path(r"目标PDF文件路径")
   output = Path(r"输出PDF文件路径")
   ```

3. 运行脚本：
   ```bash
   python 转移书签.py
   ```

## 注意事项

- 源PDF和目标PDF应该具有相同的页数和页面顺序，以确保书签能正确对应到页面
- 输出文件将包含目标PDF的内容和源PDF的书签结构
- 工具会保留嵌套的书签结构（多级目录）

## API说明

### transfer_bookmarks(source_pdf, target_pdf, output)

将源PDF的书签转移到目标PDF

**参数:**
- `source_pdf`: Path对象，包含书签的源PDF路径
- `target_pdf`: Path对象，需要添加书签的目标PDF路径
- `output`: Path对象，输出文件路径

## 依赖库

- [PyPDF2](https://pypi.org/project/PyPDF2/) - 用于处理PDF文件和书签操作