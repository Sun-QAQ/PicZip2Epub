import zipfile
from ebooklib import epub
import os

def create_epub_from_zip(zip_path, output_epub):
    # 打开ZIP文件并获取其成员列表
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 获取所有图片文件名，并排序
        images = sorted([name for name in zip_ref.namelist() if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))])
        
        # 创建一个新的EPUB书籍
        book = epub.EpubBook()
        
        # 设置元数据
        book.set_identifier('id123456')
        book.set_title('Image Book')
        book.set_language('en')
        
        # 假设作者是'Unknown'
        book.add_author('Unknown')

        # 图片章节内容
        chapter_content = '<html><body>'

        # 添加图片到Epub
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
        chapter = epub.EpubHtml(title='Images', file_name='chap_1.xhtml', lang='en')
        chapter.content = chapter_content
        book.add_item(chapter)

        # 添加章节到书籍对象并同时添加到脊
        book.spine.append(chapter)  # 确保章节被添加到脊中
            
        # 定义目录
        book.toc = [chapter]

        # 添加导航文件
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # 写入EPUB文件
        epub.write_epub(output_epub, book)

# 使用函数
zip_path = "D:\Downloads\\126419240_ugoira600x600.zip"  # 替换为你的ZIP文件路径
output_epub = '126419240_ugoira600x600.epub'      # 输出EPUB文件名
create_epub_from_zip(zip_path, output_epub)