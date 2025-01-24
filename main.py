import zipfile
from ebooklib import epub
import os
import tkinter as tk
from tkinter import filedialog

def create_epub_from_zip(zip_path, output_epub):
    # 打开ZIP文件并获取其成员列表
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 获取所有图片文件名，并排序
        images = sorted([name for name in zip_ref.namelist() if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))])
        
        # 创建一个新的EPUB书籍
        book = epub.EpubBook()
        
        # 设置元数据
        book.set_identifier('id123456')
        book.set_title(os.path.splitext(os.path.basename(zip_path))[0])
        book.set_language('en')
        
        # 假设作者是'Unknown'
        book.add_author('Unknown')

        # 获取ZIP文件中的文件夹结构
        folders = set()
        for image in images:
            folder = os.path.dirname(image)
            if folder:
                folders.add(folder)

        # 如果没有文件夹，直接创建一个章节
        if not folders:
            chapter_content = '<html><body>'
            for i, image_name in enumerate(images):
                # 从ZIP文件中读取图片
                with zip_ref.open(image_name) as image_file:
                    img_data = image_file.read()

                # 添加图片到EPUB
                img_item = epub.EpubImage(
                    uid=f'image{i}',
                    file_name=image_name,
                    media_type=f'image/{image_name.split(".")[-1].lower()}',  # 确定媒体类型
                    content=img_data
                )
                book.add_item(img_item)

                # 将图片添加到章节内容中
                chapter_content += f'<img src="{image_name}" alt="Image {i + 1}"/><br/>'

            chapter_content += '</body></html>'

            # 创建章节以显示所有图片
            chapter = epub.EpubHtml(title=os.path.splitext(os.path.basename(zip_path))[0], file_name='chap_1.xhtml', lang='en')
            chapter.content = chapter_content
            book.add_item(chapter)

            # 添加章节到书籍对象并同时添加到脊
            book.spine.append(chapter)  # 确保章节被添加到脊中
        else:
            # 如果有文件夹，为每个文件夹创建一个章节
            for folder in folders:
                folder_images = sorted([image for image in images if image.startswith(folder + '/')])
                chapter_content = '<html><body>'
                for i, image_name in enumerate(folder_images):
                    # 从ZIP文件中读取图片
                    with zip_ref.open(image_name) as image_file:
                        img_data = image_file.read()

                    # 添加图片到EPUB
                    img_item = epub.EpubImage(
                        uid=f'image{i}',
                        file_name=image_name,
                        media_type=f'image/{image_name.split(".")[-1].lower()}',  # 确定媒体类型
                        content=img_data
                    )
                    book.add_item(img_item)

                    # 将图片添加到章节内容中
                    chapter_content += f'<img src="{image_name}" alt="Image {i + 1}"/><br/>'

                chapter_content += '</body></html>'

                # 创建章节以显示所有图片
                chapter_title = os.path.basename(folder) if folder else os.path.splitext(os.path.basename(zip_path))[0]
                chapter = epub.EpubHtml(title=chapter_title, file_name=f'chap_{folders.index(folder) + 1}.xhtml', lang='en')
                chapter.content = chapter_content
                book.add_item(chapter)

                # 添加章节到书籍对象并同时添加到脊
                book.spine.append(chapter)  # 确保章节被添加到脊中

        # 定义目录
        book.toc = book.spine

        # 添加导航文件
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # 写入EPUB文件
        epub.write_epub(output_epub, book)

def main():
    # 创建Tkinter根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出文件选择对话框
    zip_path = filedialog.askopenfilename(title="选择ZIP文件", filetypes=[("ZIP files", "*.zip")])
    if not zip_path:
        print("未选择文件，程序退出。")
        return

    # 弹出保存文件对话框
    output_epub = filedialog.asksaveasfilename(title="保存EPUB文件", defaultextension=".epub", filetypes=[("EPUB files", "*.epub")])
    if not output_epub:
        print("未选择保存路径，程序退出。")
        return

    # 调用创建EPUB函数
    create_epub_from_zip(zip_path, output_epub)
    print(f"EPUB文件已保存到 {output_epub}")

if __name__ == "__main__":
    main()