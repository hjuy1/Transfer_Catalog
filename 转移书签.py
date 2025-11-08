from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import IndirectObject, Destination
from pathlib import Path


def transfer_bookmarks(source_pdf: Path, target_pdf: Path, output: Path) -> None:
    """
    将源PDF的书签转移到目标PDF

    参数:
        source_pdf_path: 包含书签的源PDF路径
        target_pdf_path: 需要添加书签的目标PDF路径
        output_path: 输出文件路径
    """

    # 读取源PDF和目标PDF
    source_reader = PdfReader(source_pdf)
    target_reader = PdfReader(target_pdf)

    # 创建PdfWriter对象
    writer = PdfWriter()

    # 将目标PDF的所有页面添加到writer中
    for page in target_reader.pages:
        writer.add_page(page)

    # 获取源PDF的书签
    outline = source_reader.outline

    parent_list: list[IndirectObject | None] = [None, None]

    # 递归函数：复制书签项
    def copy_outline_items(
        outline_items: list, parent: IndirectObject | None = None
    ) -> None:
        global time
        for item in outline_items:
            if isinstance(item, list):
                parent_list.append(None)
                parent = parent_list[-2]
                # 如果是书签组（子书签），递归处理
                copy_outline_items(item, parent)
                parent_list.pop()
                parent = parent_list[-2]
            elif isinstance(item, Destination):
                # 创建书签
                title = item.title or "NoTitle"
                # 在目标PDF中找到对应的页面
                page_number = source_reader.get_destination_page_number(item)

                # 添加书签到目标PDF
                new_bookmark = writer.add_outline_item(
                    title=title, page_number=page_number, parent=parent
                )
                parent_list[-1] = new_bookmark

    # 复制所有书签
    copy_outline_items(outline)

    # 写入输出文件
    with open(output, "wb") as fout:
        writer.write(fout)


# 使用示例
if __name__ == "__main__":
    source = Path(r".\sourse.pdf")
    target = Path(r".\target.pdf")
    output = Path(r".\out.pdf")

    transfer_bookmarks(source, target, output)
